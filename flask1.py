from flask import Flask, render_template, request
import mysql.connector
import pandas as pd
import sqlalchemy
import pymysql


mydb = mysql.connector.connect(
    host = "localhost",
    user = "harsh",
    password = "Rogerharsh89#",
    database = "mydatabase"
)
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def form():
    if (request.method == 'POST'):
        name = request.form.get('uname')
        password = request.form.get('psw')
        engine = sqlalchemy.create_engine('mysql+pymysql://harsh:Rogerharsh89#@localhost:3306/mydatabase')
        df = pd.read_sql_table("login_info", engine)
        if((name in set(df["email"])) & (password in set(df["password"]))):
            return render_template("index.html")
        else:
            return render_template("loginform.html", a = "Wrong password")
        
    return render_template("loginform.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        mes = request.form.get('message')
        print(name, email, phone, mes)

        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE if not exists info(name char(50) , email varchar(50) , phone bigint, message varchar(500));")
        sql = "INSERT INTO info (name , email , phone, message) VALUES (%s , %s , %s , %s)"
        val = (name, email, phone, mes)
        mycursor.execute(sql , val)

        mycursor.execute("CREATE TABLE if not exists info(name char(50) , email varchar(50) , phone bigint, message varchar(500));")
        sql = "INSERT INTO info (name , email , phone, message) VALUES (%s , %s , %s , %s)"
        val = (name, email, phone, mes)
        mycursor.execute(sql , val)
        print("Value inserted !")


    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)