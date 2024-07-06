#!/usr/bin/python3
"""This sends a post request with an email to the required url"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    req = requests.post(url, data=data)
    print(req.text)
