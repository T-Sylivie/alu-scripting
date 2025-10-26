#!/usr/bin/python3
"""
Module for recursively querying the Reddit API.

This module provides functions to recursively interact with the Reddit API
and retrieve all hot posts from a subreddit using pagination.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query Reddit API and return list of all hot article titles.

    Uses recursion and pagination to retrieve all hot posts from a subreddit.
    If no results are found or subreddit is invalid, returns None.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): Accumulator list for hot post titles (default: []).
        after (str): Pagination token for next page (default: None).

    Returns:
        list: List of all hot post titles, or None if subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'python:alu.scripting.project:v1.0 (by /u/student)'
    }
    params = {'limit': 100}

    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json()
        posts_data = data.get('data', {})
        posts = posts_data.get('children', [])

        if not posts:
            return None if not hot_list else hot_list

        for post in posts:
            title = post.get('data', {}).get('title', '')
            if title:
                hot_list.append(title)

        after = posts_data.get('after')

        if after is None:
            return hot_list

        return recurse(subreddit, hot_list, after)

    except Exception:
        return None
