sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
percentage=(sub1+ sub2+ sub3+ sub4+ sub5)/5
if(percentage>=90):
print(“Grade=A”)
elif(percentage>=80):
print(“Grade=B”)
elif(percentage>=70):
print(“Grade=C”)
elif(percentage>=60):
print(“Grade=D”)
elif(percentage>=40):
print(“Grade=E”)
else:
print(“Grade=F")