import get_diffrent_day as gbd

gdb.get_data_about_stock(dt.datetime(2020, 12, 13, 0, 0).timestamp(), 86400, 'GME')
gdb.get_data_about_stock(dt.datetime(2020, 12, 13, 0, 0).timestamp(), 86400*7, 'GME')
gdb.get_data_about_stock(dt.datetime(2020, 12, 13, 0, 0).timestamp(), 86400*30, 'GME')
