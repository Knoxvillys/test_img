FROM python:3.7-slim-buster

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

