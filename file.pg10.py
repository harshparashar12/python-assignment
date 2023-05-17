f=open("harsh.txt","r")
wrd=input("enter the word ")
# store in the string.
s=f.read()
lst=s.split()
count=0
for i in lst:
    if(i==wrd):
        count+=1
        print("word {} occured {} times".format(wrd,count))
