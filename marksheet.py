print('''
========================================================================================
Please Provide the Asked Information and Data to Generate your Automatic E-Marksheet.
========================================================================================\n\n\n
''')

#Data Required To Generate Marksheet
student_name = str(input("Student Name: "))
father_name = str(input("Father's Name: "))
gender = str(input("Gender: "))
date_of_birth = str(input("Date of Birth (DD/MM/YYYY): "))
clas = int(input("Class (in numbers): "))
school_name = str(input("School Name: "))
school_address = str(input("School Address: "))
print('''\n\n\n
^^^^^^^^^^^^^^^^^^^^^^^^
Please Provide Marks*
------------------------
''')

#Checking the class
sub1 = int(input("English: "))
sub2 = int(input("Urdu: "))
sub3 = int(input("Islamiat: "))
sub4 = int(input("Computer: "))
sub5 = int(input("Physics: "))
sub6 = int(input("Mathematics: "))

#Calculations
total_marks_obtained = (sub1+sub2+sub3+sub4+sub5+sub6)
percentage = float((total_marks_obtained/500)*100)
if percentage <= 100.0:
    grade = 'A+'
elif percentage < 80.0:
    grade = 'A'
elif percentage < 70.0:
    grade = 'B'
elif percentage < 60.0:
    grade = 'C'
elif percentage < 50.0:
    grade = 'D'
elif percentage < 33.0:
    grade = 'F'

t = total_marks_obtained
#Marksheet Generating
print('''
*****************************************************************************************
                                        Marksheet
*****************************************************************************************
\n\n\n\n
Student Name: '''+str(student_name)+'''
Father's Name: '''+str(father_name)+'''
Class: '''+str(clas)+'''
Gender: '''+str(gender)+'''
Date of Birth: '''+str(date_of_birth)+'''
School Name: '''+str(school_name)+'''
School Address: '''+str(school_address)+'''

-----------------------------------------------------------------------------------------
    |   Subject     |   Obtained Marks   |  Marks  |   Total Marks |
    |---------------|--------------------|---------|---------------|
    |English        |\t\t'''+str(sub1)+'''\t |  100    |    -          |
    |               |                    |         |               |
    |Urdu           |\t\t'''+str(sub2)+'''\t |  100    |    -          |
    |               |                    |         |               |
    |Islamiat       |\t\t'''+str(sub3)+'''\t |  50     |    -          |
    |               |                    |         |               |
    |Computer       |\t\t'''+str(sub4)+'''\t |  75     |    -          |
    |               |                    |         |               |
    |Physics        |\t\t'''+str(sub5)+'''\t |  75     |    -          |
    |               |                    |         |               |
    |Mathematics    |\t\t'''+str(sub6)+'''\t |  100    |    -          |
    |---------------|--------------------|---------|---------------|
    |               |                    |         |               |
    |Total Marks    |                    |         |\t'''+str(t)+'''\t   |
    |_______________|____________________|_________|_______________|


    Percentage: '''+str(percentage)+'''
    Grade: '''+str(grade)+'''


    _________                                                           _________
    Signature                                                           Signature

''')