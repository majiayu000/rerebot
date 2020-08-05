import praw
from requests import Session

session = Session()
session.proxies['https'] = 'socks5://localhost:10808'   #使用代理 否则连不上reddit
reddit = praw.Reddit('bot1',requestor_kwargs={'session': session} )
subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")