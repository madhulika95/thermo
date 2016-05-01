# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
CE Lab Experiment No.15
Error estimation in f and RE calcuation of Static Mixer.
The least counts of the measuring equipments are
measuring cylinder(laminar)-5 ml=emc
measuring cylinder(turbulent)-10 ml=emc2
stopwatch-1 sec=esw
scale=0.00001 m
'''
import scipy
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

'''Import values from the excel file'''
data=pd.read_excel('13che1020.xlsx', 'c1', index_col=None, na_values=['NA'])
data9=pd.read_excel('13che1020.xlsx', 'c2', index_col=None, na_values=['NA'])
data8=pd.read_excel('13che1020.xlsx', 'c3', index_col=None, na_values=['NA'])
data7=pd.read_excel('13che1020.xlsx', 'c4', index_col=None, na_values=['NA'])

#Data
rho_mercury=13600 #kg/m^3
rho_water=1000 #kg/m^3
g=9.80665 #m/s^2
mu=0.00095 #Pa.s
d=0.0209 #m
emc=scipy.array([5.0,5.0,5.0,5.0,5.0]) #LC ml
emcb=scipy.array([10.0,10.0,10.0,10.0,10.0])#LC ml
emc1=scipy.array([5.0,5.0,5.0,5.0]) #LC ml
emcb1=scipy.array([10.0,10.0,10.0,10.0])#LC ml
esw=scipy.array([1.0,1.0,1.0,1.0,1.0]) #LC sec
esw1=scipy.array([1.0,1.0,1.0,1.0]) #LC sec

'''Without Static Mixer:Laminar Regime'''

#1D arrays
xt=data["Volume Collected(ml)"].values 
xt=xt.astype(np.float)
yt=data["Time(sec)"].values 
yt=yt.astype(np.float)


'''Error in the estimation of Flowrate:
Flow Rate= Volume Collected/time
error(flowrate)/flowrate=((error(volume)/volume)^2+(error(time)/time)^2)^0.5
'''
e1=(emc/xt)**2
e2=(esw/yt)**2
e3=(e1+e2)**0.5
fr_obtained=(xt/yt)

e_flowrate=(e3*fr_obtained) #this is the error in the measured flowrate in ml/s

'''Error in the estimation of velocity:'''
a1=(scipy.pi*0.25*d*d)
e4=scipy.array([0.00001,0.00001,0.00001,0.00001,0.00001])#error in vc=0.001cm=0.00001m 
e5=(a1*(((2*e4)/d))) # error in the measurement of area
fr=(fr_obtained/(1000000)) #coversion of ml/s to m^3/s
e_flowrate1=(e_flowrate/1000000) # error in flow rate
v_ob=(fr/a1) #m/s
e_velocity=v_ob*(((e_flowrate1/fr)**2+(e5/a1)**2)**0.5)# error in velocity

'''Error in Pressure'''
H=data["Delta H"].values #height observed (cm)
H1=0.01*H # conversion of cm to m
e6=scipy.array([0.001,0.001,0.001,0.001,0.001]) #m; error in measurement of height

p_ob=H1*487*9.80665 # Pa
e_pressure=(p_ob*(e6/H1))

'''Error in Friction Factor'''
l=scipy.array([2.9,2.9,2.9,2.9,2.9]) #m
e7=scipy.array([0.001,0.001,0.001,0.001,0.001])

f_ob=((p_ob*d)/(2*1000*l*v_ob*v_ob))

e_frictionfactor=f_ob*(((e7/l)**2+(2*e_velocity/v_ob)**2+(e_pressure/p_ob)**2+(e4/d)**2)**0.5)

f_obtainedplus=(f_ob+e_frictionfactor)
f_obtainedminus=(f_ob-e_frictionfactor)
f0=scipy.array([f_obtainedminus[0],f_ob[0],f_obtainedplus[0]])
f1=scipy.array([f_obtainedminus[1],f_ob[1],f_obtainedplus[1]])
f2=scipy.array([f_obtainedminus[2],f_ob[2],f_obtainedplus[2]])
f3=scipy.array([f_obtainedminus[3],f_ob[3],f_obtainedplus[3]])
f4=scipy.array([f_obtainedminus[4],f_ob[4],f_obtainedplus[4]])

'''Reynolds No Calculation'''
Re=data["Re"].values

Re0=([Re[0],Re[0],Re[0]])
Re1=([Re[1],Re[1],Re[1]])
Re2=([Re[2],Re[2],Re[2]])
Re3=([Re[3],Re[3],Re[3]])
Re4=([Re[4],Re[4],Re[4]])
 
'''Without Static Mixer:Turbulent Regime'''

#1D arrays
xt9=data9["Volume Collected(ml)"].values 
xt9=xt9.astype(np.float)
yt9=data9["Time(sec)"].values 
yt9=yt9.astype(np.float)

'''Error in the estimation of Flowrate:
Flow Rate= Volume Collected/time
error(flowrate)/flowrate=((error(volume)/volume)^2+(error(time)/time)^2)^0.5
'''
e19=(emcb/xt9)**2
e29=(esw/yt9)**2
e39=(e19+e29)**0.5
fr_obtained9=(xt9/yt9)

e_flowrate9=(e39*fr_obtained9) #error in the measured flowrate in ml/s

'''Error in the estimation of velocity:'''
a19=(scipy.pi*0.25*d*d)
e49=scipy.array([0.00001,0.00001,0.00001,0.00001,0.00001])#error in vc=0.001cm=0.00001m 
e59=(a19*(((2*e49)/d))) # error in area
fr9=(fr_obtained9/(1000000)) #coversion of ml/s to m^3/s
e_flowrate19=(e_flowrate9/1000000) # error in flow rate 
v_ob9=(fr9/a19) #m/s
e_velocity9=v_ob9*(((e_flowrate19/fr9)**2+(e59/a19)**2)**0.5)# error in velocity

'''Error in Pressure'''
H9=data9["Delta H"].values #height observed (cm)
H19=0.01*H9 # conversion of cm to m
e69=scipy.array([0.001,0.001,0.001,0.001,0.001]) #m; error in height


p_ob9=H19*487*9.80665 # Pa
e_pressure9=(p_ob9*(e69/H19))

'''Error in Friction Factor'''
l9=scipy.array([2.9,2.9,2.9,2.9,2.9]) #m
e79=scipy.array([0.001,0.001,0.001,0.001,0.001])

f_ob9=((p_ob9*d)/(2*1000*l9*v_ob9*v_ob9))

e_frictionfactor9=f_ob9*(((e79/l9)**2+(2*e_velocity9/v_ob9)**2+(e_pressure9/p_ob9)**2+(e49/d)**2)**0.5)

f_obtainedplus9=(f_ob9+e_frictionfactor9)
f_obtainedminus9=(f_ob9-e_frictionfactor9)
f09=scipy.array([f_obtainedminus9[0],f_ob9[0],f_obtainedplus9[0]])
f19=scipy.array([f_obtainedminus9[1],f_ob9[1],f_obtainedplus9[1]])
f29=scipy.array([f_obtainedminus9[2],f_ob9[2],f_obtainedplus9[2]])
f39=scipy.array([f_obtainedminus9[3],f_ob9[3],f_obtainedplus9[3]])
f49=scipy.array([f_obtainedminus9[4],f_ob9[4],f_obtainedplus9[4]])

'''Reynolds No Calculation'''
Re9=data9["Re"].values

Re09=([Re9[0],Re9[0],Re9[0]])
Re19=([Re9[1],Re9[1],Re9[1]])
Re29=([Re9[2],Re9[2],Re9[2]])
Re39=([Re9[3],Re9[3],Re9[3]])
Re49=([Re9[4],Re9[4],Re9[4]])

'''With Static Mixer:Laminar Regime'''

#1D arrays
xt8=data8["Volume Collected(ml)"].values 
xt8=xt8.astype(np.float)
yt8=data8["Time(sec)"].values 
yt8=yt8.astype(np.float)

'''Error in the estimation of Flowrate:
Flow Rate= Volume Collected/time
error(flowrate)/flowrate=((error(volume)/volume)^2+(error(time)/time)^2)^0.5
'''
e18=(emc1/xt8)**2
e28=(esw1/yt8)**2
e38=(e18+e28)**0.5
fr_obtained8=(xt8/yt8)

e_flowrate8=(e38*fr_obtained8) #error in the measured flowrate in ml/s

'''Error in the estimation of velocity:'''
a18=(scipy.pi*0.25*d*d)
e48=scipy.array([0.00001,0.00001,0.00001,0.00001])#error in vc=0.001cm=0.00001m 
e58=(a18*(((2*e48)/d))) # error in area
fr8=(fr_obtained8/(1000000)) #coversion of ml/s to m^3/s
e_flowrate18=(e_flowrate8/1000000) # error in flow rate
v_ob8=(fr8/a18) #m/s
e_velocity8 = v_ob8*(((e_flowrate18/fr8)**2+(e58/a18)**2)**0.5) # error in velocity

'''Error in Pressure'''
H8=data8["Delta H"].values #height observed (cm)
H18=0.01*H8 # conversion of cm to m
e68=scipy.array([0.001,0.001,0.001,0.001]) #m; error in measurement of height

p_ob8=H18*487*9.80665 # Pa
e_pressure8=(p_ob8*(e68/H18))

'''Error in Friction Factor'''
l8=scipy.array([2.9,2.9,2.9,2.9]) #m
e78=scipy.array([0.001,0.001,0.001,0.001])

f_ob8=((p_ob8*d)/(2*1000*l8*v_ob8*v_ob8))

e_frictionfactor8=f_ob8*(((e78/l8)**2+(2*e_velocity8/v_ob8)**2+(e_pressure8/p_ob8)**2+(e48/d)**2)**0.5)

f_obtainedplus8=(f_ob8+e_frictionfactor8)
f_obtainedminus8=(f_ob8-e_frictionfactor8)
f08=scipy.array([f_obtainedminus8[0],f_ob8[0],f_obtainedplus8[0]])
f18=scipy.array([f_obtainedminus8[1],f_ob8[1],f_obtainedplus8[1]])
f28=scipy.array([f_obtainedminus8[2],f_ob8[2],f_obtainedplus8[2]])
f38=scipy.array([f_obtainedminus8[3],f_ob8[3],f_obtainedplus8[3]])
f48=scipy.array([f_obtainedminus8[4],f_ob8[4],f_obtainedplus8[4]])

'''Reynolds No Calculation'''
Re8=data8["Re"].values

Re08=([Re8[0],Re8[0],Re8[0]])
Re18=([Re8[1],Re8[1],Re8[1]])
Re28=([Re8[2],Re8[2],Re8[2]])
Re38=([Re8[3],Re8[3],Re8[3]])


'''With Static Mixer:Turbulent Regime'''

#1D arrays
xt7=data7["Volume Collected(ml)"].values 
xt7=xt7.astype(np.float)
yt7=data7["Time(sec)"].values 
yt7=yt7.astype(np.float)

'''Error in the estimation of Flowrate:
Flow Rate= Volume Collected/time
error(flowrate)/flowrate=((error(volume)/volume)^2+(error(time)/time)^2)^0.5
'''
e17=(emcb1/xt7)**2
e27=(esw1/yt7)**2
e37=(e17+e27)**0.5
fr_obtained7=(xt7/yt7)

e_flowrate7=(e37*fr_obtained7) #error in the measured flowrate in ml/s

'''Error in the estimation of velocity:'''
a17=(scipy.pi*0.25*d*d)
e47=scipy.array([0.00001,0.00001,0.00001,0.00001])#error in vc=0.001cm=0.00001m 
e57=(a17*(((2*e47)/d))) # error in area
fr7=(fr_obtained7/(1000000)) #coversion of ml/s to m^3/s
e_flowrate17=(e_flowrate7/1000000) # error in flow rate
v_ob7=(fr7/a17) #m/s
e_velocity7 = v_ob7*(((e_flowrate17/fr7)**2+(e57/a17)**2)**0.5) # error in velocity


'''Error in Pressure'''
H7=data7["Delta H"].values #height observed (cm)
H17=0.01*H7 # conversion of cm to m
e67=scipy.array([0.001,0.001,0.001,0.001]) #m; error in measurement of height

p_ob7=H17*12600*9.80665 # Pa
e_pressure7=(p_ob7*(e67/H17))

'''Error in Friction Factor'''
l7=scipy.array([2.9,2.9,2.9,2.9]) #m
e77=scipy.array([0.001,0.001,0.001,0.001])

f_ob7=((p_ob7*d)/(2*1000*l7*v_ob7*v_ob7))

e_frictionfactor7=f_ob7*(((e77/l7)**2+(2*e_velocity7/v_ob7)**2+(e_pressure7/p_ob7)**2+(e47/d)**2)**0.5)

f_obtainedplus7=(f_ob7+e_frictionfactor7)
f_obtainedminus7=(f_ob7-e_frictionfactor7)
f07=scipy.array([f_obtainedminus7[0],f_ob7[0],f_obtainedplus7[0]])
f17=scipy.array([f_obtainedminus7[1],f_ob7[1],f_obtainedplus7[1]])
f27=scipy.array([f_obtainedminus7[2],f_ob7[2],f_obtainedplus7[2]])
f37=scipy.array([f_obtainedminus7[3],f_ob7[3],f_obtainedplus7[3]])
f47=scipy.array([f_obtainedminus7[4],f_ob7[4],f_obtainedplus7[4]])

'''Reynolds No Calculation'''
Re7=data7["Re"].values

Re07=([Re7[0],Re7[0],Re7[0]])
Re17=([Re7[1],Re7[1],Re7[1]])
Re27=([Re7[2],Re7[2],Re7[2]])
Re37=([Re7[3],Re7[3],Re7[3]])


'''a1=a1**0.5
a19=a19**0.5
a18=a18**0.25
a17=a17**0.25

