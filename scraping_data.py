#use pushscrap to get a lot of data off of reddit
import csv
import pandas as pd
from pmaw import PushshiftAPI
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt




'''
This function takes up year, month, and day, and the stock ticker along with the time and csv_file_name, the time is how much into the 
future you want to look at the stock, the csv file name gives you the name of the csv file you want

It givs you the author, the body of the comment and the created_utc(time of comment)'''
def get_data_about_stock( year,month,day ,ticker, csv_file_name, time = 86400 ):
    date = int(dt.datetime(year, month, day, 0, 0).timestamp())
    pushShiftAPI = PushshiftAPI()
    #this is the fact that we are looking at the whole day for this thing
    after = date
    before = date + time
    subreddit="wallstreetbets"
    comments = pushShiftAPI.search_comments(q = ticker,fields = ['author', 'body', 'created_utc'],
    subreddit=subreddit, before=before, after=after)
    comments_df = pd.DataFrame(comments)
    if not comments_df.empty:
        comments_df['created_utc'] = comments_df['created_utc'].transform(dt.datetime.fromtimestamp)
        comments_df.to_csv('./'+csv_file_name+'.csv', header=True,index=False, columns=list(comments_df.axes[1]))
        print(ticker + ' has data')
        return True
    else:
        print(ticker +' did not have any data on asked timeframe')
        return False




#get a list of the stock tickers
stock_tickers = pd.read_csv("listOfTICKERS.csv")['TICKER'].tolist()
#this is the starting date y,m,d,h,s is how it is written

def _process_list(list):
    stock = ''
    for i in list:
        stock = stock + "|" + i
    return stock[3 :]

how_many = len(stock_tickers)
while(not get_data_about_stock( year = 2022 ,ticker = _process_list(stock_tickers), csv_file_name = 'allTheFiles', month = 8, day = 4,   time = 86400 )):
    print(len(stock_tickers))
    del stock_tickers[0]
    how_many = len(stock_tickers)

print('--------------------------------------------------------')
print(how_many)





#print(len(stock))
#it will continu untill the end date
'''while date < dt.datetime(2022, 12, 14, 0, 0).timestamp():
    list(map(lambda x : get_data_about_stock(date,x),
        stock_tickers ))
    date = date + 86400'''