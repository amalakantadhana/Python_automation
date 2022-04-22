import pandas as pd
import mysql.connector as msql
from mysqlx.protobuf.mysqlx_pb2 import Error
from sqlalchemy import create_engine
#
# # Credentials to database connection
# hostname="localhost"
# dbname="readcsv"
# uname="root"
# pwd="admin"

csvdata=pd.read_csv('D:\\CSV\\SampleCSVFile_10Rows.csv',encoding="ISO-8859-1")
print(csvdata.head())
#print(csvdata)

try:
    conn = msql.connect(host='localhost',
                           database='readcsv', user='root',
                           password='admin')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS company;')
        print('Creating table....')
        cursor.execute("create table company(id int, orgname varchar(100), name varchar(50), companyno int, companyvalue float, "
					   "orgvalue float, serialno int, specialcategory varchar(30),companystoname varchar(30), percentvalue float)")
        print("company table is created....")
        for i,row in csvdata.iterrows():
            print(i)
            sql = "INSERT INTO readcsv.company VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            #print(tuple(row))
            # the connection is not autocommitted by default, so we
            # must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

# Execute query
sql = "SELECT * FROM company"
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
