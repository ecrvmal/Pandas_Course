# https://www.youtube.com/watch?v=GAECkZMPkyI

# -------------------------------------  Lesson 2_1 Load data --------------------------

import pandas as pd

df = pd.read_csv('data.csv', encoding='1251')
df2 = pd.read_csv('data.csv', encoding='1251')

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

# ------------------------- Lesson_2_2 -------------------------
# https://www.youtube.com/watch?v=GAECkZMPkyI

print(df.shape)    # dimensioning of df
                    # (4462, 21 )
print(df.size)       # num of elements
                     # 93702
print(df.dtypes)    #  type of data bu clolumns

print(df.index)      # what is index
                     # RangeIndex(start=0, stop=4462, step=1)

# index example
index_data = pd.DataFrame([[1,5,6,3],[2,10,12,6]],
             index = ['station_1', 'station_2'],
             columns=['wind', 'solar', 'pressure', 'speed']).index

print(index_data)    # Index(['station_1', 'station_2'], dtype='object')

print(df.index)   # list of rows
print(df.columns)
'''
output df.columns    - list of columns: 
Index(['DR_Dat', 'DR_Tim', 'DR_NChk', 'DR_NDoc', 'DR_Apt', 'DR_Kkm', 'DR_TDoc',
       'DR_TPay', 'DR_CDrugs', 'DR_NDrugs', 'DR_Suppl', 'DR_Prod', 'DR_Kol',
       'DR_CZak', 'DR_CRoz', 'DR_SDisc', 'DR_CDisc', 'DR_BCDisc', 'DR_TabEmpl',
       'DR_VZak', 'DR_Pos'],
      dtype='object')
'''

column_list = ['DR_Dat', 'DR_Tim', 'DR_NChk', 'DR_NDoc', 'DR_Apt', 'DR_NDrugs','DR_Kol',
               'DR_CZak', 'DR_CRoz', 'DR_SDisc', 'DR_TPay', 'DR_CDrugs',  'DR_Suppl',
               'DR_CDisc','DR_BCDisc', 'DR_TabEmpl',  'DR_VZak', 'DR_Pos']

# set columns to print:
print(df[['DR_Dat', 'DR_Tim']])
'''
          DR_Dat    DR_Tim
0     2022-08-11  10:15:35
1     2022-08-11  10:27:46
.....
'''

# Чтобы напечатать нужные столбцы указываем нужные столбцы в нужном порядке
print(df[column_list])

# можно переприсвоить
df = df[column_list]
print(df.head())
print(df.shape)    # (4462, 18)

# column rename
df.columns = ['dat', 'tim', 'nchk', 'ndoc', 'apt', 'ndrugs','kol',
               'czak', 'croz', 'sdisc', 'tpay', 'cdrugs',  'suppl',
               'cdisc','bcdisc', 'tabEmpl',  'vzak', 'pos']
print(df.columns)
"""
Index(['dat', 'tim', 'nchk', 'ndoc', 'apt', 'ndrugs', 'kol', 'czak', 'croz',
       'sdisc', 'tpay', 'cdrugs', 'suppl', 'cdisc', 'bcdisc', 'tabEmpl',
       'vzak', 'pos'],
      dtype='object')
"""

# -----------------   Урок 2.3. Обработка данных: работа с типами данных ---------------------
# определить тип данных
print(df.dtypes)
print(df['bcdisc'].dtype)    # float64

# change data type
# df['bcdisc'].astype('str')
print(df['bcdisc'].dtype)    # float64
print(df['bcdisc'].astype('str'))  # меняет тип на время распечатки    only for print
'''
0       200000000492.0
1       200010010204.0
2       200010010204.0
3       200010010204.0
'''
# delete trailing .0   only for print
print(df['bcdisc'].astype('str').replace('\.0',"",regex=True))
'''
0       200000000492
1       200010010204
2       200010010204
'''

# changing column format in dataframe
df['bcdisc'] = df['bcdisc'].astype('str').replace('\.0',"",regex=True)
print(df['bcdisc'])
'''
0       200000000492
1       200010010204
2       200010010204
3       200010010204
'''
print(df['bcdisc'].dtypes)   # object


print(df.columns)
print (df.head)
df['cdisc'] = df['cdisc'].astype('str').replace('\.0',"",regex=True)
print(df['cdisc'])
"""
was
0       925.00
1         9.00
2         9.00
3         9.00
4       925.00
now
0       925
1         9
2         9
3         9
4       925

"""

