import scipy.optimize
def func(x):
    f1=x[0]+.5*(x[0]-x[1])**3-1
    f2=0.5*(x[1]-x[0])**3+x[1]
    return [f1,f2]
x0=[0,0]
ans=scipy.optimize.fsolve(func,x0)
print ans

    