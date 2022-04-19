-- Script name: inserts.sql
-- Author: Natalie Christie
-- Purpose: Insert database into the appointment database system.

-- the database that this script will be inserting into
USE OnlineAppointmentDB;

-- Truncating tables in order to eliminate repeats and test

-- Doing this so I can truncate tables with foreign key restraints
SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE Patient;
TRUNCATE TABLE Employee;
TRUNCATE TABLE Doctor;
TRUNCATE TABLE Nurse;
TRUNCATE TABLE Receptionist;
TRUNCATE TABLE Clinic;
TRUNCATE TABLE Appointment;
TRUNCATE TABLE Payment;
TRUNCATE TABLE Card;
TRUNCATE TABLE Insurance;
TRUNCATE TABLE Services;
TRUNCATE TABLE Doctor_Services;
TRUNCATE TABLE Nurse_Services;
TRUNCATE TABLE Schedule;
TRUNCATE TABLE Specialties;
TRUNCATE TABLE Doctor_Specialty;
TRUNCATE TABLE Appointment;
TRUNCATE TABLE Medical_Records;
TRUNCATE TABLE Prescriptions;
TRUNCATE TABLE Insurance_Providers;
TRUNCATE TABLE InsuranceP_Clinic;
TRUNCATE TABLE Fees;
TRUNCATE TABLE Appointment_Fee;
TRUNCATE TABLE Permissions;
TRUNCATE TABLE Employee_Permissions;
TRUNCATE TABLE Languages;
TRUNCATE TABLE Doctor_Language;
TRUNCATE TABLE Reviews;

-- Inserting in order of what is showing in the M1 Document.

-- Patient table inserts
INSERT INTO Patient (name, dob, gender, email, phone, address) VALUES 
("Alice Bark", "1998-07-04", "female", "AliceB@gmail.com", "745-783-4960", "123 6th st"),
("Tom Jones", "1980-06-02", "male", "TomJ2@yahoo.com", "234-895-8679", "753 Park Ln"),
("Sarah Pink", "2000-03-19", "female", "Sarah888@gmail.com", "123-567-8943", "576 Foothill Blvd"),
("Parker Hancock", "1995-07-23", "male", "PH4000@outlook.com", "456-123-8635", "222 Berry Street"),
("Nicole Hardy", "1997-10-28", "female", "NicoleHH@gmail.com", "198-749-9999", "1311 Woodside Blvd"),
("Gary Silva", "1990-11-11", "male", "GarySilv@outlook.com", "999-567-4333", "199 Bright Yd");

-- Employee table inserts
INSERT INTO Employee (name, dob, gender, clinic) VALUES
("Robert Bear", "1970-07-25", "male", 1), 
("Jesse Park", "1980-03-02", "female", 2), 
("Rachel Fair", "1999-12-22", "female", 3),
("Leanne Winters", "1977-05-17", "female", 2),
("Luke Golden", "1982-01-01", "male", 1),
("Clyde Booker", "1985-09-28", "male", 3),
("Mary Hayes", "1969-06-09", "female", 2),
("Jem Holden", "1990-10-19", "female", 1),
("Amber Burns", "1984-09-12", "female", 3);

-- Doctor table inserts
INSERT INTO Doctor (employee_id) VALUES
(1),
(2),
(3);

-- Nurse table inserts
INSERT INTO Nurse(employee_id) VALUES
(4),
(5),
(6);

-- Receptionist table inserts
INSERT INTO Receptionist(employee_id) VALUES
(7),
(9),
(8);

-- Clinic table inserts
INSERT INTO Clinic(address, phone) VALUES
("123 Willow St", "740-678-9000"),
("478 Adeline St", "740-123-7000"),
("533 Foothill Blvd", "640-555-8000");

-- Payment table inserts
INSERT INTO Payment (patient, card, insurance_id) VALUES
(1, 1, NULL),
(2, NULL, 1),
(3, 2, NULL),
(4, 3, 2),
(5, NULL, 3),
(6, 4, NULL);

-- Card table inserts
INSERT INTO Card(patient, card_no, expiration, CVV) VALUES
(1, "4916062140006706", "11/25", "484"),
(3, "4916368933064129", "09/28", "210"),
(6, "4539825954733574", "08/27", "595"),
(2, "929947322299654", "02/29", "738");

