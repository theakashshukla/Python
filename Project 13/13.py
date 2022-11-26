# Write a python program to find factorial of a number using recursion
def rec_fact(n):
   if n == 1:
       return n
   else:
       return n*rec_fact(n-1)

num = int(input("Enter a number: "))
print("------------Akash Shukla------------")
if num < 0:
   print("Negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", rec_fact(num))