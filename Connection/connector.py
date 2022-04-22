
# to establish a connection to mysql databse

import mysql.connector

#def mysqlconnection():
mydb =mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='demo'
    )
print(mydb)
mycursor =mydb.cursor()
mycursor.execute("select * from credentials")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)