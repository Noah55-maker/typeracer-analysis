import requests
import re

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
speeds = pattern.findall(cleanup)

for i in range(len(speeds)):
	speeds[i] = speeds[i].split('>')[1]

with open(f"speeds-{username}.txt", 'w') as race_file:
	for r in speeds:
		race_file.write(r)
		race_file.write('\n')

if write_raw:
	with open(f"raw-{username}.html", 'w') as raw_file:
		raw_file.write(cleanup)