# change object 2022-08-12   to date_time format
print(pd.to_datetime(df['dat']))
# Name: cdisc, Length: 4462, dtype: object
# 0      2022-08-11
# 1      2022-08-11
# 2      2022-08-11
# ...
# 4460   2022-08-12
# 4461   2022-08-12
# Name: dat, Length: 4462, dtype: datetime64[ns]
print(pd.to_datetime(df['dat']).dt.year)
print(pd.to_datetime(df['dat']).dt.day)
print(pd.to_datetime(df['dat']).dt.day_of_week)
print(pd.to_datetime(df['dat']).dt.day_of_year)
print(pd.to_datetime(df['dat']).dt.month)
# Name: dat, Length: 4462, dtype: datetime64[ns]
# 0       2022
# 1       2022
# 2       2022
#         ...
# 4459    2022
# 4460    2022
# 4461    2022
# Name: dat, Length: 4462, dtype: int32

# change format  приведение формата
print(pd.to_datetime(df['dat']).dt.strftime('%d.%m.%Y'))
'''
4460    12.08.2022
4461    12.08.2022
Name: dat, Length: 4462, dtype: object
'''

df['dat'] = pd.to_datetime(df['dat']).dt.strftime('%d.%m.%Y')
print(df['dat'])
'''
Name: dat, Length: 4462, dtype: object
0       11.08.2022
1       11.08.2022
2       11.08.2022
'''

# get unique values from column
print(df['vzak'].unique())       # [1 2]

# Замена значений
print(df['vzak'].astype('str').replace('1', "Обычный").replace('2', 'Интернет'))
'''
0       Обычный
1       Обычный
2       Обычный
3       Обычный
4       Обычный
'''

# change values in DF + save
df['vzak'] = df['vzak'].astype('str').replace('1', "Обычный").replace('2', 'Интернет')

# Check new values
print(df['vzak'].unique())
# ['Обычный' 'Интернет']

# ------------------------------------ Lesson 2_4 ------------------------------
# https://www.youtube.com/watch?v=uZfZp9Z-oY4
# работа с пропусками

print(df.isna())  # вывести строки с пропусками ???
# df.isna().any()
# df.isna().all()

"""
        dat    tim   nchk   ndoc    apt  ndrugs    kol   czak   croz  sdisc  \
0     False  False  False  False  False   False  False  False  False  False   
1     False  False  False  False  False   False  False  False  False  False   
2     False  False  False  False  False   False  False  False  False  False   
3     False  False  False  False  False   False  False  False  False  False   
4     False  False  False  False  False   False  False  False  False  False 
"""
print(df.isna().any())  # определить столбцы где есть пропуски
"""
dat        False
tim        False
nchk       False
ndoc       False
apt        False
ndrugs     False
kol        False
czak       False
croz       False
...
"""
# fill empty cell with char
df.fillna(0).isna().any()     # fill empty cells with zero    - for print, no saving

# show lines with empty cells:
print(df.isna())
print(df.isna().values)
'''
[[False False False ... False False False]
 [False False False ... False False False]
 [False False False ... False False False]
 ...
 [False False False ... False False False]
 [False False False ... False False False]
 [False False False ... False False False]]
 '''
print(df.isna().values.any())
# True                              - there is at least 1 empty cell

print(df.isna().values.any(axis=0)) # наличие пропусков в каждом столбце
'''
[[False False False ... False False False]
 [False False False ... False False False]
 [False False False ... False False False]
 ...
 [False False False ... False False False]
 [False False False ... False False False]
 [False False False ... False False False]]
 '''

print(df2.isna().values.any(axis=1)) # наличие пропусков в каждой строке
# [False False False ...  True  True False]

print(df2[df2.isna().values.any(axis=1)])  # усли использовать это выражение в качестве индекса, то выведутся только строки с пропусками
                                           # в исходном df пропуск === NaN
'''
      DR_CRoz  DR_SDisc  DR_CDisc  DR_BCDisc  DR_TabEmpl  DR_VZak  DR_Pos  
15      18.00      0.00       NaN        NaN         205        1    1.00  
16      18.00      0.00       NaN        NaN         205        1    2.00  
20     560.00      0.00       NaN        NaN         205        1    1.00  
21     458.00      0.00       NaN        NaN         205        1    2.00  
'''

# new dataframe with NaN
df3 = df2[df2.isna().values.any(axis=1)]
print(df3.fillna(0).head(2))                  # Заполняем пропуски нулями
'''
         DR_Prod  DR_Kol  DR_CZak  DR_CRoz  DR_SDisc  DR_CDisc  DR_BCDisc  \
15  ЛЕККО ФФ ЗАО    1.00    12.94    18.00      0.00      0.00       0.00   
16  ЛЕККО ФФ ЗАО    1.00    12.94    18.00      0.00      0.00       0.00  
'''

# заполнение пропусков по методу интерполяции

df2['DR_CDisc'].interpolate(method='cubic')     # заполняем столбец DR_CDisc (пропуски)
                                                 # по методу интерполяции

df2.dropna()                   # delete lines where is at least 1 NaN
df2.dropna().shape
# ( 4462, 21) -> (1765,21)

df2.dropna(axis=1).shape     # delete columns  where is at least 1 NaN
# ( 4462, 21) -> (4462, 19)


