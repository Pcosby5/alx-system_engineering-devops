#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns a list containing the titles of all hot articles
for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list containing the titles of hot articles (default is None).
        after (str): The name of the last post in the previous page (default is None).

    Returns:
        list: A list containing the titles of all hot articles for the subreddit.
              Returns None if no results are found or the subreddit is invalid.
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
