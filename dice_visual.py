from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
poss_results = range(2, die_1.num_sides + die_2.num_sides + 1)
for value in poss_results:
    frequencies.append(results.count(value))

#visualize
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1) # to label each bar
fig.show()