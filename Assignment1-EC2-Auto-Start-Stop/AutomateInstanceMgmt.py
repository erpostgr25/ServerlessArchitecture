import boto3
import json

def lambda_handler(event, context):
    aws_region = event.get('region', 'eu-west-2')
    ec2 = boto3.client('ec2', region_name=aws_region)

    try:
        response = ec2.describe_instances()
        instances_info = []

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                name_tag = next(
                    (tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'),
                    'No tags'
                )
                if name_tag == "Auto-Start":
                    if state == 'stopped':
                        ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
                        instances_info.append({
                            'InstanceId': instance_id,
                            'Name': name_tag,
                            'Action': 'Trigger Start Operation'
                        })
                    else:
                        instances_info.append({
                            'InstanceId': instance_id,
                            'Name': name_tag,
                            'Action': 'Already Running'
                        })
                elif name_tag == "Auto-Stop":
                    if state == 'running':
                        ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
                        instances_info.append({
                            'InstanceId': instance_id,
                            'Name': name_tag,
                            'Action': 'Trigger Stop Operation'
                        })
                    else:
                        instances_info.append({
                            'InstanceId': instance_id,
                            'Name': name_tag,
                            'Action': 'Already Stopped'
                        })

        return {
            'statusCode': 200,
            'body': json.dumps(instances_info)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
