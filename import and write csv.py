#import csv using pandas
import pandas as pd
df = pd.read_csv('hrdata.csv',
        index_col='Employee',
        parse_dates=['Hired'],
        header=0,
        names=['Employee','Hired','Salary','Sick Days'])
print(df)

#writing csv using pandas
df.loc['Cookie Cat'] =['2016-07-04',20000.00,0]
df.to_csv('hrdata_modified.csv')
