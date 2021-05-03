# -*- coding: utf-8 -*-
"""
Created on Sun May  2 07:20:48 2021

@author: USER
"""

class check_prime:
    def __init__(self,number):
        self.number = number
        self.op()
    def op(self):
        self.file = open('data.txt','r').read()
        self.file_data = list(map(int(),(self.file).split(",")))
        self.file.close()
    def prime(self):
        flag = True
        if self.number in self.file_data:
            return flag
        for i in self.file_data:
            if i % self.number == 0:
                flag = False
                break
        if flag:
            if not self.number in self.file_data:
                file = open('data.txt','w').write(f',{self.number}') 
                file.close()
    
        return flag
            
        