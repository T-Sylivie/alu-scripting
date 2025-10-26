#!/usr/bin/python3
"""
Module to query Reddit API for subreddit subscriber count.

This module contains a function that retrieves the total number
of subscribers for a given subreddit using Reddit's API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        int: The number of subscribers, or 0 if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    headers = {
        'User-Agent': 'python:subreddit.subscriber.counter:v1.0 (by /u/studentproject)'
    }
    
    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0
            
    except Exception:
        return 0

