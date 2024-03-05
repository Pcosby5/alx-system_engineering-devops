# #!/usr/bin/python3

# """
# a function to retrieve the number of subscribers for a given subreddit
# using the Reddit API.
# """

# import requests


# def number_of_subscribers(subreddit):
#     """
#     Retrieve the number of subscribers for a given subreddit.

#     Args:
#         subreddit (str): The name of the subreddit.

#     Returns:
#         int: The number of subs for the subreddit. Returns 0 if the
#         subreddit is invalid.
#     """
#     # Reddit API endpoint for fetching subreddit information
#     url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

#     # Set custom User-Agent to avoid Too Many Requests error
#     headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}

#     # Send GET request to the Reddit API
#     response = requests.get(url, headers=headers, allow_redirects=False)

#     # Check if the response is successful
#     if response.status_code == 200:
#         # Extract number of subscribers from the response JSON
#         data = response.json()
#         subscribers = data['data']['subscribers']
#         return subscribers
#     else:
#         # Invalid subreddit or other error occurred
#         return 0


#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
