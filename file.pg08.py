n=int(input("enter the number N:-"))
f=open("myfile.txt","r")
s=f.read()
lst=s.split()

for i in lst:
    if(len(i)>n):
        print(i)