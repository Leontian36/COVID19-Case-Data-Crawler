'''
@Author: Matthew Shabet
@Date: 2020-08-26 21:51:00
@LastEditTime: 2020-08-26 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup

url = "https://ncov.moh.gov.vn/"

# Get the data
response = requests.get(url, headers={'Connection': 'close'}, verify=False)
soup = BeautifulSoup(response.content, 'lxml')
tag = soup.findAll("section", {"class": "bg-xam pad-30"})[0]
table = tag.findAll("table")[0]
table = table.findAll("tbody")[0]
data = table.findAll("tr")

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/Vietnam/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Tỉnh, Thành phố", "Số ca nhiễm", "Đang điều trị", "Khỏi", "Tử vong"]
headers = ["Province, City", "Number of cases", "In treatment", "Recoveries", "Deaths"]
writer.writerow(headers)
for d in data:
	nums = d.findAll("td")
	row = [nums[i].contents[0] for i in range(5)]
	writer.writerow(row)