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
	RETURN last_insert_id() ;
END //
DELIMITER ;


drop function CreateEventWithTimeSlot;
-- Call the CreateEventWithTimeSlot function with dummy values
select CreateEventWithTimeSlot('Dummy Event', 300, 'Sport', 1, '2023-01-01', '12:00:00', '18:00:00') as event_id;
























    