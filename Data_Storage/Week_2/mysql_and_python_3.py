import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)

cursor = db.cursor()

sql = "INSERT INTO table1 (title, creation_date) VALUES (%s, %s)"
val = ("Title 1", "1998-05-06")
cursor.execute(sql, val)

db.commit()

print(cursor.rowcount, "record inserted.")