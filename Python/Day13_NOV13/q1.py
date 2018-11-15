import xml.dom.minidom as dom

fd = open("emp.csv")
data = fd.read()
print data
data = data.as_matrix()
print data
