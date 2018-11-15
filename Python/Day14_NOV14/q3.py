import re

fd = open("emp.csv")
lines  = fd.readlines()
f = open("ini2.csv","w+")
for line in lines:
	if len(re.findall(r'(?=\w)*\.[^0-9]+',line)) > 0:
		f.writelines(line)
fd.close()
f.close()
