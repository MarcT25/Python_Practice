import os
os.system('cls')

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
#fig, represents the whole figure. ax, represents a single point in the graph.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squares of value", fontsize=14)

#set size of tick labels.
ax.tick_params(labelsize=24)

plt.show()