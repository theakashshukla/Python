# Write a python program to show Hybrid Inheritance. class Parent:

print("------------Akash Shukla------------")
class Father:
    def func1(self):
         print("This function is in Father")

class FirstChild(Father):
    def func2(self):
        print("This function is in FirstChild")

class SecondChild(Father):
    def func3(self):
        print("This function is in SecondChild")

class GrandChild(FirstChild, Father):
    def func4(self):
        print("This function is in GrandChild")

object = GrandChild()
object.func1()
object.func2()

