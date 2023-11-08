#!/usr/bin/python3
"""function to queries the Reddit API and return
the number of subscribers
"""
import requests


def top_ten(subreddit):
    """Return he total number of subscriber for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 119.0.6045.105'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return 0
    results = response.json()['data']['children']
    for result in results:
        print(result['data']['title'])
