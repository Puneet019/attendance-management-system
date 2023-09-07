
# Initialize an empty dictionary to store student records
student_records = {}

# Function to add a student to the system
def add_student():
    roll_no = input("Enter student roll number: ")
    name = input("Enter student name: ")
    marks1 = float(input("Enter student marks for Math: "))
    marks2 = float(input("Enter student marks for Physics: "))
    
    # Store the student information in the dictionary
    student_records[roll_no] = {'name': name, 'marks1': marks1 ,'marks2':marks2}
    print(f"Student with roll number {roll_no} added successfully!")

# Function to display all students
def display_students():
    print("\nStudent Records:")
    for roll_no, student_info in student_records.items():
        print(f"Roll Number: {roll_no}")
        print(f"Name: {student_info['name']}")
        print(f"Marks1: {student_info['marks1']}")
        print(f"Marks2: {student_info['marks2']}")
        print('-' * 20)

# Function to search for a student by roll number
def search_student():
    roll_no = input("Enter student roll number to search: ")
    if roll_no in student_records:
        student_info = student_records[roll_no]
        print(f"Student Found:")
        print(f"Roll Number: {roll_no}")
        print(f"Name: {student_info['name']}")
        print(f"Marks1: {student_info['marks1']}")
        print(f"Marks2: {student_info['marks2']}")
    else:
        print(f"Student with roll number {roll_no} not found!")

# Function to delete a student by roll number
def delete_student():
    roll_no = input("Enter student roll number to delete: ")
    if roll_no in student_records:
        del student_records[roll_no]
        print(f"Student with roll number {roll_no} deleted successfully!")
    else:
        print(f"Student with roll number {roll_no} not found!")

# Main program loop
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
Student Management System
1. Add Student
2. Display Students
3. Search Student
4. Delete Student
5. Exit
Enter your choice: 1
Enter student roll number: 31
Enter student name: Puneet
Enter student marks for Math: 70
Enter student marks for Physics: 96
Student with roll number 35 added successfully!

Student Management System
1. Add Student
2. Display Students
3. Search Student
4. Delete Student
5. Exit
Enter your choice: 2

Student Records:
Roll Number: 31
Name: Puneet
Marks1: 70.0
Marks2: 96.0
--------------------

Student Management System
1. Add Student
2. Display Students
3. Search Student
4. Delete Student
5. Exit
Enter your choice: 5
 
