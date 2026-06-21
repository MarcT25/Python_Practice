from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data\sitka_weather_2021_simple.csv')
path_2 = Path('weather_data\death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()
lines_2 = path_2.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

reader_2 = csv.reader(lines_2)
header_row_2 = next(reader_2)

#Extract high temperature.
dates, dates_2, highs_sitka, highs_death_valley = [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    s_high = int(row[4])
    dates.append(current_date)
    highs_sitka.append(s_high)

for row in reader_2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
     d_high = int(row[3])
    except ValueError:
     print(f"Missing data for {current_date}")
    else:
        d_high = int(row[3])
        dates_2.append(current_date)
        highs_death_valley.append(d_high)
     


#Plot the highh temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs_sitka, color='red', alpha=0.5)
ax.plot(dates_2, highs_death_valley, color='blue', alpha=0.5)
ax.fill_between(dates, highs_sitka, highs_death_valley, facecolor='blue', alpha=0.1)

#format plot.
ax.set_title("Daily High Temperature in Sitka and Death Valley, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()