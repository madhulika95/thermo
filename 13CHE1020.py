# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:06:23 2016

@author: Madhu
"""

class contactor:
    def Co2absorbtion(self):
        import numpy as np
        from scipy.integrate import odeint
        import math
        #Henry's coefficient from Compilation of Henry’s Law Constants for Inorganic
        #and Organic Species of Potential Importance in Environmental Chemistry
        #http://www.henrys-law.org/henry-3.0.pdf
        Hco2=0.034 #listed henry's constant for co2 mol/lit.atm
        Hch4=0.014 # listed henry's constant for ch4 mol/lit.atm
        kl=0.00088 # liquid mass transfer coefficient (m/s) 
        #Reference-Perry's Handbook pg.23.43
        kg=0.0001   # gas mass transfer coefficient (m/s) 
        #Reference-Perry's Handbook pg.23.43
        a=200 #specific interfacial area (1/m)
        T=298#K
        rho=55.5555555 #molar density of water (mol/l) 
        #assuming it doesnt change through the operation
        P=1 #operating pressure (atm)
        A=1.0 #cross sectional area (m^2)-assumed
        h=20.0 #height of column(m)-assumed
        def pressure(T): 
            A=18.3036
            B=3816.44
            C=-46.13
            pressure= math.exp(A-(B/(T+C)))#Antoine equation for VP of water
            return pressure
        Psat= pressure(T)/760 #atm 
        
        #input conditions in gas phase(mol/s)
        Gco2in=50 
        Gch4in=50
        Gh2oin=0 

        #initial assumed conditionss in liquid phase outlet(mol/s)
        Lco2assumed=0 
        Lch4assumed=0 
        Lh2oassumed=100 
    
        #series of differential equations solver from Python man book method
        def f(molar_flow_rates,x,param):
            Gco2,Gch4,Gh2o,Lco2,Lch4,Lh2o=molar_flow_rates
            kl,kg,a,Hco2,Hch4,Psat,P,A,rho=param
            yco2=(Gco2/Gco2+Gch4+Gh2o)
            xco2=(Lco2/(Lco2+Lch4+Lh2o))
            ych4=(Gch4/Gco2+Gch4+Gh2o)
            xch4=(Lch4/(Lco2+Lch4+Lh2o))
            yh2o=(Gh2o/Gco2+Gch4+Gh2o)
            VA=-kl*a*A*((Hco2*P*yco2)-(rho*xco2))
            VB=-kl*a*A*((Hch4*P*ych4)-(rho*xch4))
            VC=kg*a*A*((P*yh2o)-Psat)
            VD=kl*a*A*((Hco2*P*yco2)-(rho*xco2))
            VE=kl*a*A*((Hch4*P*ych4)-(rho*xch4))
            VF=-kg*a*A*((P*yh2o)-Psat)
            derivs=[VA,VB,VC,VD,VE,VF]
            return derivs
        
        xstop=h
        xinc=0.02

        x=np.arange(0.,xstop,xinc)
    

        param=[kl,kg,a,Hco2,Hch4,Psat,P,A,rho]
        
        molar_flow_rates0=[Gco2in,Gch4in,Gh2oin,Lco2assumed,Lch4assumed,Lh2oassumed]
        #now the initial value is used to get the final solution
        #where the initial value acts as a guess value
        psoln=odeint(f,molar_flow_rates0,x,args=(param,))
        print"initial solution :",psoln[999]
        
        print"Final Values for liquid phase(mol/s):"
        print"water in",Lh2oassumed
        print"ch4 in",Lch4assumed
        print"co2 in",Lco2assumed
        print"water out",psoln[999,5]
        print"ch4 out",psoln[999,4]
        print"co2 out",psoln[999,3]
        
        print"Final Values for gas phase(mol/s):"
        print"water in",Gh2oin
        print"ch4 in",Gch4in
        print"co2 in ",Gco2in
        print"water out",psoln[999,2]
        print"ch4 out",psoln[999,1]
        print"c02 out",psoln[999,0]
        
        eh2o=abs(-psoln[999,5]+Lh2oassumed-psoln[999,2])*0.01
        ech4=abs(Gch4in-psoln[999,4]-psoln[999,1])*0.01
        eco2=abs(Gco2in-psoln[999,3]-psoln[999,0])*0.01
        
        print"error in mass balance of ch4(mol/s):",ech4
        print"error in mass balance of co2(mol/s):",eco2
        print"error in mass balance of water(mol/s):",eh2o
        
        raw_input("press enter to exit")
        
        