import mysql.connector
from mysql.connector import Error
import  database_functions as df

connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
def fetch_events():
    try:
        connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
        cursor = connection.cursor(dictionary=True)
        cursor.execute('''SELECT
        e.event_id,
        e.event_name,
        t.start_time,
        t.end_time
    FROM
        Event_ e
    JOIN
        Timing t ON e.time_slot_id = t.time_slot_id;
    ''')
        events=cursor.fetchall()
        print(events)
        return events
    except:
        print("error while fetching event")
def fetch_staff(id):
    try:
        cursor = connection.cursor(dictionary=True)  # Use dictionary cursor to fetch results as dictionaries
        query = "SELECT * FROM staff where stadium_id=%s"
        cursor.execute(query,(id,))
        staff_list = cursor.fetchall()
        print(staff_list)
        return staff_list
    except Error as e:
        print(f"Error: {e}")
        return None

def fetch_vendors(id):
    try:
        cursor = connection.cursor(dictionary=True)  # Use dictionary cursor to fetch results as dictionaries
        query = "SELECT * FROM Vendor where stadium_id=%s"
        cursor.execute(query,(id,))
        vendors = cursor.fetchall()
      
        return vendors
    except Error as e:
        print(f"Error: {e}")
        return None
def calculate_and_insert_seats(event_id):
    try:
        cursor = connection.cursor()

        # Get the total number of seats and the number of stands for the given event
        query_event = "SELECT no_of_seats, stadium_id FROM Event_ WHERE event_id = %s"
        cursor.execute(query_event, (event_id,))
        event_data = cursor.fetchone()
        if not event_data:
            print("Event not found.")
            return

        total_seats = event_data[0]

        query_stands = "SELECT stand_name FROM Stands WHERE stadium_id = %s"
        cursor.execute(query_stands, (event_data[1],))
        stands = cursor.fetchall()
        total_stands = len(stands)

        # Calculate the number of seats for each stand
        seats_per_stand = total_seats // total_stands
        remaining_seats = total_seats % total_stands

        # Insert seats for each stand using the insert_seats function
        for stand in stands:
            for i in range(1,seats_per_stand):
                df.insert_seats(i, stand[0], event_id)

        print("Seats information calculated and inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def create_event(event_name, no_of_seats, event_type, stadium_id, event_date, start_time, end_time):
    try:
        cursor = connection.cursor()

       
        cursor.execute("select CreateEventWithTimeSlot(%s,%s,%s,%s,%s,%s,%s)", (
            event_name,
            no_of_seats,
            event_type,
            stadium_id,
            event_date,
            start_time,
            end_time,
        ))

        # Fetch the result (event_id) from the stored function
        result = cursor.fetchone()

        # Commit the changes to the database
        connection.commit()
        calculate_and_insert_seats(result[0])

        return result[0]  # Assuming the result is a tuple with a single element (event_id)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
def no_of_available_seats(event_id):
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("CALL GetAvailableSeatsForEvent(%s)",(event_id,))
        result = cursor.fetchall()
        return result[0]['availableSeats']
    except Exception as e:
        print(f"Error: {e}")
   

def show_stand_prices(event_id):
    connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
    cursor=connection.cursor(dictionary=True)
    cursor.execute('''SELECT
    
    stand_name,
    stand_price
FROM
    Event_
NATURAL JOIN
    Stadium
NATURAL JOIN
    Stands
where event_id=%s''',(event_id,) )
    stand_prices=cursor.fetchall()
   
    stand_with_price={}
    for dict in stand_prices:
        print(dict['stand_name'])
        stand_with_price[dict['stand_name']]=dict['stand_price']
   
    return stand_with_price

def show_available_seats(event_id):
    try:
        connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
       
        cursor = connection.cursor(dictionary=True)
        available_seats={}
        cursor.execute("""SELECT stand_name
FROM Event_ e
JOIN Stands s ON e.stadium_id = s.stadium_id
WHERE e.event_id = %s;
""",(event_id,))
        stand_names=cursor.fetchall()
       
        for stand_name in stand_names:



        
        
            cursor.execute("""
                    SELECT stand_name,seat_no
    FROM Event_ e
    NATURAL JOIN Seats s
    where e.event_id=%s  and s.stand_name=%s and ticket_id is null
                """,(event_id,stand_name['stand_name']))
            
            available_seats[stand_name['stand_name']]=cursor.fetchall()
        
        return available_seats
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")
def get_price(standname):
    connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
    cursor=connection.cursor()
    cursor.execute('''select stand_price 
                   from stands
                   where stand_name=%s''',(standname,))
    price=cursor.fetchone()
    print(price)
    return price[0]
    
def book(seats_dict,event_id,payment_mode,total_price):
    connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)

    cursor=connection.cursor()
   

    
    ticket_id = df.insert_ticket(payment_mode, total_price, event_id)

    # Update each seat in the dictionary
    for stand_name, seat_numbers in seats_dict.items():
        
        
        # Update each seat in the current stand
        for seat_no in seat_numbers:
            df.update_seat(seat_no, stand_name, ticket_id,event_id)

    print("Booking successful")
    return ticket_id
    

    

        
def get_stand_names(id):
    connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT stand_name
FROM Event_ e
JOIN Stands s ON e.stadium_id = s.stadium_id
WHERE e.event_id = %s;
""",(id,))
    stand_names=cursor.fetchall()
    return stand_names
   
# seats=show_available_seats(1)
# print(seats)
#nested query
def show_events_in_city(city):
    connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
       
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT *
FROM Event_
WHERE stadium_id IN (SELECT stadium_id FROM stadium WHERE stadium_location = %s)""",(city,))
    events=cursor.fetchall()
    return events
    
def count_of_staff_by_category(id):
    connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
       
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT  st.type_, COUNT(*) AS staff_count
FROM staff st
where st.stadium_id=%s
GROUP BY st.type_;
)""",(id,))
    counts=cursor.fetchall()
    return counts


# create_event(
#     event_name="Dummy Concert",
#     no_of_seats=350,
#     event_type="concert",
#     stadium_id=1,
#     event_date="2023-12-01",
#     start_time="18:00:00",
#     end_time="22:00:00"
# )



