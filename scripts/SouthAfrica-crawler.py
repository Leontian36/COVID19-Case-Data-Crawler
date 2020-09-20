'''
@Author: Matthew Shabet
@Date: 2020-09-14 19:51:00
@LastEditTime: 2020-09-14 23:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import os
from datetime import datetime
from bs4 import BeautifulSoup

regions = ["Eastern Cape", "Free State", "Gauteng", "KwaZulu-Natal", "Limpopo", "Mpumalanga", "North West", "Northern Cape", "Western Cape"]

url = "https://sacoronavirus.co.za/category/press-releases-and-notices/"

# Get the data url
response = requests.get(url, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'html.parser')
tag = soup.findAll("div", {"class": "fusion-posts-container fusion-blog-layout-grid fusion-blog-layout-grid-4 isotope fusion-blog-equal-heights fusion-blog-pagination fusion-blog-rollover"})
pages = tag[0].contents
links = [p.contents[0].contents[1].contents[0].contents[0].contents[0]["href"] for p in pages]
link = [l for l in links if l.find("update-on-covid-19") >= 0][0]

# Get the data
response = requests.get(link, headers={'Connection': 'close'})
soup = BeautifulSoup(response.content, 'html.parser')
tags = soup.findAll("table", {"class": "NormalTable"})
cases_body = tags[0].contents[0]
death_recov_body = tags[1].contents[0]

# Construct the tables
cases = []
death_recov = []
rows = cases_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    cases.append([ele for ele in cols if ele])
rows = death_recov_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    death_recov.append([ele for ele in cols if ele])

# Construct the reference
case_map = {cases[i][0]: i for i in range(len(cases))}
death_recov_map = {death_recov[i][0]: i for i in range(len(death_recov))}

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/SouthAfrica/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)

# Write each line to the CSV
headers = ["Region", "Cases", "Percentage total", "Deaths", "Recoveries", "Active"]
writer.writerow(headers)
for r in regions:
	c = cases[case_map[r]]
	dr = death_recov[death_recov_map[r]]
	row = [r, c[1], c[2], dr[1], dr[2], dr[3]]
	writer.writerow(row)