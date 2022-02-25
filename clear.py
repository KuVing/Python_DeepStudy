# *{Zs}+([A-Za-z0-9]+|\.|\?) *{Zs}+([+\-]?[0-9]+|\.|\?) *{Zs}*
import xml.sax
from xml.sax import handler
import re

class DNAHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.CurrentData = ""
        self.id = ""
        self.content=""
        self.info = []

   # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if(tag=="PDBx:atom_record"):
            self.id=attributes['id']

   # 元素结束事件处理
    def endElement(self, tag):
        if(tag=="PDBx:atom_record"):
            print("end")


   # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "PDBx:atom_record":
            self.content = content
            self.matchContent()

    def matchContent(self):
        content = self.content
        myPattern = " *(ATOM|HETATM) *(\d) *([A-Za-z0-9.?]+) *([A-Za-z0-9.?]+|[\-]) *([0-9]+|\.) *([0-9]+).*?([A-Za-z0-9]+) *([A-Za-z0-9]+) *([A-Za-z]) *([A-Za-z0-9_\*,\'+]+|\.|\?) *([A-Za-z0-9_\*,\'+]+|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+|\.|\?) *([+\-]?[0-9]+|\.|\?)"
        matchObj = re.match(myPattern, content, re.I)
        if(matchObj):
            dnfinfo = matchObj.group(1)+","+matchObj.group(2)+","+matchObj.group(3)+","+matchObj.group(4)+","+matchObj.group(5)+","+matchObj.group(6)+","+matchObj.group(7)+","+matchObj.group(8)+","+matchObj.group(9)+","+matchObj.group(10)+","+matchObj.group(11)+","+matchObj.group(12)+","+matchObj.group(14)+","+matchObj.group(16)+","+matchObj.group(18)+","+matchObj.group(20)+","+matchObj.group(22)+","+matchObj.group(23)
            self.info.append(self.id+","+dnfinfo)
            print(dnfinfo)
        else:
            print("Match Error")



parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler = DNAHandler()
parser.setContentHandler(handler)
parser.parse("./6wig_DNA.xml")

f=open("./dna.txt", "w")
for i in range(len(handler.info)):
    f.write(handler.info[i]+'\n')
f.close()