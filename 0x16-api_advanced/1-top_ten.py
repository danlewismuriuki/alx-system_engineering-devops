#!/usr/bin/python3
"""task 1 module"""
import requests
import sys


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to retrieve the hot posts from.

    Returns:
        None: Prints the titles of the hot posts to the console.
    """
    # Define the user agent header
    headers = {'User-Agent': 'double_header'}

    # response of the url
    response = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
        sys.argv[1]), headers=headers)

    # check response status code
    if response.status_code == 200:
        # response is stored in the variable
        data = response.json()
        # loop through the data extracting children
        if 'data' in data and 'children' in data['data']:
            # access the children in the data
            posts = data['data']['children']

            # loop through the posts (childrens data) getting the data
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
