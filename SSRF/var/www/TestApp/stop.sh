#!/bin/bash
app="docker.ssrf"
docker stop ${app}
docker rm ${app}
docker image rm ${app}