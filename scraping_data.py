#use pushscrap to get a lot of data off of reddit
import csv
import pandas as pd
from pmaw import PushshiftAPI
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt
#Now we will acces the reddit app




#get a list of the stock tickers
stock_tickers = pd.read_csv("z3tagczldqedjrsv.csv")['TICKER'].tolist()






#might need to change how this is done to make it more effecent but so far I think it is actualy more memory effecent to
#creat the data frame and csv files one day and stock ticker at a time
def get_data_about_stock(date, ticker):
    pushShiftAPI = PushshiftAPI()
    #this is the fact that we are looking at the whole day for this thing
    after = date
    before = date + 86400
    subreddit="wallstreetbets"
    comments = pushShiftAPI.search_comments(q = ticker,fields = ['author', 'body', 'created_utc'],subreddit=subreddit, 
    before=before, after=after)
    comments_df = pd.DataFrame(comments)
    comments_df['created_utc'] = comments_df['created_utc'].transform(dt.datetime.fromtimestamp)
    comments_df['stock'] = 'GME'
    comments_df.to_csv('./'+ticker + '_' +str()+'.csv', header=True,
     index=False, columns=list(comments_df.axes[1]))



