# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 21:10:25 2016

@author: Madhu
"""
import xlrd
import scipy as sc
from scipy import array
import numpy as np
import scipy,scipy.optimize
import matplotlib.pyplot as plt
from math import exp
#import scipy.optimize as optimization
#from scipy.optimize import curve_fit
#calc of mole fraction from weight fraction
w=[.800, .700, 0.600, 0.500, 0.400, 0.300, 0.200, .015, .010]#weight fraction
m1=86.845#molecular wt of LiBr
m2=84.1157#molecular wt of HCOOK
m3=18#molecular wt of H2O
#calc 2w/3 w/3 (1-w)
#N1=(2/3)*np.divide(w/m1)
N1=2*w/(3*m1);
N2=w/(3*m2);
N3=(1-w)/m3;
Ntotal=N1+N2+N3;
x1=N1/Ntotal;
x2=N2/Ntotal;
x3=N3/Ntotal;
#calculating VP
N=[0.11670521452767*(10^4),-724213.16703206,-17.073846940092,0.12020824702470*(10^5),-3232555.0322333,0.14915108613530*(10^2),-4823.2657361591,0.40511340542057*(10^6),-0.23855557567849,0.65017534844798*(10^3)]
T=333.15 #K
v=T+(N(1,9)/(T-N(1,10)))
A=v^2+N(1,1)*v+N(1,2)
B=N(1,3)*v^2+N(1,4)*v+N(1,5)
C=N(1,6)*v^2+N(1,7)*v+N(1,8)
VP=(2*C/(-B+(B^2-4*A*C)^0.5))^4 #MPa
P=[8, 9, 10, 10, 11.7, 13.6, 15.3, 16, 17]

fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(x3,P,'b*')
fig.canvas.draw()
plt.show()
#A(1)=T12 A(2)=T13 A(3)=T23
#A(4)=T21 A(5)=T31 A(6)=T32
#A(7)=ALPHA 12 A(8)=ALPHA 13 A(9)=ALPHA 23
A0=[.2, .2, .2, .2, .2, .2, .2, .2, .2]
x=np.array([x1,x2,x3])
x=np.transpose(x)
Z=np.array([x,P])
def datafit_1(x,A):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    K=(x1*exp(-A(8)*A(2))*A(2)+x2*exp(-A(9)*A(3))*A(3))/(x1*exp(-A(8)*A(2))+x2*exp(-A(9)*A(3))+x3);
    B=(x1*exp(-A(8)*A(5)))/(x1+x2*exp(-A(4)*A(7))+x3*exp(-A(5)*A(8)));
    C=A(5)-((x2*exp(-A(7)*A(4))*A(4)+x3*exp(-A(8)*A(5))*A(5))/(x1+x2*exp(-A(7)*A(4))+x3*exp(-A(8)*A(5))));
    D=(x2*exp(-A(9)*A(6)))/(x1*exp(-A(7)*A(1))+x2+x3*exp(-A(9)*A(6)));
    E=A(6)-((x1*exp(-A(7)*A(1))*A(1)+x3*exp(-A(9)*A(6))*A(6))/(x1*exp(-A(7)*A(1))+x2+x3*exp(-A(9)*A(6))));
    F=x3/(x1*exp(-A(8)*A(2))+x2*exp(-A(9)*A(3))+x3);
    G=(x1*exp(-A(8)*A(2))*A(2)+x2*exp(-A(9)*A(3))*A(3))/(x1*exp(-A(8)*A(2))+x2*exp(-A(9)*A(3))+x3);
    gama3=exp(K+B*C+D*E-F*G);
    y=VP*x3*gama3;
    return y

def myerror(A,z):
    x1,x2,x3,P=z
    x=np.array([x1,x2,x3])
    e= P - datafit_1(x,A)
    return e[0]
    
ans1=scipy.optimize.leastsq(myerror,A0,Z)
ans=ans1[0]
print ans
a,b,c,d,e,f=ans
ycalc=datafit_1(x,ans)
fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(x[2],P,'*')
ax.plot(x[2],ycalc[0],'b')    
ax.title.set_text('P Vs x3')
fig.canvas.draw()
plt.show()