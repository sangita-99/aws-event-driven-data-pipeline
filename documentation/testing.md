**Testing the Pipeline**



The pipeline was tested to ensure that the event-driven workflow functions correctly.



*Step 1 – Upload Dataset*

The dataset **sales\_data.csv** was uploaded to the raw folder in the S3 bucket.



*Step 2 – Send SQS Message*

A message containing file information was sent to the SQS queue.



{

"file\_name": "sales\_data.csv",

"source\_path": "raw/",

"destination\_path": "processed/"

}



*Step 3 – Lambda Execution*

The SQS message triggered the Lambda function automatically. The Lambda function extracted the message details and initiated the AWS Glue job.



*Step 4 – Glue Job Execution*

The Glue job read the dataset from the raw folder, performed the transformation, and wrote the output data to the processed folder in S3.



*Step 5 – Output Verification*

The successful execution of the pipeline was verified by checking the processed folder in S3. The transformed dataset was generated in Parquet format.



*Step 6: CloudWatch Logs*

CloudWatch logs were also reviewed to confirm that the Lambda function and Glue job executed successfully.



