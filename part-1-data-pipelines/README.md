# Question 1: Data Pipelines


## Key Requirements Gathered

Schedule:
    - Function should be run on an hourly basis. (use 0 * * * * * CRON expression later on)

Filters:
    - Filter by mobile number. (must be exactly 8 digits in length)
    - Filter by age. (must be > 18 years after 1st Jan 2022)
    - Filter by valid email (email should follow @emailprovider.com or @emailprovider.net. use REGEX)
    
Transformation
    - Split up into two dataframes. One with names and the other with null valued names.
    - Name column to be split into full_name and last_name. (pandas apply)
    - Date of birth field to be parsed into YYYYMMDD format.
    - Create 'above_18' column. (where age > 18)
    - Create 'membership_id' column that follows the formula <last_name>_<SHA256hash(YYYYMMDD)[-5]>

