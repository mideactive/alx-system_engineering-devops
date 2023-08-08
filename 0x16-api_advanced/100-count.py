#!/usr/bin/python3
"""
100-count
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    children = results.get("children")

    for c in children:
        title = c.get("data").get("title").lower()
        for word in word_list:
            if f' {word.lower()} ' in f' {title} ':
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)
    return word_count


def print_sorted_count(word_count):
    sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_count:
        print(f"{word}: {count}")
