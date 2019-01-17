import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv('GES2015csv/accident.csv', low_memory=False)
di = {1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
}

crash_byDay = df['WKDY_IM'].value_counts().reset_index().sort_values(by=['index'])
crash_byDay.columns = ['day','count']
crash_byDay.sort_values(by=['day'])
crash_byDay['day'] = crash_byDay['day'].map(di) 

# set bar parameters
n_bars = 7
fig, ax = plt.subplots()
x_pos = np.arange(n_bars)
bar_width = 0.95
opacity = 1.0

# set color list
clrs = ['#5aee0f','#000080','#000080','#000080','#000080','#cc0000','#5aee0f']

# build list of bars to chart
barlist = plt.bar(x_pos, crash_byDay['count'], bar_width,
                 alpha=opacity,
                 color=clrs)

#  set chart title & lables 
plt.xlabel('Weekday', labelpad=15, fontsize='small')
plt.ylabel('# of Accidents', labelpad=15, fontsize='small')
plt.title('Accident Frequency by Day of Week', pad=20, fontsize='large')

# set x-axis tick marks
plt.xticks(x_pos - 0.45,
                ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),
                rotation=90,
                fontsize='x-small')

# plot
plt.tight_layout()
plt.show()

print(crash_byDay)