#Plotting
fig=plt.figure()
fig.show
axy=fig.add_subplot(121)
axy.title.set_text('Without StaticMixer:f vs Re')
axy.plot(Re,f_ob,'x')
axy.plot(Re,f_obtainedplus)
axy.plot(Re,f_obtainedminus)
axy.plot(Re9,f_ob9,'x')
axy.plot(Re9,f_obtainedplus9)
axy.plot(Re9,f_obtainedminus9)


axy2=fig.add_subplot(122)
axy2.title.set_text('With StaticMixer:f vs Re')
axy2.plot(Re8,f_ob8,'x')
axy2.plot(Re7,f_ob7,'x')
axy2.plot(Re8,f_obtainedplus8)
axy2.plot(Re8,f_obtainedminus8)
axy2.plot(Re7,f_obtainedplus7)
axy2.plot(Re7,f_obtainedminus7)

#curve fitting
f=[f_ob,f_ob9,f_ob8,f_ob7]
rey=[Re,Re9,Re8,Re7]
e=[e_frictionfactor,e_frictionfactor9,e_frictionfactor8,e_frictionfactor7]
print e

def func(x,a,b):
    tt=a*(x**b)
    return tt
p=curve_fit(func,f_ob,Re)
print p

res1=(f_ob-a1)/e_frictionfactor
res2=(f_ob9-a19)/e_frictionfactor9
res3=(f_ob8-a18)/e_frictionfactor8
res4=(f_ob7-a17)/e_frictionfactor7

