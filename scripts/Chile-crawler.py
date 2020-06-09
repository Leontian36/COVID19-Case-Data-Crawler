'''
@Author: Yifei Tian
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-06-09 14:34:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import requests
from urllib import request
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime
import pandas as pd 

url = 'https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/'


response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tables = soup.select('table')



mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
print(mkfile_time)

folder_path = './photo/Chile/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

table_name = folder_path +'.csv'

    
try:
    df = pd.read_html(tables[0].prettify())
    df = pd.concat(df)
    df.to_csv(folder_path+'table.csv', encoding='utf-8-sig')
    print('抓取完成')
except IOError:
 	print("error")
#print (df)
