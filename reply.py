import praw
import pdb
import re
import os
from requests import Session




session = Session()
session.proxies['https'] = 'socks5://localhost:10808'

# Create the  Reddit instance
reddit = praw.Reddit('bot1',requestor_kwargs={'session': session})


if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=5):

    if submission.id not in posts_replied_to:

        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("It is good!!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)



with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
