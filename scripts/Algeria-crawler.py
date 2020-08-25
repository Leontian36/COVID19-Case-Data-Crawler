'''
@Author: Matthew Shabet
@Date: 2020-07-31 23:30:00
@LastEditTime: 2020-08-1 02:52:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import json
import csv
import requests
import os
from datetime import datetime

url = "https://dz-covid19.com/ws/?EIO=3&transport=polling"
sid = requests.get(url, headers={'Connection': 'close'}).text[12:32]

url = url + "&sid=" + sid

response = requests.get(url, headers={'Connection': 'close'}).text
data = response[response.index("wilayas") + 9:-1]
data = json.loads(data)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/Algeria/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

headers = ["name", "confirmed", "deaths", "recovered", "active"]
writer.writerow(headers)
for d in data:
	row = [d[h] for h in headers]
	writer.writerow(row)