use stadium_database;
create table Customer(
	customer_id int primary key,
    first_name char(15) NOT NULL,
    last_name char(15) NOT NULL,
    gender ENUM('M','F') not null,
    age int,
    contact_no char(10),
    ticket_id int not null,
    location varchar(7) not null
    
    );

create table Ticket(
	ticket_id int primary key,
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
	time_slot_id int primary key,
    date_ date,
    start_time time,
    end_time time
    );
create table Seats(

	Seat_no int primary key,
    status_ enum('booked','available') default 'available',
    ticket_id int,
    stand_name varchar(20)
    );
create table Event_(
	event_id int primary key,
    event_name varchar(20),
    no_of_seats int,
    type_ enum('Sport','concert'),
    stadium_id int,
    time_slot_id int
    );
    

    
    

    