#!/bin/bash

echo "running PEP8 verification..."
flake8 --max-line-length=120 --statistics --count --exclude=.git,./.venv/ --ignore=E402 . || exit 1

exit;
