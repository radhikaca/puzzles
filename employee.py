# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:14:07 2020
unittest example

@author: rad
"""

class Employee:
    def __init__(self,fname, lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        
    def raise1(self, r=5000):
        if (r>0):
            self.salary+=r
            return "Success"
        else:
            return "False"
        


