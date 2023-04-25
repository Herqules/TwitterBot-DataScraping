import os
import requests
import json

BEARER_TOKEN = "BEARER TOKEN HERE"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

def get_top_tweets(usernames):
    tweets_dict = {}
    for username in usernames:
        user_response = requests.get(f"https://api.twitter.com/2/users/by/username/{username}", headers=headers)
        if user_response.status_code != 200:
            raise ValueError(f"Invalid response {user_response.status_code}: {user_response.text}")
        user_id = user_response.json()["data"]["id"]
        tweets_response = requests.get(f"https://api.twitter.com/2/users/{user_id}/tweets", headers=headers, params={"max_results": 10})
        if tweets_response.status_code != 200:
            raise ValueError(f"Invalid response {tweets_response.status_code}: {tweets_response.text}")
        tweets_dict[username] = [tweet["text"] for tweet in tweets_response.json()["data"]]
    return tweets_dict


if __name__ == "__main__":
    usernames = ["Reuters", "AFP", "AP"]
    try:
        tweets_dict = get_top_tweets(usernames)
        for username, tweets in tweets_dict.items():
            print(f"Tweets from {username}:")
            for tweet in tweets:
                print(tweet)
            print()  # Add blank line for separation
    except Exception as e:
        print(f"An error occurred: {str(e)}")
