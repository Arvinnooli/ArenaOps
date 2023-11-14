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
        events=cursor.execute('''SELECT
        e.event_name,
        t.start_time,
        t.end_time
    FROM
        Event_ e
    JOIN
        Timing t ON e.time_slot_id = t.time_slot_id;
    ''')
        return events
    except:
        print("error while fetching event")


def insert_customer(first_name, last_name, gender, age, contact_no, ticket_id, location, user_password):
  
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Customer (first_name, last_name, gender, age, contact_no, ticket_id, location, Userpassword)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (first_name, last_name, gender, age, contact_no, ticket_id, location, user_password)
        cursor.execute(query, data)
        connection.commit()
        print("Customer inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_event(event_name, no_of_seats, type_, stadium_id, time_slot_id):

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Event_ (event_name, no_of_seats, type_, stadium_id, time_slot_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (event_name, no_of_seats, type_, stadium_id, time_slot_id)
        cursor.execute(query, data)
        connection.commit()
        print("Event inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_ticket(mode_of_payment, price, event_id):
   
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Ticket (mode_of_payment, price, event_id)
        VALUES (%s, %s, %s)
        """
        data = (mode_of_payment, price, event_id)
        cursor.execute(query, data)
        connection.commit()
        print("Ticket inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_parking(location, number_plate, status, automobile_type):
    """Insert parking information into the Parking table.""" 
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Parking (location, number_plate, status, automobile_type)
        VALUES (%s, %s, %s, %s)
        """
        data = (location, number_plate, status, automobile_type)
        cursor.execute(query, data)
        connection.commit()
        print("Parking information inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_timing(date_, start_time, end_time):
  
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Timing (date_, start_time, end_time)
        VALUES (%s, %s, %s)
        """
        data = (date_, start_time, end_time)
        cursor.execute(query, data)
        connection.commit()
        print("Timing information inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_seats(seat_no,ticket_id, stand_name):

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Seats (Seat_no, ticket_id, stand_name)
        VALUES (%s, %s, %s)
        """
        data = (seat_no,ticket_id, stand_name)
        cursor.execute(query, data)
        connection.commit()
        print("Seat information inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_stadium(stadium_id,stadium_name, stadium_location):

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO stadium (stadium_id,stadium_name, stadium_location)
        VALUES (%s,%s, %s)
        """
        data = (stadium_id,stadium_name, stadium_location)
        cursor.execute(query, data)
        connection.commit()
        print("Stadium information inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_stands(stand_name, stand_price, stadium_id):
   
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Stands (stand_name, stand_price, stadium_id)
        VALUES (%s, %s, %s)
        """
        data = (stand_name, stand_price, stadium_id)
        cursor.execute(query, data)
        connection.commit()
        print("Stand information inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_vendor(stand_name, vendor_name, category, stadium_id):
    """Insert vendor information into the Vendor table."""
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Vendor (stand_name, Vendor_name, category, stadium_id)
        VALUES (%s, %s, %s, %s)
        """
        data = (stand_name, vendor_name, category, stadium_id)
        cursor.execute(query, data)
        connection.commit()
        print("Vendor information inserted successfully")
    except Error as e:
        print(f"Error: {e}")
def insert_staff(staff_start_time, staff_end_time, type_, stadium_id):
    """Insert staff information into the staff table."""
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO staff (staff_start_time, staff_end_time, type_, stadium_id)
        VALUES (%s, %s, %s, %s)
        """
        data = (staff_start_time, staff_end_time, type_, stadium_id)
        cursor.execute(query, data)
        connection.commit()
        print("Staff information inserted successfully")
    except Error as e:
        print(f"Error: {e}")



