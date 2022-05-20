import get_diffrent_day as gbd
import datetime as dt

gbd.get_data_about_stock(dt.datetime(2020, 12, 13, 0, 0).timestamp(), 300, 'GME')
gbd.get_data_about_stock(dt.datetime(2020, 12, 13, 0, 0).timestamp(), 86400, 'GME')
gbd.get_data_about_stock(dt.datetime(2020, 12, 13, 0, 0).timestamp(), 86400*7, 'GME')
gbd.get_data_about_stock(dt.datetime(2020, 12, 13, 0, 0).timestamp(), 86400*30, 'GME')
