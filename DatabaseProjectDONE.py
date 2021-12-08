
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 17:14:15 2021

@author: jamesmcsweeney
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3;
import pandas as pd;
import numpy as np;

conn = sqlite3.connect('examples18.db')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()





# =============================================================================
Student=("""CREATE TABLE Student( 
           StudentID int UNIQUE NOT NULL, 
           Name varchar(255), 
           initials varchar(255), 
           Primary Key(StudentID) 
         ); """)
#=============================================================================     
Major=("""CREATE TABLE Major( 
             MajorCode int CHECK (length(MajorCode) == 3),
             Major varchar(255) NOT NULL, 
             DepartmentName varchar(255) Check (departmentName LIKE 'department%'),
             Primary Key(Major),
             Foreign Key(DepartmentName) REFERENCES Department(DepartmentName)
                    );  """)
#=============================================================================
Department=("""CREATE TABLE Department( 
     DepartmentName varchar(255) NOT NULL Check (departmentName LIKE 'department%'), 
     chairName varchar(255), 
     NumofFacualty int, 
     Primary Key(DepartmentName) 
     ); """)
#=============================================================================
Event=("""CREATE TABLE Event( 
            EventID int UNIQUE NOT NULL, 
             EventName varchar(255), 
             StartDate DATETIME check (startDate <= EndDate), 
             EndDate DATETIME, 
             Primary Key(EventID) 
                 ); """)
#=============================================================================
Enrollment=("""CREATE TABLE Enrollment( 
             StudentID int UNIQUE NOT NULL, 
             Major varchar(255) UNIQUE NOT NULL, 
             PRIMARY KEY (StudentID, Major), 
             FOREIGN KEY (StudentID) REFERENCES Student(StudentID), 
             FOREIGN KEY (Major) REFERENCES Major(Major) 
                 ); """)
#=============================================================================
EventAttendence=("""CREATE TABLE EventAttendence( 
             StudentID int UNIQUE NOT NULL, 
             EventID int UNIQUE NOT NULL, 
             AttendedEvent int check(AttendedEvent==0 |AttendedEvent==1), 
             PRIMARY KEY (StudentID, EventID), 
             FOREIGN KEY (StudentID) REFERENCES Student(StudentID), 
             FOREIGN KEY (EventID) REFERENCES Event(EventID) 
            ); """)
#=============================================================================
EventHost=("""CREATE TABLE EventHost( 
         EventID int UNIQUE NOT NULL, 
         DepartmentName varchar(255) UNIQUE NOT NULL Check (departmentName LIKE 'department%'), 
        PRIMARY KEY (DepartmentName, EventID), 
         FOREIGN KEY (DepartmentName) REFERENCES Department(DepartmentName), 
         FOREIGN KEY (EventID) REFERENCES Event(EventID) 
             ); """)
#=============================================================================

# =============================================================================
cursor.execute(Student)
cursor.execute(Department)
cursor.execute(Event)
cursor.execute(Major)
cursor.execute(Enrollment)
cursor.execute(EventAttendence)
cursor.execute(EventHost)
# =============================================================================

studentRows=[]
cursor.execute("INSERT INTO Student VALUES (111001,'jake t swarm', 'jts')")
cursor.execute("INSERT INTO Student VALUES (111003,'john H water', 'jhw')")
cursor.execute("INSERT INTO Student VALUES (111002, 'Daniel B buter' ,'dbb')")
cursor.execute("INSERT INTO Student VALUES (110004,'Matt S socks', 'mss')")
cursor.execute("INSERT INTO Student VALUES (110005,'Rafeal T Turtle','rtt')")

print("\nStudent Table")
for row in cursor.execute('SELECT * FROM Student'):
      studentRows.append(row)

studentnum = np.array(studentRows)
print(pd.DataFrame(studentnum, columns=['StudentID','Name','initials']))


# =============================================================================
DepartmentRows=[]
cursor.execute("INSERT INTO Department VALUES ('department of math', 'John Luck', 23)")
cursor.execute("INSERT INTO Department VALUES ('department of CS', 'matthew bone',12)")
cursor.execute("INSERT INTO Department VALUES ('department of Biology', 'zach space',30)")
cursor.execute("INSERT INTO Department VALUES ('department of English', 'roger roger',44)")
cursor.execute("INSERT INTO Department VALUES ('department of French', 'Jake McSweeney',8)")

print("\nDepartment Table")
for row in cursor.execute('SELECT * FROM Department'):
      DepartmentRows.append(row)

Departmentnum = np.array(DepartmentRows)
print(pd.DataFrame(Departmentnum, columns=['DepartmentName','Chair Name','NumofFacualty']))
# =============================================================================



