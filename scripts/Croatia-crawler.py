'''
@Author: Matthew Shabet
@Date: 2020-08-28 18:00:00
@LastEditTime: 2020-08-28 18:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime

url = "https://www.koronavirus.hr/json/?action=po_danima_zupanijama_zadnji"

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)[0]["PodaciDetaljno"]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/Croatia/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "Cases", "Deaths", "Active"]
writer.writerow(headers)
for d in data:
	row = [d["Zupanija"], d["broj_zarazenih"], d["broj_umrlih"], d["broj_aktivni"]]
	writer.writerow(row)