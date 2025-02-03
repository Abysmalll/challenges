FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

WORKDIR /challenge

RUN git clone https://github.com/Abysmalll/genie2.git .

RUN pip install --no-cache-dir flask

EXPOSE 80

WORKDIR /challenge/app

ENV FLASK_APP=/challenge/app/app.py

CMD sh -c 'echo "${FLAG_VALUE}" > /challenge/app/flag.txt && flask run --host=0.0.0.0 --port=80'