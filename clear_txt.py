# *{Zs}+([A-Za-z0-9]+|\.|\?) *{Zs}+([+\-]?[0-9]+|\.|\?) *{Zs}*
import re

class DNAHandler():
    def __init__(self):
        self.info = []
    def matchContent(self,file_name):
        done=0
        f=open(file_name,"r")
        while not done:
            content= f.readline()
            myPattern = "(ATOM|HETATM) *(\d) *([A-Za-z0-9.?]+) *([A-Za-z0-9.?]+) *([A-Za-z0-9.?]+) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?) *([+\-]?[0-9]+(\.?[0-9]+)?|\.|\?)"
            matchObj = re.match(myPattern,content, re.I)
            if(matchObj):
                dnfinfo = matchObj.group(1)+","+matchObj.group(2)+","+matchObj.group(3)+","+matchObj.group(4)+","+matchObj.group(5)+","+matchObj.group(6)+","+matchObj.group(7)+","+matchObj.group(8)+","+matchObj.group(9)+","+matchObj.group(10)+","+matchObj.group(11)+","+matchObj.group(12)+matchObj.group(13)+","+matchObj.group(14)
                self.info.append(dnfinfo)
                print(dnfinfo)
            else:
                done=1
                print("Match Error")
        f.close()


def main():
    a=DNAHandler()
    for j in range(1,23):    #这个是数字型
        k=str(j)
        a.matchContent("./chr"+k+".txt")
        f = open("./tmp"+k+".txt", "w")
        for i in range(len(a.info)):
            f.write(a.info[i] + '\n')
    f.close()

    """dic=["X","Y"]      #这个是X/Y型
    for j in dic:
        a.matchContent("./chr"+j+".txt")
        f = open("./tmp"+j+".txt", "w")
        for i in range(len(a.info)):
            f.write(a.info[i] + '\n')
    f.close()"""

if __name__=="__main__":
    main()
