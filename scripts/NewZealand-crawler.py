'''
@Author: Yifei Tian
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-06-06 22:51:17
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

url = 'https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-current-situation/covid-19-current-cases'


response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tables = soup.select('table')

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
print(mkfile_time)

folder_path = './photo/New Zealand/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

table_name = folder_path +'.csv'


#for table in tables:
#  df_list.append(pd.concat(pd.read_html(table.prettify())))
#print(pd, pd.read_html, tables[0])

    
try:
    df = pd.read_html(tables[1].prettify())
    df = pd.concat(df)
    df.to_csv(folder_path+'table.csv', encoding='utf-8-sig')
    print('抓取完成')
except IOError:
 	print("error")
print (df)
# head = []
# for tr in tables[1].findAll('tr'):
#     row = []
#     for td in tr.findAll('td'):
#         row.append(td.text)
        
#     if row:
#         df_list.append(row)
#     else:
#         for th in tr.findAll('th'):
#            head.append(th.text)
#         df_list.append(head)

#print (df_list)     
#df = pd.DataFrame(df_list)
#print(df)
#df.to_csv(folder_path+'table.csv', encoding='utf-8-sig')
#print('抓取完成')





# mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
# print(mkfile_time)

# folder_path = './photo/New Zealand/'+ mkfile_time + '/'
# if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
#     os.makedirs(folder_path)

# table_name = folder_path +'.csv'

# df_list = []

# try:
#     for table in tables:
#         df_list.append(pd.concat(pd.read_html(table.prettify())))
#     df = pd.concat(df_list)
#     df.to_csv(folder_path+'table.csv', encoding='utf-8-sig')
#     print('抓取完成')
# except IOError:
#  	print("error")

