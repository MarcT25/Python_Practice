from die import Die
import plotly.express as px

#Create a D6.
die = Die()

#Make some rolls, and store the results in a list.
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyze the results.
frequencies = []

poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results.
title = "Results of Rolling one D6 1,000 times."
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

