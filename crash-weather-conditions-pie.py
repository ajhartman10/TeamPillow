import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('GES2015csv/accident.csv', low_memory=False)

di = {1: 'Clear',
        2: 'Rainy',
        3: 'Other',
        4: 'Snowy',
        5: 'Other',
        6: 'Other',
        7: 'Other',
        8: 'Other',
        10: 'Cloudy',
        11: 'Snowy',
        12: 'Other',
        98: 'Other',
        99: 'Other'
}

df = df['WEATHER'].map(di) 
weather_conditions = df.value_counts().reset_index() #.rename_axis('condition_type').to_frame('# of Accidents')
weather_conditions.columns = ['Condition', 'count']

clrs = ['#b0e0e6','#b3cde0','#609fe5','#d5d8d1','#a59e99']
explode = (0.05, 0.01, 0.01, 0.05, 0.05)

fig1, ax1 = plt.subplots()

patches, texts, autotexts = ax1.pie(weather_conditions['count'],
        explode = explode,
        labels = weather_conditions['Condition'],
        colors = clrs,
        autopct = '%1.1f%%',
        pctdistance = 0.85,
        labeldistance = 1.1,
        startangle = 25,
        radius = 0.9,
        textprops={'size': 'smaller',
                'fontname': 'monospace',
                'fontstyle': 'italic'},
       )

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.setp(autotexts, size='x-small')
plt.setp(texts, fontname='serif')


plt.title('Weather Conditions at Time of Accident')

plt.show()

print(weather_conditions)