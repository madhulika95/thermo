

import scipy 
import matplotlib.pyplot as plt
import scipy.optimize

#import scipy.optimize as optimization
#from scipy.optimize import curve_fit
#calc of mole fraction from weight fraction
w=[.800, .700, 0.600, 0.500, 0.400, 0.300, 0.200, .035, .010]#weight fraction
m1=86.845#molecular wt of LiBr
m2=84.1157#molecular wt of HCOOK
m3=18.0#molecular wt of H2O
#calc 2w/3 w/3 (1-w)
#N1=(2/3)*np.divide(w/m1)
N1,N2,N3,Ntotal = [], [], [], []
X1, X2, X3 = [], [], []

for i in range(len(w)):
    n1=2*w[i]/(3*m1); N1.append(n1)
    n2=w[i]/(3*m2); N2.append(n2)
    n3=(1-w[i])/m3; N3.append(n3)
    ntotal=n1+n2+n3; Ntotal.append(ntotal)
    x1=n1/ntotal; X1.append(x1)
    x2=n2/ntotal;X2.append(x2)
    x3=n3/ntotal; X3.append(x3)

#calculating VP
N=[0.11670521452767*(10^4),-724213.16703206,-17.073846940092,0.12020824702470*(10^5),-3232555.0322333,0.14915108613530*(10^2),-4823.2657361591,0.40511340542057*(10^6),-0.23855557567849,0.65017534844798*(10^3)]
T=333.15 #K
v=T+(N[8]/(T-N[9]))
A=v**2+N[0]*v+N[1]
B=N[2]*v**2+N[3]*v+N[4]
C=N[5]*v**2+N[6]*v+N[7]
VP=0.25*(2*C/(-B+(B**2-4*A*C)**0.5))**4 #MPa
print VP
P = scipy.array([8, 9, 10, 11.7, 13.6, 15.3, 16, 19, 20])
#print x3
fig=plt.figure();
ax=fig.add_subplot(111)
X3 = scipy.transpose(X3)
ax.plot(X3,P,'*')
fig.canvas.draw()
plt.show()
#A(1)=T12 A(2)=T13 A(3)=T23
#A(4)=T21 A(5)=T31 A(6)=T32
#A(7)=ALPHA 12 A(8)=ALPHA 13 A(9)=ALPHA 23
A0=scipy.array([.2, .2, .2, .2, .2, .2, .2, .2,.2,.2])
X1=scipy.transpose(X1)
X2=scipy.transpose(X2)
X=scipy.array([X1,X2,X3])
#x=np.transpose(x)
Z=scipy.array([X,P])

def datafit_1(A,x1,x2,x3,P):
    K=(x1*scipy.exp(-A[7]*A[1])*A[1]+x2*scipy.exp(-A[8]*A[2])*A[2])/(x1*scipy.exp(-A[7]*A[1])+x2*scipy.exp(-A[8]*A[2])+x3);
    B=(x1*scipy.exp(-A[7]*A[4]))/(x1+x2*scipy.exp(-A[3]*A[6])+x3*scipy.exp(-A[4]*A[7]));
    C=A[4]-((x2*scipy.exp(-A[6]*A[3])*A[3]+x3*scipy.exp(-A[7]*A[4])*A[4])/(x1+x2*scipy.exp(-A[6]*A[3])+x3*scipy.exp(-A[7]*A[4])));
    D=(x2*scipy.exp(-A[8]*A[5]))/(x1*scipy.exp(-A[6]*A[0])+x2+x3*scipy.exp(-A[8]*A[5]));
    E=A[5]-((x1*scipy.exp(-A[6]*A[0])*A[0]+x3*scipy.exp(-A[8]*A[5])*A[5])/(x1*scipy.exp(-A[6]*A[0])+x2+x3*scipy.exp(-A[8]*A[5])));
    F=x3/(x1*scipy.exp(-A[7]*A[1])+x2*scipy.exp(-A[8]*A[2])+x3);
    G=(x1*scipy.exp(-A[7]*A[1])*A[1]+x2*scipy.exp(-A[8]*A[2])*A[2])/(x1*scipy.exp(-A[7]*A[1])+x2*scipy.exp(-A[8]*A[2])+x3);
    gama3=scipy.exp(K+B*C+D*E-F*G);
    y=VP*x3*gama3;
    return y


def myerror(A,X1,X2,X3,P):
    e = P - datafit_1(A,X1,X2,X3,P)
    return e

Ydata = []    
for i in range(len(w)):
     x1 = X1[i];x2 = X2[i]; x3 = X3[i]; p = P[i]  
     ans1=scipy.optimize.minimize(myerror,A0,args = (x1,x2,x3,p))
     ans=ans1.x
     ycal = datafit_1(ans, x1,x2,x3,p); Ydata.append(ycal)
     
#a,b,c,d,e,f,g,h,i=ans
ax=fig.add_subplot(111)
ax.plot(X[2],P)
ax.plot(X[2],Ydata,'b')    
ax.title.set_text('P Vs x3')
fig.canvas.draw()
plt.show()