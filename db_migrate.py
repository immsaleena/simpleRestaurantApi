import sqlite3

#Initializing the database
DATABASE = 'restaurants.db'
connection = sqlite3.connect(DATABASE)

#create table if not exist
with open('schema.sql') as f:
    connection.executescript(f.read())