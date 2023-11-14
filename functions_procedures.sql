use stadium_database;
DELIMITER //

CREATE PROCEDURE GetAvailableSeatsForEvent(IN eventId INT)
BEGIN
    DECLARE totalSeats INT;
    DECLARE bookedSeats INT;

    -- Get the total number of seats for the event
    SELECT no_of_seats INTO totalSeats
    FROM Event_
    WHERE event_id = eventId;

    -- Get the number of booked seats for the event
    SELECT COUNT(*) INTO bookedSeats
    FROM Seats
    WHERE ticket_id IS NOT NULL
    AND stand_name IN (
        SELECT stand_name
        FROM Event_
        WHERE event_id = eventId
    );

    -- Calculate and return the number of available seats
    SELECT totalSeats - bookedSeats AS availableSeats;
END //

DELIMITER ;
DELIMITER //

CREATE FUNCTION CreateEventWithTimeSlot(
    eventName VARCHAR(20),
    noOfSeats INT,
    eventType ENUM('Sport','concert'),
    stadiumId INT,
    eventDate DATE,
    startTime TIME,
    endTime TIME
)
RETURNS INT
DETERMINISTIC
BEGIN
    declare newEventId int;
-- Insert the corresponding time slot
    INSERT INTO Timing (date_, start_time, end_time)
    VALUES (eventDate, startTime, endTime);
    -- Insert the event
    INSERT INTO Event_ (event_name, no_of_seats, type_, stadium_id, time_slot_id)
    VALUES (eventName, noOfSeats, eventType, stadiumId, last_insert_id());
  set newEventId=last_insert_id();
  RETURN newEventId;
END //
DELIMITER ;

    