# Quantum computation and Quantum control
This is the notes and code for optimization of control of qubit in quantum computer.

Physical realizations of *quantum computer* includes photonics, NMR, cavity-QED, NV Center, joseph junction, ion trap, silicon quantum dot, Rydberg atom and the most exciting Quantum Topology.

Meanwhile, three models for *quantum computation* are quantum circuit model, one way quantum computation model and adiabatic quantum computation model which we will discuss later. And the three is all equivalent.

Adiabatic quantum computation model, transforms the process of quantum computation to a relatively complex Hamiltionian to be solved. Thus its ground state is the solution of our initial problem. Through adiabatic process (that is why we call it Adiabatic quantum computation model), we could control a rather simpler Hamiltionian to the Hamiltionian we want by experimental tools.  

So, the problem is how we control the Hamiltionian so that the ground state could evolve to the outcome state of computation and meets actual experimental conditions. That is what *Quantum Control* focuses on. And the regulatable Hamiltionian is the basis of *Quantum Control*.

The so-called **actual experimental conditions**, explicitly, meaning:

1. 控制时间要短，控制要快。我们的控制要足够快以免系统退相干(decoherence), 一旦超过这个“相干时间”，量子比特就可能会丢失它们的量子信息，从而在计算中引入错误。
2. Robustness, 抗噪声性。也就是说我们的控制要对控制条件的细小变化不够敏感，这才与实际相吻合，因为我们的激光相位、频率、脉冲面积不可能无限精确。
3. 高保真度。我们的演化出来的末态要与实际相差的足够小，通常需要低于1%的错误率，才能应用量子纠错surface code。通常要99.99%的保真度才能进行有效的量子计算。这也就是为啥量子拓扑很exciting。(当我们操纵系统的演化达到末态我们如何来测量保真度，by QPT,QST,GST, RB)。
4. 控制变化应平缓。 起伏大意味着掺杂的高频分量多，易导致更高的激发，由二能级变为多能级。

所以控制量子态的方法有哪些呢？这里以里德堡原子为例，主要是利用电磁调控。


## 脉冲控制

电磁波操控两能级系统(即qubit)，一般是用激光来操控，这称为Rabi问题，让二能级系统产生Rabi振荡，也就是在ground state与excited state中产生周期性的震荡。我们最常用的两种模型为
Landau-Zener model和 Jaynes–Cummings model. 

Landau-Zener model, its Hamiltionian is:

$ H=\Delta(t)\sigma_z+\omega_R\sigma_x=\left(
    \begin{array}{ccc}
        \Delta(t) & \omega_R \\
        \omega_R & -\Delta(t) \\
    \end{array}
\right)$

其中$\Delta(t)$ 是detuning的参数,  为Rabi频率，我们的控制过程优化即优化$\Delta(t)$。通过控制激光的pulse area。当激光的pulse area达到 pi 的时候关掉激光可以得到NOT gate。当pulse area= pi/2, 得到hadamard gate。这种方法在“快速”上达标，但是很难精准控制，在鲁棒性上不达标。

而常用于超导量子比特的模型称为Jaynes–Cummings model, 于1963年为Edwin Jaynes和Fred Cummings发现, 其模型见于广大量子光学书籍,

$ H=H_{field}+H_{atom}+H_{int} $

其中$ H_{field}$是腔内电磁波， $H_{atom}$ 是二能级原子，$H_{int} $为两者的相互作用，






## 绝热演化

我们通过缓慢的调整激光改变哈密顿量，使得二能级的基态进行演化，使得Hamiltonian的对角元变成原Hamiltonian的eigenvalue。
理论上来说只要时间够长绝热量子控制可以达到很高的保真度。绝热控制的鲁棒性很好，但是速度很慢。

Now items included:
1. adiabatic evolution wtih qutip and without qutip just primary code

This part especially focus on stimulation on three-level system interacting with two light fields, STIRAP, CPT
explicitly.


2. Rabi oscilation
3. dissipative items
4. 


## Reference
本文大量引用蔡老师的文章（（（，毕竟我从16年就开始关注“浅斟低唱”嘞。具体文献下述文章也都提到过。

[CRAB & dCRAB 简述](https://zhuanlan.zhihu.com/p/350422093)

[Quantum-opitcs-with-python](https://github.com/caidish/Quantum-Optics-with-Python)

[Documents on QuTiP](https://qutip.org/docs/latest/guide/dynamics/dynamics-data.html)

[相干布居囚禁与绝热布居转移,chaoli](https://chaoli.club/index.php/4037/0#p44776)

[用QuTip学量子光学(四):三原子系统(1):相干布局囚禁(CPT),绝热拉曼路径(STIRAP)](https://zhuanlan.zhihu.com/p/33913599)

[量子调控在量子计算领域有哪些应用和影响？](https://www.zhihu.com/question/274423673/answer/374468139)

[使用RWA化简多能级原子与多模场耦合](https://zhuanlan.zhihu.com/p/165347166)

[Rotation wave approximation](https://zhuanlan.zhihu.com/p/266297809)
