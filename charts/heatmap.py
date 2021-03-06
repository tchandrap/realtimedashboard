from bokeh.charts import HeatMap, bins, output_file, show
from bokeh.palettes import RdYlGn6, RdYlGn9
from bokeh.sampledata.autompg import autompg
from bokeh.sampledata.unemployment1948 import data

# setup data sources
del data['Annual']
data['Year'] = data['Year'].astype(str)

fruits = {'fruit': ['apples', 'apples', 'apples', 'apples', 'apples',
                    'pears', 'pears', 'pears', 'pears', 'pears',
                    'bananas', 'bananas', 'bananas', 'bananas', 'bananas'],
          'fruit_count': [4, 5, 8, 12, 4, 6, 5, 4, 8, 7, 1, 2, 4, 8, 12],
          'year': [2009, 2010, 2011, 2012, 2013, 2009, 2010, 2011, 2012, 2013, 2009, 2010,
                   2011, 2012, 2013]}
                   
fruits['year'] = [str(yr) for yr in fruits['year']]

hm1 = HeatMap(autompg, x=bins('mpg'), y=bins('displ'))

hm2 = HeatMap(autompg, x=bins('mpg'), y=bins('displ'), values='cyl', stat='mean')

hm3 = HeatMap(autompg, x=bins('mpg'), y=bins('displ', bin_count=15),
              values='cyl', stat='mean')

hm4 = HeatMap(autompg, x=bins('mpg'), y='cyl', values='displ', stat='mean')

hm5 = HeatMap(autompg, y=bins('displ'), x=bins('mpg'), values='cyl', stat='mean',
              spacing_ratio=0.9)

hm6 = HeatMap(autompg, x=bins('mpg'), y=bins('displ'), stat='mean', values='cyl',
              palette=RdYlGn6)

hm7 = HeatMap(autompg, x=bins('mpg'), y=bins('displ'), stat='mean', values='cyl',
              palette=RdYlGn9)

hm8 = HeatMap(autompg, x=bins('mpg'), y=bins('displ'), values='cyl',
              stat='mean', legend='top_right')

hm9 = HeatMap(fruits, y='year', x='fruit', values='fruit_count', stat=None)

output_file("heatmap.html", title="heatmap.py example")

show(hm1)