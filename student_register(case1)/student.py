student_list = open("student_list.txt","r+")
student_listt = student_list.readlines()
def student_add():
    name=input("type student's name:")
    surname = input("type student's surname:")
    number = input("type student's number:")
    student = (name+" "+surname+" "+number+"\n")
    student_listt.append(student)
    with open("student_list.txt" , "a" , encoding="utf-8") as file:
        file.writelines(student+"\n")
    print("Student is added")

def student_show():
    with open("student_list.txt" , "r" , encoding="utf-8") as file:
        for i in file:
            print(i)
def student_delete():
    name = input("type student's name:")
    surname = input("type student's surname:")
    number = input("type student's number:")
    student = (name+" "+surname+" "+number+"\n")
    if student_listt.count(student) == 0:
         print("Student info doesn't exist")
    else:
      print("Student is deleted")
      student_listt.remove(student)
    student_backup = student_listt
    with open("student_list.txt", "w+", encoding="utf-8") as file:
      file.close
    with open("student_list.txt", "w+", encoding="utf-8") as file:
      file.writelines(student_backup)
while True :
    command = input("choose an action (add,delete,show,stop):")

    if command == "add":
      student_add()
    elif command =="show":
        student_show()
    elif command=="delete":
        student_delete()
    elif command=="stop":
        break
        print("Program has been stopped")
    else:
        print("You tried to execute an undefined process")
