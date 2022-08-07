import csv
import pandas as pd
from pmaw import PushshiftAPI
import math
import functools
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


def collect_retail_data_csv(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets'):
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
    print('-------------------------------------------------------------------------')
    if call_returns_df:
        if len(call_returns_df)>1:
            total_df = list(functools.reduce(lambda left, right: left.merge(right, how = 'inner'),
            call_returns_df))
        else:
            total_df = call_returns_df[0]
        
        total_df['created_utc'] = total_df['created_utc'].transform(dt.datetime.fromtimestamp)
        total_df.to_csv('./'+csv_file_name+'.csv', header=True,index=False, columns=list(total_df.axes[1]))
        return True
    else:
        print('In the subreddit:', subreddit, '\n',
        'in the time period:', dt.datetime.fromtimestamp(after).isoformat(), ' to ', dt.datetime.fromtimestamp(before).isoformat(), '\n',
        'with the list :', *ticker_list[: 10], '...')
        return False




def collect_retail_data_df(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets'):
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
    print('-------------------------------------------------------------------------')
    if call_returns_df:
        if len(call_returns_df)>1:
            total_df = list(functools.reduce(lambda left, right: left.merge(right, how = 'inner'),
            call_returns_df))
        else:
            total_df = call_returns_df[0]
        
        total_df['created_utc'] = total_df['created_utc'].transform(dt.datetime.fromtimestamp)
        return total_df
    else:
        print('In the subreddit:', subreddit, '\n',
        'in the time period:', dt.datetime.fromtimestamp(after).isoformat(), ' to ', dt.datetime.fromtimestamp(before).isoformat(), '\n',
        'with the list :', *ticker_list[: 10], '...')
        return pd.DataFrame()

    






