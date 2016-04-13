# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:44:03 2016

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
m3=18.0#molecular wt of H2O
#calc 2w/3 w/3 (1-w)
#N1=(2/3)*np.divide(w/m1)
N1=[.0,.0,.0,.0,.0,.0,.0,.0,.0]
N2=[.0,.0,.0,.0,.0,.0,.0,.0,.0]
N3=[.0,.0,.0,.0,.0,.0,.0,.0,.0]
Ntotal=[.0,.0,.0,.0,.0,.0,.0,.0,.0]
x1=[.0,.0,.0,.0,.0,.0,.0,.0,.0]
x2=[.0,.0,.0,.0,.0,.0,.0,.0,.0]
x3=[.0,.0,.0,.0,.0,.0,.0,.0,.0]
for i in range(9):  
    N1[i]=2*w[i]/(3*m1);
    N2[i]=w[i]/(3*m2);
    N3[i]=(1-w[i])/m3;
    Ntotal[i]=N1[i]+N2[i]+N3[i];
    x1[i]=N1[i]/Ntotal[i];
    x2[i]=N2[i]/Ntotal[i];
    x3[i]=N3[i]/Ntotal[i];
#calculating VP
#N=[0.11670521452767*(10^4),-724213.16703206,-17.073846940092,0.12020824702470*(10^5),-3232555.0322333,0.14915108613530*(10^2),-4823.2657361591,0.40511340542057*(10^6),-0.23855557567849,0.65017534844798*(10^3)]
T=333.15 #K
VP=0.01979529#MPa
#loge(Pw) = −6094.4642 T−1 + 21.1249952 − 2.724552×10−2 T + 1.6853396×10−5 T2 + 2.4575506 loge(T)
#v=T+(N(1,9)/(T-N(1,10)))
#A=v^2+N(1,1)*v+N(1,2)
#B=N(1,3)*v^2+N(1,4)*v+N(1,5)
#C=N(1,6)*v^2+N(1,7)*v+N(1,8)
#VP=(2*C/(-B+(B^2-4*A*C)^0.5))^4 #MPa
P=[8, 9, 10, 10.8, 11.7, 13.6, 15.3, 16.5, 17]
print x3
fig=plt.figure();
ax=fig.add_subplot(111)
x3=np.transpose(x3)
ax.plot(x3,P,'*')
fig.canvas.draw()
plt.show()
#A(1)=T12 A(2)=T13 A(3)=T23
#A(4)=T21 A(5)=T31 A(6)=T32
#A(7)=ALPHA 12 A(8)=ALPHA 13 A(9)=ALPHA 23
A0=[.2, .2, .2, .2, .2, .2, .2, .2, .2]
x1=np.transpose(x1)
x2=np.transpose(x2)
x=np.array([x1,x2,x3])
#x=np.transpose(x)
Z=np.array([x,P])
def datafit_1(x,A):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    K=(x1*exp(-A[7]*A[1])*A[1]+x2*exp(-A[8]*A[2])*A[2])/(x1*exp(-A[7]*A[1])+x2*exp(-A[8]*A[2])+x3);
    B=(x1*exp(-A[7]*A[4]))/(x1+x2*exp(-A[3]*A[6])+x3*exp(-A[4]*A[7]));
    C=A[4]-((x2*exp(-A[6]*A[3])*A[3]+x3*exp(-A[7]*A[4])*A[4])/(x1+x2*exp(-A[6]*A[3])+x3*exp(-A[7]*A[4])));
    D=(x2*exp(-A[8]*A[5]))/(x1*exp(-A[6]*A[0])+x2+x3*exp(-A[8]*A[5]));
    E=A[5]-((x1*exp(-A[6]*A[0])*A[0]+x3*exp(-A[8]*A[5])*A[5])/(x1*exp(-A[6]*A[0])+x2+x3*exp(-A[8]*A[5])));
    F=x3/(x1*exp(-A[7]*A[1])+x2*exp(-A[8]*A[2])+x3);
    G=(x1*exp(-A[7]*A[1])*A[1]+x2*exp(-A[8]*A[2])*A[2])/(x1*exp(-A[7]*A[1])+x2*exp(-A[8]*A[2])+x3);
    gama3=exp(K+B*C+D*E-F*G);
    y=VP*x3*gama3;
    return y

def myerror(A,Z):
    #x1,x2,x3,P=Z
    M=Z[0]; N=Z[1];
    x1,x2,x3=M
    P=N
    x=np.array([x1,x2,x3])
    e= P - datafit_1(x,A)
    return e[0]
    
ans1=sc.optimize.leastsq(myerror,A0,Z)
ans=ans1[0]
print ans
#a,b,c,d,e,f,g,h,i=ans
ycalc=datafit_1(x,ans)
fig=plt.figure();
ax=fig.add_subplot(111)
ax.plot(x[2],P)
ax.plot(x[2],ycalc[0],'b')    
ax.title.set_text('P Vs x3')
fig.canvas.draw()
plt.show()