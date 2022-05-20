#use pushscrap to get a lot of data off of reddit
import csv
import pandas as pd
from pmaw import PushshiftAPI
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt




#might need to change how this is done to make it more effecent but so far I think it is actualy more memory effecent to
#creat the data frame and csv files one day and stock ticker at a time
def get_data_about_stock(date, ticker):
    date = int(date)
    pushShiftAPI = PushshiftAPI()
    #this is the fact that we are looking at the whole day for this thing
    after = date
    before = date + 86400
    subreddit="wallstreetbets"
    comments = pushShiftAPI.search_comments(q = ticker,fields = ['author', 'body', 'created_utc'],subreddit=subreddit, 
    before=before, after=after)
    comments_df = pd.DataFrame(comments)
    if not comments_df.empty:
        print(ticker + ' has data')
        comments_df['created_utc'] = comments_df['created_utc'].transform(dt.datetime.fromtimestamp)
        comments_df['stock'] = ticker
        comments_df.to_csv(('./'+ticker + '_' +str(dt.datetime.fromtimestamp(date))+'.csv').replace(' ', '_').replace(':', '-'), header=True,
        index=False, columns=list(comments_df.axes[1]))
        print(ticker + ' has data')
    else:
        print(ticker +' did not have any data on this day')



#get a list of the stock tickers
stock_tickers = pd.read_csv("listOfTICKERS.csv")['TICKER'].tolist()
#this is the starting date y,m,d,h,s is how it is written
date = dt.datetime(2020, 12, 13, 0, 0).timestamp()
#it will continu untill the end date
while date < dt.datetime(2022, 12, 14, 0, 0).timestamp():
    list(map(lambda x : get_data_about_stock(date,x),
        stock_tickers ))
    date = date + 86400
