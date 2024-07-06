#!/usr/bin/python3
"""This fetches a header value from the required url using requests"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
