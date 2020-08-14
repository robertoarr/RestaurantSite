FROM python:3.7-alpine3.8

RUN apk update
RUN apk upgrade
RUN apk add mariadb-connector-c-dev
RUN apk add g++

RUN mkdir /code

COPY . /code/

RUN cd /code/ && pip install -r requirements

WORKDIR /code
