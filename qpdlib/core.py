import sys
import os
import numpy as np
import time
#from scipy.special import gamma
#from tools.config import conf
from numba import jit
from qpdlib import constants as const
from qpdlib.special import beta

@jit(nopython=True)
def get_s(Q2):
    lam2 = const.lam2
    Q20  = const.Q20
    return np.log(np.log(Q2/lam2)/np.log(Q20/lam2))

@jit(nopython=True)
def __get_shape(x,p):
    return p[0]*x**p[1]*(1-x)**p[2]*(1+p[3]*x+p[4]*x**2)

@jit(nopython=True)
def _get_shape(x,p,s):
    N=p[0] + p[5] * s
    a=p[1] + p[6] * s
    b=p[2] + p[7] * s
    c=p[3] + p[8] * s
    d=p[4] + p[9] * s
    n= 1
    return __get_shape(x,np.array([N/n,a,b,c,d]))

@jit(nopython=True)
def get_shape(x,Q2,p1,p2):
    s=get_s(Q2)
    shape=_get_shape(x,p1,s)
    shape2=_get_shape(x,p2,s)
    if p2[0]!=0: shape=shape*(1+shape2)
    n1 = beta(p1[1]+2,p1[2]+1) + p1[3]*beta(p1[1]+3,p1[2]+1) + p1[4]*beta(p1[1]+4,p1[2]+1)
    n2 = p2[0] * (beta(p1[1]+p2[1]+2,p1[2]+p2[2]+1) + p1[4]*p2[4]*beta(p1[1]+p2[1]+6,p1[2]+p2[2]+1))
    n3 = p2[0] * (p1[3]+p2[3])*beta(p1[1]+p2[1]+3,p1[2]+p2[2]+1)
    n4 = p2[0] * (p1[3]*p2[4]+p2[3]*p1[4])*beta(p1[1]+p2[1]+5,p1[2]+p2[2]+1)
    n5 = p2[0] * (p1[3]*p2[3]+p1[4]+p2[4])*beta(p1[1]+p2[1]+4,p1[2]+p2[2]+1)
    n=n1+n2+n3+n4+n5
    shape=shape/n
    return shape

@jit(nopython=True)
def get_collinear(x,Q2,shape1,shape2):
    N = np.zeros(11)
    for i in range(11):
        N[i] = get_shape(x,Q2,shape1[i],shape2[i])
    return N

@jit(nopython=True)
def __get_dshape(x,p):
    return p[0]*x**p[1]*(1-x)**p[2]*(p[3]+2*p[4]*x+(1+p[3]*x+p[4]*x**2)*(p[1]/x-p[2]/(1-x)))

@jit(nopython=True)
def _get_dshape(x,p,s):
    N=p[0] + p[5] * s
    a=p[1] + p[6] * s
    b=p[2] + p[7] * s
    c=p[3] + p[8] * s
    d=p[4] + p[9] * s
    n=1
    return __get_dshape(x,[N/n,a,b,c,d])

@jit(nopython=True)
def get_dshape(x,Q2,p1,p2):
    s=get_s(Q2)
    dshape=_get_dshape(x,p1,s)
    shape=_get_shape(x,p1,s)
    dshape2=_get_dshape(x,p2,s)
    shape2=_get_shape(x,p2,s)
    if p2[0]!=0: dshape = shape*dshape2 + (1+shape2)*dshape
    n1 = beta(p1[1]+2,p1[2]+1) + p1[3]*beta(p1[1]+3,p1[2]+1) + p1[4]*beta(p1[1]+4,p1[2]+1)
    n2 = p2[0] * (beta(p1[1]+p2[1]+2,p1[2]+p2[2]+1) + p1[4]*p2[4]*beta(p1[1]+p2[1]+6,p1[2]+p2[2]+1))
    n3 = p2[0] * (p1[3]+p2[3])*beta(p1[1]+p2[1]+3,p1[2]+p2[2]+1)
    n4 = p2[0] * (p1[3]*p2[4]+p2[3]*p1[4])*beta(p1[1]+p2[1]+5,p1[2]+p2[2]+1)
    n5 = p2[0] * (p1[3]*p2[3]+p1[4]+p2[4])*beta(p1[1]+p2[1]+4,p1[2]+p2[2]+1)
    n=n1+n2+n3+n4+n5
    dshape=dshape/n
    return dshape

@jit(nopython=True)
def get_dcollinear(x,Q2,shape1,shape2):
    N = np.zeros(11)
    for i in range(11):
        N[i] = get_dshape(x,Q2,shape1[i],shape2[i])
    return N

@jit(nopython=True)
def __get_mom(p,s,i):
    N=p[0] + p[5] * s
    a=p[1] + p[6] * s
    b=p[2] + p[7] * s
    c=p[3] + p[8] * s
    d=p[4] + p[9] * s
    ni= beta(i+p[1],p[2]+1) + p[3]*beta(i+p[1]+1,p[2] + 1) + p[4]*beta(i+p[1]+2,p[2] + 1)
    n1= beta(1+p[1],p[2]+1) + p[3]*beta(1+p[1]+1,p[2] + 1) + p[4]*beta(1+p[1]+2,p[2] + 1)
    return N*ni/n1

@jit(nopython=True)
def _get_mom(Q2,p1,p2,i):
    s=get_s(Q2)
    mom=__get_mom(p1,s,i)
    if p2[0]!=0: mom+=__get_mom(p2,s,i)
    return mom

@jit(nopython=True)
def get_mom(Q2,iflav,i):
    return _get_mom(Q2,shape1[iflav],shape2[iflav],i)

@jit(nopython=True)
def get_widths(Q2):
    s=get_s(Q2)
    return np.abs(self.widths1+s*self.widths2)

@jit(nopython=True)
def charge_conj(p):
    out=np.zeros(len(p))
    cnt=0
    for i in [0,2,1,4,3,6,5,8,7,10,9]:
        out[cnt]=p[i]
        cnt+=1
    return out
@jit(nopython=True)
def p2n(p):
    out=np.zeros(len(p))
    cnt=0
    for i in [0,3,4,1,2,5,6,7,8,9,10]:
        out[cnt]=p[i]
        cnt+=1
    return out


class CORE:
    
    def get_widths(self,Q2):
        s=get_s(Q2)
        return np.abs(self.widths1+s*self.widths2)

    def get_tmd(self,x,Q2,kT,hadron,dist,icol=False,deriv=False):

        col=self.get_C(x,Q2)

        if icol: return col

        widths=self.get_widths(Q2)
        if dist=='ffpi' or dist=='ffk' or dist=='collinspi': gauss=np.exp(-x**2 * kT**2/widths)
        else: gauss=np.exp(-kT**2/widths)

        if   hadron=='p' : M=const.M
        elif hadron=='pi': M=const.Mpi
        elif hadron=='k' : M=const.Mk

        if   dist=='pdf':           norm=1/np.pi/widths
        elif dist=='transversity':  norm=1/np.pi/widths
        elif dist=='sivers':        norm=(2*M**2/widths) * (1/np.pi/widths)

        elif dist=='ffpi' :         norm=1/np.pi/widths
        elif dist=='collinspi':     norm=2*x**2*M**2/widths * (1/np.pi/widths)

        return norm*col*gauss
