#!/bin/bash

cd ..
nohup ./server.py 9001 >> log/app.log 2>&1 & 
