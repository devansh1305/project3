FROM python

WORKDIR /opt/demo/
COPY /app .

RUN pip install -r requirements.txt
EXPOSE 80

ENTRYPOINT python app.py

