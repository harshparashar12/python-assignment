file=open("read data.txt","r")
data=file.read()
file.close()

with open("write data.txt","a") as file:
    file.write(data)