import numpy as np

#--lepton masses
me    = 0.000511
mmu   = 0.105658
mtau  = 1.77684

me2 = me**2 
mm2 = mmu**2
mt2 = mtau**2

#--quark masses

mc=1.28

mc2=mc**2

#--couplings
alfa0 = 1/137.036

M=0.938
M2=M**2
Mpi=0.134
Mk = 0.497


#--TMD
Q20=2.0
lam2=0.04


#--EM parton charges
eu2, ed2 = 4/9., 1/9.
e2 = []
e2.append(0)    # g
e2.append(eu2)  # u
e2.append(eu2)  # ub
e2.append(ed2)  # d
e2.append(ed2)  # db
e2.append(ed2)  # s
e2.append(ed2)  # sb
e2.append(0)    # c
e2.append(0)    # cb
e2.append(0)    # b
e2.append(0)    # bb
e2 = np.array(e2)








