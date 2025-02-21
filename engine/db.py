import sqlite3
import csv
con=sqlite3.connect("jarvis.db")
cursor=con.cursor()

query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
cursor.execute(query)
# query="INSERT INTO sys_command VALUES(null,'Excel','C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe')"
# cursor.execute(query)
# conn.commit()

query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query="INSERT INTO web_command VALUES(null,'youtube','https://youtube.com')"
# cursor.execute(query)
# conn.commit()

# app_name="Excel"
# cursor.execute('SELECT path from sys_command where name in (?)',(app_name,))
# results=cursor.fetchall()
# print(results[0][0])

# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 18]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

query = "INSERT INTO contacts VALUES (null,'jack', '+91999999999','null')"
cursor.execute(query)
con.commit()

# query = 'ammi'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])