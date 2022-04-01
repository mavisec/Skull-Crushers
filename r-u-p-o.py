#a script to read contents from a file.
import sys #importing sys module

f = open('100.txt','r') #reading from the file

for i in f:
    print("The Usernames in the file {} are: {}".format(sys.argv,i)) #adding a custom line before the usernames or passwords.
f.seek(0)
