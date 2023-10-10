#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests
from typing import List, Dict


def count_words(subreddit: str, word_list: List[str], after: str = '', word_dict: Dict[str, int] = {}) -> None:
    """
    A function that queries the Reddit API, parses the titles of hot articles in a given subreddit,
    and prints a sorted count of specified keywords.
    It is case-insensitive and treats JavaScript as a separate keyword from Java.

    :param subreddit: A string representing the name of the subreddit to query.
    :param word_list: A list of strings representing the keywords to count.
    :param after: A string representing the 'after' parameter for pagination
    in the Reddit API (optional, default is an empty string).
    :param word_dict: A dictionary representing the count of keywords (optional,
    default is an empty dictionary).
    :return: None
    """
    if not word_dict:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_dict:
            if count:
                print(f'{word}: {count}')
        return None

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=parameters, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()['data']
        hot = data['children']
        aft = data['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict:
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dict)
