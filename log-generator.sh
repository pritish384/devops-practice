#!/bin/bash
while true
do
  echo "$(date '+%Y-%m-%d %H:%M:%S') ERROR Random failure occurred" >> app.log
  sleep 2
done
