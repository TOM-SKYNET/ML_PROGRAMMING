import xml.sax

class conHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.title = ''
        self.author = ''
        self.year = ''
        self.price = ''
        self.curtag = ''
        self.line = ''
        self.category = ''

    def startElement(self,tagname, attrs):
        self.curtag = tagname
        if tagname == 'book':
            self.category = attrs['category']

    def characters(self,content):
        if self.curtag == 'title':
            self.title = content
        if self.curtag == 'author':
            self.author = content
        if self.curtag == 'year':
            self.year = content
        if self.curtag == 'price':
            self.price = content

    def endElement(self,tag):
        if tag == 'title':
            self.line += 'The book ' + self.title + ' belongs to ' + self.category
        if tag == 'author':
            self.line += ' written by ' + self.author
        if tag == 'year':
            self.line += ' published on ' + self.year
        if tag == 'price':
            self.line += ' and price is ' + self.price
        if tag == 'book':
            open('book.txt', 'a+').writelines(self.line + '\n')
            self.line = ''

parserObj = xml.sax.make_parser()
parserObj.setContentHandler(conHandler())
parserObj.parse('book.xml')

