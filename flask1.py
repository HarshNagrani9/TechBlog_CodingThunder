from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "harsh",
    password = "Rogerharsh89#",
    database = "mydatabase"
)
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

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

@app.route("/post")
def post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)