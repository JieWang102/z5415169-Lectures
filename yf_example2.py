""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf

def yf_prc_to_csv(tic, pth, start=None, end=None): #fuction名字：yf_prc_to_csv
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    #function做了两件事：
    df = yf.download(tic, start=start, end=end) #1.yf下载三个数据
    df.to_csv(pth) #2.下载路径

#module中yf_prc_to_csv('QAN.AX', 'qan_stk_prc.csv')执行function

#console中import yf_example2之后才能使用其中function，代码见课件

#print (f"the value of __name__ is: '{__name__}'")
#无importyf_example时，__name__值为__main__
#import function后，值为yf_example2

import os

if __name__ == '__main__':
    tic = "QAN.AX"
    datadir = r'/Users/wangjie/PycharmProjects/toolkit_/data'
    pth = os.path.join(datadir, 'qan_stk_prc.csv')
    yf_prc_to_csv(tic, pth)

