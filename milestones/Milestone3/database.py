# database.py
# Handles all the methods interacting with the database of the application.
# Students must implement their own methods here to meet the project requirements.

import os
import pymysql.cursors
import datetime
from datetime import datetime as dt
from prettytable import PrettyTable

db_host = os.environ['DB_HOST']
db_username = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']

def connect():
    try:
        conn = pymysql.connect(host=db_host,
                               port=3306,
                               user=db_username,
                               password=db_password,
                               db=db_name,
                               charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
        print("Bot connected to database {}".format(db_name))
        return conn
    except:
        print("Bot failed to create a connection with your database because your secret environment variables " +
              "(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME) are not set".format(db_name))
        print("\n")

# your code here

def response(msg):
  db_response = None
  command_parts = msg.split()
  bot_command = command_parts[0]
  if "\\no_of_patients" in bot_command:
    doctor = command_parts[1]
    db_response = no_of_patients(doctor)
  elif "\doctor_presc" in bot_command:
    no_patients = command_parts[1]
    db_response = doctor_presc(no_patients)
  elif "\cancel_appointment" in bot_command:
    patient = command_parts[1]
    # join date time for variable
    datetime = command_parts[2]+' '+command_parts[3]
    db_response = cancel_appointment(patient, datetime)
  elif "\clinic_all_doct_nurse" in bot_command:
    clinic = command_parts[1]
    db_response = clinic_all_doct_nurse(clinic)
  elif "\\create_notif" in bot_command:
    appointment = command_parts[1]
    content = command_parts[2]
    for i in range(3, len(command_parts)):
      content = content+' '+command_parts[i]
    content.replace('"','')
    print(content)
    db_response = create_notif(appointment, content)
  # remove quotes from name if present 
  elif "\patient_doctor_appt" in bot_command:
    patient = command_parts[1].replace('"','')+' '+command_parts[2].replace('"','')
    doctor = command_parts[3].replace('"','')+' '+command_parts[4].replace('"','')
    db_response = patient_doctor_appt(patient, doctor)
  elif "\doc_clinic_lang" in bot_command:
    clinic = command_parts[1]
    language = command_parts[2]
    db_response = doc_clinic_lang(clinic, language)
  elif "\clinic_cancellations" in bot_command:
    date = command_parts[1]
    db_response = clinic_cancellations(date)
  elif "\clinics_insurance_provider" in bot_command:
    # start at first part of command
    finalinput = command_parts[1]
    # concat all input to make final name
    for i in range(2, len(command_parts)):
      finalinput = finalinput+' '+command_parts[i]
    db_response = clinics_insurance_provider(finalinput)
  elif "\patient_fees" in bot_command:
    #start at firstf part of command
    finalinput = command_parts[1]
    # concat all input to make final name
    for i in range(2, len(command_parts)):
      finalinput = finalinput+' '+command_parts[i]
    db_response = patient_fees(finalinput)
  elif "\clinic_reviews" in bot_command:
    clinic = command_parts[1]
    db_response = clinic_reviews(clinic)
  elif "\clinic_schedule" in bot_command:
    status = command_parts[1]
    db_response = clinic_schedule(status)
  elif "\doct_appt_dates" in bot_command:
    startdate = command_parts[1]
    enddate = command_parts[2]
    db_response = doct_appt_dates(startdate, enddate)
  elif "\get_patients_provider" in bot_command:
    insurance_p = command_parts[1]
    db_response = get_patients_provider(insurance_p)
  elif "\patient_appointments_time" in bot_command:
    patient = command_parts[1]
    start = command_parts[2]
    end = command_parts[3]
    db_response = patient_appointments_time(patient, start,      end)
  elif "\\find_doctor_specialty" in bot_command:
    clinic = command_parts[1]
    # replace quotes jic
    specialty = command_parts[2].replace('"','')
    # concat if specialty is more than one word
    for i in range(3, len(command_parts)):
      specialty = specialty+' '+command_parts[3].replace('"','')
    db_response = find_doctor_specialty(clinic, specialty)
  elif "\\find_reviews" in bot_command:
    patient = command_parts[1]
    doctor = command_parts[2]
    db_response = find_reviews(patient, doctor)
  elif "\most_clinic_services" in bot_command:
    db_response = most_clinic_services()
  return db_response

# default execute as to not repeat this same code 
def execute(query, variables):
  results = None
  try:
    connection = connect()
    if connection:
      cursor = connection.cursor()
      cursor.execute(query, variables)
      results = cursor.fetchall()
  except Exception as error:
      print(error)
      results = "Error"
  connection.commit()
  connection.close()
  return results

def no_of_patients(doctor):
  result = None 
  query = """SELECT COUNT(*) AS "Total Patients" FROM Patient JOIN Appointment ON Patient.patient_id = Appointment.patient JOIN Doctor ON Appointment.doctor = Doctor.doctor_id WHERE Doctor.doctor_id = %s"""
  variables = (doctor)
  results = execute(query, variables)
  if results:
    temp = []
    for data in results:
      no_patient = data["Total Patients"]
      temp.append((no_patient))
    print(temp)
    result = PrettyTable()
    result.field_names = ["Total Patients"]
    for data in temp:
      result.add_row([data])
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def doctor_presc(num):
  result = []
  query = """SELECT Employee.name AS "Doctor" FROM Doctor JOIN Employee ON Employee.employee_id = Doctor.employee_id WHERE 
(SELECT COUNT(Patient.patient_id) FROM Patient JOIN Prescriptions
ON Patient.patient_id = Prescriptions.patient WHERE Doctor.doctor_id = Prescriptions.doctor) >= %s"""
  variables = (num)
  results = execute(query, variables)
  if results:
    for data in results:
      doctor = data["Doctor"]
      result.append(doctor)
    temp = PrettyTable()
    temp.field_names = ["Doctor Name"]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def cancel_appointment(patient, date):
  result = None 
  query1 = """UPDATE Schedule SET Schedule.status = "Available" WHERE Schedule.date = %s """
  query2 = """UPDATE Appointment SET Appointment.cancelled = 1 WHERE Appointment.patient = %s AND Appointment.date = %s """
  variables1 = (date)
  variables2 = (patient, date)
  results = execute(query1, variables1)
  results2 = execute(query2, variables2)
  print(results)
  print(results2)
  if results == "Error" or results2 == "Error":
    result = "Error updating database."
  else:
    result = "Database successfully updated!"
  return result

def clinic_all_doct_nurse(clinic):
  result = None 
  query = """SELECT
(SELECT COUNT(Doctor.doctor_id) FROM Doctor JOIN Employee ON Employee.employee_id = 
Doctor.employee_id WHERE Employee.clinic = %s)
+
(SELECT COUNT(Nurse.nurse_id) FROM Nurse JOIN Employee ON Employee.employee_id =
Nurse.employee_id WHERE Employee.clinic = %s) 
AS "Sum" """
  variables = (clinic, clinic)
  results = execute(query, variables)
  if results:
    result = []
    for data in results:
      no_patient = data["Sum"]
      result.append((no_patient))
    temp = PrettyTable()
    temp.field_names = ["Sum of Doctors and Nurses at Clinic "+clinic]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result
  
def create_notif(appt, content):
  result = None 
  query = """INSERT INTO Notifications(appointment, send_date, content) VALUES
(%s, DATE_SUB(
(SELECT Appointment.date FROM Appointment WHERE Appointment.appointment_id = 1), INTERVAL 1 DAY
), %s),
(%s, DATE_SUB(
(SELECT Appointment.date FROM Appointment WHERE Appointment.appointment_id = 1), INTERVAL 1 WEEK
), %s)"""
  variables = (appt, content, appt, content)
  results = execute(query, variables)
  if results == "Error":
    result = "Error updating database."
  else:
    result = "Database successfully updated!"
  return result

def patient_doctor_appt(patient, doctor):
  result = None 
  query = """SELECT Appointment.date AS "Appointment Date" FROM Appointment JOIN Patient ON Appointment.patient = Patient.patient_id
JOIN Doctor ON Appointment.doctor = Doctor.doctor_id JOIN Employee ON Employee.employee_id = Doctor.employee_id
WHERE Patient.name = %s AND Employee.name = %s"""
  variables = (patient, doctor)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      appointment_date = data["Appointment Date"]
      new_date = appointment_date.strftime("%m/%d/%Y, %H:%M:%S")
      result.append((new_date))
    temp = PrettyTable()
    temp.field_names = ["Appointment Dates"]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def doc_clinic_lang(clinic, language):
  result = None 
  query = """SELECT Employee.name AS "Doctor" FROM Employee JOIN 
Doctor ON Employee.employee_id = Doctor.employee_id JOIN
Clinic ON Employee.clinic = Clinic.clinic_id 
JOIN Doctor_Language ON Doctor.doctor_id = Doctor_Language.doctor JOIN Languages
ON Doctor_Language.language = Languages.language_id WHERE Clinic.clinic_id = %s AND
Languages.name = %s"""
  variables = (clinic, language)
  results = execute(query, variables)
  if results:
    result = []
    for data in results:
      doctor = data["Doctor"]
      result.append((doctor))
    temp = PrettyTable()
    temp.field_names = ["Doctors Who Speak "+language]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def clinic_cancellations(date):
  result = None 
  query = """SELECT Clinic.address AS "Clinic", Count(Appointment.appointment_id) AS "Total Cancellations" FROM Appointment 
JOIN Clinic ON Appointment.location = Clinic.clinic_id WHERE Appointment.cancelled > 0 
AND Date(Appointment.date) >= %s AND Date(Appointment.date) < DATE_ADD(%s, INTERVAL 1 MONTH)
GROUP BY Clinic.address"""
  # get current year, conver to string
  today = datetime.date.today()
  year = today.year
  year_str = str(year)
  # convert month input
  month = str((dt.strptime(date,'%B')).month)
  # get total month from start date
  new_date = year_str+'-'+month+'-'+'01'
  variables = (new_date, new_date)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      clinic = data["Clinic"]
      cancellations = data["Total Cancellations"]
      result.append((clinic, cancellations))
    temp = PrettyTable()
    temp.field_names = ["Clinic Address", "Total Cancels"]
    for data in result:
      temp.add_row(data)
    temp.hrules = 3
    result = temp
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def clinics_insurance_provider(provider):
  result = None 
  query = """SELECT Clinic.address AS "Clinic" FROM Clinic JOIN InsuranceP_Clinic ON Clinic.clinic_id = InsuranceP_Clinic.clinic
JOIN Insurance_Providers ON InsuranceP_Clinic.insurance = Insurance_Providers.provider_id 
WHERE Insurance_Providers.name = %s"""
  variables = (provider)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      clinic = data["Clinic"]
      result.append((clinic))
    temp = PrettyTable()
    temp.field_names = ["Clinics That Accept "+provider]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def patient_fees(patient):
  result = None 
  query = """SELECT SUM(Fees.price) AS "Total Fees" FROM Fees JOIN Appointment_Fee ON Fees.fee_id = Appointment_Fee.Fee 
JOIN Appointment ON Appointment.appointment_id = Appointment_Fee.Appointment JOIN
Patient ON Patient.patient_id = Appointment.patient WHERE Patient.name = %s"""
  variables = (patient)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      fees = data["Total Fees"]
      result.append((fees))
    temp = PrettyTable()
    temp.field_names = ["Total Fees Accrued By "+patient]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def clinic_reviews(clinic):
  result = None 
  query = """SELECT Employee.name AS "Doctor", Reviews.content AS "Review" FROM Reviews JOIN Doctor ON Reviews.doctor = Doctor.doctor_id 
JOIN Employee ON Employee.employee_id = Doctor.employee_id 
JOIN Clinic ON Employee.clinic = Clinic.clinic_id WHERE Clinic.clinic_id = %s"""
  variables = (clinic)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      review = data["Review"]
      doctor = data["Doctor"]
      result.append((doctor, review))
    temp = PrettyTable()
    temp.field_names = ["Doctor","Review"]
    for data in result:
      temp.add_row(data)
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def clinic_schedule(status):
  result = None 
  query = """SELECT Clinic.address AS "Clinic" , Schedule.date AS "Date" FROM Clinic JOIN Schedule ON
Clinic.clinic_id = Schedule.clinic WHERE Schedule.status = %s"""
  variables = (status)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      clinic = data["Clinic"]
      date = data["Date"]
      new_date = date.strftime("%m/%d/%Y, %H:%M")
      result.append((clinic, new_date))
    temp = PrettyTable()
    temp.field_names = ["Clinic Address","Appointment With Status "+status]
    for data in result:
      temp.add_row(data)
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

# format: 2022-06-01
def doct_appt_dates(start, end):
  result = None 
  query = """SELECT COUNT(Appointment.appointment_id) AS "Total", Employee.name AS "Doctor" FROM Appointment JOIN Schedule ON 
Appointment.date = Schedule.date JOIN Doctor ON Appointment.doctor = Doctor.doctor_id JOIN Employee
 ON Employee.employee_id = Doctor.employee_id 
WHERE Schedule.status = "Booked" AND Date(Appointment.date) >= %s AND Date(Appointment.date) <= %s
GROUP BY Employee.name"""
  variables = (start, end)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      doctor = data["Doctor"]
      total = data["Total"]
      result.append((doctor, total))
    temp = PrettyTable()
    temp.field_names = ["Doctor","Number of Booked Appointments"]
    for data in result:
      temp.add_row(data)
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def get_patients_provider(insurance_p):
  result = None 
  query = """SELECT Count(DISTINCT Appointment.patient) AS "Total Patients" FROM Appointment JOIN Clinic ON Appointment.location = 
Clinic.clinic_id JOIN InsuranceP_Clinic ON InsuranceP_Clinic.clinic = Clinic.clinic_id 
WHERE InsuranceP_Clinic.insurance = %s"""
  variables = (insurance_p)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      total = data["Total Patients"]
      result.append((total))
    temp = PrettyTable()
    temp.field_names = ["Total Patients"]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def patient_appointments_time(patient, start, end):
  result = None 
  query = """ SELECT Count(Appointment.appointment_id) AS "Total Cancelled" FROM Appointment WHERE
Appointment.cancelled > 0 
AND DATE(Appointment.date) >= %s AND DATE(Appointment.date) <= %s
AND Appointment.patient = %s """
  variables = (start, end, patient)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      total = data["Total Cancelled"]
      result.append((total))
    temp = PrettyTable()
    temp.field_names = ["Total Appointments Made by patient with id '"+patient+"' between "+start+" and "+end]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def find_doctor_specialty(clinic, specialty):
  result = None 
  query = """SELECT Employee.name AS "Doctor" FROM Employee
JOIN Doctor ON Employee.employee_id = Doctor.employee_id JOIN Clinic 
ON Employee.clinic = Clinic.clinic_id JOIN Doctor_Specialty ON
Doctor.doctor_id = Doctor_Specialty.doctor JOIN Specialties
ON Specialties.specialty_id = Doctor_Specialty.specialty 
WHERE Specialties.type = %s AND
Clinic.clinic_id = %s"""
  variables = (specialty, clinic)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      doctor = data["Doctor"]
      result.append((doctor))
    temp = PrettyTable()
    temp.field_names = ["Doctors With Specialty "+specialty]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def find_reviews(patient, doctor):
  query = """SELECT Reviews.content AS "Review" FROM Reviews JOIN Patient ON Reviews.patient = Patient.patient_id
JOIN Doctor ON Reviews.doctor = Doctor.doctor_id WHERE Doctor.doctor_id = %s AND 
Patient.patient_id = %s"""
  variables = (doctor, patient)
  results = execute(query, variables)
  result = None
  if results:
    result = []
    for data in results:
      review = data["Review"]
      result.append((review))
    temp = PrettyTable()
    temp.field_names = ["Reviews for "+doctor+" made by patient "+patient]
    for data in result:
      temp.add_row([data])
    temp.hrules = 3
    result = temp
    result.align = "c"
    result.junction_char = ' '
    result.border = False
    result.preserve_internal_border = True
  else:
    result = "No results found"
  return result

def most_clinic_services():
  result = None 
  try:
    connection = connect()
    if connection:
      cursor = connection.cursor()
      query = """SELECT 
(SELECT Count(DISTINCT Services.service_id) FROM Services JOIN Doctor_Services ON Services.service_id = Doctor_Services.service
JOIN Doctor ON Doctor_Services.doctor = Doctor.doctor_id JOIN Employee ON Employee.employee_id = Doctor.employee_id
JOIN Clinic ON Clinic.clinic_id = Employee.clinic)
+
(SELECT Count(DISTINCT Services.service_id) FROM Services JOIN Nurse_Services ON Services.service_id = Nurse_Services.service
JOIN Nurse ON Nurse_Services.nurse = Nurse.nurse_id JOIN Employee ON Employee.employee_id = Nurse.employee_id
JOIN Clinic ON Clinic.clinic_id = Employee.clinic) AS "Sum", Clinic.address AS "Clinic"
FROM Clinic ORDER BY "Sum" DESC LIMIT 1"""
      cursor.execute(query)
      results = cursor.fetchall()
      result = []
      if results:
        for data in results:
          appt = data["Sum"]
          clinic = data["Clinic"]
          result.append((clinic, appt))
        temp = PrettyTable()
        temp.field_names = ["Clinic Address","Sum of Services"]
        for data in result:
          temp.add_row(data)
          temp.hrules = 3
        result = temp
        result.align = "c"
        result.junction_char = ' '
        result.border = False
        result.preserve_internal_border = True
  except Exception as error:
    print(error)
    result = -1 
  connection.close()
  return result
