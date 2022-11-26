# Write a python program to show Operation on File.

print("------------Akash Shukla------------")
text_file = open('I:\hi.txt','w')
  
word_list= []

for i in range (1, 5):
    print("Please enter data: ")
    line = input() 
    word_list.append(line) 
text_file.writelines(word_list) 
text_file.close()