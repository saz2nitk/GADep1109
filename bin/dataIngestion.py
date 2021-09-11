# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:29:58 2021

@author: saz2n
"""
import os

class Ingest:
    
    def findAllClass(path):
        """To find the class names.
        
        Input:
            path: A string for path of data
        Output:
            classArr: An array of String(class names)"""
        
        classArr = os.listdir(path)
        return classArr
        
        return classArr
    
    def readContentFromDir():
        pass
    
    def collectData():
        pass