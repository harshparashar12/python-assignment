basic_salary=int(input(“Enter your basic salary”))
if(basic_salary<=10000):
hra=basic_salary*0.2
Da=basic_salary*0.8
elif(basic_salary<=20000):
hra=basic_salary*0.25
Da=basic_salary*0.9
else:
hra=basic_salary*0.3
Da=basic_salary*0.95
gross_salary=basic_salary+hra+da
print(“Your gross salary is “,gross_salary)