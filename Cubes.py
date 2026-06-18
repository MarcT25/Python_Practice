import os
os.system('cls')

import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=10)

#set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=24)
ax.set_ylabel("Cube of values", fontsize=24)

#set the size of the tick labels.
ax.tick_params(labelsize=24)

#set the range for each axis
ax.axis([0,5000,0,150_000_000_000])


plt.show()