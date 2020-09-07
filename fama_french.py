import pandas as pd
import requests
import zipfile
import io
from time import time

def get_fama_french(factor = 5):

    assert factor == 3 or factor == 5, 'Factor should be only 3 or 5'

    if factor ==5:

        site = r'http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_daily_CSV.zip'
        file = r'F-F_Research_Data_5_Factors_2x3_daily.CSV'

    elif factor == 3:

        site = r'http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip'
        file = r'F-F_Research_Data_Factors_daily.CSV'

    df_FF = read_csv_from_zip(site,file)

    df_FF.rename(columns={"Unnamed: 0": "Date"},inplace=True)

    return df_FF

def read_csv_from_zip(site,file):
    '''
    reads csv from zip file from the interent into a dataframe

    paramaters:
        site:str:target link
        file:str:target file in zip file

    returns:
        df:pandas dataframe:a dataframe
    '''

    request = requests.get(site).content
    zip_folder = zipfile.ZipFile(io.BytesIO(request))

    target_csv = zip_folder.open(file)

    df = pd.read_csv(target_csv,skiprows=[0,1,2])

    return df

def get_price_yahoo(ticker,date_end = int(time()),date_start=None,freq='1d'):

    if not date_start:

        date_start = date_end - 31536000

    else:

        date_start = int(date_start)

    request = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=1567807509&period2={date_end}&interval={freq}&events=history'

    df = pd.read_csv(io.BytesIO(requests.get(request).content))

    return df


def get_price(ticker,date_end,date_start):

    return None