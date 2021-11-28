import mysql.connector

mydb = mysql.connector.connect(
  host="database-2.cfzxixaaphva.us-east-2.rds.amazonaws.com",
  user="admin",
  password="password",
  port='3306'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE crud2")

