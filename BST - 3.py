# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:33:22 2020

@author: rad
"""

class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value
        
class BinaryTree:
    def __init__(self,value):
        self.root=Node(value)
        
    def getRootNode(self):
        
        return self.root
    
    def insert(self,root,value):

        if(root==None):
            root=Node(value)
            

        if(value>root.data):
            root.right=self.insert(root.right,value)
        
        if(value<root.data):
            root.left=self.insert(root.left,value)
        
        print(root.data, "inserted")
        return root
    
    def printroot(self,root):       

        
            
        if(root.left):
                self.printroot(root.left)
        print(root.data, id(root))
        
        if(root.right):   
                self.printroot(root.right)

obj=BinaryTree(5)

#r=obj.getRootNode()
l=[6,4,7,3,2,1]


for i in l:
    
    r=obj.insert(r,i)
    print("******************************")

obj.printroot(r)