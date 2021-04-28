import subprocess
import os
def is_compressed(filename):
    if(".gz" in filename):
        return True
    return False


def compress(filename, flag):
    request = ""
    if(flag == 0):
        request = "zip:81/gzip?filename="+filename
    else:
        request = "zip:81/gunzip?filename="+filename
    output = subprocess.Popen(
        ["curl", request], stdout=subprocess.PIPE).communicate()[0]
    return output


def uploadfile(filepath):
    request = "storage:80/upload?filepath="+filepath
    uopt = subprocess.Popen(
        ["curl", request], stdout=subprocess.PIPE).communicate()[0]
    return uopt


def downloadfile(filename):
    request = "storage:80/getfile?filename="+filename
    dopt = subprocess.Popen(
        ["curl", request], stdout=subprocess.PIPE).communicate()[0]
    return dopt
