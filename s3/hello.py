import boto3

ADDRESS = os.getenv('ADDRESS_PORT', 'localstack:4566')
ACCESS_ID = os.getenv('AWS_ACCESS_KEY_ID', 'id')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'secret')

my_session = boto3.Session(
    aws_access_key_id=ACCESS_ID, 
    aws_secret_access_SECRET_KEY,
    region_name = 'us-west-2')

# default session will look at `~/.aws/credentials`
#s3 = boto3.resource(

s3 = my_session.resource(
    servdice_name = 's3',
    endpoint_url=f"http://{ADDRESS}",
    region_name='us-west-2')

#s3.meta.client.upload_file(
#    Filename = 'test.txt', 
#    Bucket = '', 
#    Key = '')


