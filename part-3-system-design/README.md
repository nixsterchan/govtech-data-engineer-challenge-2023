# Question 3: System Design
For this section, I will be designing the data infrastructure of the given proposal on AWS Cloud. 

## Key Requirements Gathered
    - Web application 1 (user uploads)
    - Web application 2 (hosts Kafka stream for image upload)
    - Code prepared for image processing, requires to be hosted on cloud.
    - Stored images and metadata in cloud env needs to be purged after 7 days.
    - Cloud env requires a Business Intel resource for analysts.

## Potential Services
    - VPC
    - EC2
    - Lambda
    - Fargate
    - S3
    - Glue
    - Athena
    - Quicksight

