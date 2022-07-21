from flask import Flask,request,redirect,render_template,session
from dbms import addData,fetchData, specificdata, updatedata,deletedata,addData2,addData3
import pymysql as p

app=Flask(__name__)

app.secret_key="abc"

def getConnection():
    return p.connect(host='localhost',user='root',port=3306,database='food_details')


#First Routing
@app.route("/")
def home_func():
    return render_template("home.html")

@app.route("/indexlink")
def index_func():
      return render_template("index.html")

#Second Routing
@app.route("/reglink")
def register_func():
      return render_template("register.html")


#third Routing
@app.route("/savelink",methods=["POST"])
def save_func():
    name=request.form['name']
    password=request.form['password']
    city=request.form['city']
    t=(name,password,city)
    addData(t)

    return redirect("reglink")

 #Second Routing
@app.route("/contactlink")
def contact_func():
      return render_template("contact.html")


#third Routing
@app.route("/savelink3",methods=["POST"])
def save2_func():
    Name=request.form['Name']
    People=request.form['People']
    Date=request.form['Date']
    
    t=(Name,People,Date)
    addData2(t)

    return render_template("index.html")  


@app.route("/menulink")
def menu_func():
      return render_template("menu.html")

#third Routing
@app.route("/savelink4",methods=["POST"])
def save3_func():
    name=request.form['name']
    person=request.form['person']
    Quintity=request.form['Quintity']
    t=(name,person,Quintity)
    addData3(t)
    return render_template("index.html")
    return "<h1>hi</h1>"   

#Fourth Routing
@app.route("/loginlink")
def login_func():
    return render_template("login.html")


@app.route("/indexlink",methods=["POST"])
def login_save():
    if request.method=='POST' and 'name' in request.form and 'password' in request.form:
        username=request.form['name']
        password=request.form['password']
        con=getConnection()
        cur=con.cursor()
        cur.execute("select * from food_info where name=% s AND password=% s",(username,password))
        result=cur.fetchone()
        

    return redirect("indexlink")
    

#fifth Routing
@app.route('/logoutlink')
def logout_func():
    session.pop('name',None)
    session.pop('password',None)
    return render_template("login.html")
   # return "<h1> LOGOUT SUCCESSFUL </h1>"

#sixth Routing
@app.route('/showlink')
def show_func():
    datalist=fetchData()
    return render_template("display.html",data=datalist)

@app.route("/editlink/<int:id>")
def displayforupdate(id):
    datalist=specificdata(id)
    return render_template("edit.html",data=datalist)

@app.route("/updatelink/<int:id>",methods=["POST"])
def updatefun(id):
    name=request.form["name"]
    password=request.form["password"]
    city=request.form["city"]
    t=(name,password,city,id)
    updatedata(t)
    return redirect("/showlink")

@app.route("/deletelink/<int:id>")
def deletefun(id):
    deletedata(id)
    return redirect("/showlink") 
 
if __name__=='__main__':
     app.run(debug=True)