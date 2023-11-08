from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='lmao#711'
app.config['MYSQL_DB']='stadium_database'

db=MySQL(app)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)