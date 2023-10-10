#!/usr/bin/python3
"""
    This module contains a function that queries the
    Reddit API and returns a list of the hottest post for
    a given subreddit.
"""
import requests
from typing import List


def recurse(
    subreddit: str, hot_list: List[str] = [], after: str = "", count: int = 0
) -> List[str]:
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Args:
        - subreddit (str): The name of the subreddit to retrieve hot
        posts from.
        - hot_list (List[str], optional): A list to store the titles
        of the hot posts (default is an empty list).
        - after (str, optional): The ID of the last post in the previous
        batch (default is an empty string).
        - count (int, optional): The total number of posts retrieved so
        far (default is 0).

    Returns:
        List[str]: A list of strings containing the titles of all hot
        posts on the given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "/u/Suspicious-Jelly920"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")

    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
