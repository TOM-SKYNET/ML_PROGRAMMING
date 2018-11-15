import re

fd = open("emp.csv")
lines  = fd.readlines()
f = open("empphno.csv","w+")
for line in lines:
	splitData = line.split(",")
	name = splitData[0]
	phno = re.sub('[^0-9]','',splitData[4])
	f.writelines('Name: ' + name + ', Phone # '+phno + '\n')
fd.close()
f.close()
