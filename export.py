import csv
import cx_Oracle

username = 'BD3'
password = 'oracle123'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()
tables = ['map', 'author', 'game', 'country']

try:
    for table in tables:

        
        with open(table + '.csv', 'w', newline='') as csv_file:
            query = 'SELECT * FROM ' + table
            cursor.execute(query)
            row = cursor.fetchone()

            headers = tuple(map(lambda x: x[0], cursor.description))
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow(headers)

            while row:
                csv_writer.writerow(row)
                row = cursor.fetchone()

finally:
    cursor.close()
    connection.close()