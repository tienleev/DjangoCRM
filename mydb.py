import mysql.connector

dataBase = mysql.connector.connect(
    host="127.0.0.1",
    user = "root",
    passwd = "root",
)

mycursor = dataBase.cursor()

mycursor.execute("CREATE DATABASE levati")
print("Database created successfully")
