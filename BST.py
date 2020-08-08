# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:30:04 2020

Binary Search Tree

@author: rad
"""

class Node:
    
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
    
class Tree:
 
   
        
    def insert(self,root,value):
        
        if root==None :
            return Node(value)
        else:
            if(value <= root.value):
                cur=self.insert(root.left,value)
                root.left=cur
            else:
                cur=self.insert(root.right,value)
                root.right=cur            
        return root

    def inorder(self,root):
        
       if(root.left):
           self.inorder(root.left)           
       print(root.value)       
       if(root.right):
           self.inorder(root.right)
           
    def pre_order(self,root):
        
       print(root.value)       
       if(root.left):
           self.pre_order(root.left)
       if(root.right):
           self.pre_order(root.right)
           
    def post_order(self,root):
        
       if(root.left):
           self.inorder(root.left)              
       if(root.right):
           self.inorder(root.right)
       print(root.value)
        
    def find_elt(self,root,value):
        if(root==None):
            return False
        if(root.value==value):
            return (root,root.value)
        elif(value<=root.value):
            return self.find_elt(root.left,value)
        elif(value>=root.value):
            return self.find_elt(root.right,value)
        else:
            return False
        
    
myTree=Tree()
root=None
l=[5,2,1,4,13]

for i in l:
    root=myTree.insert(root,i)
    #print("outside root", root.value)
print("***In-order***")
myTree.inorder(root)
print("***Pre-order***")
myTree.pre_order(root)
print("***Post-order***")
myTree.post_order(root)

print("Found elt :",myTree.find_elt(root,4))
