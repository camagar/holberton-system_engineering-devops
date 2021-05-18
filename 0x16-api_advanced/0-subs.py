#!/usr/bin/python3
""" total of subscribers"""

import requests


base_url = 'http://reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    """number of suscribers"""
    headers = {'User-agent': 'karenahv'}
    req = requests.get(base_url.format(subreddit), headers=headers)
    if req.status_code != 200:
        return 0
    return req.json().get('data').get('subscribers')
