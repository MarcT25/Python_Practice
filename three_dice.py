from die import Die
import plotly.express as px

#create two D8 die
die_1 = Die()
die_2 = Die()
die_3 = Die()

#make a list and store the results of the rolls in it.
results = []

for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualization.
title = "Results of rolling three D6 100,000 times."
labels = {'x': 'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
