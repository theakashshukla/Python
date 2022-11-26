# Write a python program to Print Prime numbers less than 20

print("-----------Akash Shukla-----------") 
print("Prime numbers between 1 and 20 are:")
numbers=20;
for num in range(numbers):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
