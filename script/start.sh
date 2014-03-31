#!/bin/bash

cd ..
nohup python ./server.py 9001 >> log/app.log 2>&1 & 
