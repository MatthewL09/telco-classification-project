PROJECT DETAILS FOR TELCO DATASET

1. Overview
    Project Goals
    - Identify drivers of customer churn and find a solution to help improve customer retention
    - Construct a machine learning model that predicts churn so Telco can focus retention efforts on at risk customers 

    Project Description
    - Telco Communications prides itself on customer satisfaction and quality of service. Maintaing a good reputation comes by focusing efforts on current customers and keeping up with patterns in the data. By reducing the rate at which customers churn we can help improve customer retention and increase company revenue. After identifying key drivers of churn Telco can then focus on improving customer experience and quality of product.

    Initial Hypothesis/Questions

    - What is the rate of churn for monthly contracts compared to 1 year and 2 year contracts?
    - Is there a length of tenure before customers decide to churn? 
    - Does service type play a key factor in the decision to churn? 
    - What is the average charge amount for customers who churn?
    
    Data Dictionary

    |Column | Description | Dtype|
    |--------- | --------- | ----------- |
    customer_id | id number to identify cust | int64 |
    is_senior_citizen | whether customer is senior citizen | int64 |
    tenure | months with the company | int 64 |
    multiple_lines | whether customer has more than one line | int 64 |
    monthly_charges | customer monthly rate | float64 |
    total_charges | how much customer has paid | float 64 |
    contract_type | one year, two year, month-to-month | object |
    internet_service_type | DSL, Fiber optic, None | object |
    payment_type | how the customer pays balance | object |
    is_male | whether customer is male or not | uint8 |
    has_partner | whether customer has partner or not | uint8 |
    has_dependents | whether customer has dependents or not | uint8 |
    online_security | whether customer has online security or not | uint8 |
    online_backup | whether customer has online back up or not |uint8 |
    phone_service | whether customer has phone service or not | uint8 |
    device_protection | whether customer has device protection or not | uint8 |
    tech_support | whether customer has tech support or not | uint8 |
    streaming_tv | whether customer streams tv or not | uint8  |
    streaming_movies | whether customer streams movies or not | uint |
    paperless_billing | whether customer has paperless billing or not | uint8 |
    churn | whether customer has churned or not | uint8 |
    one_line | whether customer has one line or not | uint8 |
    no_phone_service | whether customer has no phone service or not | uint8 |
    has_multiple_lines | whether customer has multiple lines or not | uint8 |
    month_to_month_contract | whether customer has month to month or not | uint8 |
    one_year_contract | whether customer has one year contract or not | uint8 |
    two_year_contact | whether customer has two year contract or not | uint8 |
    dsl_internet | whether customer has dsl internet or not | uint8 |
    fiber_optic_internet | whether custome rhas fiber optic or not | uint8 |
    no_internet_service | whether a customer has no internet or not | uint8 |
    bank_transfer_autopay | whether a customer pays via bank transfer | uint8 |
    credit_card_autopay | whether a customer pays via credit card | uint8 |
    electronic_check_nonauto | whether a customer pays via e-check | uint8 |
    mailed_check_nonauto | whether a customer pays via mailed check | uint8 |
    is_autopay | whether a customer has autopay or not | uint8 |

    Project Plan

    Planning
    - Define goals
    - Determine audience and delivery format