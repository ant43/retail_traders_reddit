import collecting_ticker_data_retail_reddit as cr
import datetime as df


cr.collect_retail_data_csv(year = 2020, month = 12, day =13, ticker_list = ['the', 'GME'],
 csv_file_name = 'testCSV', time = 86400, subreddit = 'wallstreetbets')