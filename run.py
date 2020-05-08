import subprocess
from datetime import date, timedelta

subprocess.run(["python", "json2csv.py"])

for d in range(1, 4):
    day = date.today() - timedelta(days=d)
    day = day.strftime('%Y-%m-%d')
    subprocess.run(["python", "json2csv.py", day])