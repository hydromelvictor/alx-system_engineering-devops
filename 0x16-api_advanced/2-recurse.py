#!/usr/bin/python3
"""Write a recursive function that queries
the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """recursion subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "hydro agent 1.0"}
    params = {
        "limit": 10,
        "after": after,
        "count": count
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
