# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:55:32 2020
linkedList Operations
@author: rad
"""


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
        
    def insert(self,value):
        
        if(self.head==None):
            self.head=Node(value)
        else:
            cur=self.head
            while(cur.next!=None):
                cur=cur.next
            cur.next=Node(value)
    
    def traverse(self):
        if(self.head==None):
            print("empty")

        cur=self.head
        while(cur !=None):
            print(cur.value)
            cur=cur.next
            
    def find(self,num):
        ctr=1
        if(self.head==None):
            return -1
        cur=self.head
        while(cur !=None):
            if(cur.value==num):
                return ctr
            else:
                ctr+=1
                cur=cur.next
        return -1
head=LinkedList()
for i in range(1,10):
    head.insert(i)

head.traverse()
print(head.find(3))