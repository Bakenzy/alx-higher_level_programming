#!/usr/bin/python3
"""This connects to a github account"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/users/{sys.argv[1]}"
    header = {"Authorization": f"Bearer {sys.argv[2]}",
              "X-GitHub-Api-Version": "2022-11-28"}
    req = requests.get(url, headers=header)
    try:
        print(req.json()['id'])
    except KeyError:
        print("None")
