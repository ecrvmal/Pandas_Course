import pandas as pd

df = pd.read_csv('itresume-users-pandas.csv', sep=';' ,skiprows=1)
df2 = df.tail(3)

# --------------------------------test 2 ----------------------------

import pandas as pd

df = pd.read_csv('itresume-users-pandas.csv', sep=';' ,skiprows=1)
params = {}
params['Имена столбцов'] = list(df.columns)
params['Размер'] = df.size
params['Форма'] = df.shape

'''
result
{
    'Имена столбцов': ['id', 'username', 'date_joined'],
    'Размер': 300,
    'Форма': (100, 3)
}
'''

# --------------------------------test 3 ----------------------------
import pandas as pd

df = pd.read_csv('itresume-users-pandas.csv', sep=';' ,skiprows=1)
df.columns = ['user_id','login', 'created_at']       # rename columns
df = df[['user_id','created_at', 'login']]                   # re-order columns

# --------------------------------test 4 ----------------------------
import pandas as pd

df = pd.read_csv('itresume-users-pandas.csv', sep=';' ,skiprows=1)
are_types_equal = df['username'].dtype == df['date_joined'].dtype   # chec if colmn type are eq

# --------------------------------test 5 ----------------------------
import pandas as pd

df = pd.read_csv('itresume-users-pandas.csv', sep=';' ,skiprows=1)

df['username'] = df['username'].str.replace('$', '')    # все знаки долларов просто удалены
df = df.dropna()                                        # строки с пропусками удалены

# --------------------------------test 6 ----------------------------
'''
Создайте словарь registrations_by_weekday, который будет содержать информацию о дне недели и количестве зарегистрированных в этот день пользователей:
{ 'Monday': 61, ... }
Элементы словаря должны быть отсортированы по убыванию количества дней.
'''

import pandas as pd
from collections import Counter

df = pd.read_csv('itresume-users-pandas.csv', sep=';' ,skiprows=1)
days = pd.to_datetime(df['date_joined']).dt.day_name()
# print(days)
# 0 Sunday 1 Thursday 2 Wednesday 3 Saturday 4 Tuesday ... 95 Saturday 96 Saturday

registrations_by_wd = dict(Counter(days))
registrations_by_weekday  = dict(sorted(registrations_by_wd.items(), key=lambda x: x[1], reverse=True))

# --------------------------------test 6 ----------------------------
'''
Сформируйте список dates, который будет содержать уникальные даты регистрации пользователей в формате YYYY-MM-DD.
dates должен представлять из себя стандартный список Python
время регистрации нас не интересует
'''
import pandas as pd

df = pd.read_csv('itresume-users-pandas.csv', sep=';' ,skiprows=1)
dates = list(pd.to_datetime(df['date_joined']).dt.date.unique())   # pd.to_datetime(df['date_joined'])  - work with data
                                                                    # .dt.date.unique()
dates = [dt.strftime("%Y-%m-%d") for dt in dates]                   # reformat
                                                                    # datetime.date(2021, 7, 1) ->  '2022-01-02'
