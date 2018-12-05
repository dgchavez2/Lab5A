# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:06:20 2018

@author: danie
"""

class Heap:
    def __init__(self):
        self.heap_array = []
    
    def insert(self, k):
        self.heap_array.append(k)
        
        self.heap_array.percolate_up(len(self.heap_array) - 1)
        
    def percolate_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            
            if self.heap_array[index] >= self.heap_array[parent_index]:
                return
            else:
                temp = self.heap_array[index]
                self.heap_array[index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                
                index = parent_index
    
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array.append[0]
        if self.heap_array.left_child() == min(self.heap_array.left_child(), self.heap_array.right_child()):
            i = 1
        else:
            i = 2    
        temp = min(self.heap_array.left_child(), self.heap_array.right_child())
        self.heap_array.percolate_up(i)
        self.heap_array[0] = temp
        
        return min_elem
    
    def is_empty(self):
        return len(self.heap_array)== 0
    