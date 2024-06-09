#!/usr/bin/python3
""" task 2 module """


import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """ return list of all hot spots titles of a subreddit """

    headers = {'User-agent': 'test45'}
    response = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                            .format(subreddit, after), headers=headers)

    if response.status_code == 200:
        outer_json_data = response.json()['data']
        after = outer_json_data['after']
        child_data = outer_json_data['children']

        for post in child_data:
            hot_list.append(post['data']['title'])

        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    else:
        return(None)
