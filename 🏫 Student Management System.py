#============================
#🏫 Student Management System
#=============================
import json
#========================================
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

    def to_dict(self):
             return {
             "ID": self.ID,
             "Name": self.Name,
             "Group": self.Group,
             "Age": self.Age,
             "Grade": self.Grade
         }


#==========================================================
class Management:
    def __init__(self):
        self.students = []
        self.load_from_json() 
#=================================================================================================

    def addstudent(self,student):
        self.students.append(student)
        self.save_to_dict()
        print("✅ Student added successfully!")
#=================================================================================================

    def search_student(self):
        while True:
            try:
                student_id = (input("Student ID (q to quit) ")).strip()
                if student_id.lower()  in ["q","exist"]:
                    break # exist loop
                else:
                    student_id = int(student_id)
                for student in self.students:
                    if student_id == student.ID:
                        print("Execution complete.")
                        student.showdetails()
                        break
                else:# this belong to for loop
                    print(f"Student wit this id {student_id}. not found")
        
            except ValueError:
                print("Invalid input ! Please enter a number.")

          
#=================================================================================================

    def create_student(self):
        while True:
            Id = input("Enter new student ID: ")
            if (not Id.isdigit() or len(Id) != 4):
                print("Student ID must contain exactly 4 digits")
                continue
            Id = int(Id)
            duplicate = False
            for student in self.students:
                if (Id  == student.ID):
                    print(f"ID {Id} already exists . Enter a different ID.")
                    duplicate = True
                    break

        #if duplicate was a found
        # go back and ask again for a new id
            if duplicate:
                continue 
            print("✅ ID is available")

            duplicate = False
            while True:

                name = input("Enter new student name: ").strip()
                duplicate = False
                for i in self.students:
                    if (name.lower()  == i.Name.lower()):
                        print(f"Name  not available {name}")
                        duplicate = True
                        break

                if duplicate:
                   continue
                print("✅ Name is available")
                
                break
        
        

            group = input("Enter new student group: ").strip()

            while True:
                try:
                    age = int(input("Enter new student age: "))
                except ValueError:
                    print("Invalid input ! Please enter a valid input numeric number")
                    continue    
            
          
            
                   
                grade = input("Enter new student grade: ").strip()
                student = Student(Id,name,group,age,grade)
            #     return it to addstudent()
                    
                return student 



                
                
              

#=================================================================================================
        
    def show_one_student(self):
        while True:
            try:
                student_id = (input("Student ID:(q to quit): ")).strip()
                if student_id.lower() in ["q" ,"exit"]:
                    print("You Exit")
                    break
                else:
                    student_id = int(student_id)
                found = False
                for student in self.students:
                  
                    if student.ID == student_id:
                        print(f"Student with this id {student_id}. found it")
                        student.showdetails()
                        found = True
                        break
                if not found:
                    print(f"Student with this id {student_id}. not found")
            except  ValueError:
                print("❌ Invalid input! Enter a numeric student ID or 'q' to quit.")

#=================================================================================================
   
    def delete_student(self):
        while True:
            try:
                student = self.validate_student_id()
                self.students.remove(student)
                print(f"Student   Name {student.Name}..  ID {student.ID} . delete")
                self.save_to_dict()
                break
            except ValueError:
                print("Invalid input ! Please enter a numeric number.")
          
                
                    
        
