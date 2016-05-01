import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
b=c=1
def g(y,x):
    y=np.exp(x)/np.tan(x)
    return y
x=np.linspace(0,0.02,100)
init=0
sol=odeint(g,init,x)
#print sol
plt.plot(x,sol[:,0])
plt.show()
