


# retail_traders_reddit
This script scraps data off subreddits. You choose the time posts start, the particular subreddit, and the data that will be scraped off the subreddit.

collect_retail_data_csv(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets')
=======

        This looks through the subreddit comments data on a specific time frame (starting at year, month, day specified, then adding a specific number of seconds with the default beuing a day=86,400 seconds, and a specific list of strings to look for in the comments, which you will probably want to be stock tickers or company names. It creates a CSV file which includes the author of the comment, the body of the comment, the time the comment was made, and a "ticker" columns that reports the search terms found in the body of the message. For exanmple, if two of the search terms were "AAPL" and "GOOG" the ticker column with be the string "AAPL|GOOG" (that is, the search terms separated by the pipe symbol "|"

        Parameters
        ----------
        year : int
            the year of the starting date
        month: int
            the month of the starting date
        day: int
            the day of the starting date
        ticker_list: list of str
            the list of strings to be searched (e.g., name of stocks, or tickers)
        csv_file_name: str
            the name csv file (with no '.csv' in it) that will be created by the function
        time: int, optional
            the lenght of time you want to look for in seconds. The default is set to 86,400 seconds which is one day
        subreddit: str, optional
            the subreddit that you will be looking through, e.g., "wallstreetbets" (which is the default)




        Returns
        ------
        boolean
            returns 'True' if the data you're looking for exists, returns 'False' if nothing was returnd in the search







collect_retail_data_df(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets')
=======

         This similar looks through the subreddit comments data on a specific time frame (starting at year, month, day specified, then adding a specific number of seconds with the default beuing a day=86,400 seconds, and a specific list of strings to look for in the comments, which you will probably want to be stock tickers or company names. It a pandas dataframe including the author of the comment, the body of the comment, the time the comment was made, and a "ticker" columns that reports the search terms found in the body of the message. For exanmple, if two of the search terms were "AAPL" and "GOOG" the ticker column with be the string "AAPL|GOOG" (that is, the search terms separated by the pipe symbol "|". The difference compared with "collect_retail_data_csv" is that this function returns a dataframe. 

        Parameters
        ----------
        year : int
            the year of the starting date
        month: int
            the month of the starting date
        day: int
            the day of the starting date
        ticker_list: list of str
            the list of strings to be searched (e.g., name of stocks, or tickers)
        time: int, optinal
            the lenght of time you want to look for in seconds. The default is set to 86,400 seconds which is one day
        subreddit: str, optional
            the subreddit that you will be looking through, e.g., "wallstreetbets" (which is the default)




        Returns
        ------
        pandas.DataFrame
            It returns a pandas dataframe which includes the author of the comment, the body ofg the comment, the time the comment was made, and a string containing the search terms found in the comment separated by "|" (for example, if "GOOG", "F", and "AAPL" are search terms and "F" and "GOOG" ap[pear in the comment, the last column element will be the string "F|GOOG"). It returns an empty dataframe if the search returns no terms. 