#=================================================================================================

    def update_student(self):
       student = self.validate_student_id()
       if student:
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
                self.save_to_dict()
        
            elif choise == "2":
                change_group = input("Enter new group name: ")
                student.Group = change_group                        
                print(f"✅ Name updated successfully! {student.Group}.") 
                student.showdetails()
                self.save_to_dict()
                        
                    
            elif choise == "3":
                while True:
                    try:
                        update_age = int(input("Enter student age: "))
                        student.Age = update_age
                        print(f"✅ Student age update successfully! {student.Age}.")
                        student.showdetails()
                        self.save_to_dict()
                        return
                    
                    except ValueError:
                        print("Invalid age ! Please enter valid age!")
                
                    
            elif choise == "4":
                update_grade = input("Updata student grade: ")
                student.Grade = update_grade
                print(f"✅Student with there new grade {student.Grade}.")
                self.save_to_dict()    

            elif choise == "5":
                print("📋 Current Details.")
                student.showdetails()
                    
            elif choise == "6":
                print("👋 Goodbye")
                break
            else:
                print(f"Invalid choice . Try again.")
         
         
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
            student_name = input('Enter search name (Q): ').strip()
            if student_name.lower() in ["quit","exit"]:
                print("You Exit")
                return
                 
            found = False
            for student in self.students:# check all list 
                if student_name.lower() == student.Name.lower():
                    print(student_name,"Student Found ✅")
                    found = True
                    break
            if not found:
                print(student_name,"Student Not Found ❌")  
#=================================================================================================

    def clear_all_student(self):
        clear_student = input("Are you sure? (q to quit) ")
        if clear_student.lower() in ["quit", "exist", "q"]:
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
            if student_name.lower() == student.Name.lower():
                print(student_name,f"✅ Student found it ")
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
            
        print(f"Top Grade Student: {Top_Grade_Student}") 
        
#=================================================================================================   
    
    def youngest_age(self):
        if not self.students:
          print("NO student available")
          return
        youngest = self.students[0]#"Take the first student object as my starting answer."
        for student in self.students:
            if student.Age < youngest.Age:
                youngest = student      
                print([youngest.Name,youngest.Age])
            elif not self.students:
                print(f"No Student available.")
                return
        print()
        youngest.showdetails()
#================================================================================================          
    
    def oldest_student(self):
        if not self.students:
            print("No student available")
            return
        oldeststudent = self.students[0]
        
        for student in self.students:
            if student.Age > oldeststudent.Age:
                oldeststudent = student
                print(oldeststudent,f"Oldest Student with {oldeststudent}.")
        oldeststudent.showdetails()   
#================================================================================================
    def validate_student_id(self):
        while True:
            
            student_ID = input("Student ID: ")
            if len(student_ID) == 4:
                student_ID = int(student_ID)             
            else:
                print("Student ID must contain exactly 4 digits.")
                return        
            for student in self.students:
                if student_ID == student.ID:
                   print("ID Valid ✅",student.Name,student.ID)
                   return student #otherwise return object
                
            else:
                print("ID not valid")
            

#================================================================================================
   
    def save_to_dict(self):
        data = []
        for student in self.students:
            data.append(student.to_dict())

        with open("student.json", "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Students saved successfully!")
       

#================================================================================================

    def load_from_json(self):
        try:
            with open("student.json", "r") as file:
                data = json.load(file)
                for student in data:
                    student = Student(
                    student["ID"],
                    student["Name"],
                    student["Group"],
                    student["Age"],
                    student["Grade"],
                    )
                    self.students.append(student)
        except FileNotFoundError:
            print("student.json file not found")
#================================================================================================
    def search_group(self):
        
        searchGroup = input("Enter a Group name: ").strip()
        found_students = [s for s in self.students if s.Group.lower() == searchGroup.lower()]
        if found_students:
            print(f"😎======== {searchGroup.upper()} GROUP =========😎")
            for student in found_students:
                student.showdetails()
                print("⚡============================⚡")
            print(f"Total student in {searchGroup.upper()} GROUP = {len(found_students)}")
        else:
            print("Group dose not exists...")

        
        

#================================================================================================



    
    
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
            print("8. Highist Grade Student")
            print("9. Youngest Student")
            print("10. Oldest Student")
            print("11. Total Student")
            print("12. Search One Student")
            print("13. Exit")
            
            choise = input("Enter your chosie: ")
            print()
            if choise == "1":
                student = self.create_student()
                self.addstudent(student)
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

mangment = Management()
#============================================================================
#add student
mangment.search_group()

#===============================================================================

# add 0bject Mangment

