import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('GES2015csv/accident.csv', low_memory=False)

di = {1: 'No Intersection',
        2: 'Four-Way',
        3: 'T-Intersection',
        4: 'Other',
        5: 'Roundabout',
        6: 'Roundabout',
        7: 'Other',
        10: 'Other',
        98: 'Other',
        99: 'Other'
}

df = df['TYP_INT'].map(di) 
intersection_type = df.value_counts().reset_index() #.rename_axis('condition_type').to_frame('# of Accidents')
intersection_type.columns = ['intersection', 'count']


clrs = ['#b0e0e6','#b3cde0','#609fe5','#d5d8d1','#a59e99']
explode = (0.05, 0.01, 0.01, 0.05, 0.05)

fig1, ax1 = plt.subplots()

patches, texts, autotexts = ax1.pie(intersection_type['count'],
        explode = explode,
        labels = intersection_type['intersection'],
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


plt.title('Intersection Type')

plt.show()

print(intersection_type)