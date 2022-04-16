
omiga_0, omiga, omiga_1 = map(float, input().split())
delta = omiga_0 - omiga
Delta = np.sqrt(delta**2 + omiga_1**2)
#H = -omiga_0* qp.sigmaz()+omiga_1/2*np.array([[0,np.exp(1j*omiga*times)],[np.exp(-1j*omiga*times),0]],dtype=object)
#H=-delta/2*qp.sigmaz()+omiga_1/2*qp.sigmax()
# delta_t=4*times/T-2
# epsilon=1
#H=epsilon*qp.sigmax()+delta_t*qp.sigmaz()

import numpy as np
import matplotlib.pyplot as plt
import qutip as qp


times = np.linspace(0.0, 10.0, 500)

T=10

psi0 = qp.basis(3, 0)
psi1=qp.basis(3,1)
psi2=qp.basis(3,2)

Omiga_0=25*2*np.pi#MHz
delta_t=0.4 #\mius
sigma=0.36 #/mius
Omiga_475=Omiga_0*np.exp(-(times-delta_t/2-2)**2/(2*sigma**2))
Omiga_795=Omiga_0*np.exp(-(times+delta_t/2-2)**2/(2*sigma**2))

#epsilon=1
#H=[epsilon*qp.sigmax(),Omiga_475*qp.sigmaz()]
H_0=0*qp.sigmaz()
H_d=[[0,Omiga_795/2,0],[Omiga_795/2,0,Omiga_475/2],[0,0,Omiga_475/2]]
H=[H_0,H_d]

result=qp.mesolve(H,psi0,times,[],[qp.sigmaz(), qp.sigmay()])
state0 = psi0 * psi0.dag() # 基态的Population
state1 = psi1 * psi1.dag() # 第一激发态的 Population
state2 = psi2 * psi2.dag() # 泄露能级的概率

# 求解演化过程中每一刻的可观测变量值，记录在数组 result 中
result0 = qp.expect(state0, result.states)
result1 = qp.expect(state1, result.states)
result2 = qp.expect(state2, result.states)

# 使用Matplotlib绘图
plt.plot(times,result0,label = 'Ground')
plt.plot(times,result1,label = 'Excited')
plt.plot(times,result2,label = 'Leakage')
plt.title('Population Evolution')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()
# plt.xlabel("time")
# plt.ylabel("probability")
# plt.xticks(np.linspace(0,10,10,endpoint=True))
# plt.plot(times,result.expect[0],linewidth=0.4,linestyle='-',color="b",label='P_0')
# plt.plot(times, result.expect[1], linewidth=0.4, linestyle='-', color="r",label='P_1')
# plt.legend()
# plt.show()




#class evolution_of_state():
#    def __init__(self):

# def probabilty_of_psi_1_and_psi_0():
#     t=np.linspace(0,10,500)
#     omiga_0, omiga, omiga_1 = map(float, input().split())
#     delta = omiga_0 - omiga
#     Delta = np.sqrt(delta**2 + omiga_1**2)
#
#     psi_0=np.exp(1j*omiga*t/2)*(np.cos(Delta*t/2)+1j*delta/Delta*np.sin(Delta*t/2))
#     psi_1=-1j*np.exp(-1j*omiga/2)*omiga_1/Delta*np.sin(Delta*t/2)
#     P_0=[]
#     P_1=[]
#
#     for i in range(len(psi_1)):
#         module=np.sqrt(abs(psi_0[i])**2+(abs(psi_1[i])**2))
#         P_0.append((abs(psi_0[i])/module)**2)
#         P_1.append((abs(psi_1[i])/module)**2)
#
#     # P_0 = [i.conj()*i for i,j in psi_0,psi_1 ]
#     # P_1 = np.sin(Delta*t/2)**2*omiga_1*2/Delta**2
#     # P_0=P_0/np.linalg.norm(P_0)
#     # P_1= P_1 / np.linalg.norm(P_1)
#     # for i in range(len(psi_1)):
#     #     module=np.sqrt((psi_0[i].conj()*psi_0[i])**2+(psi_1[i].conj()*psi_1[i])**2).real
#     #     P_0.append(psi_0[i].conj()*psi_0[i].real/module)
#     #     P_1.append(psi_1[i].conj()*psi_1[i].real/module)
#
#
#     plt.xlabel("time")
#     plt.ylabel("probability")
#     plt.xticks(np.linspace(0,10,10,endpoint=True))
#     plt.plot(t,P_0,linewidth=0.4,linestyle='-',color="b",label='P_0')
#     plt.plot(t, P_1, linewidth=0.4, linestyle='-', color="r",label='P_1')
#     plt.legend()
#     plt.show()
#
#
# probabilty_of_psi_1_and_psi_0()

# def adiabaticaappro():
#     t=np.linspace(0,10,500)
#     T=10
#     epsilon=1
#     delta_t=-1+2*t/T

#     paulix = np.array([[0, 1], [1, 0]])
#     pauliz = np.array([[1, 0], [0, -1]])
#     hamiltionian=delta_t*pauliz+epsilon*paulix
#     initial_state=np.array([1+0j,0+0j]).T
#     hamiltionian_eigenvalues,hamiltionian_eigenvectors=np.linalg.eig(hamiltionian)
#     state=hamiltionian_eigenvectors.T.conj()*np.diag(np.exp(-1j*hamiltionian_eigenvalues*t))*hamiltionian_eigenvectors*initial_state
#     P_0 = []
#     P_1 = []
#
#     for i in range(len(state[0])):
#         module = np.sqrt(abs(state[i]) ** 2 + (abs(state[i]) ** 2))
#         P_0.append((abs(state[i]) / module) ** 2)
#         P_1.append((abs(state[i]) / module) ** 2)
#
#
#
#     plt.plot(t, P_0, 'r-', label='0 probability')
#     plt.plot(t, P_1, 'k-', label='1 probability')
#     plt.xlabel('time')
#     plt.ylabel('probability')
#     plt.title('probability evolves over time image')
#     plt.legend()
#     plt.ylim(0, +1)
#     plt.show()
#
# adiabaticaappro()


# import cmath
# import random
# epsilon=float(input())
# paulix=np.array([[0,1],[1,0]])
# pauliz=np.array([[1,0],[0,-1]])
# origin=np.array([1+0j,0+0j]).reshape(-1,1)
# def f(phi,deltat,t,epsilon):
#     ls0=[]
#     ls1=[]
#     lst=[]
#     T=t*deltat
#     for i in range(t):
#         influence=random.uniform(-0.5,+0.55)
#         H=epsilon*paulix+(-2+4*i*deltat/T+influence)*pauliz
#         phi=phi-1j*deltat*np.dot(H,phi)
#         modle=np.sqrt(abs(phi[0])**2+abs(phi[1])**2)
#
#         ls0.append((abs((phi[0]))/modle)**2)
#         ls1.append((abs((phi[1]))/modle)**2)
#         lst.append((i+1)*deltat)
#     return ls0,ls1,lst
# prob0,prob1,time=f(origin,1,500,epsilon)
# prob0,prob1,time=np.array(prob0),np.array(prob1),np.array(time)
# #totalprob=prob0+prob1
# pc1=plt.plot(time,prob0,'r-',label='0 probability')
# pc2=plt.plot(time,prob1,'k-',label='1 probability')
# #pc3=plt.plot(time,totalprob,'b-',label='total probility')
# plt.xlabel('time')
# plt.ylabel('probability')
# plt.title('probability evolves over time image')
# plt.legend()
# plt.ylim(0,+1)
# plt.show()

