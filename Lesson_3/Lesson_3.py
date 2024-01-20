# https://www.youtube.com/watch?v=GAECkZMPkyI

# -------------------------------------  Lesson 2_1 Load data --------------------------

import pandas as pd
import matplotlib

df = pd.read_csv('data.csv', encoding='1251')
df2 = pd.read_csv('data.csv', encoding='1251')

pd.options.display.max_columns = None             #  after this display all columns, else displays first and last

pd.set_option('display.max_columns', 40)    # set option : max_columns


pd.set_option('display.float_format', '{:.2f}'.format)    # format was 2.000100e+11
print(df.tail(10))                                        # format now 200010027618.00

column_list = ['DR_Dat', 'DR_Tim', 'DR_NChk', 'DR_NDoc', 'DR_Apt', 'DR_NDrugs','DR_Kol',
               'DR_CZak', 'DR_CRoz', 'DR_SDisc', 'DR_TPay', 'DR_CDrugs',  'DR_Suppl',
               'DR_CDisc','DR_BCDisc', 'DR_TabEmpl',  'DR_VZak', 'DR_Pos']

df = df[column_list]                 # remove some columns

print(df.head())
print(df.shape)    # (4462, 18)

# column rename
column_list = ['dt', 'c_time', 'nchk', 'ndoc', 'apt', 'drug','kol',
               'zak', 'roz', 'disc', 'pay_type', 'drug_id',  'suppl',
               'disc_id','disc_barcode', 'empl',  'vzak', 'pos']

df.columns = column_list

df['disc_barcode'] = df['disc_barcode'].astype('str').replace('\.0',"",regex=True)
df['disc_id'] = df['disc_id'].astype('str').replace('\.0',"",regex=True)
df['dt'] = pd.to_datetime(df['dt']).dt.strftime('%d.%m.%Y')
df['vzak'] = df['vzak'].astype('str').replace('1', "Обычный").replace('2', 'Интернет')
# -------------------------------------  above - data from lesson 2 ----------------------------
print(df)
#  Урок 3.1. Исследовательский анализ
# https://www.youtube.com/watch?v=aZxE-IR4WYw

