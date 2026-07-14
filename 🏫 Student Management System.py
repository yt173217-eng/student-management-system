#============================
#🏫 Student Management System
#=============================

class Student:
    def __init__(self,id,name,group,age,grade):
        self.ID = id
        self.Name = name
        self.Group = group
        self.Age = age
        self.Grade = grade


    def showdetails(self):
        print(f"ID =",self.ID)
        print(f"Name =",self.Name)
        print(f"Group =",self.Group)
        print(f"Age =",self.Age)
        print(f"Grade =",self.Grade)
    


class Mangment:
    def __init__(self):
        self.students = []
#=================================================================================================

    def addstudent(self,student):
        self.students.append(student)
#=================================================================================================

    def search_student(self):
        
        for student in self.students:
            student_id = int(input("Enter student ID: "))
            if student_id:
                student.showdetails()
                break
            else:
                print("Student not found")
#=================================================================================================
        
    def show_one_student(self):
        student_id = int(input("Enter Search student for id: "))
        for student in self.students:
            if student_id == student.ID:
                print(f"Student Found it: {[student_id]}")
                student.showdetails()
                break
            else:
                print(f"Student with this id {[student_id]} not foud")


#=================================================================================================
   
    def delete_student(self):
        student_id = int(input("Enter student ID: "))
        found = False
        for student in self.students:
            if student_id == student.ID:
                self.students.remove(student)
                print(f"Student with this ID {student_id}.. delete")
                found = True
        if not found:
            print("Student not found")
        
#=================================================================================================

    def update_student(self):
        student_id =  int(input("Enter student id: "))
        for student in self.students:
            if student_id == student.ID:
                print()
                [student.showdetails()]
                while True:
                    print("1. Name")
                    print("2. Group")
                    print("3. Age")
                    print("4. Grade")
                    print("5. New Details")
                    print("6. Exit")

                    choise = input("What do you change: ")
                    
                    if choise == "1":
                        new_name = input("Enter new name ")
                        student.Name = new_name 
                        print(f"Student with new {student.Name}")
                        print()
                        student.showdetails()

                    
                    elif choise == "2":
                        change_group = input("Enter new group name: ")
                        student.Group = change_group                        
                        print(f"✅ Name updated successfully! {student.Group}.") 
                        student.showdetails()
                
                    elif choise == "3":
                        change_age = int(input("Change your age: "))
                        student.Age = change_age
                        print(f"✅ Student age update successfully! {student.Age}. ")
                        student.showdetails()
                
                    elif choise == "4":
                        update_grade = input("Updata student grade: ")
                        student.Grade = update_grade
                        print(f"✅Student with there new grade {student.Grade}.")
                    elif choise == "5":
                        print("✅ New Details.")
                        student.showdetails()
                    elif choise == "6":
                        print("Goodbye")
                        break
                    else:
                        print(f"Invalid systnx.") 
#=================================================================================================
 
    def total_student(self):
        
        total = len(self.students)
        print(f"📊 Total students = {total}.")
        return total

#=================================================================================================

    def show_all_student(self):
        for student in self.students:
            [student.showdetails()]
            print()
#=================================================================================================

    def check_student_exist(self):
        student_name = input('Enter search name: ').strip()
        found = False
        for student in self.students:# check all list 
            if student_name in student.Name:
                print(student_name,"Student Found ✅")
                found = True
                break

        if not found:
                print(student_name,"Student Not Found ❌")
                 
#=================================================================================================

    def clear_all_student(self):
        clear_student = input("Are you sure? (Y/N) ")
        if clear_student == "Y".lower():
            self.students.clear()
            print(f"Clear all students.✅")
            return clear_student        
        else:
            print(f"Return.❌")

#=======================================================================================
   
    def search_name(self):
        student_name = input("Enter student name: ").strip()
        found = False
        for student in self.students:
            if student_name in student.Name:
                print([student_name],f"Student found it ")
                student.showdetails()
                found = True
                break
        if not found:
            print([student_name],f"Student not found it..")
#===================================================================================================  
    def search_by_grade(self):
        grade_student = input("Enter search Grade: ").strip()
        found = False
        
        for student in self.students:
            if grade_student == student.Grade:
                print(f"Student find it with this {grade_student}.")
                student.showdetails()
                found = True
                break

        if not found:
            print(f"Student  not find out with this {grade_student}..")
#=================================================================================================
    def highist_grade(self):
        
        #define grade rankking 
        grade_rank = {"A+":5, "A":4 , "B+":3,"B":2,"C+":1,"C":0}

        Top_Grade_Student = ""
        top_grade_value = -1
        for student in self.students:
            
            if grade_rank[student.Grade] > top_grade_value:
                top_grade_value = grade_rank[student.Grade]
                Top_Grade_Student = student.Name
            
        print(f"Top Grade Student: {Top_Grade_Student} with {top_grade_value}")

