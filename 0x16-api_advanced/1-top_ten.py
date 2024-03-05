#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    user_agent = {'User-Agent': 'Custom-User-Agent'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    response = requests.get(url, headers=user_agent, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            for post in data.get('children', []):
                print(post['data']['title'])
        else:
            print("No data found for the subreddit.")
    else:
        print(None)

# Example usage:
subreddit = 'python'
top_ten(subreddit)
