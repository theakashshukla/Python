# Write a python program to construct the given pattern using nested for loop
num=6;

print("-------------Akash Shukla-------------")
for i in range(num):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(num,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')