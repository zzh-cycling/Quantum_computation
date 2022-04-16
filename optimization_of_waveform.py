import numpy as np
import scipy.optimize as so
from random import random

so.minimize(fun, x0, args=(), method='Nelder-Mead', bounds=None, tol=None, callback=None, options={'func': None, 'maxiter': None, 'maxfev': None, 'disp': False, 'return_all': False, 'initial_simplex': None, 'xatol': 0.0001, 'fatol': 0.0001, 'adaptive': False})

omiga_0=2
n_c=4
Omiga_t=0
T=10
t=np.linspace(0,T,100)

def fun(x=[])
for i in range(n_c):
    r_k=random()
    omiga_k=2*np.pi*(i+r_k)
    Omiga_t += omiga_0 *(+A_k*np.cos(omiga_k*t)+B_k*np.sin(omiga_k*t))

#可以手解四个偏微分方程，\rho\dagger=\rho, Tr(\rho)=1 五个条件，
 #\partial \rho=\gamma [sigma_-*\rho*sigma_+-1/2*(sigma_+*sigma_-*\rho+\rho*sigma_+*sigma_-)]

# CRAB such as Nelder-meal BFGS  algorithm GRAPE 梯度下降算法 deep learning 里的正向传播
#有些东西自己来写不调包，能够发现，算出更多的东西，但是Nelder-meal很古老哩。
#H=Delta(t)*sigmaz()+0.1sigmax()

#那么调用mesolve函数时，[expect]参数需要设置为空，否则出错。如果需要获得算符的期望值，那么可以调用expect函数，输入参数为算符和量子态。
import qutip as qt
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize

rho_0=qt.Qobj([[1,0],
               [0,0]])

a=qt.Qobj([[1,0],
           [0,0]])


Nc=4

wc_max=8

w_per_Nc=wc_max/Nc

#total time
T=10

#initial guess, simplex
coeff=[0]*2*Nc
r=coeff.copy()
for each in range(0,2*Nc):
    r[each]=random.uniform(-0.5*np.pi/T,0.5*np.pi/T)

#Hamiltonian
#time independent part
H_0=qt.sigmax()

#time dependent part
H_1=0.2*qt.sigmaz()

def Omega0(t):
    n=3
    return (-9/((-T/2)**n))*(t-T/2)**n

def g(t,args):
    i,outcome_f=1,1
    w=list(range(1,Nc+1))
    while i<=Nc:
        outcome_f+=(args[str(i-1)]*np.cos((w[i-1]*(w_per_Nc)+r[i-1])*t)+
                    args[str(Nc+i-1)]*np.sin((w[i-1]*(w_per_Nc)+
                         r[Nc+i-1])*t))*np.sin((np.pi/T)*t)
        i+=1
    return outcome_f*Omega0(t)

def evolution(para):
    global result0
    global args0
    key1=list(range(0,2*Nc))
    for each in range(0,len(key1)):
        key1[each]=str(key1[each])
    args0=dict(zip(key1,para))
    t=np.linspace(0,T,1001)
    H=[H_0,[H_1,g]]
    result0=qt.mesolve(H,rho_0,t,[],[a],args=args0)
    infidelity=result0.expect[0][-1]
    return infidelity

result=minimize(evolution,coeff,method="nelder-mead",
                options={'xtol':1e-4,'ftol':1e-3,'disp': True})

t=np.linspace(0,T,1001)

plt.plot(t,result0.expect[0])
plt.xlabel('time')
plt.ylabel('infidelity')
plt.show()

plt.plot(t,g(t,args0))
plt.xlabel('time')
plt.ylabel('g(t)')
plt.show()