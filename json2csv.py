import json
from functools import reduce
import codecs
import sys
import requests


def print_record(keys=[]):
    names = [
        x for x in reduce(dict.get, keys, data).keys()
        if not x in ['confirmedCount', 'curedCount', 'deadCount', 'ENGLISH']
    ]
    for name in names:
        new_keys = keys[:]
        new_keys.append(name)

        confirmed = reduce(dict.get, new_keys, data)['confirmedCount']
        deaths = reduce(dict.get, new_keys, data)['deadCount']
        recovered = reduce(dict.get, new_keys, data)['curedCount']
        dates = list(set().union(confirmed.keys(), deaths.keys(),
                                 recovered.keys()))
        dates.sort()
        if (len(new_keys) >= 2):
            admin0_zh = new_keys[0]
            admin_zh = '|'.join(new_keys[1:])

            names_en = []
            for i in range(1, len(new_keys) + 1):
                names_en.append(
                    reduce(dict.get, new_keys[:i], data)['ENGLISH'])
            admin0_en = names_en[0]
            admin_en = '|'.join(names_en[1:])

            # find match in dictionary
            hasc = next((hasc for hasc, prop in dictionary.items()
                         if prop["country_zh"] == admin0_zh
                         and prop["region_zh"] == admin_zh), None)
            if hasc is None: continue

            for date in dates:
                confirmed_num = str(
                    confirmed[date]) if date in confirmed else ''
                deaths_num = str(deaths[date]) if date in deaths else ''
                recovered_num = str(
                    recovered[date]) if date in recovered else ''
                csv_line = ','.join([
                    dictionary[hasc]['id'], date, dictionary[hasc]['iso'],
                    admin0_en, hasc, admin_en, confirmed_num, deaths_num,
                    recovered_num
                ])
                if (new_keys[0] == '中国' and len(new_keys) >= 4):
                    #file2.write(csv_line + '\n')
                    pass
                elif (new_keys[0] == '美国' and len(new_keys) >= 3):
                    #file2.write(csv_line + '\n')
                    pass
                elif (new_keys[0] == '意大利' and len(new_keys) >= 3):
                    #file2.write(csv_line + '\n')
                    pass
                else:
                    if (export_date == date): file.write(csv_line + '\n')
        print_record(new_keys)


dictionary = {}
with open('admin1_names.csv', 'r') as file:
    lines = file.readlines()
    for idx, line in enumerate(lines):
        if idx == 0: continue
        lineSplit = line.strip().split(',')
        id = lineSplit[0]
        iso = lineSplit[1]
        country_zh = lineSplit[3]
        region_zh = lineSplit[5]
        type = lineSplit[6]
        hasc = lineSplit[8]
        if (hasc != ''):
            dictionary[hasc] = {
                "id": id,
                "iso": iso,
                "type": type,
                "country_zh": country_zh,
                "region_zh": region_zh
            }

url = 'https://covid19.health/data/all.json'
data = requests.get(url=url).json()
export_date = sys.argv[1]

file = codecs.open('csv/admin1_' + export_date + '.csv', 'w', 'utf-8')
#file2 = codecs.open('admin2.csv', 'w', 'utf-8')
file.write(u'\ufeff')
#file2.write(u'\ufeff')

file.write(
    ',date,iso3,admin0_name,admin1_hasc,admin1_name,confirmed,death,recovered\n'
)
#file2.write('country_en,country_zh,region_en,region_zh\n')

print_record()
file.close()
#file2.close()