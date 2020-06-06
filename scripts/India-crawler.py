'''
@Author: your name
@Date: 2020-05-31 22:37:39
@LastEditTime: 2020-06-06 12:03:02
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

url = 'https://www.mohfw.gov.in/'
# strhtml = requests.get(url)
# soup = BeautifulSoup(strhtml.text,'lxml')
# img = soup.select('#top > div.main-content > section.rte.w-max > accordions:nth-child(14) > div.accordion.card.accordion-open > div > div > p:nth-child(21) > img')
# urllib.request.urlretrieve(img,'D:/google drive/crawler/%s.jpg"%(x)')

response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tables = soup.select('table')

print(tables)

mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
print(mkfile_time)

folder_path = './photo/India/'+ mkfile_time + '/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)

table_name = folder_path +'.csv'

df_list = []

try:
    for table in tables:
        df_list.append(pd.concat(pd.read_html(table.prettify())))
    df = pd.concat(df_list)
    df.to_csv(folder_path+'table.csv', encoding='utf-8-sig')
    print('抓取完成')
except IOError:
 	print("error")

