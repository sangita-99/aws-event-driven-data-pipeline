# Event-Driven Data Pipeline on AWS

Designed and implemented a scalable, event-driven ETL pipeline to automate data ingestion, validation, transformation, and delivery using AWS services.

The pipeline processes incoming files in real-time, ensuring data quality, fault tolerance, and observability for reliable downstream analytics.

---

## Architecture

S3 (Raw Data) → Lambda (Trigger & Validation) → AWS Glue (ETL Processing) → S3 (Processed Data)

### Supporting Components
- **Amazon SQS (Dead Letter Queue)** – Captures failed or malformed records for debugging and reprocessing
- **Amazon CloudWatch** – Logging and monitoring of pipeline execution
- **Amazon SNS** – Sends alerts for failures and critical events

---

## ⚙️ Key Features

- Real-time event-driven data processing using S3 triggers
- Automated ETL transformation using AWS Glue (PySpark)
- Fault-tolerant design with SQS Dead Letter Queue
- End-to-end monitoring using CloudWatch and SNS alerts
- Structured storage using raw and processed data layers

---

## 🔄 Workflow

1. File is uploaded to S3 (raw layer)
2. S3 event triggers AWS Lambda
3. Lambda validates input and triggers AWS Glue job
4. Glue performs ETL (CSV → Parquet transformation)
5. Processed data is stored in S3 (processed layer)
6. Failures are routed to SQS Dead Letter Queue
7. Alerts are sent via SNS and logs captured in CloudWatch

---

## 🛑 Error Handling & Reliability

- Implemented AWS native retry mechanisms for transient failures
- Configured **SQS Dead Letter Queue** to isolate failed records
- Enabled CloudWatch alarms integrated with SNS for real-time alerts
- Designed pipeline to prevent data loss and ensure recovery

---

## ⚡ Performance Optimization

- Optimized data partitioning to improve processing efficiency
- Reduced data shuffling during transformations
- Leveraged efficient storage format (Parquet) for analytics

---

## 📊 Impact

- Automated end-to-end data pipeline reducing manual intervention
- Improved data reliability through validation and monitoring
- Enabled faster query performance with optimized storage format

---

## 📸 Pipeline Execution Evidence

*(Add only 3–5 strong screenshots here)*

- Glue job success
- Lambda logs
- CloudWatch monitoring
- SQS Dead Letter Queue

---

## Tech Stack

- AWS S3
- AWS Lambda
- AWS Glue (PySpark)
- Amazon SQS
- Amazon SNS
- Amazon CloudWatch