import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="1234",
database="stadium_database"
)
c=conn.cursor()


def fetch_events():
    try:
        events=c.execute('''SELECT
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

def insert_customer():
    pass
