#!/usr/bin/python3
""" task 0 module """

import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    Args:
        subreddit (str): The name of the subreddit to query.
    Returns:
        int: The number of subscribers for the subreddit.
        Returns 0 if the subreddit is invalid.
    """
    # Set the User-Agent to a custom value to avoid being blocked by Reddit
    headers = {'User-Agent': 'test'}

    # Get response of the reddit url
    response = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        sys.argv[1]), headers=headers, allow_redirects=False)
    # Check status code of the response
    if response.status_code == 200:
        # store the response in json format
        data = response.json()
        # extract subscribers from the data
        return data['data']['subscribers']
    else:
        # return 0 when it fails
    return 0

