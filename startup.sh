#!/usr/bin/env bash

PID=$(ps -ef | grep 'python3 app.py' | grep -v 'grep' | awk '{print $2}')
if [ -z $PID ]; then
    nohup python3 app.py >/dev/null 2>&1 &
    echo 'file server started!'
else
    echo 'file server is running,please shutdown it!'
fi
