from die import Die
import plotly.express as px

die = Die()
results = []

for roll_num in range(1000):
    results.append(die.roll())

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequencies.append(results.count(value))

#visualize
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

fig.write_html('die_D6_visual.html')