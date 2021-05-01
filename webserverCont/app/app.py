from flask import Flask
from flask import request

import subprocess
#from helperfunctions import *
import os

def is_compressed(filename):
    if(".gz" in filename):
        return True
    return False

def compress(filename,flag):
    request = ""
    if(flag==0): request = "zipcont:81/gzip?filename="+filename
    else: request = "zipcont:81/gunzip?filename="+filename
    output = subprocess.Popen(["curl" ,request],stdout=subprocess.PIPE).communicate()[0]
    return output

def uploadfile(filepath):
    request = "storagecont:80/upload?filepath="+filepath
    uopt = subprocess.Popen(["curl",request],stdout=subprocess.PIPE).communicate()[0]
    return uopt

def downloadfile(filename):
    request = "storagecont:80/getfile?filename="+filename
    dopt = subprocess.Popen(["curl",request],stdout=subprocess.PIPE).communicate()[0]
    return dopt

app = Flask(__name__)


@app.route('/')
def hello():
    return "This is my webserver microservice\n"


@app.route('/upload', methods=['POST'])
def upload():
    filepath = request.args['filepath']
    filepath = filepath[1:]
    #compress = request.args['compress']
    if(is_compressed(filepath)):
        uploadfile(filepath)
    else:
        copt = compress(filepath, 0)
        if(b"success" not in copt):
            return copt
        filepath = filepath+".gz"
        uopt = uploadfile(filepath)
        return uopt


@app.route('/getfile', methods=['GET'])
def getfile():
    filename = request.args['filename']
    dopt = downloadfile(filename)
    return dopt


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=82, debug=True)
