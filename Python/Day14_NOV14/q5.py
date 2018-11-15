import re

fd = open("emp.csv")
lines  = fd.readlines()
f = open("emp2.csv","w+")
for line in lines:
	splitData = line.split(",")
	id = splitData[1]
	if int(id) > 200:
		f.writelines(line)
fd.close()
f.close()
