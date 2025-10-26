#!/usr/bin/python3
"""
Module for querying Reddit API.

This module contains functions to interact with the Reddit API
and retrieve information about subreddits.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit,
             or 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        'User-Agent': 'python:subreddit.checker:v1.0 (by /u/student)'
    }

    try:
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False,
                                timeout=10)

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0

    except Exception:
        return 0
