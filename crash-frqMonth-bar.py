import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

df = pd.read_csv('GES2015csv/accident.csv', low_memory=False)
di = {1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
}
crash_byMonth = df['MONTH'].value_counts().reset_index().sort_values(by=['index'])
crash_byMonth.columns = ['month','count']
crash_byMonth.sort_values(by=['month'])
crash_byMonth['month'] = crash_byMonth['month'].map(di) 

# set bar parameters
n_bars = 12
fig, ax = plt.subplots()
x_pos = np.arange(n_bars)
bar_width = 0.95
opacity = 1.0

# set color list
clrs = ['#000080','#000080','#000080','#000080','#000080','#000080',
        '#cc0000','#cc0000','#cc0000','#cc0000','#cc0000','#cc0000']

# build list of bars to chart
barlist = plt.bar(x_pos, crash_byMonth['count'], bar_width,
                 alpha=opacity,
                 color=clrs)

#  set chart title & lables 
plt.xlabel('Time of Day', labelpad=15, fontsize='small')
plt.ylabel('# of Accidents', labelpad=15, fontsize='small')
plt.title('Accident Frequency by Month', pad=20, fontsize='large')

# set x-axis tick marks
plt.xticks(x_pos - 0.45,
                ('January','February','March','April','May','June',
                'July','August','September','October','November','December'),
                rotation=90,
                fontsize='x-small')

# plot
plt.tight_layout()
plt.show()

print(crash_byMonth)