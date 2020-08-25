'''
@Author: Matthew Shabet
@Date: 2020-08-26 21:51:00
@LastEditTime: 2020-08-26 22:48:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
'''
import csv
import requests
import json
import os
from datetime import datetime

translate = {
	"Total Cases": "casos_totales",
	"Recovered": "recuperados",
	"Deaths": "fallecidos",
	"Deaths (last 7 days)": "fallecidos_ultimos_7_dias",
	"Active Cases": "casos_activos",
	"Region": "comunidad_autonoma",
	"Diagnosed (last 24 hours)": "diagnosticados_ultimas_24_horas",
	"Diagnosed (last 7 days)": "diagnosticados_ultimos_7_dias",
	"Diagnosed (last 14 days)": "diagnosticados_ultimos_14_dias",
	"Hospitalizations": "hospitalizados",
	"Hospitalizations (last 7 days)": "hospitalizados_ultimos_7_dias",
	"ICU": "uci",
	"ICU (last 7 days)": "uci_ultimos_7_dias",
	"Total PCR": "pcr_totales",
	"PCR per 1000 pop": "pcr_1000_hab",
	"Increase in PCR capaticy (last week)": "incremento_capacidad_ultima_semana",
	"Cumulative incidence": "ia",
	"Basic reproduction number": "rt"
}

url = 'https://www.rtve.es/aplicaciones/infografias/rtve_2020/noticias/mapa-datosCCAA/territorios.json'

# Get the data
response = requests.get(url, headers={'Connection': 'close'})
data = json.loads(response.text)

# Create and open the CSV
mkfile_time = datetime.strftime(datetime.now(), '%Y%m%d%H%M')
folder_path = './photo/Spain/'+ mkfile_time + '/'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file = open(folder_path+'table.csv', 'w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)


# Write each line to the CSV
headers = ["Region", "Total Cases", "Diagnosed (last 24 hours)", "Diagnosed (last 7 days)", "Diagnosed (last 14 days)", "Cumulative incidence", "Basic reproduction number", "Active Cases", "Recovered", "Hospitalizations", "Hospitalizations (last 7 days)", "ICU", "ICU (last 7 days)", "Deaths", "Deaths (last 7 days)", "Total PCR", "PCR per 1000 pop", "Increase in PCR capaticy (last week)"]
writer.writerow(headers)
for d in data:
  row = [d[translate[h]] for h in headers]
  writer.writerow(row)