from pathlib import Path
import json

#Read data as a string and convert to a Python object.
path = Path('Chapter 16\\eq_data\\readable_eq_data.json')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Create a more readable version of the data file.
#path = Path('Chapter 16\\eq_data\\eq_data_1_day_m1.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contents)

#Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
#print(len(all_eq_dicts))


#magnitudes and locations
mags, lons, lats = [], [], []
for eq__dict in all_eq_dicts:
    mag = eq__dict['properties']['mag']
    lon = eq__dict['geometry']['coordinates'][0]
    lat = eq__dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#print(mags[:10])
print(lats[:5])
print(lons[:5])



