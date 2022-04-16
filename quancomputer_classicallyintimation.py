from qutip import *
import numpy as np
import matplotlib.pyplot as plt

#qobj needs list or array, column vector
# print(Qobj([[1,1,1,1]])) run
# print(Qobj([1,1,1,1])) didn't run
# x=np.array([1,1,1,1]) row vector input with column vector output
# print(Qobj(x))

# 电磁场量子化 量子光学
# Fock state/ Number state 光子数态是光子数算符和电磁场哈密顿量的共同本征态。 升降算符从 |0>态开始，类似谐振子态，可以组成场算符，类似广义坐标广义动量
# 湮灭算符的本征态为相干态
# 在量子化过程中，我们将电磁场分解为一系列以波矢 k 标记的驻波或行波模式，电磁场的哈密顿量 H 也可被拆解为各模式哈密顿量 H_k的叠加，
# 即 [公式] 在之前的量子化过程中，为了简便起见，我们的分析都是针对单模场的哈密顿量
# 最终得到的本征态|n> 、本征值 n也只是针对单个模式。因此对于多模场而言，每个模式独立地享有一套哈密顿量、光子生成/湮灭算符、场算符、本征态与本征值。
#
# 要将单模场的结论迁移到多模场其实很简单，既然每个波矢为k的模式的本征态都是与k 相关的光子数态，
# 则多模场的本征态可直接写为这些由 k标记的数态 |n_k>的直积. 光子生成/湮灭算符对其中某个模场的光子数态的作用是独立的
# 需要注意的是，“模式数”与“光子数”是两个互不影响的值。单模场可以处于单光子态或多光子态，多模场也可以处于单光子态（只要除单光子态外的其他模式处于真空态）或多光子态。
# 此时有三类谐振子模型了：1. 经典谐振子（e.g. 弹簧振子）；2. 量子谐振子（在经典谐振子的基础上引入坐标算符与动量算符的对易式进行量子化）；
# 3. 电磁谐振子（在经典谐振子的基础上引入场算符的对易式进行量子化）。电磁谐振子模型是通过与量子谐振子进行类比得来的。
# 现在，让我们来比较一下经典谐振子与量子/电磁谐振子的解的性质。按理来说，随着量子/电磁谐振子本征态 |n> 中 n 的增大，光子增多，其行为应该越来越趋近于经典。然而我们发现，无论本征态中的n取多大，坐标与动量的期望也始终为零。
# 也就是说，在随时间演化的过程中，光子数态的波包在 [公式] 轴上并不会发生移动，这与经典谐振子的行为很不一样。要模拟经典谐振子，我们需要得到一个随着时间演化，波包能在 q 轴上来回运动的态。
# 为了得到这个与经典谐振子类似的态，我们先思考一下经典谐振子是如何“谐振”起来的，首先应该给它一个外力，或者说给它一个偏离平衡位置的位移，再松手任其谐振。在量子/电磁谐振子模型当中，我们也可以这么做——对基态波包引入一个初始的空间平移。
# 对谐振子基态psi_0(q) ，即真空态 |0> 波包进行平移，将得到相干态（Coherent state）|\alpha> 。需要注意的是，此处的“平移”指的是场算符 p 或 q 的平移，并不是真正的“位置坐标”的平移。

#Fock state ket vector
#N,m,p,alpha=2,0,0,1
#a=basis(N,0)  #/fock(N,m)

#Fock density matrix (outer product of basis)

#b=fock_dm(N,p)

#Coherent state

#c=coherent(N,alpha)

# alpha = complex number (eigenvalue) for requested coherent, // state coherent_dm(N,alpha)
sphere=qutip.Bloch()
a=basis(2,0)
b=basis(3,1)
c=basis(3,2)
a1=np.array(a)

#b2.add_states(a) #b3d=qutip.Bloch3d()
sphere.add_states(a)
sphere.show()

值得注意的是：N表示希尔波尔空间维度，n表示激发能级的位置（position of excitation），实际上就是福克态向量元素为1的位置。叠加态就能通过福克态相加，然后归一化得到。纠缠态则需要通过tensor算符得到，比如 [公式] 其在Qutip中的定义为

S_entangled = (tensor(fock(N,0),fock(N,1)) + tensor(fock(N,1),fock(N,0))).unit()

