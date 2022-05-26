# Write a python program to show Single Inheritance.
print("-----------Akash shukla-------------")
class Course:
     def func1(self):
          print("This is function one")
class Subject(Course):
     def func2(self):
          print("This is function Two ")
ob = Subject()
ob.func1()
ob.func2()
