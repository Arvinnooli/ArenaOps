from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="templates", static_folder="static")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'lmao#711'
app.config['MYSQL_DB'] = 'stadium_database'

db = MySQL(app)

# Route for the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = db.connection.cursor()
        cur.execute("SELECT * FROM Users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()

        if user and user['password'] == password:
            return redirect(url_for('events'))
        else:
            return "INVALID USER"

    return render_template('login.html')

# Route for the events page
@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

# Routes for individual event pages (football, cricket, concert, car show)
@app.route('/football')
def football():
    return render_template('football.html')

@app.route('/cricket')
def cricket():
    return render_template('cricket.html')

@app.route('/taylor_swift_concert')
def taylor_swift_concert():
    return render_template('taylor_swift_concert.html')

# Route for the payment page
@app.route('/payment')
def payment():
    return render_template('payment.html')

# Route for the ticket confirmation page
@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

if __name__ == '__main__':
    app.run(debug=True)
