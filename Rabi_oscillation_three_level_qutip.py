import numpy as np
import matplotlib.pyplot as plt
import qutip as qp

times = np.linspace(0.0, 10.0, 500)

T=10

e = qp.basis(3, 0)
g = qp.basis(3, 1)
r = qp.basis(3, 2)

Omiga_0=2*np.pi#MHz
delta_t=0.4 #\mus
sigma=0.36 #/mus
Omiga_475=Omiga_0*4.75
Omiga_795=Omiga_0*7.95

#epsilon=1
#H=[epsilon*qp.sigmax(),Omiga_475*qp.sigmaz()]
H=(Omiga_795*(e*g.dag()+g*e.dag())+Omiga_475*(e*r.dag()+r*e.dag()))/2

state0 = e * e.dag() # 基态的Population
state1 = g * g.dag() # 第一激发态的 Population
state2 = r * r.dag() # 泄露能级的概率
result=qp.sesolve(H, e, times, [], [state0, state1,state2])
# 求解演化过程中每一刻的可观测变量值，记录在数组 result 中
result0 =result.expect[0]
result1 =result.expect[1]
result2 =result.expect[2]

# 使用Matplotlib绘图
plt.plot(times,result0,label = 'Ground')
plt.plot(times,result1,label = 'Excited')
plt.plot(times,result2,label = 'Leakage')
plt.title('Population Evolution')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()

# plt.savefig('./three_level_qutip.png')
plt.show()