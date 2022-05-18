Natalie Christie
918376646

Discord link:
https://discord.gg/Zhc9zgCPvZ

Replit link:
https://replit.com/join/jhixzurquc-nkchristie

1. Find the total number of individual patients treated by a doctor at appointments in descending order.
Command: “\no_of_patients <doctor>”
Example:  \no_of_patients 2 

2. Find the number of doctors who have written prescriptions to over X patients. Command: “\doctor_presc <number of patients>”
Example: \doctor_presc 0

3. Update the schedule to make a schedule day available and the appointment marked as cancelled when it is cancelled by the patient.
(This command will find the appointment date, then the associated schedule date, and change its status to available)
Command: “\cancel_appointment <patient id> <date>”
Example: \cancel_appointment 1 2020-06-01 10:00:00

4. Show the total number of doctors and nurses for a clinic. 
Command: “\clinic_all_doct_nurse <clinic id>”
Example: \clinic_all_doct_nurse 1

5. Create a notification for 1 week and 1 day before an appointment is made. (This command will take an appointment date, find the date a week and a day before and create a notification for the patient with the specified content) 
Command: “\create_notif <appointment id> <content>”
Example: \create_notif 5 "Don't forget your appointment!"

6. Find all the appointments where a patient was serviced by specific doctor. 
Command: “\patient_doctor_appt <patient name> <doctor name>”
Example: 
\patient_doctor_appt Sarah Pink Robert Bear
or
\patient_doctor_appt "Sarah Pink" "Robert Bear"

7. Find all doctors at clinic X who speak Y language. 
Command: “\doc_clinic_lang <clinic id> <language>”
Example: \doc_clinic_lang 2 English

8. For every clinic, find the total number of cancelled appointments within a specified month.
Command: “\clinic_cancellations <date>”
Example: \clinic_cancellations July

9. Find all clinics that accept an insurance provider X. 
Command: “\clinics_insurance_provider <provider>”
Example: \clinics_insurance_provider Anthem

10. Create a function that returns the total cash value in fees accrued by a patient.
 Command: “\patient_fees <patient>”
Example: \patient_fees Alice Bark

11. Find all the reviews for doctors that work at clinic X. 
Command: “\clinic_reviews <clinic>”
Example: \clinic_reviews 3

12. For each clinic find all the days on schedule based on a specified status. (Ex: available)
Command: “\clinic_schedule <status>”
Example: \clinic_schedule Booked

13. Create a function that returns the total number of appointments marked as booked for each doctor within a certain timeframe.
Command: “\doct_appt_dates <start date> <end date>”
Example: \doct_appt_dates 2022-06-01 2022-07-03

14. Create a function that returns the total number of patients for all clinics that have an insurance provider X on their payment.
Command: “\get_patients_provider <insurance provider id>”
Example: \get_patients_provider 1

15.  Find the total number of appointments made by a patient within a specified timeframe.
Command: “\patient_appointments_time <patient id> <start date> <end date>”
Example: \patient_appointments_time 2 2022-06-01 2022-07-03

16. For a clinic X find all doctors who work there who have a specialty Y. 
Command: “\find_doctor_specialty <clinic id> <specialty>”
Example: \find_doctor_specialty 2 Optometrist

17. For a patient X find all the reviews they made for a doctor Y. 
Command: “\find_reviews <patient id> <doctor id>”
Example: \find_reviews 1 2

18.  Create a procedure that finds the clinic with the most services provided by nurses and doctors combined.
Command: “\most_clinic_services”
* no input needed.