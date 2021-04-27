from flask import Flask
from flask import request

import subprocess

import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "This is my zipping microservice\n"


@app.route('/gzip',methods = ['GET'])
def upload():
    a = request.args['filename']
    a = "/contData/"+a
    output = subprocess.Popen(["gzip",a,"-v"],stdout=subprocess.PIPE).communicate()[0]
    output = output + "\n"
    return output

@app.route('/gunzip',methods = ['GET'])
def getfile():
    a = request.args['filename']
    output = subprocess.Popen(["gunzip",a,"-v"],stdout=subprocess.PIPE).communicate()[0]
    output = output + "\n"
    return output

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81, debug=True)
