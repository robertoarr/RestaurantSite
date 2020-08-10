#!/bin/sh -l

echo "Hello $1"
# time=$(date)
# echo "::set-output name=time::$time"

# pytest --html=report.html main.py

python main.py
