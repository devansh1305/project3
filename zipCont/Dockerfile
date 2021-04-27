FROM python:3-alpine

RUN apk update
RUN apk add vim
RUN apk add curl
RUN apk add gzip

WORKDIR /opt/demo/
COPY /app .

RUN pip install -r requirements.txt
EXPOSE 81
ENTRYPOINT python app.py
