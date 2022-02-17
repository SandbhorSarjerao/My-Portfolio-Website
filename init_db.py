import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO contacts (email, subject, message) VALUES (?, ?, ?)")

connection.commit()
connection.close()
