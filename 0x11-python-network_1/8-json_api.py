#!/usr/bin/python3
"""This script takes a leter and sends a post request to our url"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    url = 'http://0.0.0.0:5000/search_user'
    req = requests.post(url, data=data)
    try:
        ans = req.json()
        if ans == {}:
            print("No result")
        else:
            print(f"[{ans['id']}] {ans['name']}")
    except ValueError:
        print("Not a valid JSON")
