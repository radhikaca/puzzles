# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:16:43 2020

@author: rad
"""

import unittest
from employee import Employee

class testEmployee(unittest.TestCase):
    
    def setUp(self):
        self.empObj=Employee("radhika","CA",45000)
        self.r=-1
        
    def test_give_default_raise(self):
        output=self.empObj.raise1()
        print(output)
        print(self.assertEqual(output,"Success"))
    
    def test_give_custom_raise(self):
        output=self.empObj.raise1(self.r)
        print(output)
        print(self.assertEqual(output,"Success"))

unittest.main()