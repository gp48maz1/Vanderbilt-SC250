'''
Created on Aug 29, 2012

Gary Mazzone Peters
SC 250 HW1 Problem 2

@author: GMP
'''

i=1
k=600000
top=float(4*i*i)
bottom=float((4*i*i)-1)
pi = 2*float(top/bottom)

while i<k:
    i=i+1
    ptop=float(4*i*i)
    pbottom=float((4*i*i)-1)
    pi = (float(ptop/pbottom))*pi

print pi