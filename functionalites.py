import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
def fetch_events():
    try:
        cursor = connection.cursor()
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
        return events
    except:
        print("error while fetching event")

def create_event(event_name, no_of_seats, event_type, stadium_id, event_date, start_time, end_time):
    try:
        cursor = connection.cursor()

        # Call the stored function to create an event and get the event_id
        cursor.callproc("CreateEventWithTimeSlot", (
            event_name,
            no_of_seats,
            event_type,
            stadium_id,
            event_date,
            start_time,
            end_time
        ))

        # Fetch the result (event_id) from the stored function
        result = cursor.fetchone()

        # Commit the changes to the database
        connection.commit()

        return result[0]  # Assuming the result is a tuple with a single element (event_id)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
def no_of_available_seats(event_id):
    cursor=connection.cursor()
    cursor.callproc("GetAvailableSeatsForEvent",(event_id,))
    no_of_seats=cursor.fetchone()
    return no_of_seats

def show_stand_prices(event_id):
    cursor=connection.cursor()
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
    return stand_prices

def show_available_seats(event_id,stand_name):
    cursor=connection.cursor()
    cursor.execute('''SELECT s.Seat_no, s.stand_name
FROM Seats s
JOIN Ticket t ON s.ticket_id = t.ticket_id
WHERE s.ticket_id IS NULL
  AND t.event_id = %s;
''',(event_id))
    available_seats=cursor.fetchall()
    return available_seats
    
def book(seats,event_id,stand_name,payment_mode):
    cursor=connection.cursor()
    cursor.execute("insert into ticket")
    for seat_no in seats:
        
        






