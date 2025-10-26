#!/usr/bin/python3
"""
Module for recursively querying Reddit API and counting keywords.

This module provides functions to recursively query the Reddit API,
parse hot article titles, and count occurrences of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively count and print sorted keyword occurrences in hot posts.

    Queries the Reddit API recursively, parses titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count.
        after (str): Pagination token for next page (default: None).
        word_count (dict): Dictionary tracking word counts (default: None).

    Returns:
        None: Prints results directly.
    """
    if word_count is None:
        word_count = {}

    if subreddit is None or not isinstance(subreddit, str):
        return

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
            return

        data = response.json()
        posts_data = data.get('data', {})
        posts = posts_data.get('children', [])

        if not posts and after is None:
            return

        for post in posts:
            title = post.get('data', {}).get('title', '')
            if title:
                words_in_title = title.lower().split()

                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    count = words_in_title.count(keyword_lower)
                    if count > 0:
                        if keyword_lower in word_count:
                            word_count[keyword_lower] += count
                        else:
                            word_count[keyword_lower] = count

        after = posts_data.get('after')

        if after is None:
            if word_count:
                sorted_words = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    print("{}: {}".format(word, count))
            return

        return count_words(subreddit, word_list, after, word_count)

    except Exception:
        return
