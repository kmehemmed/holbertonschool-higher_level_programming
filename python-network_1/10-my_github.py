#!/usr/bin/python3
"""Takes GitHub credentials and uses the GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=HTTPBasicAuth(username, password))

    try:
        json_dict = r.json()
        print(json_dict.get('id'))
    except ValueError:
        print("None")
