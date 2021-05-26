#!/usr/bin/env bash

PID=$(ps -ef | grep 'python3 app.py' | grep -v 'grep' | awk '{print $2}')
if [ -z $PID ]; then
    echo 'file server is not running!'
else
    echo 'file server is running, killing...'
    kill -9 $PID
    echo 'file server has been killed.'
fi
