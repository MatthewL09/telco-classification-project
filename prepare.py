import pandas as pd
import os
from sklearn.model_selection import train_test_split

import warnings
warnings.filterwarnings("ignore")

# Module(s) with user-defined functions for acquiring and preparing the data should be created.

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

def clean_telco_data(df):
    ''' This function takes in the telco data and cleans it
    '''
    # drops duplicate columns if there are any present
    df.drop_duplicates()

    # change dtype in column from string so it can be used
    df.total_charges = pd.to_numeric(df.total_charges, errors = 'coerce')
    
    # reassigning dataframe and dropping the null values
    df = df[df.total_charges.notnull()]

    # changing 'no internet service', which is present in a lot of columns, to 'no'
    df.replace('No internet service', 'No', inplace = True)

    # get dummies for columns that have two values (yes,no) or gender, and dropping first
    dummy_df = pd.get_dummies(df[['gender', 'partner', 'dependents', 'online_security', 'online_backup', 'phone_service',
                              'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 
                              'paperless_billing', 'churn']], drop_first = True)

    # get dummies for columns that have more than two values
    dummy_df2 = pd.get_dummies(df[['multiple_lines', 'contract_type', 'internet_service_type', 'payment_type']])

    # dropping columns that are now duplicates, from the dummies created, or not needed

    drop_cols = ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id',
                'gender', 'partner', 'dependents', 'online_security', 'phone_service',
                'online_backup', 'device_protection', 'tech_support', 'streaming_tv',
                'streaming_movies', 'paperless_billing', 'churn']
    df = df.drop(columns = drop_cols)

    # combine df and dummy_df that I created
    df = pd.concat([df, dummy_df, dummy_df2], axis =1)

    # rename column names for clarity

    df.rename(columns ={ 'gender_Male': 'is_male',
                        'partner_Yes': 'has_partner',
                        'dependents_Yes': 'has_dependents',
                        'online_security_Yes': 'online_security',
                        'online_backup_Yes': 'online_backup',
                        'phone_service_Yes': 'phone_service',
                        'device_protection_Yes': 'device_protection',
                        'tech_support_Yes': 'tech_support',
                        'streaming_tv_Yes': 'streaming_tv',
                        'streaming_movies_Yes': 'streaming_movies',
                        'paperless_billing_Yes': 'paperless_billing',
                        'churn_Yes': 'churn',
                        'multiple_lines_No': 'one_line',
                        'multiple_lines_No phone service': 'no_phone_service',
                        'multiple_lines_Yes': 'has_multiple_lines',
                        'contract_type_Month-to-month': 'month_to_month_contract',
                        'contract_type_One year': 'one_year_contract',
                        'contract_type_Two year': 'two_year_contract',
                        'internet_service_type_DSL': 'dsl_internet',
                        'internet_service_type_Fiber optic': 'fiber_optic_internet',
                        'internet_service_type_None': 'no_internet_service',
                        'payment_type_Bank transfer (automatic)': 'bank_transfer_autopay',
                        'payment_type_Credit card (automatic)': 'credit_card_autopay',
                        'payment_type_Electronic check': 'electronic_check_nonauto',
                        'payment_type_Mailed check': 'mailed_check_nonauto'}, inplace = True)

    return df     

def split_data(df):
    '''
    This function takes in a dataframe and splits the data into train, validate and test samples. 
    Test, validate, and train are 20%, 24%, & 56% of the original dataset, respectively. 
    The function returns train, validate and test dataframes. 
    '''
    # split dataframe 80/20, stratify on churn to ensure equal proportions in both dataframes
    train_validate, test = train_test_split(df, test_size=.2, 
                                            random_state=123, 
                                            stratify=df.churn)
    # split previous larger dataframe by 70/30, stratify on churn
    train, validate = train_test_split(train_validate, test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    # results in 3 dataframes
    return train, validate, test

def prep_telco_data(df):
    '''
    Cleaning and splitting the data using the 2 functions above
    '''
    clean_df =clean_telco_data(df)
    train, validate, test = split_data(clean_df)

    return train, validate, test                     

