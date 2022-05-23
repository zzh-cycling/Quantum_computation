import numpy as np
import matplotlib.pyplot as plt
import qutip as qp

times=np.linspace(0,5,200)

def hamiltionian(omiga_0, omiga, omiga_1):
    delta = omiga_0 - omiga
    Delta = np.sqrt(delta ** 2 + omiga_1 ** 2)
    H = -delta / 2 * qp.sigmaz() + omiga_1 / 2 * qp.sigmax()
    psi_0=qp.basis(2,0)
    psi_1=qp.basis(2,1)
    n_0=psi_0*psi_0.dag()
    n_1=psi_1*psi_1.dag()
    result=qp.mesolve(H,psi_0,times,[],[n_0,n_1])

    return result


plt.title(r"$\omega_0 =1, \omega =1, \omega_1 =2 \pi$")
plt.xlabel("time")
plt.ylabel("probability")
plt.xticks(np.linspace(0,5,11,endpoint=True))
plt.plot(times,hamiltionian(1,1,2*np.pi).expect[0],linewidth=0.4,linestyle='-',color="b",label='P_0')
plt.plot(times,hamiltionian(1,1,2*np.pi).expect[1], linewidth=0.4, linestyle='-', color="r",label='P_1')
plt.legend()
plt.savefig('./two_level_rabi.png')

plt.show()





