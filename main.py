import praw
import requests
import time

reddit = praw.Reddit(
    client_id="kxf0GGRMJumzRHQkxNNjhQ",
    client_secret="1jR3OC3TB35DoYV7lF9bayCUOm5Mvg",
    user_agent="<console:PUPPY:1.0>",
    username="purrfect--puppy--bot",
    password="66bt9wyDHcrSZ8E")


def find_puppy_pic_link():
    """Returns a link to a puppy picture from the Dog API"""

    response = requests.get(url="https://dog.ceo/api/breeds/image/random")
    response.raise_for_status()

    response = response.json()["message"]

    return response


# sort through each comment of the top 10 "hot posts, for a given subreddit"
for submission in reddit.subreddit("testingground4bots").hot(limit=10):

    for comment in submission.comments:  # searches comments from oldest to newest by default
        if "pup4me!" in comment.body:
            print(f"Replying to comment: {comment.body}...")
            comment.reply(body=find_puppy_pic_link())
            time.sleep(600)  # arbitrary amount of time to wait, so as to not exceed API rate limit
