print('''
Welcome To The Student Management System
''')
students = []
#MAKING DICTIONARY USING FUNCTIONS
#def add_students() WORKING
def add_student():
    student = {}
    student['Name'] =  input("Name:\t\t")
    student['Father Name'] = input("Father Name:\t")
    student['Age'] = input("Age:\t\t")
    student['Address'] = input("Address:\t")
    student['Contact'] = input("Contact:\t")        
    students.append(student)
    print("Student Has Been Added Successfully.")

# def edit_student()
def edit_student(std_ID):
    for x in range(len(students)):
        if std_ID == x:
            print(students[std_ID])
            students[x]['Name'] =  input("Name:\t\t")
            students[x]['Father Name'] = input("Father Name:\t")
            students[x]['Age'] = input("Age:\t\t")
            students[x]['Address'] = input("Address:\t")
            students[x]['Contact'] = input("Contact:\t")
            print("\n\nStudent Has Been Edited Successfully.")
            break
        else:
            print("Student Does Not Exists.")
            
#def delt_student() WORKING
def delt_student(std_ID):
    for ind in students:
        if ind in students:
            del students[std_ID]
            print("Student Has Been Deleted Successfully.")
            break
        else:
            print("Sorry, ID does not exists.")
    
#def show_all _students() WORKING
def show_all_student():
    for x in range(len(students)):
        print('ID:\t',x,'\n===========')
        print(students[x])

#def search_student() WORKING
def search_student(std_ID):
    for x in range(len(students)):
        if std_ID == x:
            print(students[std_ID])
            break
        else:
            print("Student Does Not Exists.")
while True:
    print('''
    Press 1 to Add Student
    Press 2 to Edit Student
    Press 3 to Delete Student
    Press 4 to Show All Students
    Press 5 to Search Student
    Press 6 to Exit the Program
    ''')

    opt = int(input("Choose an option:\t"))
    if opt == 1:
        add_student()
    elif opt == 2:
        std_ID = int(input("Enter ID"))
        edit_student(std_ID)
    elif opt == 3:
        std_ID = int(input("Enter ID:\t"))
        delt_student(std_ID)
    elif opt == 4:
        show_all_student()
    elif opt == 5:
        std_ID = int(input("Enter ID:\t"))
        search_student(std_ID)
    elif opt == 6:
        print("Good Bye.")
        break
    else:
        print("You Chose The Wrong Menu, the program is exiting.")
        break



    