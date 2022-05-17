# Write a python program to find largest of three numbers
a= int(input("Enter the First Number: "))
b= int(input("Enter the Second Number: "))
c= int(input("Enter the Third Number: "))

print("-------Akash Shukla-------") 
if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number is", largest)