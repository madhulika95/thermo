
from scipy.integrate import odeint
from scipy import linspace
from scipy import array
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
kla=0.007
 #1/s Mass transfer Coefficient(Perry's Handbook)
A=1
pT=1#"""atm"""
Hc=.034## (in M/atm at T=298.15K)
de=([0.523, 0.554])
MDc=.523/40#"M"-# kg/ m^3 http://www.peacesoftware.de/einigewerte/calc_co2.php5,http://www.peacesoftware.de/einigewerte/calc_methan.php5
Hm=0014## (in M/atm at T=298.15K)
a=350 # m^2/m^3
kg=.00002 #gmol/m^2-Pa-s Mass transfer Coefficient
MDm=.554/40#"M"
kGa=7*10**(-7) # gmol/L-Pa-s
Pwsat=0.03125#"atm"
def derivate(y,t):
    yc=y[0]/(y[0]+y[1]+y[2])
    ym=y[1]/(y[0]+y[1]+y[2])
    yw=y[2]/(y[0]+y[1]+y[2])
    xc=y[3]/(y[3]+y[4]+y[5])
    xm=y[4]/(y[3]+y[4]+y[5])
    #xw=y[5]/(y[3]+y[4]+y[5])
    dGc=-kla*A*(yc*pT*Hc-MDc*xc)
    dLc=-kla*A*(yc*pT*Hc-MDc*xc)
    dGm=-kla*A*(ym*pT*Hm-MDm*xm)
    dLm=-kla*A*(ym*pT*Hm-MDm*xm)
    dGw=kGa*A*(pT*yw-Pwsat)
    dLw=kGa*A*(pT*yw-Pwsat)
    return array([dGc,dLc,dGm,dLm,dGw,dLw])
a=array ([10,10,80])
t=linspace(0.0,10.0,100)
#yinitial=([50,50,0,a1,a2,a3])
#y=odeint(derivate,yinitial,t)
#print y[9,5]
def error(a):
    #t=linspace(0.0,10.0,100)
    yinitial=([50,a[0],50,a[1],0,a[2]])
    y=odeint(derivate,yinitial,t)
    return array([y[99,5]-100,y[99,3],y[99,1]])
ans=fsolve(error,a)
print ans
yinitial=([50,ans[0],50,ans[1],0,ans[2]])
y=odeint(derivate,yinitial,t)
#print y[99,:]
print 'Gas cmponent,Inlet Composition'
print 'Co2 -50'
print 'CH4 -50'
print 'H2O -0'
print 'Gas cmponent,Outlet Composition'
print 'Co2 -',y[99,0]
print 'CH4 -',y[99,2]
print 'H2O -',y[99,4]
print 'Liquid cmponent,Oulet Composition'
print 'Co2 -',ans[0]
print 'CH4 -',ans[1]
print 'H2O -',ans[2]
print 'liquid cmponent,Inlet Composition'
print 'Co2 -',y[99,1]
print 'CH4 -',y[99,3]
print 'H2O -',y[99,5]


        #  Plotting 

# Gc Vs Height
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,0],'g')#Gc
ax.title.set_text('Gc Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Gc')
plt.show()
# Gm Vs Height
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,2],'b')#Gm
ax.title.set_text('Gm Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Gm')
plt.show()
# Gw Vs Height    
fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,4],'r')#Gw
ax.title.set_text('Gw Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Gw')
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,1],'g')#Lc
ax.title.set_text('Lc Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Lc')
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,3],'b')#Lm
ax.title.set_text('Lm Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Lm')
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111)
plt.plot(t,y[:,5],'r')#Lw
ax.title.set_text('Lw Vs height')
ax.xaxis.label.set_text('height')
ax.yaxis.label.set_text('Lw')
plt.show()
error=200-(y[99,0]+y[99,1]+y[99,2]+y[99,3]+y[99,4]+y[99,5])
#print error