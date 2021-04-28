#!/bin/bash
docker-compose stop
docker rm webserverCont zipCont storageCont
docker image rm webserver-image:latest zip-image:latest storage-image:latest
