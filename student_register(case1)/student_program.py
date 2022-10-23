temp ={"name" : "","surname" : "" , "number":""}
students = []
command = input("choose an action (add,delete,show):")
if command == "add":
    name = input("type student's name:")
    surname = input("type student's surname:")
    number = input("type student's number:")
    temp["name"] = name
    temp["surname"] = surname
    temp["number"] = number
    students.append(temp)
    print(students)
    #elif command == "clear":
     #   number = input("type student's number:")
    #    temp["name"] = name
    #    temp["surname"] = surname
     #   temp["number"] = number
        # print(temp)
     #   student.append(temp)











