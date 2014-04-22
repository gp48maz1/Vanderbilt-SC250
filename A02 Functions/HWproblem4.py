'''
Created on Sep 3, 2012

Gary Mazzone Peters
SC 250 HW1 Problem 1

@author: GMP
'''
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from scipy import linspace

n = 50001 

# match 
# match is a check to see if the k value is larger than the sqrt of n
# take the number smaller 

def isPrime(n):
    aaa = range(3,n+1,2)
    primes = [2];
    for i in aaa:
        if i>primes[-1]:
            for k in primes:
                if k < int(math.ceil(n**.5)):
                    if i % k:
                        if k == primes[-1]:
                            primes.append(i)        
                    else:    
                        break
                else:
                    if i % k:
                        primes.append(i)
                        break
    return len(primes)

#def primeCount(n):
 #   'make into a list not a print'
  #  primeList = [x for x in range(2,n) if not [t for t in range(2,x) if not x%t]]
   # 'count elements by finding the last indexed value in the list'
    #return len(isPrime)
    
def mathTher(n):
    top = n
    bottom = np.log([n])  
    mT = float(top/bottom)
    return mT

    
    
#a = np.linspace(2,n,1)
#print primeCount(n)
#print mathTher(n)

b=n-1

a = np.linspace(2,n,b) # cant use range
cc = [int(x) for x in a]
#yA_series = primeCount(c)

yA_list =[]
for x in cc:
    yA_series = isPrime(x)
    yA_list.append(yA_series)


yB_list =[]
for x in cc:
    yB_series = mathTher(x)
    yB_list.append(yB_series) 

#yB_series = mathTher(c)

'sudo code for plot with matplotlib'
plt.plot(cc, yA_list,'r', cc, yB_list, 'b')
#plt.legend(loc="upper left")
print "red is PrimeCount and blue is equation, x-axis is current number y-axis is number of primes"
#a, yA_series,
plt.show()