# =============================================================================
MajorRows=[]
cursor.execute("INSERT INTO Major VALUES (100,'Math','department of math')")
cursor.execute("INSERT INTO Major VALUES (200,'Computer science','department of CS')")
cursor.execute("INSERT INTO Major VALUES (300,'Biology','department of Biology') ")
cursor.execute("INSERT INTO Major VALUES (400,'English','department of English')")
cursor.execute("INSERT INTO Major VALUES (500,'French','department of French') ")

print("\nMajor Table")
for row in cursor.execute('SELECT * FROM Major'):
      MajorRows.append(row)

Majornum = np.array(MajorRows)
print(pd.DataFrame(Majornum, columns=['MajorCode','Major','DepartmentName']))
# =============================================================================


EventRow=[]
# =============================================================================
cursor.execute("INSERT INTO Event VALUES (1,'math Day', '2020-01-01 12:00:00', '2020-01-01 14:00:00')")
cursor.execute("INSERT INTO Event VALUES (2, 'CS Day', '2020-01-01 12:00:00', '2020-01-01 14:00:00')")
cursor.execute("INSERT INTO Event VALUES (3,'Biology Day', '2020-01-01 12:00:00', '2020-01-01 14:00:00') ")
cursor.execute("INSERT INTO Event VALUES (4,'English Day', '2020-01-01 12:00:00', '2020-01-01 14:00:00')")
cursor.execute("INSERT INTO Event VALUES (5,'French Day', '2020-01-01 12:00:00', '2020-01-01 14:00:00') ")

print("\nEvent Table")
for row in cursor.execute('SELECT * FROM Event'):
      EventRow.append(row)

Eventnum = np.array(EventRow)
print(pd.DataFrame(Eventnum, columns=['EventID','Event Name','Start Date','End Date']))
# =============================================================================

eaRow=[]
cursor.execute("INSERT INTO EventAttendence VALUES (111001,4,0)")
cursor.execute("INSERT INTO EventAttendence VALUES (111003,2,0)")
cursor.execute("INSERT INTO EventAttendence VALUES (111004,5,0) ")
cursor.execute("INSERT INTO EventAttendence VALUES (111005,3,0)")
cursor.execute("INSERT INTO EventAttendence VALUES (111002,1,0) ")

print("\nEventAttendence Table")
for row in cursor.execute('SELECT * FROM EventAttendence'):
       eaRow.append(row)

eanum = np.array(eaRow)
print(pd.DataFrame(eanum, columns=['StudentID','EventID','Attended Event']))

# =============================================================================

EnRow=[]
cursor.execute("INSERT INTO Enrollment VALUES (111001,'Math')")
cursor.execute("INSERT INTO Enrollment VALUES (111003,'Computer science')")
cursor.execute("INSERT INTO Enrollment VALUES (111004,'Biology') ")
cursor.execute("INSERT INTO Enrollment VALUES (111005,'English')")
cursor.execute("INSERT INTO Enrollment VALUES (111002,'French') ")

print("\nEnrollment Table")
for row in cursor.execute('SELECT * FROM Enrollment'):
       EnRow.append(row)

ennum = np.array(EnRow)
print(pd.DataFrame(ennum, columns=['StudentID','Major']))

# =============================================================================

evRow=[]
cursor.execute("INSERT INTO EventHost VALUES (1,'department of math')")
cursor.execute("INSERT INTO EventHost VALUES (2,'department of CS')")
cursor.execute("INSERT INTO EventHost VALUES (3,'department of Biology') ")
cursor.execute("INSERT INTO EventHost VALUES (4,'department of English')")
cursor.execute("INSERT INTO EventHost VALUES (5,'department of French') ")

print("\nEventHost Table")
for row in cursor.execute('SELECT * FROM EventHost'):
       evRow.append(row)

evnum = np.array(evRow)
print(pd.DataFrame(evnum, columns=['EventID','Department Name']))
# =============================================================================

print("\nGet details of the Event that the Computer Science Department is doing.")
for row in cursor.execute('SELECT Event.EventName,Event.StartDate,Event.EndDate FROM Event INNER JOIN EventHost WHERE Event.EventID=EventHost.EventID AND EventHost.DepartmentName=("department of CS")'):
       print(row)
print("\nHow many majors are at the university?")
for row in cursor.execute('SELECT count(MajorCode) FROM Major'):
       print(row)
print("\nwhat department is the Math Major in?")
for row in cursor.execute('SELECT DepartmentName FROM Major WHERE Major="Math"'):
       print(row)    
print("\nwhat are the names of the Events that take place during 2020?")
for row in cursor.execute('SELECT EventName FROM Event WHERE StartDate LIKE "2020%"'):
       print(row)  
print("\ntotal number of employees working at the school? ")   
for row in cursor.execute('SELECT SUM(NumofFacualty)+Count(chairName) FROM Department'):
    print(row)


conn.commit()
conn.close()