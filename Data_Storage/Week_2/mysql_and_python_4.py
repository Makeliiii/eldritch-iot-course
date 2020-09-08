import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM table1")

result = cursor.fetchall()

for i in result:
    print(i)