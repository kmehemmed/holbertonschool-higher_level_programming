#!/usr/bin/python3
"""Sends a POST request with a letter as a parameter to an API"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"

    try:
        r = requests.post(url, data=payload)
        json_dict = r.json()

        if json_dict:
            print("[{}] {}".format(json_dict.get('id'), json_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
