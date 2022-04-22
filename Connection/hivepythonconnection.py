
from pyhive import hive

import re,os, time

host_name="192.168.234.130"
port=10000
user="hive"
password="cloudera"
database="demo"

def hiveconnection(host_name,port,user,password,databsase):
    conn=hive.Connection(host=host_name,port=port,username=user,password=password,database=database,auth='CUSTOM')
    cur=conn.cursor()
    cur.execute('select * from emp')
    result=cur.fetchall()
    return result

output=hiveconnection(host_name,port,user,password,database)
print(output)