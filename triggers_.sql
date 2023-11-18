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

CREATE TRIGGER generate_seats_after_event_insert
AFTER INSERT
ON Event_
FOR EACH ROW
BEGIN
    DECLARE stand_capacity INT;
    DECLARE total_capacity INT;

    -- Assuming there are four stands named StandA, StandB, StandC, and StandD
    DECLARE stand_names VARCHAR(100) DEFAULT 'StandA,StandB,StandC,StandD';
    DECLARE stand_name VARCHAR(20);

    -- Calculate the total capacity and stand capacity
    SET total_capacity = NEW.no_of_seats;
    SET stand_capacity = total_capacity / LENGTH(stand_names);

    -- Loop through each stand and insert seats
    WHILE LENGTH(stand_names) > 0 DO
        SET stand_name = SUBSTRING_INDEX(stand_names, ',', 1);
        INSERT INTO Seats (Seat_no, ticket_id, stand_name, event_id)
        SELECT
            SEAT_NUMBER.Seat_no,
            NULL AS ticket_id,
            stand_name,
            NEW.event_id
        FROM (
            SELECT
                (ROW_NUMBER() OVER ()) + (STAND_NUMBER.Stand_no - 1) * stand_capacity AS Seat_no
            FROM
                (SELECT 1 AS Stand_no UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) AS STAND_NUMBER
                CROSS JOIN (SELECT 1 AS Seat_no UNION SELECT 2 UNION SELECT 3 UNION SELECT 4) AS SEAT_NUMBER
            ) AS SeatNumbers
        WHERE
            Seat_no <= stand_capacity;

        -- Remove the processed stand from the list
        SET stand_names = TRIM(BOTH ',' FROM REPLACE(stand_names, stand_name, ''));
    END WHILE;
END //

DELIMITER ;




