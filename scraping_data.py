#use pushscrap to get a lot of data off of reddit
import csv
import pandas as pd
from pmaw import PushshiftAPI
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt
#Now we will acces the reddit app





#def getDataAboutStock(stock, date, stock)

pushShiftAPI = PushshiftAPI()

#this is to test it so I am not spending a lot of time doing these things
before = int(dt.datetime(2021,2,1,0,1).timestamp())
after = int(dt.datetime(2021,2,1,0,0).timestamp())


subreddit="wallstreetbets"
comments = pushShiftAPI.search_comments(q = 'GME',fields = ['author', 'body', 'created_utc'],subreddit=subreddit, before=before, after=after)
comments_df = pd.DataFrame(comments)
comments_df['created_utc'] = comments_df['created_utc'].transform(dt.datetime.fromtimestamp)
comments_df['stock'] = 'GME'
comments_df.to_csv('./'+'wsb_comments'+'.csv', header=True, index=False, columns=list(comments_df.axes[1]))