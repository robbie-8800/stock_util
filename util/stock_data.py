import pandas_datareader as pdr
import time

def get(ticker, start_date, end_date):
    """
    Reference: https://www.programcreek.com/python/example/92135/pandas_datareader.data.get_data_yahoo
    Gets sp500 price data
    :param start_date: starting date for sp500 prices
    :type start_date: string of date "Y-m-d"
    :param end_date: end date for sp500 prices
    :type end_date: string of date "Y-m-d"
    :return: sp500_data.csv
    """
    print("Getting data {} from {} to {}".format(ticker, start_date, end_date))
    i = 1
    try:
        data = pdr.get_data_yahoo(ticker, start_date, end_date)
    except ValueError:
        print("ValueError, trying again")
        i += 1
        if i < 5:
            time.sleep(10)
            data = pdr.get_data_yahoo(ticker, start_date, end_date)
        else:
            print("Tried 5 times, Yahoo error. Trying after 2 minutes")
            time.sleep(120)
            data = pdr.get_data_yahoo(ticker, start_date, end_date)

    return data.reset_index()
            