-- Insurance table inserts
INSERT INTO Insurance(patient, provider, member_id, group_no) VALUES
(2, 1, "12356786", "000"),
(4, 2, "23456962", "111"),
(5, 3, "09586735", "222");

-- Services table inserts
INSERT INTO Services(type, price) VALUES
("General Checkup", "100"),
("Eye Checkup", "60"),
("Physical", "120");

-- Doctor_Services table insert
INSERT INTO Doctor_Services (doctor, service) VALUES 
(1, 2),
(2, 1),
(3, 1),
(2, 3);

-- Nurse_Services table insert
INSERT INTO Nurse_Services (nurse, service) VALUES
(1, 1),
(2, 1),
(3, 1);

-- Schedule table inserts
INSERT INTO Schedule (date, doctor, status, clinic) VALUES
("2022-06-01 12:30:00", 2, "Available", 1),
("2022-06-02 13:00:00", 3, "Available", 2),
("2022-06-03 15:00:00", 1, "Available", 3),
("2022-06-04 9:00:00", 3, "Available", 2),
("2022-06-05 8:00:00", 1, "Available", 3);

-- Appointment table inserts 
INSERT INTO Appointment(patient, doctor, type, location, cancelled, date) VALUES 
(1, 2, "Checkup", 1, 0, "2022-06-01 12:30:00"),
(2, 3, "Checkup", 3, 0, "2022-06-20 13:00:00"),
(3, 1, "Checkup", 2, 0, "2022-07-15 15:00:00");

-- Specialties table inserts
INSERT INTO Specialties (type) VALUES
("General Practitioner"),
("Optometrist"),
("Physical Therapist");

-- Doctor_Specialty table inserts
INSERT INTO Doctor_Specialty (doctor, specialty) VALUES
(1, 1),
(2, 3),
(3, 2);

-- Account table inserts
INSERT INTO Account(patient_id, password) VALUES
(1, "password123"),
(4, "garfield420"),
(2, "amogus");

-- Medical Records table inserts (will also be inserted by trigger)
INSERT INTO Medical_Records(patient, prescriptions) VALUES
(3, 1),
(6, 2),
(5, 3);

-- Prescriptions table inserts
INSERT INTO Prescriptions(patient, doctor, date_prescribed, refills) VALUES
(1, 1, "2020-06-20", 1),
(2, 1, "2020-06-19", 1),
(3, 2, "2020-06-15", 0),
(4, 3, "2020-06-20", 0),
(6, 2, "2020-06-24", 1);

-- Insurance Providers table inserts
INSERT INTO Insurance_Providers(name, address) VALUES
("Medi-cal", "1501 Capitol Ave"),
("Anthem", "P.O. Box 60007 Los Angeles 95670"),
("Kaiser", "1 Kaiser Plaza Oakland CA 94612");

-- InsuranceP_Clinic table inserts
INSERT INTO InsuranceP_Clinic(insurance, clinic) VALUES
(1, 1),
(2, 1),
(3, 1),
(1, 2),
(3, 2);

-- Fees table inserts
INSERT INTO Fees(description, price) VALUES
("Late", "50"),
("Bloodwork", "100"),
("Rescheduled", "20");

-- Appointment_Fee table inserts
INSERT INTO Appointment_Fee(Appointment, Fee) VALUES
(1, 1),
(2, 3),
(1, 2);

-- Permissions table inserts
INSERT INTO Permissions(description) VALUES
("Scheduling"),
("Editing patient medical record"),
("Taking payment");

-- Employee_Permissions table inserts alter
INSERT INTO Employee_Permissions(employee, permission) VALUES
(1, 2),
(2, 2),
(3, 2),
(7, 1),
(9, 1),
(8, 1),
(7, 3);

-- Languages table inserts
INSERT INTO Languages(name) VALUES
("English"),
("Spanish"),
("Chinese"),
("Japanese"),
("French");

-- Doctor_Language table inserts
INSERT INTO Doctor_Language(doctor, language) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 1),
(3, 3),
(2, 4);

-- Reviews table inserts
INSERT INTO Reviews(patient, doctor, content) VALUES
(1, 1, "Amazing services, very friendly"),
(4, 3, "Was very helpful but could have been more communicative."),
(6, 2, "Overall helpful");

