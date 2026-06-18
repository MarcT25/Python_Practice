from pathlib import Path
import csv 
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data\sitka_weather_2021_full.csv')
lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)
#retrieve the next item from an iterator.
header_row = next(reader)

#extract rainfall
rainfall, dates = [],[]
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rain = float(row[5])
    dates.append(current_date)
    rainfall.append(rain)

#Plot the rainfall percentage
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, alpha=0.25)

#format plot
ax.set_title("Daily rain fall in Sitka, 2021")
ax.set_xlabel('Dates', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Percentage(%) of Rainfall", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
