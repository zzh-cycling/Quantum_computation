from qutip import *
import numpy as np
import matplotlib.pyplot as plt
#对于sigma_-，选 |1>态 和 |+> 分别计算；对于sigma_z，选 |+> 即可,都令H=0。
a=basis(2,1)
b=basis(2,0)

plus=1/np.sqrt(2)*(a+b)
sigmaminus=1/2*(sigmax()+1j*sigmay())
H=Qobj([[0,0],[0,0]])
t=np.linspace(0,1,100)

result=mesolve(H,plus,t,[sigmaz()],[])
# sphere=qutip.Bloch()
# sphere.add_states(result.states)
# sphere.show()

output=np.array(result.states)
for i in range(len(output)):
    pnts.append(output[i][1])

trace_of_dm=[]
for i in output:  #calculate the trace of density matrix, finding it is mixed states
    trace_of_dm.append(np.dot(i.T, i))

plt.legend
plt.plot(t, trace_of_dm,)

    #计算发现 1/2 <= Tr\rho^2 <= 1
# 画Bloch球上的密度矩阵的方法除了直接调用add_states还有自己手动算出 u_x=(\rho_00-\rho_11)/2, u_y, u_z

