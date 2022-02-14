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

