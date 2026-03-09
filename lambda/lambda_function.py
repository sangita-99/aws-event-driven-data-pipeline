import json
import boto3

glue_client = boto3.client('glue')

def lambda_handler(event, context):
    
    for record in event['Records']:
        
        message = json.loads(record['body'])
        
        file_name = message['file_name']
        source_path = message['source_path']
        destination_path = message['destination_path']
        
        print("File Name:", file_name)
        print("Source Path:", source_path)
        print("Destination Path:", destination_path)
        
        response = glue_client.start_job_run(
            JobName='assignment-aws',
            Arguments={
                '--file_name': file_name,
                '--source_path': source_path,
                '--destination_path': destination_path
            }
        )
        
        print("Glue Job Triggered:", response['JobRunId'])
    
    return {
        'statusCode': 200,
        'body': 'Glue job started successfully'
    }