#!/usr/bin/env python

import sys

import requests

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <url>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
