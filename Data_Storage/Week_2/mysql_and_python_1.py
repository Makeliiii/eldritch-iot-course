import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

cursor = db.cursor()

createDB = "CREATE DATABASE IF NOT EXISTS mydatabase"
cursor.execute(createDB)