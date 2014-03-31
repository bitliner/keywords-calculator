#!/bin/bash

cd ..
nohup ./server.py 9002 >> log/app.log 2>&1 & 
