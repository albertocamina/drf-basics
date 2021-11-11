FROM python:3.7

WORKDIR /opt/

COPY . /opt/

RUN pip install -r requirements.txt