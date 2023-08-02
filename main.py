import datetime

class AttendanceManagementSystem:
    def __init__(self):
           
        self.users = {}
        self.students = {}
        self.attendance = {}

    def login(self):
        while True:
            username = input("Username: ")
            password = input("Password: ")
            if username in self.users and self.users[username] == password:
                print("Login successful.")
                break
            else:
                print("Invalid Details. Please try again.")
    
# -----  add the Student ----
    def add_student(self, student_id, student_name):
        self.students[student_id] = student_name

#----- Mark the Attendence ------
    def mark_attendance(self, date, student_id, is_present):
        if date not in self.attendance:
            self.attendance[date] = {}
        self.attendance[date][student_id] = is_present

#---- view the Student Attendence -------
    def view_student_attendance(self, student_id):
        print(f"Attendance for student {self.students.get(student_id, 'N/A')}:")
        for date, is_present in self.attendance.items():
            if student_id in is_present:
                print(f"{date}: {'Present' if is_present[student_id] else 'Absent'}")

#----  Generate Attendance Report ------
    def generate_report(self, report_type, start_date=None, end_date=None):
        if report_type not in ["daily", "weekly", "monthly"]:
            print("Invalid report type. Available options: daily, weekly, monthly")
            return

        if start_date is None:
            start_date = min(self.attendance.keys())
        if end_date is None:
            end_date = datetime.date.today()

        current_date = start_date
        while current_date <= end_date:
            if current_date in self.attendance:
                present_count = sum(1 for is_present in self.attendance[current_date].values() if is_present)
                total_count = len(self.attendance[current_date])
                print(f"{current_date} - {present_count}/{total_count} students present")

            if report_type == "daily":
                break

            if report_type == "weekly":
                current_date += datetime.timedelta(days=7)
            elif report_type == "monthly":
                next_month = current_date.month % 12 + 1
                next_year = current_date.year + 1 if next_month == 1 else current_date.year
                current_date = current_date.replace(year=next_year, month=next_month, day=1)


def main():
    attendance_system = AttendanceManagementSystem()

    # Check if there are no users, then get desired username and password
    if not attendance_system.users:
        new_username = input("Enter desired username: ")
        new_password = input("Enter desired password: ")
        attendance_system.users[new_username] = new_password
        print("Admin account created successfully.")

    attendance_system.login()

    while True:
        print("\nAttendance Management System Menu:")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Student Attendance")
        print("4. Generate Attendance Report")
        print("5. Exit")

        choice = int(input("Enter your choice (1 to 5): "))

        if choice == 1:
            student_id = input("Enter the student ID: ")
            student_name = input("Enter the student name: ")
            attendance_system.add_student(student_id, student_name)
            print(f"Student '{student_name}' with ID '{student_id}' added successfully.")

        elif choice == 2:
            date_str = input("Enter the date (YYYY-MM-DD) for attendance marking: ")
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            student_id = input("Enter the student ID: ")
            is_present = input("Is the student present? (yes/no): ").lower() == 'yes'
            print("attendance marked successfully")
            attendance_system.mark_attendance(date, student_id, is_present)

        elif choice == 3:
            student_id = input("Enter the student ID: ")
            attendance_system.view_student_attendance(student_id)

        elif choice == 4:
            report_type = input("Enter the report type (daily/weekly/monthly): ").lower()
            start_date_str = input("Enter the start date (YYYY-MM-DD): ")
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date_str = input("Enter the end date (YYYY-MM-DD): ")
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
            attendance_system.generate_report(report_type, start_date, end_date)

        elif choice == 5:
            print("Exiting from Attendance Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
