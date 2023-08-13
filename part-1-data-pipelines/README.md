# Question 1: Data Pipelines

This section is targeted at building the script required for preprocessing the data according to the given requirements in the question.

## Table of Contents

- [Project Description](#project-description)
- [Key Requirements Gathered](#key-requirements-gathered)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)

## Project Description

This project covers the preprocessing task given, and has been broken down into steps I have taken such as the requirements gathering and how I planned to tackle them. Steps have also been prepared for you to take if you will be running the script on your system.

Before proceeding with any setup, please note that for this project, the required answers are the following:
- `preprocess.py` script (main script used for the preprocessing of data) 
- `successful-applications/` and `failed-applications/` folders contain the processed datasets

## Key Requirements Gathered

Schedule:
- Function should be run on an hourly basis. (use 0 * * * * * CRON expression later on)

Filters (deemed unsuccessful applications):
- Filter by mobile number. (must be exactly 8 digits in length)
- Filter by age. (must be > 18 years after 1st Jan 2022)
- Filter by valid email (email should follow @emailprovider.com or @emailprovider.net. use REGEX)
- Filter by name (must have no null names)
    
Transformation
- Name column to be split into full_name and last_name. (pandas apply)
- Date of birth field to be parsed into YYYYMMDD format.
- Create 'above_18' column. (where age > 18)
- Create 'membership_id' column that follows the formula <last_name>_<SHA256hash(YYYYMMDD)[-5]>

## Getting Started

### Prerequisites

This project was done in Python 3.9 with the following package:

- pandas==1.5.3

### Installation

Steps:

1. Ensure that your terminal is in the part-1-data-pipelines folder. 
2. Change to the project directory (if required): `cd part-1-data-pipelines`
3. Install the required packages: `pip install -r requirements.txt`

## Usage

One of the requirements of this project is to have the processing of data done every hour.

1. Any new data files to be processed are expected to be placed in the `ingestion-data` folder.
2. Run the preprocessing script hourly: 
    - include the following cron expression within your crontab:
    ```bash
    # Make sure to change the path within the <>
    0 * * * * cd </path/to/your/govtech-data-engineer-test/part-1-data-pipelines> && ./run_script.sh
    ```
3. Processed datasets will be saved in the `successful-applications` and `failed-applications` folders.
4. Loggings can be found inside logger.log file.
5. For datasets that failed during the processing, their source file will be moved to the `unprocessed=data` folder.
6. Likewise for datasets that went through the process successfully, their source file will be moved to the `marked-for-deletion-data` folder.

## Directory Structure

After running the preprocess code for the first time, the directory should look something like the following:

```
part-1-data-pipelines/
│ README.md
│ preprocess.py
│ requirements.txt
| logger.log
├── ingestion-data/
│ data_file1.csv
│ data_file2.csv
├── failed-applications/
│ processed_data_file1.csv
│ processed_data_file2.csv
├── successful-applications/
│ processed_data_file1.csv
│ processed_data_file2.csv
```
Note: data_file_1 and data_file_2 are just generic names used for example