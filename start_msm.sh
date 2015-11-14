#!/bin/bash

H_PID=`ps -ax | grep -e "\smsmsite" | sed 's/\s*\([0-9]*\).*/\1/'`
if [ -z $H_PID ]; then
  echo "process not found."
else
  echo "shutdown process: [$H_PID]"
  kill $H_PID >> /dev/null
fi

screen -dmS msmsite /usr/bin/python run.py
# python run.py > /var/log/msm-site.log

