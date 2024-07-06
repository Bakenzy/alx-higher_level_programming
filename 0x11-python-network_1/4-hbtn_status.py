#!/usr/bin/python3
"""This fetches from the required url"""
import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(res.text)}")
    print(f"\t- content: {res.text}")