print res1

print res2

print res3

print res4
#res=(f-fbar)/e'''
'''1)For W/O-Static Mixer-Laminar'''

def func(x,a,b):
    tt=a*(x**b)
    return tt
    
p,p1=scipy.optimize.curve_fit(func,Re,f_ob)
f_bestfit=p[0]*(Re**p[1])
sigma=np.std(f_ob)
f_upper=(p[0]*(Re**p[1]))+sigma
f_under=(p[0]*(Re**p[1]))-sigma
f_upper1=f_upper+sigma
f_under1=f_under-sigma
f_upper2=f_upper1+sigma
f_under2=f_under1-sigma


'''1)For W/O-Static Mixer-Turbulent'''
p9,p19=scipy.optimize.curve_fit(func,Re9,f_ob9)
f_bestfit9=p9[0]*(Re9**p9[1])
sigma9=np.std(f_ob9)
f_upper9=(p9[0]*(Re9**p9[1]))+sigma9
f_under9=(p9[0]*(Re9**p9[1]))-sigma9
f_upper19=f_upper9+sigma9
f_under19=f_under9-sigma9
f_upper29=f_upper19+sigma9
f_under29=f_under19-sigma9

'''1)For W-Static Mixer-Laminar'''
p8,p18=scipy.optimize.curve_fit(func,Re8,f_ob8)
f_bestfit8=p8[0]*(Re8**p8[1])
sigma8=np.std(f_ob8)
f_upper8=(p8[0]*(Re8**p8[1]))+sigma8
f_under8=(p8[0]*(Re8**p8[1]))-sigma8
f_upper18=f_upper8+sigma8
f_under18=f_under8-sigma8
f_upper28=f_upper18+sigma8
f_under28=f_under18-sigma8

