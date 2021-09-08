#!/bin/bash

# If current directory is the scripts folder, go up a folder
if [[ $(basename `pwd`) == "scripts" ]]; then
	cd ..
fi

APP_NAME=$(basename `pwd`)

docker build -t $APP_NAME .
docker run -it -p 8080:8080 $APP_NAME
