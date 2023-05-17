f=open("myfile.txt","r")
line=f.readlines()
print(line)

new_lines=[x.strip() for x in line]
print(new_lines)