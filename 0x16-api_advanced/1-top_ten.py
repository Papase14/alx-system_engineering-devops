#!/usr/bin/python3
"""
    This module contains a function that queries the
    Reddit API and prints the titles of the first 10
    hot posts listed on the given subreddit
"""

import requests


def top_ten(subreddit: str) -> None:
    """
    This function sends a GET request to the Reddit API to retrieve the
    top ten hottest posts in the specified subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    headers = {"User-Agent": "/u/Suspicious-Jelly920"}
    url = f"https://api.reddit.com/r/{subreddit}/hot/"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        hottest_posts = response.json()["data"]["children"]
        for post in hottest_posts[:10]:
            print(post["data"]["title"])
    else:
        print("None")
