import sqlite3
def connect():
    conn=sqlite3.connect("onlinetrainbooking.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS train2 (trainnumber INTEGER PRIMARY KEY,berthpreference text,coach text ,departuretime integer,arrivaltime integer)" )
    conn.commit()
    conn.close()

def insert(trainnumber,berthpreference,coach,departuretime,arrivaltime):
    conn = sqlite3.connect("onlinetrainbooking.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO train2 VALUES(?,?,?,?,?)",(trainnumber,berthpreference,coach,departuretime,arrivaltime))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("onlinetrainbooking.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train2")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(trainnumber="",berthpreference=""):
    conn=sqlite3.connect("onlinetrainbooking.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM train2  WHERE trainnumber=? OR berthpreference=?",(trainnumber,berthpreference))
    rows=cur.fetchall()
    conn.close()
    return rows



def update(trainnumber,berthpreference,coach,departuretime,arrivaltime):
    conn=sqlite3.connect("onlinetrainbooking.db")
    cur=conn.cursor()
    cur.execute("UPDATE train2 SET berthpreference=?,coach=?,departuretime=?,arrivaltime=? WHERE trainnumber =?",(trainnumber,berthpreference,coach,departuretime,arrivaltime))
    conn.commit()
    conn.close()


def delete(trainnumber):
    conn=sqlite3.connect("onlinetrainbooking.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM train2 WHERE trainnumber=? ", (trainnumber,))
    conn.commit()
    conn.close()


connect()

#insert(9977,"lower","s","12","5")
#update(9876,"upper","h","12","3")
#delete(10)
print(view())
