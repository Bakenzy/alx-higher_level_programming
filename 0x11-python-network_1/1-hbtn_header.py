#!/usr/bin/python3
"""This fetches a specified header value from the required url"""
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
