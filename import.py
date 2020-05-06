import csv
import cx_Oracle
import datetime

username = 'BD3'
password = 'oracle123'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()


csv_file = open('hmm maps.csv', errors = 'ignore')
csv_reader = csv.DictReader(csv_file)


game_list=[]
author_name_list = []
country_list = []
#------------------------------------------------------------------


for line in csv_reader:

	map_id = line['id'].strip()
	map_name = line['name'].strip()
	game = line['game'].strip()
	rating = int(line['rating'])
	author_name = line['author name'].strip()
	author_url = line['author url'].strip()
	downloads = int(line['downloads'])
	date = line['upload_date'].split('-')
	upload_date = datetime.date(int(date[0]),int(date[1]) ,int(date[2]))
	country = line['country'].strip()


#-------------------------------------------------------------------

	query = '''INSERT INTO map (id, name, game, rating, author_name, downloads, map_date) 
			VALUES(:map_id, :map_name, :game, :rating, :author_name, :downloads, TO_DATE(:upload_date, 'yyyy-mm-dd'))'''

	cursor.execute(query, map_id = map_id, map_name = map_name, game = game, rating = rating, author_name = author_name, downloads = downloads, upload_date = upload_date)

	if game not in game_list:
		game_list.append(game)
		query = '''INSERT INTO game (game) VALUES (:game)'''
		cursor.execute(query, game = game)

	if author_name not in author_name_list:
		author_name_list.append(author_name)
		query = '''INSERT INTO author (author_name, country, url) VALUES (:author_name, :country, :author_url)'''
		cursor.execute(query,author_name = author_name, country = country, author_url = author_url)

	if country not in country_list:
		country_list.append(country)
		query = '''INSERT INTO country (country) VALUES (:country)'''
		cursor.execute(query, country = country)



csv_file.close()
connection.commit()
cursor.close()
connection.close()