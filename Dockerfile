FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /keygen_service
EXPOSE 8000

COPY requirements.txt /keygen_service/requirements.txt

RUN pip install -r requirements.txt

COPY /keygen_service /keygen_service
