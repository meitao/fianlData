#coding=utf-8
import re
import os
'''
Created on 2016年7月13日

@author: Administrator
'''
from IPython.utils._process_win32_controller import ReadFile
from genericpath import isdir
def readFile():
    f1= file('J:/work/data/test.txt',"r+")
    for i in f1:
        print i
    f1.close()
        
    
def writeFile():
    f1= file('J:/work/data/test.txt',"w+")
    i= 0
    while i<100000:
        f1.write(str(i))
        f1.write("\n")
        i=i+1
    f1.close()
    
def replaceFile():
    f1= file('J:/work/data/test.txt',"r")
   
    st =""
    for a in f1:
        st=st+a.replace("a", "c")
    f2= file('J:/work/data/test.txt',"w")
    f2.write(st) 
    f1.close()  
    f2.close()  
    
    
def seekReplaceFile():
    f1= file('J:/work/data/test.txt',"r+")
    st =""
    for a in f1:
        st=st+a.replace("a", "c")
    f1.seek(0)
    f1.write(st) 
    f1.close()  
    
def makedir():
    print isdir("J:/work/data/test")
    print isdir('J:/work/data/test.txt')
    print os.listdir('J:/work/data/test')
    print os.listdir('J:/work/data/test.txt')

def listdir(path):
    listfile=[]
    if isdir(path):
        lf =os.listdir(path)
        for i in lf:
            listfile.append(listdir(os.path.join(path,i)))
    listfile.append(path) 
    return listfile 
 
writeFile()    

print listdir("J:/work/data/test")
g= os.walk("J:/work/data/test")
for k in g :
    print k