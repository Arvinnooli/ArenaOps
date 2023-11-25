use stadium_database;


DELIMITER //
CREATE PROCEDURE GetAvailableSeatsForEvent(IN eventId INT)
BEGIN
    DECLARE totalSeats INT;
    DECLARE bookedSeats INT;

    select no_of_seats into totalSeats
    from event_
    where event_id=eventId;
    select	count(*) into bookedSeats
    from seats
    where ticket_id is not NULL;
    
    SELECT totalSeats - bookedSeats AS availableSeats;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE CreateEventWithTimeSlot(
    eventName VARCHAR(20),
    noOfSeats INT,
    eventType ENUM('Sport', 'concert'),
    stadiumId INT,
    eventDate DATE,
    startTime TIME,
    endTime TIME
)
BEGIN
    DECLARE newTimeSlotId INT;
    DECLARE newEventId INT;

    -- Insert the corresponding time slot
    INSERT INTO Timing (date_, start_time, end_time)
    VALUES (eventDate, startTime, endTime);

    -- Get the last inserted time slot ID
    SET newTimeSlotId = LAST_INSERT_ID();

    -- Insert the event using the obtained time slot ID
    INSERT INTO Event_ (event_name, no_of_seats, type_, stadium_id, time_slot_id)
    VALUES (eventName, noOfSeats, eventType, stadiumId, newTimeSlotId);

    -- Store the last inserted event ID in a session variable
    SET newEventId = LAST_INSERT_ID();

    -- Return the new event ID
    SELECT newEventId AS newEventId;
END //
DELIMITER ;



























    