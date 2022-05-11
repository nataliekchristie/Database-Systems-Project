  -- Script name: tests.sql
  -- Author:      Natalie Christie
  -- Purpose:     Testing the database system for functionality
  
  -- Database that will be tested.
  USE OnlineAppointmentDB;
  SET SQL_SAFE_UPDATES = 0;

  -- 1. Testing Patient table
  
  DELETE FROM Patient WHERE name = 'Tom Jones';
  UPDATE Patient SET phone = '700-345-8591' WHERE name = 'Alice Bark';
  
  -- 2. Testing Employee table
  
  DELETE FROM Employee WHERE name = 'Mary Hayes';
  UPDATE Employee SET clinic = 2 WHERE name = 'Rachel Fair';
  
  -- 3. Testing Doctor table
  
  DELETE FROM Doctor WHERE employee_id = 2;
  UPDATE Doctor SET clinic = 2 WHERE employee_id = 1;
  
  -- 4. Testing Nurse table
  
  DELETE FROM Nurse WHERE employee_id = 5;
  UPDATE Nurse SET gender = 'female' WHERE employee_id = 6; 
  
  -- 5. Testing Receptionist table
  
  DELETE FROM Receptionist WHERE employee_id = 8;
  UPDATE Receptionist SET clinic = 1 WHERE employee_id = 7;
  
  -- 6. Testing Clinic table
  
  DELETE FROM Clinic WHERE address = '123 Willow St';
  UPDATE Clinic SET phone = '555-555-5555' WHERE clinic_id = 2;
  
  -- 7. Testing Appointment table
  
  DELETE FROM Appointment WHERE patient = 1;
  UPDATE Appointment SET cancelled = 1 WHERE patient = 3;
  
  -- 8. Testing Payment table
  
  DELETE FROM Payment WHERE patient = 6;
  UPDATE Payment SET insurance_id = NULL WHERE patient = 4;
  
  -- 9. Testing Card table
  
  DELETE FROM Card WHERE patient = 3;
  UPDATE Card SET CVV = '000' WHERE card_id = 4;
  
  -- 10. Testing Insurance table
  
  DELETE FROM Insurance WHERE provider = 3;
  UPDATE Insurance SET provider = 1 WHERE patient = 4;
  
  -- 11. Testing Services table
  
  DELETE FROM Services WHERE service_id = 1;
  UPDATE Services SET price = "70" WHERE type = "Eye Checkup";
  
  -- 12. Testing Doctor_Services table
  
  DELETE FROM Doctor_Services WHERE doctor = 3;
  UPDATE Doctor_Services SET service = 3 WHERE Doctor_Services_id = 1; 
  
  -- 13. Testing Nurse_Services table
  
  DELETE FROM Nurse_Services WHERE nurse = 2;
  UPDATE Nurse_Services SET service = 2 WHERE nurse = 3;
  
  -- 14. Testing Schedule table
  
  DELETE FROM Schedule WHERE clinic = 2;
  UPDATE Schedule SET status = "Available" WHERE schedule_id = 1;
  
  -- 15. Testing Specialties table
  
  DELETE FROM Specialties WHERE type = 'Optometrist';
  UPDATE Specialties SET type = 'General' WHERE specialty_id = 1; 
  
  -- 16. Testing Doctor_Specialty table
  
  DELETE FROM Doctor_Specialty WHERE doctor = 1;
  UPDATE Doctor_Specialty SET specialty = 2 WHERE doctor = 2;
  
  -- 17. Testing Account table
  
  DELETE FROM Account WHERE patient_id = 1;
  UPDATE Account SET password = 'hellohello' WHERE patient_id = 2;
  
  -- 18. Testing Medical_Records table
  
  DELETE FROM Medical_Records WHERE patient = 6;
  UPDATE Medical_Records SET prescriptions = 2 WHERE patient = 5;
  
  -- 19. Testing Prescriptions table
  
  DELETE FROM Prescriptions WHERE refills = 0;
  UPDATE Prescriptions SET refills = 0 WHERE patient = 1;
  
  -- 20. Testing Insurance_Providers table
  
  DELETE FROM Insurance_Providers WHERE name = 'Medi-cal';
  UPDATE Insurance_Providers SET name = 'Anthem Blue Cross' WHERE name = 'Anthem'; 
  
  -- 21. Testing InsuranceP_Clinic table
  
  DELETE FROM InsuranceP_Clinic WHERE clinic = 2;
  UPDATE InsuranceP_Clinic SET clinic = 3 WHERE InsuranceP_Clinic_id = 1;
  
  -- 22. Testing Fees table
  
  DELETE FROM Fees WHERE description = 'Rescheduled';
  UPDATE Fees SET price = '55' WHERE description = 'Late'; 
  
  -- 23. Testing Appointment_Fee table
  
  DELETE FROM Appointment_Fee WHERE Appointment = 2;
  UPDATE Appointment_Fee SET Fee = 3 WHERE Appointment_Fee_id = 1;
  
  -- 24. Testing Permissions table
  
  DELETE FROM Permissions WHERE permission_id = 2;
  UPDATE Permissions SET description = 'Filing' WHERE permission_id = 3;
  
  -- 25. Testing Employee_Permissions table
  
  DELETE FROM Employee_Permissions WHERE employee = 7;
  UPDATE Employee_Permissions SET permission = 3 WHERE permission = 2;
  
  -- 26. Testing Languages table
  
  DELETE FROM Languages WHERE name = 'Japanese';
  UPDATE Languages SET name = 'Italian' WHERE language_id = 5;
  
  -- 27. Testing Doctor_Language table
  
  DELETE FROM Doctor_Language WHERE doctor = 2;
  UPDATE Doctor_Language SET language = 3 WHERE Doctor_Language_id = 1;
  
  -- 28. Testing Reviews table
  
  DELETE FROM Reviews WHERE doctor = 3;
  UPDATE Reviews SET doctor = 2 WHERE content = 'Amazing services, very friendly';
  
    
  -- Testing notfications table
  DELETE FROM Notifications WHERE appointment = 1;
  UPDATE Notifications SET send_date = "2020-07-06 11:30:00" WHERE patient = 3;
  
  -- 29. Testing set_schedule_status trigger
  
  -- This trigger causes a schedule item to be marked as booked when an appointment is made.
  -- This tests the trigger by deleting anything that is booked. If items are deleted
  -- (that corresponds to the ones added in the appointment inserts) then it worked.
  
  -- DELETE FROM Schedule WHERE status = 'Booked';
  -- No error; no rows are being effected as intended and therefore something is off with the script 
  
  -- 30. Testing add_to_medical_record_prescription trigger
  
  -- In my insert statements patient 1 is not manually inserted into the medical records.
  -- Therefore this trigger will work if a patient is inserted through the prescription table
  -- And the patient/prescription is found. If patient 1 as demonstrated here is successfully
  -- deleted then the trigger worked.
  
  -- DELETE FROM Medical_Record WHERE patient = 1;
  -- Error Code: 1146. Table 'onlineappointmentdb.medical_record' doesn't exist
  
  -- 31. Testing add_to_medical_record_appointment trigger
  
  -- In my insert statements patient 1 is not manually inserted into the medical records.
  -- Therefore this trigger will work if a patient is inserted through the appointment table
  -- And the patient/appointment is found. If patient 1 as demonstrated here is successfully
  -- deleted then the trigger worked.
  
  -- DELETE FROM Medical_Record WHERE patient = 2;
  -- Error Code: 1146. Table 'onlineappointmentdb.medical_record' doesn't exist

  -- 32. Testing add_doctor_info trigger
  
  -- Checks that values were appropriately added when a doctor is made from employee id
  -- by removing inserted doctor by name that was added in the employee insert.
  -- If it returns true it was successfully updated
  
  DELETE FROM Doctor WHERE name = 'Robert Bear';
  
  -- 33. Testing add_nurse_info trigger
  
  -- Checks that values were appropriately added when a nurse is made from employee id
  -- by removing inserted nurse by name that was added in the employee insert.
  -- If it returns true it was successfully updated
  
  DELETE FROM Nurse WHERE name = 'Leanne Winters';
  
  -- 34. Testing add_receptionist_info trigger
  
  -- Checks that values were appropriately added when a receptionist is made from employee id
  -- by removing inserted receptionist by name that was added in the employee insert.
  -- If it returns true it was successfully updated
  
  DELETE FROM Receptionist WHERE name = 'Amber Burns';