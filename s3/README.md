# How to run
## Run locally
* In main tab
```
localstack start
```

* In another tab
```
./runner.sh
python3 hello.py
```

## Run by docker
* In main tab
```
docker-compose build
docker-compose up
```

* In another tab
```
docker exec -it ${ID} /bin/bash
./runner.sh
python3 hello.py
```

## aws cli
```
$ aws configure
AWS Access Key ID [****************2S7Q]: 
AWS Secret Access Key [****************uDF5]: 
Default region name [None]: 
Default output format [None]: 
```

by default, we don't need to specify `` in aws cli command. The default endpoint is in following format
```
${protocol}://${service-code}.${region-code}.amazonaws.com
https://dynamodb.us-west-2.amazonaws.com
```

