FROM python:3.8

RUN apt-get update && apt-get install -y awscli curl vim jq

RUN mkdir -p /home/app
WORKDIR /home/app
COPY . /home/app

ENV AWS_ACCESS_KEY_ID=minioadmin
ENV AWS_SECRET_ACCESS_KEY=minioadmin

RUN pip3 install -r requirements.txt


