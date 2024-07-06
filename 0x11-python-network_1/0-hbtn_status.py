#!/usr/bin/python3
"""This fetches from the required url"""
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    html = res.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode(encoding='UTF-8}}"}
