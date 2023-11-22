create database stadium_database;

use stadium_database;

create table Customer(
	customer_id int primary key,
    first_name char(15) NOT NULL,
    last_name char(15) NOT NULL,
    gender ENUM('M','F') not null,
    age int,
    contact_no char(10),
    ticket_id int,
    location varchar(7)
);


    

create table Ticket(
	ticket_id int auto_increment primary key,
	mode_of_payment enum('upi','cash','card') not null,
    price int not null,
    event_id int not null
    );



create table Parking(
	location varchar(7) primary key,
    number_plate char(10) ,
    status enum('occupied','not occupied') default 'not occupied',
    automobile_type enum('4-wheeler','2-wheeler')
    );


create table Timing(
	time_slot_id int auto_increment key,
    date_ date,
    start_time time,
    end_time time
    );

create table Seats(

	Seat_no int,
	ticket_id int,
    stand_name varchar(20),
    event_id int,
    PRIMARY KEY (Seat_no, stand_name)
    );





create table Event_(
	event_id int auto_increment primary key,
    event_name varchar(20),
    no_of_seats int,
    type_ enum('Sport','concert'),
    stadium_id int,
    time_slot_id int
    );

create table Stands(
	stand_name varchar(20) primary key,
	stand_price int not null,
    stadium_id int,
    stand_capacity int
);



create table Vendor(
	Vendor_id int auto_increment primary key,
    stand_name varchar(20),
    Vendor_name varchar(20),
    category enum('food','merch'),
    stadium_id int
);

create table staff(
	staff_id int auto_increment primary key,
    staff_name varchar(10),
	staff_start_time time,
    staff_end_time time,
    type_ enum('hospitality','ticketing','security','cleaning'),
    stadium_id int
    );


create table stadium(
	stadium_id int  primary key,
    stadium_name varchar(20),
    stadium_location varchar(20)
    
    );


-- Add foreign key constraint for ticket_id
ALTER TABLE Customer
ADD CONSTRAINT fk_ticket_customer
FOREIGN KEY (ticket_id)
REFERENCES Ticket(ticket_id)
on update cascade;


-- Add foreign key constraint for location
ALTER TABLE Customer
ADD CONSTRAINT fk_location_customer
FOREIGN KEY (location)
REFERENCES Parking(location)
on update cascade;

-- Add foreign key constraint for stadium_id
ALTER TABLE Event_
ADD CONSTRAINT fk_stadium_event
FOREIGN KEY (stadium_id)
REFERENCES stadium(stadium_id)
ON UPDATE CASCADE;


-- Add foreign key constraint for time_slot_id
ALTER TABLE Event_
ADD CONSTRAINT fk_time_slot
FOREIGN KEY (time_slot_id)
REFERENCES Timing(time_slot_id)
ON UPDATE CASCADE;

ALTER TABLE Ticket
ADD constraint fk_event_id_ticket
foreign key(event_id)
references Event_(event_id)
on update cascade;

ALTER TABLE Seats
ADD CONSTRAINT fk_ticket_seats
FOREIGN KEY (ticket_id)
REFERENCES Ticket(ticket_id);
ALTER TABLE Seats
ADD CONSTRAINT fk_event_seats
FOREIGN KEY (event_id)
REFERENCES Event_(event_id);
-- Add foreign key constraint for stadium_id in Stands table
ALTER TABLE Stands
ADD CONSTRAINT fk_stadium_stands
FOREIGN KEY (stadium_id)
REFERENCES stadium(stadium_id)
ON UPDATE CASCADE; 

-- Add foreign key constraint for stadium_id in Vendor table
ALTER TABLE Vendor
ADD CONSTRAINT fk_stadium_vendor
FOREIGN KEY (stadium_id)
REFERENCES stadium(stadium_id)
ON UPDATE CASCADE; 

ALTER TABLE Vendor
ADD CONSTRAINT fk_standname_vendor
FOREIGN KEY (stand_name)
REFERENCES stands(stand_name)
ON UPDATE CASCADE;

-- Add foreign key constraint for stadium_id in staff table
ALTER TABLE staff
ADD CONSTRAINT fk_stadium_staff
FOREIGN KEY (stadium_id)
REFERENCES stadium(stadium_id)
ON UPDATE CASCADE;



INSERT INTO Stands (stand_name, stand_price, stadium_id, stand_capacity)
VALUES 
    ('StandA', 50, 1, 100),
    ('StandB', 40, 1, 80),
	('StandC', 30, 1, 120),
    ('StandD', 35, 1, 90);

    

    











 








    
    
	

    
    
    

    

    
    

    