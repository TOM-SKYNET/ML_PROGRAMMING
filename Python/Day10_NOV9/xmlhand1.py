import xml.sax

class myHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.text = []
        self.keeping_text = False
        self.attributes = []
        self.strval = ''

    def startElement(self, name, attrs):
        if name.lower() in ('title', 'author', 'price'):
            self.keeping_text = True

        try:
            # must attribute1 be on a tag2 or anywhere?
            attr = attrs.getValue('attribute1')
            self.attributes.append(attr)
        except KeyError:
            pass

    def endElement(self, name):
        self.keeping_text = False

    def characters(self, content):
        if self.keeping_text:
            self.text.append(content)
            self.strval += '--' + content
            print content
parser = xml.sax.make_parser()
handler = myHandler()
parser.setContentHandler(handler)
parser.parse(open("book.xml", "r"))

print handler.strval
#print handler.attributes
