#!/usr/bin/python3
"""Function to count words in all hot
posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 404:
        return

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title").lower()
        for word in word_list:
            if f' {word.lower()} ' in f' {title} ':
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(
            counts.items(),
            key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_counts:
            print(f"{word}: {count}")
