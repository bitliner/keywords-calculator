#!/bin/bash

cd ..
nohup ./server.py 3010 >> log/app.log 2>&1 & 