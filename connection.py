
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

import pyodbc


conn=pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=YOUR SERVER NAME,1433;DATABASE=YOUR DATABASE NAME;UID=YOUR USER NAME;PWD=YOUR USER PASSWORD')

cursor = conn.cursor()
data=cursor.execute('SELECT * FROM YOUR_TABLE_NAME')

print(data)


df=pd.DataFrame(data)


df.to_csv (r'C:\Users\username\desktop\filename.csv', index = False, header=True)
