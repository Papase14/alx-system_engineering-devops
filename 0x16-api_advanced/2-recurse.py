#!/usr/bin/python3
"""
    This module contains a function that queries the
    Reddit API and returns a list of the hottest post for
    a given subreddit.
"""
import requests
from typing import List, Optional


def recurse(
    subreddit: str, hot_list: List[str] = [], after: Optional[str] = None
) -> List[str]:
    """
    Returns a list of the hottest posts of a subreddit or None.

    Args:
    - subreddit (str): The name of the subreddit to retrieve the
    hottest posts from.
    - hot_list (List[str]): The list of hottest posts.
    - after (Optional[str]): The 'after' parameter for pagination.

    Returns:
    - List[str]: A list of child posts extracted from the hottest
    posts of the given subreddit.
    """
    user_agent = {"User-Agent": "/u/Suspicious-Jelly920"}
    url = f"https://api.reddit.com/r/{subreddit}/hot?after={after}"
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        data = response.json()["data"]
        hottest = data["children"]
        after = data["after"]

        if after is None:
            hot_list.extend(get_children(hottest, len(hottest)))
            return hot_list

        hot_list.extend(recurse(subreddit, hot_list, after=after))
        hot_list.extend(get_children(hottest, len(hottest)))

    return hot_list


def get_children(hottest: List[dict], count: int) -> List[str]:
    """
    Extracts the list of child posts from the hottest posts.

    Args:
    - hottest (List[dict]): The list of hottest posts.
    - count (int): The number of hottest posts.

    Returns:
    - List[str]: A list of child posts extracted from the hottest
    posts of the given subreddit.
    """
    children = []
    for i in range(count):
        children.append(hottest[i]["data"]["title"])
    return children
