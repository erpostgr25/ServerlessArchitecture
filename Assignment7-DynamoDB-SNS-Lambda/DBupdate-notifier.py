import json
import boto3
import os

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    topic_arn = os.environ.get('SNS_TOPIC_ARN','arn:aws:sns:eu-west-2:975050024946:shashi-dbupdate-topic')

    for record in event['Records']:
        if record['eventName'] == 'MODIFY':
            new_image = record['dynamodb'].get('NewImage', {})
            old_image = record['dynamodb'].get('OldImage', {})
            
            message = {
                "Event": "DynamoDB Item Updated",
                "OldItem": old_image,
                "NewItem": new_image
            }

            # Log to CloudWatch
            print("Change detected in DynamoDB table:")
            print(json.dumps(message, indent=2))

            # Send alert via SNS
            sns_client.publish(
                TopicArn=topic_arn,
                Subject="DynamoDB Item Updated",
                Message=json.dumps(message, indent=2)
            )
    
    return {"statusCode": 200, "body": "Processed DynamoDB Stream Event"}
