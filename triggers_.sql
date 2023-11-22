DELIMITER //
CREATE TRIGGER before_insert_event
BEFORE INSERT ON Event_
FOR EACH ROW
BEGIN
    DECLARE total_seats INT;

    -- Retrieve the total number of seats in the stadium
    SELECT COUNT(*) INTO total_seats
    FROM stadium AS st
    JOIN stands AS s ON st.stadium_id = s.stadium_id
    JOIN seats AS se ON s.stand_name = se.stand_name;

    -- Check if the _no_of_seats for the new event exceeds the total seating capacity
    IF NEW.no_of_seats > total_seats THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: The number of seats exceeds the total seating capacity';
    END IF;
END;
//
DELIMITER ;
DELIMITER //

CREATE TRIGGER CheckTimeSlotOverlap
BEFORE INSERT ON Timing
FOR EACH ROW
BEGIN
    DECLARE existing_start_time TIME;
    DECLARE existing_end_time TIME;

    -- Check for overlapping time slots
    SELECT start_time, end_time
    INTO existing_start_time, existing_end_time
    FROM Timing
    WHERE NEW.date_ = date_
    AND (NEW.start_time BETWEEN start_time AND end_time
         OR NEW.end_time BETWEEN start_time AND end_time
         OR (NEW.start_time <= start_time AND NEW.end_time >= end_time));

    IF existing_start_time IS NOT NULL AND existing_end_time IS NOT NULL THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'New time slot overlaps with an existing time slot';
    END IF;
END //

DELIMITER ;

DELIMITER //





