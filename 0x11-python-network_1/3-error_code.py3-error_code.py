#!/usr/bin/python3
"""This fetches from the required url and handles errors"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode())
    except error.HTTPError as e:
        print(f"Error code: {e.code}
