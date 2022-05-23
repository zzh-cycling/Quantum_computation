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