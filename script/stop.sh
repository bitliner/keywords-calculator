#!/bin/bash

kill `ps aux|egrep 'python.*server'|head -1|awk '{print $2}'`