import csv
import pandas as pd
from pmaw import PushshiftAPI
import math
#becuae the API works with datetime I will have to import another package to deal with this
import datetime as dt
'''This takes a list and returns a string with each elment in the list written in the string seperated by |'''
def _process_list(list):
    stock = ''
    for i in list:
        stock = stock + "|" + i
    return stock[3 :]


'''This function takes a list and devides into num_lists(a number) of diffrent lists of as much equal size as possible'''
def _divide_list(list, num_lists):
    input_size = len(list)
    slice_size = input_size / num_lists
    remain = input_size % num_lists
    result = []
    iterator = iter(list)
    for i in range(num_lists):
        result.append([])
        for j in range(slice_size):
            result[i].append(iterator.next())
        if remain:
            result[i].append(iterator.next())
            remain -= 1
    return result


def collect_retail_data(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets'):
    date = int(dt.datetime(year, month, day, 0, 0).timestamp())
    after = date
    before = date + time

    #this number is the number of peaces i must devid the list into becuase of how the push shift api limits my or calls
    num_divisions = math.ceil(len(ticker_list)/10000)
    
    lists_of_calls = _divide_list(list, num_divisions)

    date = int(dt.datetime(year, month, day, 0, 0).timestamp())
    pushShiftAPI = PushshiftAPI()
    after = date
    before = date + time

    q_inputs = map(_process_list, lists_of_calls)

    call_returns = map(lambda x: pushShiftAPI.search_comments(q = x,fields = ['author', 'body', 'created_utc'],
    subreddit=subreddit, before=before, after=after),
    q_inputs)

    call_returns_df = map(pd.DataFrame,
    call_returns)

    call_returns_df = filter(lambda x: not x.empty,
    call_returns_df)


    if call_returns_df:
        total_df = reduce(lambda left, right: left.merge(right, how = 'inner'),
        call_returns_df)
        call_returns_df['created_utc'] = call_returns_df['created_utc'].transform(dt.datetime.fromtimestamp)
        call_returns_df.to_csv('./'+csv_file_name+'.csv', header=True,index=False, columns=list(call_returns_df.axes[1]))
        return True
    else:
        print('In the subreddit:', subreddit, '\n',
        'in the time period:', dt.datetime.fromtimestamp(after).isoformat(), ' to ', dt.datetime.fromtimestamp(before).isoformat(), '\n',
        'with the list :', ticker_list)
        return False

    






