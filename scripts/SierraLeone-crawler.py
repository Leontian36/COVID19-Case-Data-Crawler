'''
@Author: Matthew Shabet
@Date: 2020-08-17 15:00:00
@LastEditTime: 2020-08-17 16:17:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import ast
import csv
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

url = 'https://covid19.mic.gov.sl/'
url = 'https://covid19.mic.gov.sl/static/media/districts.beade2ed.csv'

# Make the directory
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/SierraLeone/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Download the data
req = requests.get(url).content.decode('utf-8')

# Create the dictrict csv
file = open(folder_path+'districts.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
file.write(req)
file.close()

# Create a names dictionary
req = req.splitlines()
names = ast.literal_eval("['" + req[0].replace(",","','") + "']")
n = {k: v for v, k in enumerate(names)}

eastern = ["kailahun", "kono", "kenema"]
northern = ["bombali", "falaba", "kambia", "koinadugu", "portloko", "tonkolili"] 
southern = ["bo", "bonthe", "moyamba", "pujehun"]
western = ["western rural", "western urban"]

# Create the region csv
file = open(folder_path+'regions.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
labels = ["Date", "Eastern", "Northern", "Southern", "Western"]
writer.writerow(labels)
req = ["['"+r.replace(",","',",1)+"]" for r in req[1:]]
req = [ast.literal_eval(r) for r in req]

for r in req:
	row = [r[0], sum([r[n[i]] for i in eastern]), sum([r[n[i]] for i in northern]), sum([r[n[i]] for i in southern]), sum([r[n[i]] for i in western])]
	writer.writerow(row)