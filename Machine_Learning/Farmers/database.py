import sqlite3
conn = sqlite3.connect('farmer.db')   # connection with database

#import mysql.connector as mc
#conn = mc.connect(host = 'localhost',user = 'root',passwd = '')

query = "create table farmerdata (N int,P int,k int,t int,h int,ph int,r int,prediction)"
curs_obj = conn.cursor()   # cursor - temporary memory (cur_obj an object)

curs_obj.execute(query)
print("successfully created database and table")
conn.commit()
curs_obj.close()
conn.close()