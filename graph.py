import matplotlib.pyplot as plt
import numpy as np

username = "typer_noah"
rolling_average_size = 50

file_name = f"speeds-{username}.txt"

raw_speeds = []
with open(file_name, "r") as speed_file:
	raw_speeds = speed_file.readlines()

raw_speeds.reverse()

speeds = []
for i in range(len(raw_speeds)):
	parsed_speed = float(raw_speeds[i][0:-1])
	speeds.append(parsed_speed)

plt.plot(speeds)
plt.show()

if len(speeds) < rolling_average_size:
	print(f"Please provide at least {rolling_average_size} races")
	print(f"You provided {len(speeds)} races")
	exit(1)

sum = 0
for i in range(rolling_average_size):
	sum += speeds[i]
rolling_average = [sum / rolling_average_size]

for i in range(len(speeds)-rolling_average_size):
	sum += speeds[i+rolling_average_size] - speeds[i]
	rolling_average.append(sum / rolling_average_size)

plt.plot(rolling_average, 'o')
plt.show()
