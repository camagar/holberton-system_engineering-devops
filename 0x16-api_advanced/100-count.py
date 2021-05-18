#!/usr/bin/python3
""" all posts recursively"""

import requests
import sys


base_url = 'http://reddit.com/r/{}/hot.json'


def count_words(subreddit, word_list, hot_list=[], after=""):
    """all posts recursively"""
    headers = {'User-agent': 'camagar'}
    params = {'t': all, 'after': after}
    req = requests.get(base_url.format(subreddit), headers=headers,
                       params=params)
    if not req or req.status_code != 200:
        return None
    info = req.json()
    for hot in info['data']['children']:
        hot_list.append(hot['data']['title'])
    after = info.get('data').get('after')
    if after:
        count_words(subreddit, word_list, hot_list, after)
    return hot_list
