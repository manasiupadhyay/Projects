import pymysql as p

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='food_details')

def addData(t):
    con=getConnection()
    cur=con.cursor()
    query1="insert into food_info (name,password,city) values(%s,%s,%s)"
    cur.execute(query1,t)
    con.commit()
    con.close()

def fetchData():
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from food_info")
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist

def specificdata(id):
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from food_info where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()
    return datalist[0]

def updatedata(t):
    con=getConnection()                  
    cur=con.cursor()
    query="update food_info set name=%s,password=%s,city=%s where id=%s"
    cur.execute(query,t)
    con.commit()
    con.close()


def deletedata(id):
    con=getConnection()                  
    cur=con.cursor()
    query="delete from food_info where id=%s"
    cur.execute(query,(id,))
    con.commit()
    con.close()

def addData1(t):
    con=getConnection()
    cur=con.cursor()
    query1="insert into food_info (name,password,city) values(%s,%s,%s)"
    cur.execute(query1,t)
    con.commit()
    con.close()

def addData2(t):
    con=getConnection()
    cur=con.cursor()
    query2="insert into contact(Name, People, Date) values(%s,%s,%s)"
    cur.execute(query2,t)
    con.commit()
    con.close()

def addData3(t):
    con=getConnection()
    cur=con.cursor()
    query3="insert into menu_details(name, person, Quintity) values(%s,%s,%s)"
    cur.execute(query3,t)
    con.commit()
    con.close()