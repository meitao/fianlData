#coding=utf-8
param ={'a':1,'b':4}

print "你好" 

def test(x=0,**map):
    print x,map

test(8,y=1,k=9)  