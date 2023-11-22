from flask import Flask, render_template, request, redirect, url_for,session
import database_functions as df
import functionalites
import json

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')




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
    return redirect('/admin/manage_event')

@app.route('/admin/manage_vendor')
def manage_vendor():
    vendors = functionalites.fetch_vendors()
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


    


@app.route('/admin/manage_staff', methods=['GET'])
def manage_staff():
    staff_list = functionalites.fetch_staff()
    counts=functionalites.count_of_staff_by_category(1)
    return render_template('manage_staff.html',staff_list=staff_list,counts=counts)

@app.route('/admin/add_staff', methods=['GET', 'POST'])
def create_staff():
    if request.method == 'POST':
        
        staff_name=request.form['staff_name']
        type_ = request.form['type_']
        staff_start_time = request.form['staff_start_time']
        staff_end_time = request.form['staff_end_time']
        
        df.insert_staff(staff_name, staff_start_time, staff_end_time)
        return redirect('/admin/manage_staff')

    return render_template('add_staff.html')


@app.route('/admin/delete_staff/<int:id>')
def remove_staff(id):
    df.delete_staff(id)
    return redirect('/admin/manage_staff')
    



    


@app.route('/events')
def events():
    events=functionalites.fetch_events()
    return render_template('events.html',events=events)   



@app.route('/booking_page/<int:id>',methods=['POST','GET'])
def booking_page(id):
    if request.method=='POST':
        selected_seats = request.form.getlist('selected_seats')
        seats_dict = {}
    
        for seat_value in selected_seats:
            stand_name, seat_no = seat_value.split('_')
            if stand_name not in seats_dict:
                seats_dict[stand_name] = []
            seats_dict[stand_name].append(seat_no)
        print(seats_dict)
        total_price=0
        for stand_name, seat_numbers in seats_dict.items():
            total_price += len(seat_numbers) * functionalites.get_price(stand_name)

        print(total_price)
        
        return render_template('payment.html', event_id=id,seats_dict=seats_dict,total_price=total_price)


    
    else:
        no_of_seats=functionalites.no_of_available_seats(id)
        seats=functionalites.show_available_seats(id)
        prices=functionalites.show_stand_prices(id)
        print(prices)
        
        standnames=functionalites.get_stand_names(id)
        return render_template('bookingpage.html',id=id,seats=seats,standnames=standnames,prices=prices,no_of_seats=no_of_seats)


    



# Flask route for handling payment confirmation
@app.route('/ticket/<int:event_id>', methods=['POST'])
def ticket(event_id):
    seats_dict_str = request.form.get('seats_dict')
    total_price = request.form.get('total_price')
    payment_mode=request.form.get('payment_mode')
    first_name =request.form.get('first_name')
    last_name=request.form.get('last_name') 
    gender=request.form.get('gender')
    age=request.form.get('age')
    contact_no=request.form.get('contact_no')
    
    
    seats_dict = json.loads(seats_dict_str.replace("'", "\""))

    booked_ticket_id = functionalites.book(seats_dict,event_id,payment_mode,total_price)
    df.insert_customer(first_name, last_name, gender, age, contact_no, booked_ticket_id)

    return render_template('ticket.html', booked_ticket_id=booked_ticket_id, seats_dict=seats_dict, total_price=total_price)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        cursor = db.cursor()
        # Check if the provided credentials match an admin in the database
        cursor.execute("SELECT * FROM admin WHERE admin_username = %s AND admin_password = %s", (username, password))
        admin = cursor.fetchone()
        cursor.close()

        if admin:
            # Successful login, redirect to admin panel or specific page
            return redirect('/admin')  # Replace with your admin panel route
        else:
            # Invalid credentials, show login page again with an error message
            return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
