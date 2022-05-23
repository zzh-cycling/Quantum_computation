from qutip import *
import numpy as np
import matplotlib.pyplot as plt


r=basis(2,0)
g=basis(2,1)

def Hamiltionian(V,Omega,Delta):
    H_1 = Omega / 2 * (r * g.dag() + g * r.dag()) - Delta * (r * r.dag())
    H_2 = Omega / 2 * (r * g.dag() + g * r.dag()) - Delta * (r * r.dag())
    H_12 = V * tensor((r * r.dag()), (r * r.dag()))
    return tensor(H_1,qeye(2))+tensor(qeye(2),H_2)+H_12

rr=tensor(r,r)
rg=tensor(r,g)
gr=tensor(g,r)
gg=tensor(g,g)
psi=(tensor(r,g)+tensor(g,r)).unit()
n_psi=psi*psi.dag()

t=np.linspace(0,5,100)
n_rr=rr*rr.dag()
n_rg=rg*rg.dag()
n_gr=gr*gr.dag()
n_gg=gg*gg.dag()
plt.figure(1)

plt.subplot(2,3,1)
result=mesolve(Hamiltionian(0,2,0),gg,t,[],[n_rr,n_rg,n_gr,n_gg,n_psi])
plt.title(r'$V=0, \Omega =2, \Delta =0$')
plt.ylabel("fidelity")
plt.plot(t,result.expect[0],label='rr',color='r')
plt.plot(t,result.expect[1],label='rg',color='k') #01 10一样
plt.plot(t,result.expect[2],label='gr',linestyle='-',color='g')
plt.plot(t,result.expect[3],label='gg',color='b')
plt.plot(t,result.expect[4],label='psi',color='m')
plt.xticks([])  # 去y坐标刻度


plt.subplot(2,3,4)
result=mesolve(Hamiltionian(0,2,0.1),gg,t,[],[n_rr,n_rg,n_gr,n_gg,n_psi])
plt.title(r'$V=0, \Omega =2, \Delta =0.1$')
plt.xlabel("time")
plt.ylabel("fidelity")
plt.plot(t,result.expect[0],label='rr',color='r')
plt.plot(t,result.expect[1],label='rg',color='k') #01 10一样
plt.plot(t,result.expect[2],label='gr',linestyle='-',color='g')
plt.plot(t,result.expect[3],label='gg',color='b')
plt.plot(t,result.expect[4],label='psi',color='m')


plt.subplot(2,3,2)
result=mesolve(Hamiltionian(1,2,0),gg,t,[],[n_rr,n_rg,n_gr,n_gg,n_psi])
plt.title(r'$V=1, \Omega =2, \Delta =0$')
plt.plot(t,result.expect[0],label='rr',color='r')
plt.plot(t,result.expect[1],label='rg',color='k') #01 10一样
plt.plot(t,result.expect[2],label='gr',linestyle='-',color='g')
plt.plot(t,result.expect[3],label='gg',color='b')
plt.plot(t,result.expect[4],label='psi',color='m')
plt.xticks([])  # 去x坐标刻度
plt.yticks([])  # 去y坐标刻度


plt.subplot(2,3,5)
result=mesolve(Hamiltionian(1,2,0.1),gg,t,[],[n_rr,n_rg,n_gr,n_gg,n_psi])
plt.title(r'$V=1, \Omega =2, \Delta =0.1$')
plt.xlabel("time")
plt.plot(t,result.expect[0],label='rr',color='r')
plt.plot(t,result.expect[1],label='rg',color='k') #01 10一样
plt.plot(t,result.expect[2],label='gr',linestyle='-',color='g')
plt.plot(t,result.expect[3],label='gg',color='b')
plt.plot(t,result.expect[4],label='psi',color='m')
plt.yticks([])  # 去y坐标刻度


plt.subplot(2,3,3)
result=mesolve(Hamiltionian(24,2,0),gg,t,[],[n_rr,n_rg,n_gr,n_gg,n_psi])
plt.title(r'$V=24, \Omega =2, \Delta =0$')
plt.plot(t,result.expect[0],label='rr',color='r')
plt.plot(t,result.expect[1],label='rg',color='k') #01 10一样
plt.plot(t,result.expect[2],label='gr',linestyle='-',color='g')
plt.plot(t,result.expect[3],label='gg',color='b')
plt.plot(t,result.expect[4],label='psi',color='m')
plt.legend(loc=1)
plt.xticks([])  # 去x坐标刻度
plt.yticks([])  # 去y坐标刻度


plt.subplot(2,3,6)
result=mesolve(Hamiltionian(24,2,0.1),gg,t,[],[n_rr,n_rg,n_gr,n_gg,n_psi])
plt.title(r'$V=24, \Omega =2, \Delta =0.1$')
plt.xlabel("time")
plt.plot(t,result.expect[0],label='rr',color='r')
plt.plot(t,result.expect[1],label='rg',color='k') #01 10一样
plt.plot(t,result.expect[2],label='gr',linestyle='-',color='g')
plt.plot(t,result.expect[3],label='gg',color='b')
plt.plot(t,result.expect[4],label='psi',color='m')
plt.yticks([])  # 去y坐标刻度

plt.savefig('./six_figs.png')
plt.show()




