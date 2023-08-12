# Question 2: Databases

## Table of Contents

- [Description](#project-description)
- [Key Requirements Gathered](#key-requirements-gathered)
- [Table Restrictions](#table-restrictions)

## Description

For this project, the `preprocess.py` script is the main script used for the preprocessing of data based on the requirements given. The `successful-applications` and `failed-applications` folders contain the processed datasets required for submission.

## Key Requirements Gathered

Identified tables to create:
- Members (follows schema from the processed data from part 1)
- Items (schema based on the given)
- Transactions (schema based on the given)
- TransactionItems (junction table for m-to-m relationship btwn Items and Transactions)


## Table Restrictions

Members:
- membership_id must be UNIQUE
- rest of the fields should be NULL given that they were critical components during the filtering in part 1
- mobile_number and date_of_birth can have VARCHAR(10) since they are expected to have less than 10 string length

Items:
- item_name must be UNIQUE

Transactions:
- membership_id FOREIGN KEY
- items_bought uses TEXT field as we will upload one or many items as a JSON string as a value

TransactionItems:
- transaction_id FOREIGN KEY
- item_id FOREIGN KEY