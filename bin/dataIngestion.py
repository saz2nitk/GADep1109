# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 09:29:58 2021

@author: saz2n
"""
import os

class Ingest:
    
    def findAllClass(self,basePath):
        """To find the class names.
        
        Input:
            path: A string for path of data
        Output:
            classArr: An array of String(class names)"""
        
        classArr = os.listdir(basePath)
        return classArr
    
    def readContentFromDir(self,basePath,className):
        
        classDir = os.path.join(basePath,className)
        files = os.listdir(classDir)
        contentList = []
        for file in files:
            with open(os.path.join(classDir,file)) as fl:
                content = fl.read()
            contentList.append(content)        
        return contentList
    
    def collectData(self,basePath):
        
        classNames = self.findAllClass(basePath)
        finalData = {}
        for className in classNames:
            contentList = self.readContentFromDir(basePath,className)
            finalData[className] = contentList
        return finalData
        