# Problem
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

For more details, check https://github.com/InsightDataScience/h1b_statistics

# Approach
First, read cvs file, split by ';' and store in dict

Use dict_soc and dict_state to store the items (occupations and states) and their corresponding number of applications

For each row, if certified, find in which occupation and state it is and add 1.

At the meantime, record the totally number of certified applications.

Finally, use function get_output_list to sort dict, find the top 10 and calculate the percentage

Use write_output to write output into txt file.

# Run instructions
Use Python3 (may need to change run.sh script to specify)

Each year of data can have different columns. 

Check headers and define ```key_name``` in ```h1b_counting.py``` before running.

# Repo directory structure

The directory structure for your repo should look like this:
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   └──h1b_counting.py
      ├── input
      ├── output
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── mytest_2015_TOP1000
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```