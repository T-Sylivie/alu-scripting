#!/usr/bin/python3
"""
Module for querying the Reddit API.

This module provides functions to interact with the Reddit API
and retrieve information about hot posts in subreddits.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.

    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid, prints None.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'python:alu.scripting.project:v1.0 (by /u/student)'
    }
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print("None")
                return
            for post in posts:
                title = post.get('data', {}).get('title', '')
                if title:
                    print(title)
        else:
            print("None")
    except Exception:
        print("None")