'''1)For W-Static Mixer-Turbulent'''
p7,p17=scipy.optimize.curve_fit(func,Re7,f_ob7)
f_bestfit7=p7[0]*(Re7**p7[1])
sigma7=np.std(f_ob7)
f_upper7=(p7[0]*(Re7**p7[1]))+sigma7
f_under7=(p7[0]*(Re7**p7[1]))-sigma7
f_upper17=f_upper7+sigma7
f_under17=f_under7-sigma7
f_upper27=f_upper17+sigma7
f_under27=f_under17-sigma7


'''To Plot the Predicted values and the actual experimental values'''

fig3=plt.figure()
fig3.show
axy3=fig3.add_subplot(111)
axy3.title.set_text('With Static Mixer: f vs Re with Experimental and Fitted Values')
axy3.set_xlabel('Re')
axy3.set_ylabel('f')

axy3.plot(Re8,f_ob8,'bo')
axy3.plot(Re8,f_bestfit8,'r')
axy3.plot(Re8,f_upper8,'y--')
axy3.plot(Re8,f_under8,'y--')


axy3.plot(Re7,f_ob7,'bo')
axy3.plot(Re7,f_bestfit7,'r')
axy3.plot(Re7,f_upper7,'y--')
axy3.plot(Re7,f_under7,'y--')

