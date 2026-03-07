# AWS Event-Driven Data Processing Pipeline

## Project Overview

This project demonstrates an event-driven data processing pipeline built using AWS services. The system processes datasets stored in Amazon S3 when a processing request is received through an Amazon SQS queue.

The architecture uses serverless components to automate the data processing workflow. An SQS message triggers an AWS Lambda function, which starts an AWS Glue job to perform the ETL process. The Glue job reads raw data from Amazon S3, performs transformation operations, and stores the processed output in a separate folder.

## Architecture

The pipeline follows an event-driven architecture where services communicate asynchronously.

SQS Queue → Lambda Function → AWS Glue Job → Processed Data in Amazon S3

## Technologies Used

* Amazon S3
* Amazon SQS
* AWS Lambda
* AWS Glue
* Python
* PySpark

## Dataset

The dataset used in this project contains sales transaction records including product details, quantity, payment method, and order status.

## Pipeline Workflow

1. A dataset is uploaded to the **raw folder** in the S3 bucket.
2. A processing request is sent to the **SQS queue**.
3. The SQS message triggers the **Lambda function**.
4. Lambda extracts file information and starts the **Glue ETL job**.
5. The Glue job reads the dataset, performs transformation, and stores the processed output in the **processed folder**.

## Project Structure

aws-event-driven-data-pipeline
architecture/
architecture-diagram.png

data/
sales_data.csv

lambda/
lambda_function.py

glue/
glue_script.py

documentation/
architecture.md
setup_steps.md
testing.md

screenshots/
sqs_queue.png
lambda_trigger.png
glue_job.png
s3_output.png

## Output
The processed data is written to the **processed folder in Amazon S3** in Parquet format after applying the transformation logic.

