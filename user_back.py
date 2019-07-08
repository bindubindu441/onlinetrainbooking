import sqlite3
def connect_user1():
     conn=sqlite3.connect("onlinetrainbooking1.db")
     cur=conn.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS trainusr (aadharnumber INTEGER PRIMARY KEY ,name text,age integer,gender text,nationality text,source text,destination text,foodservice text)")
     conn.commit()
     conn.close()


def insert_user1(aadharnumber,name,age,gender,nationality,source,destination,foodservice):
    conn=sqlite3.connect("onlinetrainbooking1.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO trainusr VALUES(?,?,?,?,?,?,?,?)",(aadharnumber,name,age,gender,nationality,source,destination,foodservice))
    conn.commit()
    conn.close()


def view_user1():
    conn=sqlite3.connect("onlinetrainbooking1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM trainusr")
    rows=cur.fetchall()
    conn.close()
    return rows




def search_user1(aadharnumber="",name=""):
    conn=sqlite3.connect("onlinetrainbooking1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM trainusr WHERE aadharnumber=? OR name=?",(aadharnumber,name))
    rows=cur.fetchall()
    conn.close()
    return rows





#connect()
connect_user1()

#insert_user1(7638899,"manisha",20,"f","ind","hyd","blr","yes")
#search_user1(76312,"manisha")
#update_user1(1234,"bhagya",21,"f","ind",no)
#print(search_user1(20,"charan"))
#delete()
print(view_user1())
#submit(96317,"momin",30,40,"saudi",)


