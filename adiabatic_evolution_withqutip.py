from qutip import *
import numpy as np
import matplotlib.pyplot as plt
import math

e = basis(3, 0)
g = basis(3, 1)
r = basis(3, 2)
n_e = e * e.dag()
n_g = g * g.dag()
n_r = r * r.dag()
omiga_e = 0 * 2 * np.pi
omiga_g = 0.4 * 2 * np.pi
omiga_r = 1 * 2 * np.pi
Delta = 0.1* 2*np.pi
nu1 = omiga_e - omiga_g - Delta
nu2 = omiga_e - omiga_r - Delta
O_1 = 10* 2*np.pi
O_2 = 10* 2*np.pi
theta = np.arctan(O_1/O_2)
Delta_t = 1.1
T=4

H0 = omiga_e * n_e + omiga_g * n_g + omiga_r * n_r
def Gas_1(t):
    return np.exp(-(t-Delta_t)**2/T**2)
def Gas_2(t):
    return np.exp(-(t+Delta_t)**2/T**2)
def Omega_1(t,args):
    return Gas_1(t)*O_1/2.0*np.exp(-1j*nu1*t)
def Omega_1_dag(t,args):
    return Gas_1(t)*O_1/2.0*np.exp(1j*nu1*t)
def Omega_2(t,args):
    return Gas_2(t)* O_2/2.0*np.exp(-1j*nu2*t)
def Omega_2_dag(t,args):
    return Gas_2(t)*O_2/2.0*np.exp(1j*nu2*t)
H=[H0, [e * g.dag(), Omega_1], [g * e.dag(), Omega_1_dag], [e * r.dag(), Omega_2], [r * e.dag(), Omega_2_dag]]
psi0 = g
t=np.linspace(-20,20,100)
L_k1= np.sqrt(2*np.pi*6) * e * g.dag()
L_k2=math.sqrt(2*math.pi*0.12)*(e * e.dag() - r * r.dag())

plt.subplot(2,2,1)
result = mesolve(H, psi0, t, [], [n_e, n_g, n_r])
plt.title('without dissipation')
plt.ylabel('Population')
plt.xticks([])
plt.plot(t,result.expect[0],label='N_a',linewidth=4.0)
plt.plot(t,result.expect[1],label='N_b',linewidth=4.0)
plt.plot(t,result.expect[2],label='N_c',linewidth=4.0)
plt.legend(fontsize='large')

plt.subplot(2,2,2)
result = mesolve(H, psi0, t, [L_k1], [n_e, n_g, n_r])
plt.title('L_k1 dissipation')
plt.xticks([])
plt.plot(t,result.expect[0],label='N_a',linewidth=4.0)
plt.plot(t,result.expect[1],label='N_b',linewidth=4.0)
plt.plot(t,result.expect[2],label='N_c',linewidth=4.0)

plt.subplot(2,2,3)
result = mesolve(H, psi0, t, [L_k2], [n_e, n_g, n_r])
plt.title('L_k2 dissipation')
plt.xlabel('Time')
plt.ylabel('Population')
plt.plot(t,result.expect[0],label='N_a',linewidth=4.0)
plt.plot(t,result.expect[1],label='N_b',linewidth=4.0)
plt.plot(t,result.expect[2],label='N_c',linewidth=4.0)


plt.subplot(2,2,4)
result = mesolve(H, psi0, t, [L_k1,L_k2], [n_e, n_g, n_r])
plt.title('L_k1 L_k2 dissipation')
plt.xlabel('Time')
plt.plot(t,result.expect[0],label='N_a',linewidth=4.0)
plt.plot(t,result.expect[1],label='N_b',linewidth=4.0)
plt.plot(t,result.expect[2],label='N_c',linewidth=4.0)

plt.suptitle('STIRAP Population Evolution with and without dissipation')
plt.savefig('./STIRAP Population Evolution with and without dissipation.png')
plt.show()