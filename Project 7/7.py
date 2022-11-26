# Write a program to Demonstrate working with Dictionaries in Python

Desc = {'Name': 'Java', 'Version': '3.7.0', 'Author': 'Akash', 'Year': '2022'}

print("-------Akash Shukla-------") 

print("Before Update", Desc)

Desc['Name']='Python'

Desc["Version"]="3.10.0"

print("After Update", Desc)

Desc["Address"] = "Bhopal"

print ("After Adding New Key", Desc)

print("Key Deleted", Desc.pop("Version"))

print ("After Key Deleted", Desc )
