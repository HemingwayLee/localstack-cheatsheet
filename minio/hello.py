import os
import boto3

ADDRESS = os.getenv('ADDRESS', 'minio')
PORT = os.getenv('API_PORT', '9000')
ACCESS_ID = os.getenv('AWS_ACCESS_KEY_ID', 'id')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'secret')

my_session = boto3.Session(
    aws_access_key_id=ACCESS_ID, 
    aws_secret_access_key=SECRET_KEY,
    region_name = 'us-west-2')

# default session will look at `~/.aws/credentials`
#s3 = boto3.resource(

s3 = my_session.resource(
    service_name = 's3',
    endpoint_url=f"http://{ADDRESS}:{API_PORT}",
    region_name='us-west-2')

my_bucket = s3.create_bucket(Bucket='mybucket')

s3.meta.client.upload_file(
    Filename = 'test.txt', 
    Bucket = 'mybucket', 
    Key = 'test_file_on_s3.txt')

for file in my_bucket.objects.all():
    print("files in the bucket")
    print(file.key)


