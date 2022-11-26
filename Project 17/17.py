# Write a python program to show Multiple Inheritance.

print("------------Akash Shukla------------")
class Course:
   def func1(self):
        print("this is function 1")
class Course2:
   def func2(self):
        print("this is function 2")
class Subject(Course , Course2):
    def func3(self):
        print("this is function 3")
 
ob = Subject()
ob.func1()
ob.func2()
ob.func3()