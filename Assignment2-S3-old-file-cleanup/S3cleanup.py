import boto3
import datetime
import os

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Bucket name (hardcoded or use environment variable)
    bucket_name = os.environ.get('BUCKET_NAME', 'shashi-assignment-bucket')
    
    # Calculate cutoff date (30 days ago)
    cutoff_date = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=30)
    
    # List all objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' not in response:
        print("Bucket is empty or doesn't exist.")
        return
    
    deleted_files = []
    
    # Loop through all files
    for obj in response['Contents']:
        last_modified = obj['LastModified']
        key = obj['Key']
        
        # Compare with cutoff date
        if last_modified < cutoff_date:
            print(f"Deleting old file: {key} (LastModified: {last_modified})")
            s3.delete_object(Bucket=bucket_name, Key=key)
            deleted_files.append(key)
    
    print(f"Deleted {len(deleted_files)} old files from {bucket_name}.")
    
    return {
        'statusCode': 200,
        'deleted_files': deleted_files
    }
