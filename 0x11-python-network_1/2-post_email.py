#!/usr/bin/python3
"""This sends a post request with an email to the required url"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    req = Request(url, urlencode(data).encode())
    with urlopen(req) as res:
        print(res.read().decode())
