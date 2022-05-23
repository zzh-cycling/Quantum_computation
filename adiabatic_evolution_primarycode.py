import matplotlib.pyplot as plt
import numpy as np
import random

# def adiabaticaappro(): #一次失败的尝试，知道因为啥失败吗，我真替你感到悲哀。
#     t=np.linspace(0,10,500)
#     T=10
#     epsilon=1
#     delta_t=-1+2*t/T
#
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

epsilon=0.1
paulix=np.array([[0,1],[1,0]])
pauliz=np.array([[1,0],[0,-1]])
origin=np.array([1+0j,0+0j]).reshape(-1,1)
def f(phi,deltat,t,epsilon):
    ls0=[]
    ls1=[]
    lst=[]
    T=t*deltat
    for i in range(t):
        influence=random.uniform(-0.5,+0.5)
        H=epsilon*paulix+(-2+4*i*deltat/T+influence)*pauliz
        phi=phi-1j*deltat*np.dot(H,phi)
        modle=np.sqrt(abs(phi[0])**2+abs(phi[1])**2)

        ls0.append((abs((phi[0]))/modle)**2)
        ls1.append((abs((phi[1]))/modle)**2)
        lst.append((i+1)*deltat)
    return ls0,ls1,lst
prob0,prob1,time=f(origin,1,500,epsilon)
prob0,prob1,time=np.array(prob0),np.array(prob1),np.array(time)
#totalprob=prob0+prob1
pc1=plt.plot(time,prob0,'r-',label='0 probability')
pc2=plt.plot(time,prob1,'k-',label='1 probability')
#pc3=plt.plot(time,totalprob,'b-',label='total probility')
plt.xlabel('time')
plt.ylabel('probability')
plt.title('probability evolves over time image with epsilon=0.1')
plt.legend()
plt.ylim(0,+1)
plt.savefig('./simple_adiabatic_evolution')
plt.show()