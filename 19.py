# Write a python program to show Hierarchical Inheritance.
print("------------Akash Shukla------------")
class Course:
      def func1(self):
          print("this is function 1")
class Subject(Course):
      def func2(self):
          print("this is function 2")
class Subject2(Course):
      def func3(self):
          print("this is function 3")
 
ob =  Subject()
ob1 = Subject2()
ob.func1()
ob.func2()