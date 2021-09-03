FROM python:3.8.10-buster

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app

COPY . . 

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app