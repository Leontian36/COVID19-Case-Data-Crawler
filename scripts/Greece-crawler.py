'''
@Author: Matthew Shabet
@Date: 2020-08-25 17:00:00
@LastEditTime: 2020-08-25 18:30:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup


url = 'https://github.com/iMEdD-Lab/open-data/blob/master/COVID-19/regions_greece.csv'


# Get the data
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'lxml')
tag = soup.findAll('tbody')[0].contents[1::2]

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/Greece/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the csv
headers = ["Region", "LocalName", "Cases", "Deaths"]
writer.writerow(headers)
for t in tag:
	t = t.contents[1::2]
	row = [t[2].contents[0], t[1].contents[0], t[4].contents[0], t[5].contents[0]]
	writer.writerow(row)