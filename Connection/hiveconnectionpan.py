
import pyodbc
import pandas as pd

with pyodbc.connect("DSN=Hive_connection",autocommit=True) as conn:
    df = pd.read_sql("SELECT * FROM demo.occu", conn)

print(df)