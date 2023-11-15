from flask import Flask, render_template, request, redirect, url_for
import database_functions as df
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
        event_name=request.form['event_name']
        no_of_seats = int(request.form['no_of_seats'])
        event_type = request.form['event_type']
        stadium_id = int(request.form['stadium_id'])
        event_date = request.form['event_date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        
        functionalites.create_event(event_name,no_of_seats,event_type,stadium_id,event_date,start_time,end_time)
        return redirect('/admin/manage_event')
    else:  
        return render_template('create_event.html')

@app.route('/admin/manage_event')
def manage_event():
    events=functionalites.fetch_events()
    return render_template('manage_event.html',events=events)

@app.route('/admin/delete_event/<int:id>')
def delete_event(id):
    df.delete_event(id)
    return render_template('manage_event.html')

@app.route('/admin/manage_vendor')
def manage_vendor():
    vendors = functionalites.fetch_vendors()
    print(vendors)
    return render_template('manage_vendor.html', vendors=vendors)
@app.route('/admin/create_vendor')
def create_vendor():
    if request.method == 'POST':
        
        vendor_name = request.form['vendor_name']
        category = request.form['category']
        stand_name=request.form['stand_name']
        stadium_id=request.form['stadium_id']
        df.insert_vendor(stand_name,vendor_name, category,stadium_id)
        return redirect('/admin/manage_vendors')
    return render_template('create_vendor.html')

@app.route('/admin/delete_vendor/<int:id>')
def delete_vendor(id):
    df.delete_vendor(id)
    return redirect('/admin/manage_vendor')

@app.route('/admin/managestaff')
def manage_staff():
    

##############################################################################
@app.route('/admin/manage_staff', methods=['GET'])
def manage_staff():
    staff_list = fetch_staff()
    return render_template('manage_staff.html')

@app.route('/admin/create_staff', methods=['GET', 'POST'])
def create_staff():
    if request.method == 'POST':
        stadium_id = request.form['stadium_id']
        type_ = request.form['type_']
        staff_start_time = request.form['staff_start_time']
        staff_end_time = request.form['staff_end_time']
        
        add_staff(staff_name, staff_id, staff_start_time, staff_end_time)
        return redirect('/admin/manage_staff')

    return render_template('manage_staff.html')


@app.route('/admin/delete_staff/<staff_id>')
def remove_staff(staff_id):
    delete_staff(staff_id)
    return redirect('/admin/manage_staff')
    return render_template('manage_staff.html')

############################################################################# 


    

    



@app.route('/book/<int:id>',methods=['POST','GET'])
def book(id):
    if request.method=='POST':
        seats=request.form['selected_seats']
        standname=request.form['standname']
        price=functionalites.get_price(standname)
        total_price=len(seats)*price
        
        
        return redirect('/payment',)


    
    else:
        no_of_seats=functionalites.no_of_available_seats(id)
        seats=functionalites.show_available_seats(id)
        prices=functionalites.show_stand_price(id)

        return render_template('bookingpage.html',id=id,no_of_seats=no_of_seats,seats=seats,stand_prices=prices)


    


@app.route('/payment')
def payment():

    return render_template('payment.html',)

# @app.route('/payment')
# def book(seats,event_id,stand_name,payment_mode,price):
#     functionalites.book()

# Route for the ticket confirmation page
@app.route('/ticket')
def ticket():
    return render_template('ticket.html')


if __name__ == '__main__':
    app.run(debug=True)
