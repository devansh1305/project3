FROM python

WORKDIR /opt/demo/
COPY /app .

RUN pip install -r requirements.txt
EXPOSE 82
ENTRYPOINT python app.py

