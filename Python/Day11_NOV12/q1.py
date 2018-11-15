#!/user/bin/env python

import xml.dom.minidom as dom

dtree = dom.parse("../data/book.xml")
rn = dtree.documentElement
fd = open("book1","a+")
n = 1
for bn in rn.childNodes:
    line1 = line2 = category = ""

    if bn.nodeType == 1:
        for k in bn.attributes.keys():
            category = bn.attributes[k].value
    for tn in bn.childNodes:
        for tx in tn.childNodes:
            if tx.parentNode.nodeName == "title":
                line1 = str(n) + ". The book " + tx.nodeValue + " belongs to " + category.upper()
            if tx.parentNode.nodeName == "author":
                line1 += " category and is written by " + tx.nodeValue
            if tx.parentNode.nodeName == "year":
                line2 = ". The book is published in the year " + tx.nodeValue
            if tx.parentNode.nodeName == "price":
                line2 += " with a price of " + tx.nodeValue + ".\n"
    if bn.nodeType == 1:
        fd.writelines(line1 + line2)
        n += 1
fd.close()
