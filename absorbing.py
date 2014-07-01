import numpy as np
import matplotlib as mp
import pylab as pl

def F(x,coe,X0):
   return (np.exp(coe*(x-X0))+coe*(-x+X0)-1.)

X=np.linspace(0.,2)
pl.plot(X,F(X,1,1.))
pl.plot(X,F(X,2.,1.))
pl.plot(X,F(X,3.,1.))
pl.plot(X,F(X,4.,1.))
pl.show()
