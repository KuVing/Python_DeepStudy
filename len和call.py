# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:28:04 2021

@author: 15003
"""

class b:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        return len(self.name)
    def __call__(self,*args,**kwargs):
        print("calling")
def main():
    a=b(input("输入你想要的内容:"))
    print("输入内容的内存大小为:",len(a))
    #print(a.len())  ->   b' object has no attribute 'len'
    a()
if __name__=="__main__":
    main()
    