# Write a program to demonstrate working with tuples in python
tuple = (1,2,3,4,5.2,6,7,8,9,10)
tuple1 = ("Akash", "Pawan", "Amit", "Ankit", "Parth", "Ashish")
tuple2 = (tuple + tuple1)

print("-------Akash Shukla-------") 

print("Tuple ", tuple)
print("Tuple 1", tuple1)

print("Added Tuple", tuple2)

print("Tuple Length", len(tuple))
print("Tuple 1 Length", len(tuple1))

print("Tuple Maximum Value", max(tuple))
print("Tuple Minimum Value", min(tuple))
print("Index 3 :",tuple[3])