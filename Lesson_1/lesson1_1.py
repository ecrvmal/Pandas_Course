# https://www.youtube.com/watch?v=QlPmbcSBin4

import pandas as pd


# Series - столбцы
# Dataframe
# Index
# Lable - Значение

pd.DataFrame([[1,5,6,3],[2,10,12,6]],
             index = ['station_1', 'station_2'],
             columns=['wind', 'solar', 'pressure', 'speed'])


df = pd.read_csv('data.csv', encoding='1251')

pd.options.display.max_columns = None             #  after this display all columns, else displays first and last
# print(df)                   # print all df
# print(df.head(10))        # print first 5 raws
print(df.tail(10))        # print first 5 raws

pd.describe_option()   # long list of options
pd.set_option('display.max_columns', 40)    # set option : max_columns
print(pd.get_option('display.max_columns'))                             #  print option  -> 40

print(df.tail(10))        # print first 5 raws

print(df.dtypes)                # checking type of data in columns
# DR_Dat         object
# DR_Tim         object
# DR_NChk         int64
# DR_NDoc         int64
# DR_Apt          int64
# DR_Kkm          int64
# DR_TDoc        object
# DR_TPay         int64

# change display format
pd.set_option('display.float_format', '{:.2f}'.format)    # format was 2.000100e+11
print(df.tail(10))                                        # format now 200010027618.00


