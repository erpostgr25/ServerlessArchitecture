import json
import boto3
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    topic_arn = os.environ.get('SNS_TOPIC_ARN','arn:aws:sns:eu-west-2:975050024946:shashi-statechange-topic')

    print("Received event:")
    print(json.dumps(event, indent=2))

    # Extract instance details from the event
    detail = event.get('detail', {})
    instance_id = detail.get('instance-id', 'Unknown')
    state = detail.get('state', 'Unknown')
    region = event.get('region', 'Unknown')
    time = event.get('time', 'Unknown')

    # Create message
    message = (
        f"EC2 Instance State Change Detected:\n\n"
        f"Instance ID: {instance_id}\n"
        f"Region: {region}\n"
        f"New State: {state}\n"
        f"Time: {time}\n"
    )

    # Send notification
    sns.publish(
        TopicArn=topic_arn,
        Subject=f"EC2 Instance {state.upper()} - {instance_id}",
        Message=message
    )

    print("Notification sent successfully.")
    return {"statusCode": 200, "body": "SNS Notification Sent"}
