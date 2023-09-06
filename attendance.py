from datetime import datetime, timedelta

user_data = [{'userid':"pm", 'password':"1234"}]
student_data = {}

def register(userid, password):
  if not any(user['userid']== userid for user in user_data):
    user_data.append({'userid':userid, 'password':password})
    print("User added successfully")
  else:
    print("Userid already exists....try using another user name")

def user_login(userid, password):
  if any(user['userid']==userid and user['password']==password for user in user_data):
    print("login success.....")
    return True
  else:
    print("Oops..... you have entered wrong userid and password")
    return False

def add_student(rollno, name, email):
  if rollno not in student_data:
    student_data[rollno]={
        'name':name,
        'email':email
    }
    print("Student added sucessfully")
  else:
    print("Student id already exists")

def delete_student(rollno):
  if rollno in student_data:
    del student_data[rollno]
    print("record deleted sucessfully")
  else:
    print("Student does not exists")

def update_student(rollno, name, email):
  if rollno in student_data:
    student_data[rollno]={
        'name':name,
        'email':email
    }
    print("user updated successfully")
  else:
    print("Student does not exists")

def view_student(rollno):
  if rollno in student_data:
    info = student_data[rollno]
    for key, value in info.items():
      print({key},":",{value})
  else:
    print(f"record for {rollno} does not exists")

def view_allstudent():
  for key, value in student_data.items():
      print(f"{key} : {value}")

def markattendence(rollno):
  today = datetime.today().date()
  if rollno in student_data:
    if 'attendence' not in student_data[rollno]:
      student_data[rollno]['attendence']={}

    attendence_data = student_data[rollno]['attendence']

    if today in attendence_data:
      print(f"Attendence of {rollno} for the date - {today} has been marked as {attendence_data}")
    else:
      attendence = input(f"mark attendnece for rollno {rollno} P -> Present and A -> Absent:- ").upper()
      if attendence in ['P',"A"]:
        attendence_data[today] = attendence
        print(f"Attendence of {rollno} for the date - {today} has been marked as {attendence}")
      else:
        print("please choose btw P and A ")
  else:
    print(f"Student with {rollno} does not exists")

def viewattendence(rollno):
  if rollno in student_data and 'attendence' in student_data[rollno]:
    attendence = student_data[rollno]['attendence']
    for key, value in attendence.items():
      print(f"{key} : {value}")
  else:
    print(f"No record with rollno {rollno} is present")



def viewpastweekattendance(rollno, past_weeks=1, student_data={}):
    if rollno in student_data and 'attendance' in student_data[rollno]:
        attendance = student_data[rollno]['attendance']
        today = datetime.today().date()

        for week in range(past_weeks):
            start_date = today - timedelta(days=(today.weekday() + 7 * week))
            end_date = start_date + timedelta(days=6)
            print(f"Attendance for week {week + 1} ({start_date.strptime('%Y-%m-%d')} to {end_date.strptime('%Y-%m-%d')}):")
            for date_str, status in attendance.items():
                date_obj = datetime.strptime(date_str, '%d-%m-%y').date()
                if start_date <= date_obj <= end_date:
                    print(f"{date_str}: {status}")
    else:
        print(f"No record with rollno {rollno} is present")





def main():
  login = False
  while(login == False):
    print("Welcome to my Company -> Attendence management system")
    print("1-> Login")
    print("2-> exit")
    ch=int(input("Choose your Option:- "))

    if ch==1:
      name = input("enter your userid:- ")
      password = input("Enter your password:- ")
      login = user_login(name, password)
      while(login == True):
        print("Select your task - ")
        print("1 -> Add new user")
        print("2 -> Add new Student")
        print("3 -> Delete existing student")
        print("4 -> update student")
        print("5 -> view student")
        print("6 -> Mark attendence")
        print("7 -> View attendence")
        print("8 -> Logout")
        x = int(input("enter your choice:- "))

        if(x==1):
          userid=int(input("enter userid (numeric only):- "))
          password=input("enter your password")
          register(userid, password)
        elif(x==2):
          rollno = int(input("enter rollno:- "))
          name = input("enter name:- ")
          email = input("enter email:- ")
          add_student(rollno, name, email)
        elif(x==3):
          rollno=int(input("enter roll no:- "))
          delete_student(rollno)
        elif(x==4):
          rollno=int(input("enter rollno"))
          name = input("enter name:- ")
          email = input("enter email:- ")
          update_student(rollno, name, email)
        elif(x==5):
          print("1 -> specific data")
          print("2 -> all data")
          y=int(input("enter your choice:- "))
          if(y==1):
            rollno=int(input("enter rollno:- "))
            view_student(rollno)
          else:
            view_allstudent()
        elif(x==6):
          rollno=int(input("enter roll no:- "))
          markattendence(rollno)
        elif(x==7):
            print("select method for viewing attendence\n1 -> today's for specific rollno\n2 -> For past few days")
            x = int(input("select an option:- "))
            if x==1:
                rollno=int(input("enter roll no:- "))
                viewattendence(rollno)
            elif x==2:
                rollno = int(input("enter rollno :- "))
                viewpastweekattendence(rollno)
            else:
                print("choose correct option ")
        elif(x==8):
          login = False
        else:
          print("choose the correct option")
    elif ch==2:
      print("Thanks for using........")
      break
    else:
      print("choose from the below options")




main()
