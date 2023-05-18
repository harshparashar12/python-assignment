import random

fd=open("quotes.txt","r")
line=fd.readlines()
print(random.choice(line))
fd.close()