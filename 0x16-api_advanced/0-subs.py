#!/usr/bin/python3
"""
    This module contains a function that queries the
    Reddit API and returns the number of subscribers
    for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit: str) -> int:
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit.
    """
    headers = {"User-Agent": "/u/Suspicious-Jelly920"}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
    else:
        subscribers = 0
    return subscribers
