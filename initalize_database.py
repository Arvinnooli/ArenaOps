import database_functions as df
#insert stadium
# df.insert_stadium(1,"StadiumA","Bangalore")

# Insert Stands
stands_data = [
    ('StandA', 2000, 1),
    ('StandB', 1500, 1),
    ('StandC', 3000, 1),
    ('StandD', 1000, 1),
]
for stand in stands_data:
    df.insert_stands(*stand)

    # Insert Seats for each Stand
    stand_name = stand[0]
    for seat_no in range(1, 101):
        df.insert_seats(seat_no, None, stand_name)

print("Data inserted successfully.")



# # Insert time slots
# time_slots_data = [
#     ('2023-11-15', '18:00:00', '20:00:00'),
#     ('2023-11-15', '20:30:00', '22:30:00'),
#     # Add more time slots as needed
# ]

# for time_slot in time_slots_data:
#     df.insert_timing(*time_slot)

# print("Time slots inserted successfully.")

events_data = [
    ('Concert1', 300, 'concert', 1, 1), 
    ('SportsEvent1', 350, 'Sport', 1, 2),
]

for event in events_data:
    df.insert_event(*event)


