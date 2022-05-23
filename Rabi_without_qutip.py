import numpy as np
import matplotlib.pyplot as plt

# class evolution_of_state():
#    def __init__(self):

# def probabilty_of_psi_1_and_psi_0(): #一次失败的尝试，知道因为啥失败吗，我真替你感到悲哀。
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

omega_1 = 2*np.pi*1 #Rabi frequency of the driving field
Delta = 2*np.pi*0 #detuning of the |g>-|e> transition

sigmax=np.array([[0,1],[1,0]])
sigamz=np.array([[1,0],[0,-1]])
Hamiltionian=(omega_1*sigmax-Delta*sigamz)/2

e=np.array([1,0]) #直接写e=[1,0]也一样
g=[0,1]

psi_0=e.reshape((-1,1))
P_e=[]
P_g=[]

times=np.linspace(0,5,100)
eigenvalues, eigenvectors = np.linalg.eig(Hamiltionian) #生成哈密顿量的本征值和本征矢
inv=np.linalg.inv(eigenvectors)


for i in times: #Noted: A*B 直接写 A*B是不对的，是向量对应元素相乘，比如[[1,2],[3,4]]*[[1,2],[3,4]]=[[1,4],[9,16]],须np.dot(A,B)，是矩阵乘法。

    evolve = np.diag(np.diag(np.exp(-1j * np.diag(eigenvalues)*i))) #演化算符
    # 将哈密顿量进行谱分解后本征值排列成的矩阵应该对角化的，演化算符也应该是对角化的，这里最后要取一下对角元.
    psi_0= np.dot(np.dot(np.dot(eigenvectors , evolve) , inv), psi_0)
    P_e.append(abs(psi_0[0] ** 2))
    P_g.append(abs(psi_0[1] ** 2))


plt.xlabel("time")
plt.ylabel("probability")
plt.plot(times,P_e,label='P_e')
#plt.plot(times, P_g,label='P_g')
plt.legend()
plt.show()