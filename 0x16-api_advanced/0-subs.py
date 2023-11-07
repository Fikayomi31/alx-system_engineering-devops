#!/usr/bin/python3
"""function to queries the Reddit API and return
the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Return he total number of subscriber for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    # headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(url)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')