# структура данных
print(df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4462 entries, 0 to 4461
Data columns (total 18 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   dt            4462 non-null   object 
 1   c_time        4462 non-null   object 
 2   nchk          4462 non-null   int64  
 3   ndoc          4462 non-null   int64  
 4   apt           4462 non-null   int64  
 ...
  17  pos           4462 non-null   float64
dtypes: float64(5), int64(6), object(7)
memory usage: 627.6+ KB
None
 '''

# описательные статистики
print(df.describe())
'''
         nchk        ndoc     apt     kol      zak      roz    disc  pay_type  \
count 4462.00     4462.00 4462.00 4462.00  4462.00  4462.00 4462.00   4462.00   
mean  4903.14 10842995.33   10.84    1.03   241.64   306.05   10.56     16.90   
std   1839.70  6107181.40    6.11    0.54   454.56   532.17   31.37      1.45   
min   1698.00  2004595.00    2.00    0.01     0.01     0.01    0.00     15.00   
25%   4187.00  6003620.00    6.00    1.00    36.64    52.00    0.00     15.00   
50%   4877.50 11007039.00   11.00    1.00   103.78   137.00    0.00     18.00   
75%   5472.75 18002536.00   18.00    1.00   299.06   391.75    7.00     18.00   
max   8490.00 18002543.00   18.00   20.00 11851.13 12345.00  650.00     18.00   
'''
# mean - среднее значение (сумм всех разделили на все )
# 50% - медиана (50% дешевле этой, 50% товаров дороже этой)

# Распределение типа записей
print(df['pay_type'].value_counts())
'''
pay_type
18    2820
15    1642
Name: count, dtype: int64
'''
# Формат Записи
#  df['pay_type'].value_counts() === df.pay_type.value_counts()

print(df.apt.value_counts())  # распределение кол-ва продаж по аптекам
'''
apt
18    1207
2      979
11     870
6      511
13     322
17     243
15     177
7      153
Name: count, dtype: int64
'''

print(df.apt.value_counts(normalize=True))  # распределение кол-ва продаж по аптекам
'''
apt
18   0.27
2    0.22
11   0.19
6    0.11
13   0.07
17   0.05
15   0.04
7    0.03
'''
# 3.2	Исследовательский анализ: оценка распределений, связь между переменными
# https://www.youtube.com/watch?v=LpwxD6v4NHA

# оценить распределение количества позиций в чеке
print( df.pos.unique())
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17. 18.
#  19. 20. 21. 23. 24. 22.]                          max = 24
print( df.pos.value_counts(normalize=True))
"""
pos
1.00    0.45
2.00    0.22
3.00    0.12
4.00    0.07
5.00    0.04
6.00    0.03
7.00    0.02
8.00    0.01
9.00    0.01
10.00   0.01
...
"""
print( df.pos.value_counts())
'''
os
1.00     2019
2.00      971
3.00      528
4.00      301
5.00      178
6.00      117
7.00       76
8.00       56
9.00       42
...
'''

# построение гистограмы
df.pos.hist()                    # грубая разбивка по х
# ImportError: matplotlib is required for plotting when the default backend "matplotlib" is selected.
# pip install matplotlib
# должна построиться гисограмма

df.pos.hist(bins=24)   # разбивка по оси x на 24 позиции интервала


# оценить связь между переменными  ( одна меняется когда другая меняется)
# Тепловая карта
import seaborn as sns             # pip install  seaborn
import matplotlib.pyplot as plt

# note  корреляционная матрица  df.corr()

# sns.heatmap(df.corr())         # получилась корреляция -2... 0     > error

# графики 8 х 8
# sns.heatmap(df.corr(), vmax=1, vmin=-1)         # получилась корреляция -1... +1     > error
# sns.heatmap(df.corr(), vmax=1, vmin=-1, annot=True)


# графики 8 х 8
# plt.figure(figsize = (16,6))                    # графики 16 х 6   1-time настройка
# plt.rcParams['figure.figsize'] = (16,6)            # графики 16 х 6   long-time настройка
# sns.heatmap(df.corr(), vmax=1, vmin=-1, annot=True)

# 3.3	Исследовательский анализ: создание вычислимых столбцов, оценка распределений с box plot
# https://www.youtube.com/watch?v=OJvPx7t6LGw

# add column
print(df.dt)
'''
0       11.08.2022
1       11.08.2022
2       11.08.2022
...
'''

print(pd.to_datetime(df.c_time).dt.hour)
'''
0       10
1       10
2       10
3       10
4       10
        ..
4457    21
'''
# new_column
df['hour'] = pd.to_datetime(df.c_time).dt.hour
print(df.hour)
'''
0       10
1       10
2       10
3       10
4       10
        ..
4457    21

'''

# распределение проданных позиций по часам
# print(df.groupby(['hour'])['kol'].agg(sum))
'''
hour
8     20.10
9    236.50
10   361.65
11   326.55
12   311.59
13   422.80
14   358.30
15   432.97
16   375.88
17   375.45
18   457.50
19   419.29
20   388.57
21    97.71
22     1.00
Name: kol, dtype: float64

Process finished with exit code 0

'''

# диаграмма размаха (ящик с усами)   - doesn't work here
# gr = df.groupby(['hour'])['kol'].agg(sum)
# sns.boxplot(gr)

# 3.4	Исследовательский анализ: группировка данных
# https://www.youtube.com/watch?v=HaoQdE5f92k
# группировка
print(df.groupby(['dt', 'nchk'])['kol','roz', 'zak'].agg({
    'kol': sum,
    'roz': ['sum', 'max'],
    'zak': sum
}))       # группировка по дате и номеру чека


