use stadium_database;
DELIMITER //
CREATE TRIGGER before_insert_event
BEFORE INSERT ON Event_
FOR EACH ROW
BEGIN
    DECLARE total_stand_capacity INT;

  
    SELECT SUM(stand_capacity) INTO total_stand_capacity
    FROM Stands
    WHERE stadium_id = NEW.stadium_id;

   
    IF NEW.no_of_seats > total_stand_capacity THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No of seats exceeds stadium capacity';
    END IF;
END //
DELIMITER ;

drop trigger before_insert_event;



DELIMITER //

CREATE TRIGGER after_update_customer_location
AFTER UPDATE ON Customer
FOR EACH ROW
BEGIN
    -- Check if the location is set (NOT NULL)
    IF NEW.location IS NOT NULL THEN
        -- Update parking status to 'occupied'
        UPDATE Parking
        SET status = 'occupied'
        WHERE location = NEW.location;
    ELSE
        -- Update parking status to 'not occupied'
        UPDATE Parking
        SET status = 'not occupied'
        WHERE location = OLD.location; -- Use OLD.location since it's the value before the update
    END IF;
END //

DELIMITER ;













