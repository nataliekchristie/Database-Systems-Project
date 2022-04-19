-- Script name: triggers.sql
-- Author: Natalie Christie
-- Purpose: Additions of triggers to be run after forward engineering that react upon inserts 
-- to tables Appointment and Prescriptions

-- My database that the triggers will be applied to 
USE OnlineAppointmentDB;

-- -----------------------------------------------------
-- Trigger set_schedule_status
-- -----------------------------------------------------
-- Makes schedule day status "booked" when appointment made 

DELIMITER $$

CREATE TRIGGER set_schedule_status AFTER INSERT ON Appointment

FOR EACH ROW
	BEGIN
		UPDATE Schedule
        SET status = "Booked"
        WHERE date = new.date;
    END $$

DELIMITER ;

-- -----------------------------------------------------
-- Trigger add_to_medical_record
-- -----------------------------------------------------
-- Trigger to add to patient medical record when prescription is added

DELIMITER $$

CREATE TRIGGER add_to_medical_record AFTER INSERT ON Prescriptions
FOR EACH ROW
	BEGIN
		INSERT INTO Medical_Records(patient, prescriptions) VALUES (new.patient, new.prescription_id);
    END$$

DELIMITER ;

-- -----------------------------------------------------
-- Trigger add_doctor_info
-- -----------------------------------------------------
-- Adds all relevant info from employee table to the doctor 
-- table when created.

DELIMITER $$

CREATE TRIGGER add_doctor_info BEFORE INSERT ON Doctor
FOR EACH ROW
	BEGIN
		SET new.name = (SELECT name FROM Employee WHERE employee_id = new.employee_id);
        SET new.dob = (SELECT dob FROM Employee WHERE employee_id = new.employee_id);
        SET new.gender = (SELECT gender FROM Employee WHERE employee_id = new.employee_id);
        SET new.clinic = (SELECT clinic FROM Employee WHERE employee_id = new.employee_id);
    END$$

DELIMITER ;

-- -----------------------------------------------------
-- Trigger add_nurse_info
-- -----------------------------------------------------
-- Adds all relevant info from employee table to the nurse
-- table when created.

DELIMITER $$

CREATE TRIGGER add_nurse_info BEFORE INSERT ON Nurse
FOR EACH ROW
	BEGIN
		SET new.name = (SELECT name FROM Employee WHERE employee_id = new.employee_id);
        SET new.dob = (SELECT dob FROM Employee WHERE employee_id = new.employee_id);
        SET new.gender = (SELECT gender FROM Employee WHERE employee_id = new.employee_id);
        SET new.clinic = (SELECT clinic FROM Employee WHERE employee_id = new.employee_id);
    END$$

DELIMITER ;

-- -----------------------------------------------------
-- Trigger add_receptionist_info
-- -----------------------------------------------------
-- Adds all relevant info from employee table to the receptionist
-- table when created.

DELIMITER $$

CREATE TRIGGER add_receptionist_info BEFORE INSERT ON Receptionist
FOR EACH ROW
	BEGIN
		SET new.name = (SELECT name FROM Employee WHERE employee_id = new.employee_id);
        SET new.dob = (SELECT dob FROM Employee WHERE employee_id = new.employee_id);
        SET new.gender = (SELECT gender FROM Employee WHERE employee_id = new.employee_id);
        SET new.clinic = (SELECT clinic FROM Employee WHERE employee_id = new.employee_id);
    END$$

DELIMITER ;