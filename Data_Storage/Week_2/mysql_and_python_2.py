import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "mydatabase"
)

cursor = db.cursor()

createTbl = "CREATE TABLE IF NOT EXISTS table1 (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), creation_date DATE)"
cursor.execute(createTbl)