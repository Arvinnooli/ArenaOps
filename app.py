from flask import Flask, render_template, request, redirect, url_for
import database_functions
import functionalites



app = Flask(__name__, template_folder="templates", static_folder="static")






@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')


# Route for the events page
@app.route('/events')
def events():
    events=functionalites.fetch_events()
    print(events)
    return render_template('events.html',events=events)

@app.route('/admin/create_event')
def create_event():

    pass


@app.route('/book/<int:id>')
def book(id):
    return render_template('bookingpage.html',id=id)
    


@app.route('/payment')
def payment():
    return render_template('payment.html')

# Route for the ticket confirmation page
@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

if __name__ == '__main__':
    app.run(debug=True)
