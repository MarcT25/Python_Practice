from pathlib import Path
import csv

import plotly.express as px

#reading data from the file.
path = Path('Chapter 15\\Chapter 16\\eq_data\\world_fires_7_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#latitude, longitude and brightness.
lats, longs, brights = [], [], []

for row in reader:
    lats.append(float(row[0]))
    longs.append(float(row[1]))
    brights.append(float(row[2]))

title = "Global Fires 7 Days"
fig = px.scatter_geo(lat=lats, lon=longs, size=brights, title=title,
                     color=brights,
                     color_continuous_scale='sunsetdark',
                     projection='natural earth',
                     )

fig.show()