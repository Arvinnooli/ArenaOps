from flask import Flask, render_template, request, redirect, url_for
import database_functions



app = Flask(__name__, template_folder="templates", static_folder="static")









# Route for the events page
@app.route('/events')
def events():
    events=database_functions.fetch_events()
    
    
    return render_template('events.html',events=events)

@app.route('/admin/create_event')
def create_event():
    pass


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
