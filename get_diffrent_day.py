import csv
import pandas as pd
from pmaw import PushshiftAPI
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt

def get_data_about_stock(date, time_length, ticker):
    date = int(date)
    pushShiftAPI = PushshiftAPI()
    #this is the fact that we are looking at the whole day for this thing
    after = date
    before = date + time_length
    subreddit="wallstreetbets"
    comments = pushShiftAPI.search_comments(q = ticker,fields = ['author', 'body', 'created_utc'],subreddit=subreddit, 
    before=before, after=after)
    comments_df = pd.DataFrame(comments)
    if not comments_df.empty:
        comments_df['created_utc'] = comments_df['created_utc'].transform(dt.datetime.fromtimestamp)
        comments_df['stock'] = ticker
        comments_df.to_csv(('./'+ticker + '_' +str(dt.datetime.fromtimestamp(date))+'.csv').replace(' ', '_').replace(':', '-'), header=True,
        index=False, columns=list(comments_df.axes[1]))
    else:
        print(ticker +' did not have any data on this day')