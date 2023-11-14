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

@app.route('/admin')
def admin():
    return render_template('admin_page.html')

@app.route('/admin/create_event',methods=['POST','GET'])
def create_event():
    if request.method=='POST':
        event_name=request.form[event_name]
        no_of_seats = int(request.form['no_of_seats'])
        event_type = request.form['event_type']
        stadium_id = int(request.form['stadium_id'])
        event_date = request.form['event_date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        
        functionalites.create_event(event_name,no_of_seats,event_type,stadium_id,event_date,start_time,end_time)
        return redirect('/admin')
        
    return render_template('create_event.html')
    


    

    


@app.route('/book/<int:id>',methods=['POST','GET'])
def book(id):
    if request.method=='POST':
        seat=request.form['selected_seat']
        functionalites.book(seat,id)


    
    else:
        no_of_seats=functionalites.no_of_available_seats(id)
        seats=functionalites.show_available_seats(id)
        return render_template('bookingpage.html',id=id,seats=seats)
    


@app.route('/payment')
def payment():
    return render_template('payment.html')

# Route for the ticket confirmation page
@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

if __name__ == '__main__':
    app.run(debug=True)
