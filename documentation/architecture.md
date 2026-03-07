# Architecture Overview

This project demonstrates an event-driven data processing pipeline built using AWS services. The objective of the system is to process datasets stored in Amazon S3 whenever a processing request is received through an Amazon SQS queue.

The pipeline follows an asynchronous architecture where messages placed in the queue trigger serverless processing components. This design enables scalable, decoupled, and automated data processing.

The workflow begins when a dataset is stored in the raw folder of the S3 bucket. A message containing the dataset information is then sent to an SQS queue. The queue acts as the event source and triggers an AWS Lambda function.

The Lambda function reads the message payload and extracts the file name along with the source and destination paths. Using this information, Lambda programmatically starts an AWS Glue job.

The AWS Glue job performs the ETL process. It reads the CSV dataset from the S3 raw location, performs transformations such as filtering completed orders, and writes the transformed output to the processed folder in the same S3 bucket.

This architecture demonstrates how event-driven pipelines can automate data processing workflows while maintaining loose coupling between system components.

Pipeline Flow:

SQS Message → Lambda Trigger → Glue Job Execution → Processed Data Stored in S3
