import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

print("connection started")

#create cursor
dbCursor = connection.cursor()

#create database if not exist
dbCursor.execute("CREATE DATABASE IF NOT EXISTS users")

#show databases
dbCursor.execute("SHOW DATABASES")

# close connection


for db in dbCursor:
    print(db)