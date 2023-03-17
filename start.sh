#!/bin/bash
# Author => Aman Raj
# since => 2023
# copyright => 2023
# encoding => UTF-8

set -eu
export PYTHONUNBUFFERED=true
VIRTUALENV=.data/venv
if [ ! -d $VIRTUALENV ]; then
    python3 -m venv $VIRTUALENV
fi

if [ ! -f $VIRTUALENV/bin/pip ]; then
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

$VIRTUALENV/bin/pip install -r requirements.txt
$VIRTUALENV/bin/python3 main.py
