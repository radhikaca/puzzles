# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:55:32 2020
linkedList Operations
@author: rad
"""


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=Node()
        
    def insert(self,value):
        
            cur=self.head
            while (cur.next!=None):
                cur=cur.next
                
            cur.next=Node(value)
    
    def traverse(self):

        cur=self.head.next
        while(cur !=None):
            print(cur.value)
            cur=cur.next
            
    def delete(self,value):
        
        cur=self.head.next
        if cur.value==value :
                self.head.next=cur.next
        else:
            prev=cur
            cur=cur.next
            #print(prev.value,cur.value)
            while(cur!=None):
                if(cur.value==value):
                    prev.next=cur.next
                    return
                prev=cur
                cur=cur.next
                    

    
obj=LinkedList()
for i in range(1,5):
    obj.insert(i)
 

obj.delete(2)
obj.traverse()

