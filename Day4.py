class StudentTeacher:
    def getStudent(self):
        self.eno=input("Enter enrollment number -\n")
        self.name=input("Enter name -\n")
        self.per=input("Enter percentage -\n")

    def putStudent(self):
        print("--------------------------------------")
        print("*** STUDENT DETAILS ***")
        print("--------------------------------------")
        print("Enrollment Number :",self.eno)
        print("Name :",self.name)
        print("Email ID :",self.name + "@gmail.com")
        print("Percentage :",self.per + "%")
        print("--------------------------------------")

    def getTeacher(self):
        self.tno=input("Enter id - \n")
        self.tname =input("Enter name -\n")
        self.sal=input("Enter salary - \n")

    def putTeacher(self):
        print("--------------------------------------")
        print("*** TEACHER DETAILS ***")
        print("--------------------------------------")
        print("Teacher ID  :",self.tno)
        print("Name :",self.tname)
        print("Email ID :",self.tname + "@gmail.com")
        print("Salary :",self.sal)
        print("--------------------------------------")

s=StudentTeacher()
i=1
while(i):
     print("\n*** DETAILS ***")
     print("\n1 = Accept student details \n2 = Display student details \n3 = Accept Teacher Details \n4 = Display teacher details\n5 = Exit ")
     ch=int(input("Enter your choice -"))
     while (ch != 5):
        if(ch == 1):
          s.getStudent()
          break

        elif(ch == 2):
            s.putStudent()
            break

        elif(ch == 3):
            s.getTeacher()
            break

        elif(ch == 4):
            s.putTeacher()
            break

        else:
           print("ThankYou!")
           break

print("Do you want to continue PRESS 1 - ",ch)
pass