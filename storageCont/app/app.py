from flask import Flask
from flask import request

import subprocess

import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "This is my storage microservice\n"


@app.route('/upload',methods = ['GET'])
def upload():
    a = request.args['filepath']
    output = subprocess.Popen(["aws","s3","cp",a,"s3://devproject3bucket/"],stdout=subprocess.PIPE).communicate()[0]
    output = output + "\n"
    return output

@app.route('/getfile',methods = ['GET'])
def getfile():
    a = request.args['filename']
    bucketpath = "s3://devproject3bucket/"+a
    output = subprocess.Popen(["aws","s3","cp",bucketPath,"/contData/"],stdout=subprocess.PIPE).communicate()[0]
    output = output + "\n"
    return output

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
