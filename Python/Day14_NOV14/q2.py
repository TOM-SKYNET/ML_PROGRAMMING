import re

fd = open("emp.csv")
lines  = fd.readlines()
f = open("ini1.csv","w+")
for line in lines:
	if len(re.findall(r'^[A-Z]+\.(?=\w)*',line)) > 0:
		f.writelines(line)
	
fd.close()
f.close()
