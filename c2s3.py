import boto3
import uuid

s3 = boto3.client('s3')
bucket_name = uuid.uuid4().urn[9:]
s3.create_bucket(Bucket=bucket_name)

print(f'Successfully created bucket {bucket_name}')
