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

