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