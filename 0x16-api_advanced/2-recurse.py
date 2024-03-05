#!/usr/bin/python3
"""
Recursively queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """and returns a list of the titles of all hot articles
    """
    if hot_list is None:
        hot_list = []

    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-Agent': 'Custom-User-Agent'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after=' + after

    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children', [])
            for post in children:
                hot_list.append(post['data']['title'])
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
