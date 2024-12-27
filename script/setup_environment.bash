#!/bin/bash

echo Creating environment

# Create the environment.

python3 -m venv ./venv
source ./venv/bin/activate
# Install requirements
pip install -r requirements_test.txt

chmod a+x ./setup.py

echo Python environment created and requirements installed.