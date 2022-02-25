# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 19:28:01 2021

@author: 15003
"""
class people:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight/(self.height**2)
def main():
    p1=people("小明",90,1.90)
    print(p1.bmi)   #使用PROPERTY以后不需要使用()
    
    
if __name__=="__main__":
    main()
        
