#!/bin/bash

echo "... runner started ..."
echo "... connecting to"
echo "http://${ADDRESS_PORT}"

# wait until localstack is done, due to localstack bug,
#  it will return 404 and {"status":"running"}, so we choose to parse the returning json
# until $(curl --output /dev/null --silent --head --fail http://${ADDRESS_PORT}/health); do

res=$(curl http://${ADDRESS_PORT})
status=$(jq -r '.status' <<< "$res")
until [ "$status" == "running" ]
do
    echo '...... sleep ......'
    sleep 3
    res=$(curl http://${ADDRESS_PORT})
    status=$(jq -r '.status' <<< "$res")
done

# create
aws --endpoint-url=http://${ADDRESS_PORT} s3 mb s3://demo-bucket
aws --endpoint-url=http://${ADDRESS_PORT} s3api put-bucket-acl --bucket demo-bucket --acl public-read

# update
aws --endpoint-url=http://${ADDRESS_PORT} s3 cp test.txt s3://demo-bucket/
aws --endpoint-url=http://${ADDRESS_PORT} s3 ls
aws --endpoint-url=http://${ADDRESS_PORT} s3 ls s3://demo-bucket



