import re
import chart_studio
import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go
import chart_studio.dashboard_objs as dashboard

chart_studio.tools.set_credentials_file(username='ktoto', api_key='AckP6D0eaUH5z4FPe1GW')

username = 'BD3'
password = 'oracle123'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

query = '''
SELECT countrylike.country , countrylike.sum_like 
FROM countrylike'''

cursor.execute(query)
country = []
likes = []

row = cursor.fetchone()

while row:
    if row[0]== None: 
        pass
    else: 
       country.append(row[0]) 
       likes.append(row[1])
    row = cursor.fetchone()

bar = [go.Bar(
    x=country,
    y=likes
)]
layout = go.Layout(
    # title='Спікери та загальна тривалість їхніх виступів -- топ-10',
    xaxis={
        'title':'країни'
    },
    yaxis={
        'title':'лайки'
    }
)

fig = go.Figure(data=bar, layout=layout)

url_1 = py.plot(fig, filename='країна - лайки')

#-------------------------------------------------------------
query ='''
SELECT
    gamemapparcent.game,
    gamemapparcent.percent
    FROM gamemapparcent'''

cursor.execute(query)
game = []
percent = []

row = cursor.fetchone()

while row:
    if row[0]== None: 
        pass
    else: 
       game.append(row[0]) 
       percent.append(row[1])
    row = cursor.fetchone()

pie = go.Pie(labels=game, values=percent)
url_2 = py.plot([pie], filename='гра-відсоток')

#---------------------------------------------------


query = '''SELECT
    EXTRACT(year from Map.map_date) as year,
    COUNT(Map.id)
FROM Map
GROUP BY EXTRACT(year from Map.map_date)
ORDER BY EXTRACT(year from Map.map_date)
'''

cursor.execute(query)
date = []
maps = []

row = cursor.fetchone()

while row:
    if row[0]== None: 
        pass
    else: 
       date.append(row[0]) 
       maps.append(row[1])
    row = cursor.fetchone()


scatter = go.Scatter(
    x=date,
    y=maps,
    mode='lines+markers'
)
url_3 = py.plot([scatter], filename='дата - завантажені мапи')

connection.close()