#=================================================================================================   
    
    def youngest_age(self):
      youngest = self.students[0]#"Take the first student object as my starting answer."
      for student in self.students:
          if student.Age < youngest.Age:
              youngest = student      
              print([youngest.Name,youngest.Age])
      print()
      youngest.showdetails()
#================================================================================================          
    
    def oldest_student(self):
        oldeststudent = self.students[0]
        
        for student in self.students:
            if student.Age > oldeststudent.Age:
                oldeststudent = student
                print(oldeststudent,f"Oldest Student with {oldeststudent}.")
        oldeststudent.showdetails()          
#============================================================================================
    
    def menu(self):
        while True:
            print("===== Student Management System =====")    
            print("1. Add Student")
            print("2. Show All Students")
            print("3. Search Student (ID)")
            print("4. Search Student (Name)")
            print("5. Update Student")
            print("6. Delete Student")
            print("7. Total Students")
            print("8. Highest Grade Student")
            print("9. Youngest Student")
            print("10. Oldest Student")
            print("11. Total Student")
            print("12. Search One Student")
            print("13. Exit")
            
            choise = input("Enter your chosie: ")
            print()
            if choise == "1":
                self.addstudent()
            elif choise== "2":
                self.show_all_student()
            elif choise =="3":
                self.search_student()    
            elif choise == "4":
                self.search_name()
            elif choise == "5":
                self.update_student()
            elif choise == "6":
                self.delete_student()
            elif choise == "7":
                self.total_student()
            elif choise == "8":
                self.highist_grade()
            elif choise == "9":
                self.youngest_age()
            elif choise == "10":
                self.oldest_student()
            elif choise == "11":
                self.total_student()
            elif choise == "12":
                self.show_one_student()
               
            elif choise == "13":
                print("GoodBye")

                break
            else:
                print("Invailed systnx.")

#=================================================================================================
#=================================================================================================
#=================================================================================================
#=================================================================================================
#=================================================================================================
#=================================================================================================



#Object Class students  20 students with different details
student1  = Student(7868, "Rehan Khan", "Science", 18, "A+")
student2  = Student(1011, "Sara Ali", "Arts", 21, "A")
student3  = Student(2022, "Ahmed Raza", "Math", 19, "B+")
student4  = Student(3033, "Fatima Noor", "Biology", 20, "A")
student5  = Student(4044, "Usman Tariq", "Computer Science", 22, "A+")
student6  = Student(5055, "Ayesha Malik", "Physics", 18, "B")
student7  = Student(6066, "Bilal Hussain", "Chemistry", 19, "A")
student8  = Student(7077, "Zara Sheikh", "English", 21, "A+")
student9  = Student(8088, "Hamza Khan", "History", 20, "B+")
student10 = Student(9099, "Maryam Akhtar", "Economics", 22, "A")
student11 = Student(1111, "Ali Haider", "Science", 18, "A")
student12 = Student(1212, "Sana Javed", "Arts", 14, "B")
student13 = Student(1313, "Imran Qureshi", "Math", 20, "A+")
student14 = Student(1414, "Nida Yasir", "Biology", 21, "C")
student15 = Student(1515, "Omar Farooq", "Computer Science", 22, "B+")
student16 = Student(1616, "Hina Khan", "Physics", 18, "A")
student17 = Student(1717, "Kashif Ali", "Chemistry", 19, "A+")
student18 = Student(1818, "Rabia Shah", "English", 20, "C+")
student19 = Student(1919, "Saad Ahmed", "History", 9, "A")
student20 = Student(2020, "Mehwish Aslam", "Economics", 22, "C")

mangment = Mangment()
#============================================================================
#add student
mangment.addstudent(student1)
mangment.addstudent(student2)
mangment.addstudent(student3)
mangment.addstudent(student4)
mangment.addstudent(student5)
mangment.addstudent(student6)
mangment.addstudent(student7)
mangment.addstudent(student8)
mangment.addstudent(student9)
mangment.addstudent(student10)
#=============================================================================
mangment.addstudent(student11)
mangment.addstudent(student12)
mangment.addstudent(student13)
mangment.addstudent(student14)
mangment.addstudent(student15)
mangment.addstudent(student16)
mangment.addstudent(student17)
mangment.addstudent(student18)
mangment.addstudent(student19)
mangment.addstudent(student20)

#===============================================================================

# add 0bject Mangment



mangment.menu()
