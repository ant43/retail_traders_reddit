#use pushscrap to get a lot of data off of reddit
import csv
from pmaw import PushshiftAPI
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt
#Now we will acces the reddit app


pushShiftAPI = PushshiftAPI()

#this is to test it so I am not spending a lot of time doing these things
before = int(dt.datetime(2021,2,1,0,0).timestamp())
after = int(dt.datetime(2020,12,1,0,0).timestamp())


subreddit="wallstreetbets"
limit=100000
comments = pushShiftAPI.search_comments(subreddit=subreddit, limit=limit, before=before, after=after)
print(f'Retrieved {len(comments)} comments from Pushshift')
print(comments)