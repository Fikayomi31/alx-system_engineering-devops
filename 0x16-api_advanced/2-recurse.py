#!/usr/bin/python3
"""ecursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'Google Chrome Version 119.0.6045.105'}

    response = requests.get(base_url, params=params, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Process the retrieved posts
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there are more posts to fetch
        after = data['data'].get('after')
        if after:
            # Make a recursive call to fetch the next set of posts
            recurse(subreddit, hot_list, after)
        else:
            # Base case: no more posts to fetch, return the final hot_list
            return hot_list
    elif response.status_code == 404:
        # Invalid subreddit, return None
        return None
