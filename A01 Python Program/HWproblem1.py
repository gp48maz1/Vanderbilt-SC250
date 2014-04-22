'''
Created on Aug 29, 2012

Gary Mazzone Peters
SC 250 HW1 Problem 1
@author: GMP
'''
n=1000
print [x for x in range(2,n) if not [t for t in range(2,x) if not x%t]]
