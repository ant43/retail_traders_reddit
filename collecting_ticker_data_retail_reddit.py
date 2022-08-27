import csv
import pandas as pd
from pmaw import PushshiftAPI
import math
import functools
import time
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt
'''This takes a list and returns a string with each elment in the list written in the string seperated by |'''
def _process_list(list):
    stock = ''
    for i in list:
        stock = stock + "|" + i
    return stock[3 :]


'''This function takes a list and devides into num_lists(a number) of diffrent lists of as much equal size as possible'''
def _divide_list(lst, num_lists):
    p = len(lst) // num_lists
    if len(lst)-p > 0:
        return [lst[:p]] + _divide_list(lst[p:], num_lists-1)
    else:
        return [lst]

#now i have to creat the binary search for searching through strings will have to use it to determan what stock tickers are mentond in the data
def _strGreaterThan(string1: str, string2: str) -> bool:
    l = [string1, string2]
    l.sort()
    if l[0] == string1:
        return True
    else:
        return False

def _binarySearchString(stringList, target, beginning, end):

    if beginning <= end:
        middle = (beginning+end) // 2
        if stringList[middle] == target:
            return True
        elif _strGreaterThan(stringList[middle], target):
            return _binarySearchString(stringList, target, middle+1, end)
        elif _strGreaterThan(target, stringList[middle]):
            return _binarySearchString(stringList, target, beginning, middle-1)
    else:
        return False

def _list_of_tickers_in_comment (comment, list_of_tickers):
    commentList = comment.split()
    commentList.sort()
    return list(
        filter(lambda x: _binarySearchString(commentList, x, 0, len(commentList)-1), 
        list_of_tickers)
    )



def collect_retail_data_csv(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets'):
    total_df = collect_retail_data_df(year, month, day, ticker_list,time, subreddit)
    if not total_df.empty:
        #print(total_df['created_utc'])
        #total_df['created_utc'] = total_df['created_utc'].transform(dt.datetime.fromtimestamp)
        total_df.to_csv('./'+csv_file_name+'.csv', header=True,index=False, 
        columns=list(total_df.axes[1]))


        return True
    else:
        return False





def collect_retail_data_df(year, month, day, ticker_list, time = 86400, subreddit = 'wallstreetbets'):
    #this if statment is due to the fact that the push shift API will only work with 200 calls per minute 
    if(len(ticker_list) > 1022*200) :
        num_divisions = math.ceil(len(ticker_list)/(1022*200))
        list_of_calls = _divide_list(ticker_list, num_divisions)
        call_returns_df = []
        for i in list_of_calls:
            call_returns_df.append(collect_retail_data_df(
                year, month, day, i, time, subreddit
            ))
            time.sleep(60)
        return functools.reduce(lambda left, right: left.merge(right, how = 'inner'),
            call_returns_df)

    #if over 200 calls is not nessasary
    date = int(dt.datetime(year, month, day, 0, 0).timestamp())
    after = date
    before = date + time

    #this number is the number of peaces i must devid the list into becuase of how the push shift api limits my or calls
    num_divisions = math.ceil(len(ticker_list)/1022)
    
    lists_of_calls = _divide_list(ticker_list, num_divisions)

    date = int(dt.datetime(year, month, day, 0, 0).timestamp())
    pushShiftAPI = PushshiftAPI()
    after = date
    before = date + time

    q_inputs = map(_process_list, lists_of_calls)

    call_returns = map(lambda x: pushShiftAPI.search_comments(q = x,fields = ['author', 'body', 'created_utc'],
    subreddit=subreddit, before=before, after=after),
    q_inputs)

    call_returns_df = list(map(pd.DataFrame,
    call_returns))

    call_returns_df = list(filter(lambda x: not x.empty,
    call_returns_df))
    if call_returns_df:
        if len(call_returns_df)>1:
            total_df = functools.reduce(lambda left, right: left.merge(right, how = 'inner'),
            call_returns_df) 
        else:
            total_df = call_returns_df[0]
        

        getTickers = lambda x: '|'.join(_list_of_tickers_in_comment(x, ticker_list))
        total_df['ticker'] = list(map(getTickers, total_df['body']))
        total_df['created_utc'] =  total_df['created_utc'].transform(int)
        total_df['created_utc'] = total_df['created_utc'].transform(dt.datetime.fromtimestamp)
        return total_df
    else:
        print('In the subreddit:', subreddit, '\n',
        'in the time period:', dt.datetime.fromtimestamp(after).isoformat(), ' to ', dt.datetime.fromtimestamp(before).isoformat(), '\n',
        'with the list :', *ticker_list[: 10], '...', 'there is no results')
        return pd.DataFrame(columns = ['author', 'body', 'created_utc'])

    






