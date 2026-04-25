#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}

    r = requests.post(url, data=payload)
    print(r.text)
