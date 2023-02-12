class Student:
 
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
 
    def accept(self, Name, Rollno):
   
        ob = Student(Name, Rollno)
        ls.append(ob)
 
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("\n")