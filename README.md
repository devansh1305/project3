# project3

zipCont -> service to compress and uncompress files <br/>
storageCont -> service to upload and download files from s3 bucket <br/>
webserverCont -> service to host webserver to accept user requests <br/>

To build docker images for each service:
- Go into webserverCont/zipCont/storageCont and input below commands respectively:
	- docker build -t webserver-image .
	- docker build -t zip-image .
	- docker build -t storage-image .

To start the kubernetes cluster:
- kubectl create -f config.yaml

To delete the kubernetes cluster:
-  kubectl delete -f config.yaml

To upload a file:
- curl "http://172.17.0.3:82/upload?filepath=./contData/<filename>&cflag=<Y or N>" -X POST <br/>
example - curl "http://172.17.0.3:82/upload?filepath=./contData/hellofile&cflag=Y" -X POST <br/>

To download a file:
- curl "http://172.17.0.3:82/getfile?filename=<filename>" <br/>
example - curl "http://172.17.0.3:82/getfile?filename=hellofile.gz" <br/>
