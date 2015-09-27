__author__ = 'nicor'

import psycopg2
### psycopg2 needs postgresql-server-dev-all , install with sudo apt-get install postgresql-server-dev-all

dbname = 'db'
dbuser = 'user'
host = 'localhost'
password ='password'
connectionString = "dbname='"+dbname+"' user='"+dbuser+"' host='"+host+"' password='"+password+"'"


try:
    conn = psycopg2.connect(connectionString)
    cur = conn.cursor()
    cur.execute("""SELECT * from test""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
except:
    print("I am unable to connect to the database")