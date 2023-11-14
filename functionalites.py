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

