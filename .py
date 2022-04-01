import sys

f = open('100.txt','r')

for i in f:
    print("The Usernames in the file {} are: {}".format(sys.argv,i)) 

f.seek(0)
