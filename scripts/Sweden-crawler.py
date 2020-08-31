'''
@Author: Matthew Shabet
@Date: 2020-08-31 18:00:00
LastEditTime: 2020-08-31 13:09:14
LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup

url = 'https://github.com/covid19-eu-zh/covid19-eu-data/blob/master/dataset/covid-19-se.csv'

nregions = 21

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tag = soup.findAll("table", {"class": "js-csv-data csv-data js-file-line-container"})[0]
tag = tag.findAll("tbody")[0].contents[1::2][-nregions:]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/Sweden/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the csv
headers = ["Region", "Cases", "Cases/100k pop.", "Deaths", "Intensive care"]
writer.writerow(headers)
for t in tag:
	t = t.contents[5:-2:2]
	t.pop(3)
	row = [t[i].contents[0] for i in range(5)]
	writer.writerow(row)
print("Sweden is done!")