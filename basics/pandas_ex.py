import numpy as np

import pandas as pd

s=pd.Series([1,3,5,np.nan,6,8])

dates=pd.date_range('20230701',periods=15)

print(dates)

df=pd.DataFrame(np.random.randn(15,4),index=dates,columns=list('ABCD'))
print(df)

df2=pd.DataFrame(
    {
        "a":1.0,
        'b':pd.Timestamp('20230715'),
        'c':pd.Series(1,index=list(range(4)),dtype='float32'),
        'd':np.array([3]*4,dtype='int32'),
        'e':pd.Categorical(['vijay','ajith','kamal','rajini']),
        'f':'foo',

    }
)
print(df2)

print(df2.dtypes)

print(df.head())
print(df.tail())

print(df.index)

print(df.columns)

mydataset=pd.DataFrame(
    {
        'Cars':['bmw','tata','RR'],
        'passings':['5','6','7']
    }
)

print(mydataset)

a=[2,4,5]

x=pd.Series(a)

y=pd.Series(a,index=['x','y','z'])

print(x)
print(y['z'])

dict={'raja':[5,6,7],'gow':[6,7,8],'vij':[1,2,3]}

df=pd.Series(dict)
print(df)

df2=pd.DataFrame(dict)
print(df2)

print(df2.loc[1])

print(df2.loc[[0,2,1]])

df=pd.read_csv('stock.csv')

print(df.to_string())

print(pd.options.display.max_rows) # show the max display limit
pd.options.display.max_rows=99
print(pd.options.display.max_rows)

# info about the data set

print(df.info())

df.dropna(inplace=True)

print(df.to_string())

# for x in df.index:
#     if round(int(df.loc[x,'Open']))>4500:
#         df.loc[x,'Open']='4500'
# print(df.loc['Open'])

print(df.corr())