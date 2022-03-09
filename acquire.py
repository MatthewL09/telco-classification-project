# Wrangle

# Modules (acquire.py + prepare.py)

# Module(s) with user-defined functions for acquiring and preparing the data should be created.

# Each function contains a helpful docstring explaining what it does, its input(s) and output(s).

# Credentials (such as in an env.py file) are NOT included in the public repo.

# For example:

# test acquire function
# add to acquire.py module
# write code to clean data in notebook
# merge code into a single function & test
# write code to split data in notebook
# merge code into a single function & test
# merge functions in a single function & test
# Add all 3 functions (or more) to prepare.py file
# import into notebook and test functions

## identify drivers from storytelling
# walk through a notebook, keeping audience in mind... try to avoid technical terms. explicit and clear on takeways for sake of business.
# suggesting value of observations to someone who is on business side

# deliverables - readne description and goals. initial hypothesis on drivers of churn. data dictionary. what does senior citizen mean '0, 1' meaning was or was not. EXPLAIN
# continued - instructions on how to replicate the experiment.
import numpy as np
import pandas as pd
import os
from env import username, password, host

def get_telco_data(use_cache=True):
    '''This function returns the data from the telco_churn database in Codeup Data Science Database. 
    In my SQL query I have joined all 4 tables together, so that the resulting dataframe contains all the contract, 
    payment, and internet service options.
    '''
    if os.path.exists('telco.csv') and use_cache:
        print('Using cached csv')
        return pd.read_csv('telco.csv')
    print('Acquiring data from SQL database')

    database_url_base = f'mysql+pymysql://{username}:{password}@{host}/'
    query = '''
    SELECT *
    FROM customers
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN contract_types USING (contract_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    df = pd.read_sql(query, database_url_base + 'telco_churn')
    df.to_csv('telco.csv', index=False)
    return df

get_telco_data()