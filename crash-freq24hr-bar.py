import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# import data to pandas dataframe
df = pd.read_csv('GES2015csv/accident.csv', low_memory=False)
crash_hr = df['HOUR_IM']

# sort accident frequency by hour
by_hour = crash_hr.value_counts().sort_index(axis=0)

# set bar parameters
n_bars = 24
fig, ax = plt.subplots()
x_pos = np.arange(n_bars)
bar_width = 0.95
opacity = 1.0

# set color list
clrs = ['#000080','#000080','#000080','#000080','#000080','#000080',
        '#cc0000','#cc0000','#cc0000', # highlight AM rush hour
        '#000080','#000080','#000080','#000080','#000080','#000080',
        '#cc0000','#cc0000','#cc0000','#cc0000', # highlight PM rush hour
        '#000080','#000080','#000080','#000080','#000080']

# build list of bars to chart
barlist = plt.bar(x_pos, by_hour, bar_width,
                 alpha=opacity,
                 color=clrs)

#  set chart title & lables 
plt.xlabel('Time of Day', labelpad=15, fontsize='small')
plt.ylabel('# of Accidents', labelpad=15, fontsize='small')
plt.title('Accident Frequency by Hour of Day', pad=20, fontsize='large')

# set x-axis tick marks
plt.xticks(x_pos - 0.45,
                ('12am', '1am', '2am', '3am','4am', '5am',
                '6am', '7am','8am', '9am', '10am', '11am',
                '12pm', '1pm', '2pm', '3pm','4pm', '5pm',
                '6pm', '7pm','8pm', '9pm', '10pm', '11pm','12am'),
                rotation=90,
                fontsize='x-small')

# build legend
rush_hours = mpatches.Patch(color='#cc0000', label='Rush Hours')
plt.legend(handles=[rush_hours], fontsize='x-small')

# plot
plt.tight_layout()
plt.show()
print(by_hour)