import numpy as np
import matplotlib.pyplot as plt

times=np.linspace(0,500,10000)
omega_1 = 0.1 #Rabi frequency of the driving field

E_g=[]
E_e=[]

for i in times:
    T=500
    delta = -1+2*i/T  # detuning of the |g>-|e> transition

    sigmax = np.array([[0, 1], [1, 0]])
    sigamz = np.array([[1, 0], [0, -1]])
    Hamiltionian = (omega_1 * sigmax - delta * sigamz) / 2
    eigenvalues,eigenvectors=np.linalg.eig(Hamiltionian)
    a=eigenvalues[0]
    b=eigenvalues[1]
    if a<=b:
        a,b=b,a
    E_e.append(a)
    E_g.append(b)


plt.xlabel('times /s')
plt.ylabel('Energy /eV')
plt.plot(times,E_e,label='E_e')
plt.plot(times,E_g,label='E_g')
plt.legend()

plt.savefig('./eigenenergy.png')
plt.show()
