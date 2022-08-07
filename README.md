


# retail_traders_reddit
This is going to scrap data off of subreddits. you will chose the time the subreddit and the data that will be scraped off of reddit
In this in the collecting_ticker_data_retail_reddit file Function call

collect_retail_data_csv(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets')
=======

        This looks looks through reddit comment data on a specific time frame (starting at one date then adding the number of seconds as specified), and specific 
        list of strings too look for in the comments. creates a CSV file which includes the body of the comment, the aouther and the time the comment was made

        Parameters
        ----------
        year : int
            the year of the starting date
        month: int
            the month of the starting date
        day: int
            the day of the starting date
        ticker_list: list of str
            the list of strings of the name of stocks that you want to find when going throu the list
        csv_file_name: str
            the name csv file (with no '.csv' in it) that will be created by the function
        time: int, optinal
            the lenght of time you want to look for, it is set to 86400 which is one day so it is looking for all date not more then one day away from the
            start date
        subreddit: str
            the subreddit that you will be looking through




        Returns
        ------
        boolian
            returns a true if the data your looking for exists, returns a false other if it does not







collect_retail_data_df(year, month, day, ticker_list, csv_file_name, time = 86400, subreddit = 'wallstreetbets')

        This looks looks through reddit comment data on a specific time frame (starting at one date then adding the number of seconds as specified), and specific 
        list of strings too look for in the comments. it returns a data frame which includes the body of the comment, the aouther and the time the comment was made

        Parameters
        ----------
        year : int
            the year of the starting date
        month: int
            the month of the starting date
        day: int
            the day of the starting date
        ticker_list: list of str
            the list of strings of the name of stocks that you want to find when going throu the list
        time: int, optinal
            the lenght of time you want to look for, it is set to 86400 which is one day so it is looking for all date not more then one day away from the
            start date
        subreddit: str
            the subreddit that you will be looking through




        Returns
        ------
        pandas.DataFrame
            it returns a data frame which includes the body of the comment, the aouther and the time the comment was made, if there is no
            data to be found it will print it and then return an empty data frame

