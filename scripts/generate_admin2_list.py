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

        if (len(new_keys) >= 2):
            admin0_zh = new_keys[0]
            admin_zh = '|'.join(new_keys[1:])

            names_en = []
            for i in range(1, len(new_keys) + 1):
                names_en.append(
                    reduce(dict.get, new_keys[:i], data)['ENGLISH'])
            admin0_en = names_en[0]
            admin_en = '|'.join(names_en[1:])

            if (new_keys[0] == '中国' and len(new_keys) >= 4):
                csv_line = ','.join([
                    '', names_en[0], new_keys[0], names_en[2], new_keys[2],
                    names_en[3], new_keys[3], ''
                ])
                file.write(csv_line + '\n')
            elif (new_keys[0] == '美国' and len(new_keys) >= 3):
                #file.write(csv_line + '\n')
                pass
            elif (new_keys[0] == '意大利' and len(new_keys) >= 3):
                csv_line = ','.join([
                    '', names_en[0], new_keys[0], names_en[1], new_keys[1],
                    names_en[2], new_keys[2], ''
                ])
                file.write(csv_line + '\n')
            else:
                pass
        print_record(new_keys)


url = 'https://covid19.health/data/all.json'
data = requests.get(url=url).json()

file = codecs.open('admin2_names.csv', 'w', 'utf-8')

file.write(u'\ufeff')

file.write(
    'iso3,admin0_en,admin0_zh,admin1_en,admin1_zh,admin2_en,admin2_zh,hasc2\n')

print_record()
file.close()