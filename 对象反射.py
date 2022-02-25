# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 09:41:46 2021

@author: 15003
"""

class Foo:
    f="haha"
    def __init__(self,name,age):
       self.name = name
       self.age = age
    def say_hi(self):
        print("haha nihao")

def main():
    a=Foo("小明",20)
    print(hasattr(a,"say_hi"))
    print(hasattr(a,"say_hi()"))    #函数名不能带括号不然一定是不存在的
    
    b=getattr(a,"say_hi","方法不存在")
    print(b())
    
    c=getattr(a,"say_hiXXX","方法不存在")
    print(c)
    
    delattr(a,"name")
    #print(a.name)   #print会报错不存在
    
    setattr(a,"job","Solider")
    print(a.job)

if __name__=="__main__":
    main()