print('''
===========================================================================
||                          Enter Credentials                            ||
===========================================================================
\n
Note: Username and Password is case sensitive.
''')

username = str(input("Please Enter Username:\t"))
password = str(input("Please Enter Password:\t"))

if username == "admin" and password == "admin123":
    print("\n\nWelcome to the system. Please Continue with your operations.")
else:
    print("\n\nSorry for the inconveninve. Username or Password is incorrect.")
