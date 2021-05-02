from flask import Flask
from flask import request
from sh import gunzip
import gzip
import subprocess
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "This is my zipping microservice\n"


@app.route('/gzip', methods=['GET'])
def upload():
    a = request.args['filename']
    #a = "/contData/"+a
    # output = subprocess.Popen(
    #    ["gzip", a, "-v"], stdout=subprocess.PIPE).communicate()[0]
    #output = output + b"\n"
    gzip_name = a+".gz"
    try:
        with open(a, "rb") as src, gzip.open(gzip_name, "wb") as dst:
            dst.writelines(src)
        os.remove(a)
        return "gzip "+gzip_name+" success"
    except:
        return "gzip "+gzip_name+" failed"


@app.route('/gunzip', methods=['GET'])
def getfile():
    a = request.args['filename']
    a = "/contData/"+a
    try:
        gunzip(a)
        return "gunzip "+a+" success"
    except:
        return "gunzip "+a+" failed"
    # output = subprocess.Popen(
    #    ["gunzip", a, "-v"], stdout=subprocess.PIPE).communicate()[0]
    #output = output + b"\n"
    # return output


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81, debug=True)
