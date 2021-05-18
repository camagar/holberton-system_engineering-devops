#!/usr/bin/python3
""" top ten posts"""

import requests


base_url = 'http://reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    """top ten title posts"""
    i = 0
    headers = {'User-agent': 'karenahv'}
    req = requests.get(base_url.format(subreddit), headers=headers)
    if not req:
        print("None")
        return
    info = req.json().get('data').get('children')
    if req.status_code != 200 or not info:
        print("None")
        return
    for hot in info:
        if (i < 10):
            print(hot.get('data').get('title'))
            i = i + 1
