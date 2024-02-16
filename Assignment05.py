# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Abdullah Jawhar>,<02/15/2024>, <Assignment05>
# ------------------------------------------------------------------------------------------ #
#Import json library
import json
from json import JSONDecodeError
from typing import TextIO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
file: TextIO
parts: list[str]

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print('Text file not found')
    print('--- Technical Information ---')
    print(e,e.__doc__,type(e),sep='\n')
    print('Creating file since it does not exist')
    file = open(FILE_NAME,"w")
    json.dump(students, file)
except JSONDecodeError as e:
    print('--- Technical Information ---')
    print(e,e.__doc__,type(e),sep='\n')
    print('Data in file is not valid. Resetting it...')
    file = open(FILE_NAME, "w")
    json.dump(students, file)
except Exception as e:
    print('Unhandled exception')
    print('--- Technical Information ---')
    print(e,e.__doc__,type(e),sep='\n')
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('The first name must be alphabetic')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('The last name must be alphabetic')
            course_name = input("Please enter the name of the course: ")
            student_data = {'first_name':student_first_name,'last_name':student_last_name,'course_name':course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue
        except ValueError as e:
            print(e)
            print('--- Technical Information ---')
            print(e, e.__doc__, type(e), sep='\n')

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        for student_data in students:
            student_first_name = student_data['first_name']
            student_last_name = student_data['last_name']
            course_name = student_data['course_name']
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student_data in students:
                print(f"Student {student_data['first_name']} {student_data['last_name']} is enrolled in {student_data['course_name']}")
            continue
        except TypeError as e:
            print('JSON data was malformed')
            print('--- Technical Information ---')
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print('--- Technical Information ---')
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
