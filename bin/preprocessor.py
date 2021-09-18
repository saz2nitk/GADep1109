# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:30:33 2021

@author: saz2n
"""

class Preprocess:
    
    def __init__(self):
        self.specialChars=[',','#','.',',','$','>','<','\\']
    
    
    def removeSpecialChar(self,text):
        for specialChar in self.specialChars:
            text = text.replace(specialChar,'')
        return text
    
    def stemWords(self):
        pass