fig2=plt.figure()
fig2.show
axy2=fig2.add_subplot(111)
axy2.title.set_text('Without Static Mixer: f vs Re with Experimental and Fitted Values')
axy2.set_xlabel('Re')
axy2.set_ylabel('f')

axy2.plot(Re,f_ob,'bo')
axy2.plot(Re,f_bestfit,'r')
axy2.plot(Re,f_upper,'y--')
axy2.plot(Re,f_under,'y--')


axy2.plot(Re9,f_ob9,'bo')
axy2.plot(Re9,f_bestfit9,'r')
axy2.plot(Re9,f_upper29,'y--')
axy2.plot(Re9,f_under29,'y--')


'''To Plot the results along with the experimental errors'''
fig1=plt.figure()
fig1.show
axy1=fig1.add_subplot(111)
axy1.title.set_text('With Static Mixer: f vs Re with Experimental Errors')
axy1.set_xlabel('Re')
axy1.set_ylabel('f')

axy1.plot(Re8,f_ob8,'go')
axy1.plot(Re08,f08,'r')
axy1.plot(Re18,f18,'r')
axy1.plot(Re28,f28,'r')
axy1.plot(Re38,f38,'r')


axy1.plot(Re7,f_ob7,'bo')
axy1.plot(Re07,f07,'r')
axy1.plot(Re17,f17,'r')
axy1.plot(Re27,f27,'r')
axy1.plot(Re37,f37,'r')


'''To Plot the results along with the experimental errors'''

fig=plt.figure()
fig.show
axy=fig.add_subplot(111)
axy.title.set_text('W/O Static Mixer: f vs Re with Experimental Errors')
axy.set_xlabel('Re')
axy.set_ylabel('f')

axy.plot(Re,f_ob,'go')
axy.plot(Re0,f0,'r')
axy.plot(Re1,f1,'r')
axy.plot(Re2,f2,'r')
axy.plot(Re3,f3,'r')
axy.plot(Re4,f4,'r')

axy.plot(Re9,f_ob9,'bo')
axy.plot(Re09,f09,'r')
axy.plot(Re19,f19,'r')
axy.plot(Re29,f29,'r')
axy.plot(Re39,f39,'r')
axy.plot(Re49,f49,'r')

'''Final all values'''
f_approximated=([f_bestfit[0],f_bestfit[1],f_bestfit[2],f_bestfit[3],f_bestfit[4],f_bestfit9[0],f_bestfit9[1],f_bestfit9[2],f_bestfit9[3],f_bestfit9[4],f_bestfit8[0],f_bestfit8[1],f_bestfit8[2],f_bestfit8[3],f_bestfit7[0],f_bestfit7[1],f_bestfit7[2],f_bestfit7[3]])
e_ff=([e_frictionfactor[0],e_frictionfactor[1],e_frictionfactor[2],e_frictionfactor[3],e_frictionfactor[4],e_frictionfactor9[0],e_frictionfactor9[1],e_frictionfactor9[2],e_frictionfactor9[3],e_frictionfactor9[4],e_frictionfactor8[0],e_frictionfactor8[1],e_frictionfactor8[2],e_frictionfactor8[3],e_frictionfactor7[0],e_frictionfactor7[1],e_frictionfactor7[2],e_frictionfactor7[3]])


'''Adding data to our data frame'''
alldata=pd.read_excel('13che1020.xlsx', 'All Data', index_col=None, na_values=['NA'])
alldata["Error in f"]=e_ff
alldata["f expression"]=f_approximated

alldata.to_excel('Output.xlxs','Sheet1')
