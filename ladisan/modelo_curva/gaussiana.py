from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
import matplotlib.pyplot as plt
import time

#%matplotlib

x = ar([x*2 for x in range(8)]) # 0,2,4,...,14
y = ar([2,4,6,7,6,4,1,2])

n = len(x)                          #the number of data
mean = sum(x*y)/n                   #note this correction
sigma = sum(y*(x-mean)**2)/n        #note this correction

def gaus(x,a,x0,sigma):
    return a*exp(-(x-x0)**2/(2*sigma**2))+2

popt,pcov = curve_fit(gaus,x,y,p0=[0,mean,sigma])

absissa = [x/60 for x in range(16*60)]

def f(x): 
    global popt 
    return gaus(x,*popt)

plt.plot(absissa, f(absissa), 'b')


