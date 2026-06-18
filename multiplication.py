from die import Die
import plotly.express as px

#create two D6 die
die_1 = Die()
die_2 = Die()

#make a list and store the results of the rolls in it.
results = []

#multiply instead of add.
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualization.
title = "Results of rolling two D8 1,000 times."
labels = {'x': 'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()
