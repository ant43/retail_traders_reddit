#will be using praw to scrap information off of reddit
import praw
import pandas as pd
#Now we will acces the reddit app

reddit = praw.Reddit(client_id='5QEZMjC8rrhrCWZPvf3hrg', client_secret='JmmRYmSROtAZMS0SpdempGzi9yyFSw', user_agent='tati_work_web')

hot_posts = reddit.subreddit('all').hot(limit=10)
for post in hot_posts:
    print(post.title)