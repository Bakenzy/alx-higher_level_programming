#!/usr/bin/python3
"""This fetches from the required url and handles errors"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
