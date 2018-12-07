FROM python:3.6

RUN mkdir /twilio
WORKDIR /twilio

COPY index.py .

RUN pip install twilio --target .
