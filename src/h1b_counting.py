# Introduction
# Use dict_soc and dict_state to store the number of applications that have been certified,
# then sort these two dictionaries.
# Finally, use function get_output_list and write_output to write output into txt file.

# Created by Saina

import time
import sys
import csv


def get_output_list(count_dict, sum_certified):
    alph_order_list = sorted(count_dict.items(), key=lambda x: x[0])
    value_order_list = sorted(alph_order_list, key=lambda x: x[1], reverse=True)
    output_list = []    # output data stored in a list
    for item, numb in value_order_list[:10]:
        output_row = item, str(numb), str(round(100*(numb/sum_certified), 1)) + '%'
        # Python3 int division yields float
        output_list.append(';'.join(output_row))
    return output_list


def write_output(count_dict, sum_certified, PATH, header):
    file = open(PATH, "w")
    file.write(header + '\n')
    file.write('\n'.join(get_output_list(count_dict, sum_certified)))
    file.close()


def main():
    start = time.clock()

    PATH_INPUT = sys.argv[1]
    PATH_OUTPUT_SOC = sys.argv[2]
    PATH_OUTPUT_STATE = sys.argv[3]

    # Each year of data can have different headers
    # 2015 & 2016 selected columns
    key_name = {'status': 'CASE_STATUS', 'occupation': 'SOC_NAME', 'state': 'WORKSITE_STATE'}
    # For 2014 use {'status': 'STATUS', 'occupation': 'LCA_CASE_SOC_NAME', 'state': 'LCA_CASE_WORKLOC1_STATE'}

    with open(PATH_INPUT, "r", encoding='UTF-8') as f_csv:
        dict_reader = csv.DictReader(f_csv, delimiter=';')
        dict_soc = {}
        dict_state = {}
        sum_certified = 0
        for row in dict_reader:
            if row.get(key_name['status']) == 'CERTIFIED':
                sum_certified += 1
                dict_soc[row.get(key_name['occupation'])] = dict_soc.get(row.get(key_name['occupation']), 0) + 1
                dict_state[row.get(key_name['state'])] = dict_state.get(row.get(key_name['state']), 0) + 1

    header_soc = 'TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'
    header_state = 'TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'

    write_output(dict_soc, sum_certified, PATH_OUTPUT_SOC, header_soc)
    write_output(dict_state, sum_certified, PATH_OUTPUT_STATE, header_state)

    elapsed = time.clock() - start
    print('Time used:', elapsed)

if __name__ == '__main__':
    main()
