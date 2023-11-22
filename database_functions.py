import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)

def insert_customer(first_name, last_name, gender, age, contact_no, ticket_id):

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Customer (first_name, last_name, gender, age, contact_no, ticket_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (first_name, last_name, gender, age, contact_no, ticket_id)
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
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_inserted_id = cursor.fetchone()[0]
        
        return last_inserted_id
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

def insert_seats(seat_no,stand_name,event_id):

    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO Seats (seat_no,stand_name,event_id)
        VALUES (%s, %s, %s)
        """
        data = (seat_no,stand_name,event_id)
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
def insert_staff(staff_name,staff_start_time, staff_end_time, type_, stadium_id):
    """Insert staff information into the staff table."""
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO staff (staff_name,staff_start_time, staff_end_time, type_, stadium_id)
        VALUES (%s,%s, %s, %s, %s)
        """
        data = (staff_name,staff_start_time, staff_end_time, type_, stadium_id)
        cursor.execute(query, data)
        connection.commit()
        print("Staff information inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def get_last_inserted_id():
    try:
        cursor=connection.cursor()
        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()[0]
        return last_id
    except:
        print("error while fetching last inserted id")

def update_seat(seat_no,stand_name,event_id,ticket_id):
    
    try:
        cursor = connection.cursor()
        query = """
        UPDATE Seats
        SET ticket_id = %s
        WHERE Seat_no = %s AND stand_name = %s and event_id=%s
        """
        data = (ticket_id, seat_no, stand_name,event_id)
        cursor.execute(query, data)
        connection.commit()
        print("Seat updated successfully")
    except Error as e:
        print(f"Error: {e}")

def delete_event(event_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM Event_ WHERE event_id = %s"
        data = (event_id,)
        cursor.execute(query, data)
        connection.commit()
        print("Event deleted successfully")
    except Error as e:
        print(f"Error: {e}")
def delete_vendor(vendor_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM Vendor WHERE Vendor_id = %s"
        data = (vendor_id,)
        cursor.execute(query, data)
        connection.commit()
        print("Vendor deleted successfully")
        return 
    except Error as e:
        print(f"Error: {e}")
        return
    
def delete_staff(staff_id):
    try:
        cursor = connection.cursor()
        query = "DELETE FROM staff WHERE staff_id = %s"
        data = (staff_id,)
        cursor.execute(query, data)
        connection.commit()
        print("Staff deleted successfully")
        return 
    except Error as e:
        print(f"Error: {e}")
        return

    


