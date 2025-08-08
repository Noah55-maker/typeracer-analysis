import requests
import re
from datetime import datetime

username = "typer_noah"
num_races = 3400

# last=true, fast=false
last = True
sort_type = "last" if last else "fastest"

write_raw = False

url = f"https://typeracerdata.com/profile?username={username}&{sort_type}={num_races}"
response = requests.get(url)

if response.status_code != 200:
	print("Something went wrong")
	print(f"Status code: {response.status_code}")
	exit(1)

response_text = f"{response.content}"
cleanup = response_text.replace("\\r\\n", '\n')

pattern = re.compile(r"\d+\">\d+\.\d\d")
matches = pattern.findall(cleanup)


date_pattern = re.compile(r"20.*\n.*\d\">\d+.\d\d")
date_matches = date_pattern.findall(cleanup)
# print(date_matches)

speeds = []
# dates = []
times = []
for i in range(len(matches)):
	speeds.append(matches[i].split('>')[1])

for i in range(len(date_matches)):
	td = date_matches[i].split('<')[0]
	# dates.append(td)
	times.append(datetime.strptime(td, "%Y-%m-%d %H:%M:%S").timestamp())

# print(dates)

with open(f"speeds-{username}.txt", 'w') as race_file:
	for i in range(len(speeds)):
		race_file.write(speeds[i])
		race_file.write(',')
		race_file.write(str(times[i]))
		race_file.write('\n')

if write_raw:
	with open(f"raw-{username}.html", 'w') as raw_file:
		raw_file.write(cleanup)
