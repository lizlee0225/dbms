import pymysql as pm
import sys

### the script needs to be run with berkeley's wifi. If at home, please use VPN

### set mysql server
Mysql_host = '128.32.78.26'
Mysql_username = 'xuancheng_fan'
Mysql_password = 't3BVxkAt'
Mysql_db = 'xuancheng_fan'

### connect to server
con = pm.connect(Mysql_host, Mysql_username, Mysql_password, Mysql_db)
c = con.cursor()

### get query result
def sql_query(sql):
    try:
        c.execute(sql)
        results = c.fetchall()
    except:
        print("Error: unable to fetch data")
    return results

def sql_edit(sql):
    try:
        c.execute(sql)
        con.commit()
    except:
    # if error, rollback
        con.rollback()    

# sample 1: query        
sql = 'SELECT Artist1.Name FROM `Artist1`,`Area1` where Artist1.Area_id = 111'
results = sql_query(sql)

for items in results:
    print(items)
    
# sample 2: edit
sql = 'UPDATE Artist1 SET Area_id = Area_id +1 WHERE Name = "Terrorvision"'
sql_edit(sql)

sql = 'SELECT * from Artist1'
results = sql_query(sql)

for items in results:
    print(items)

    
# end connection
con.close()
