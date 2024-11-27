CREATE DATABASE chatbot;

USE chatbot;

CREATE TABLE timetable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    day VARCHAR(20) NOT NULL,
    time_slot VARCHAR(20) NOT NULL,
    subject VARCHAR(100)
);

INSERT INTO timetable (day, time_slot, subject)
VALUES
-- Monday Timetable
('Monday', '10:30 AM', 'PR/CC'),
('Monday', '11:30 AM', 'AIR/CNN'),
('Monday', '12:30 PM', 'NLP/IOT'),
('Monday', '01:30 PM', 'Lunch Break'),
('Monday', '02:30 PM', 'You Can Goto Library'),
('Monday', '03:30 PM', 'Club Hour'),
('Monday', '04:30 PM', 'Club Hour'),

-- Tuesday Timetable
('Tuesday', '10:30 AM', 'TP/AIG'),
('Tuesday', '11:30 AM', 'TG Slot'),
('Tuesday', '12:30 PM', 'AIR/CNN'),
('Tuesday', '01:30 PM', 'Lunch Break'),
('Tuesday', '02:30 PM', 'PR/CNN'),
('Tuesday', '03:30 PM', 'CNN Lab/AIR Lab'),
('Tuesday', '04:30 PM', 'CNN Lab/AIR Lab'),

-- Wednesday Timetable
('Wednesday', '10:30 AM', 'NLP/IOT'),
('Wednesday', '11:30 AM', 'PR/CC'),
('Wednesday', '12:30 PM', 'PR/CC'),
('Wednesday', '01:30 PM', 'Lunch Break'),
('Wednesday', '02:30 PM', 'TP/AIG'),
('Wednesday', '03:30 PM', 'NLP Lab/IOT Lab'),
('Wednesday', '04:30 PM', 'NLP Lab/IOT Lab'),

-- Thursday Timetable
('Thursday', '10:30 AM', 'AIR/CN'),
('Thursday', '11:30 AM', 'TP Lab/AIG Lab'),
('Thursday', '12:30 PM', 'Science'),
('Thursday', '01:30 PM', 'Lunch Break'),
('Thursday', '02:30 PM', 'OEC'),
('Thursday', '03:30 PM', 'Major Project Slot'),
('Thursday', '04:30 PM', 'Major Project Slot'),

-- Friday Timetable
('Friday', '10:30 AM', 'PR/CC'),
('Friday', '11:30 AM', 'NLP/IOT'),
('Friday', '12:30 PM', 'TP/AIG'),
('Friday', '01:30 PM', 'Lunch Break'),
('Friday', '02:30 PM', 'OEC'),
('Friday', '03:30 PM', 'Major Project Slot'),
('Friday', '04:30 PM', 'Major Project Slot'),

-- Saturday Timetable
('Saturday', '10:30 AM', 'Major Project Slot'),
('Saturday', '11:30 AM', 'Major Project Slot'),
('Saturday', '12:30 PM', 'Sports'),
('Saturday', '01:30 PM', 'Lunch Break'),
('Saturday', '02:30 PM', 'OEC'),
('Saturday', '03:30 PM', 'Major Project Slot'),
('Saturday', '04:30 PM', 'Major Project Slot'),

-- Sunday Timetable
('Sunday', '', 'Maajee Karo Bhai log');

SELECT * FROM timetable WHERE day = 'Monday'; 

DESCRIBE timetable;

CREATE TABLE timetable_second_year (
    day VARCHAR(20),
    time VARCHAR(50), 
    subject VARCHAR(100)
);


