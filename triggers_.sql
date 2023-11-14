DELIMITER //
CREATE TRIGGER BeforeEventInsert
BEFORE INSERT ON Event_
FOR EACH ROW
BEGIN
    DECLARE newTimeSlotId INT;

    -- Insert the corresponding time slot
    INSERT INTO Timing (date_, start_time, end_time)
    VALUES (NEW.event_date, NEW.start_time, NEW.end_time);

    -- Get the auto-generated time_slot_id
    SET newTimeSlotId = LAST_INSERT_ID();

    -- Update the event with the generated time slot id
    SET NEW.time_slot_id = newTimeSlotId;
END //

DELIMITER ;