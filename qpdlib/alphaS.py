#!/bin/env python
import numpy as np
from qpdlib.aux import AUX
from tools.config import conf

class ALPHAS:

    def __init__(self):
        if   conf['order']=='LO':  self.order=0
        elif conf['order']=='NLO': self.order=1
 
        self.Q20 = conf['Q20']
        self.setup()
  
    def setup(self):
        aux = conf['aux']
  
        self.beta=np.zeros((7,3))
        for Nf in range(3,7): 
            self.beta[Nf,0]=11.0-2.0/3.0*Nf 
            self.beta[Nf,1]=102.-38.0/3.0*Nf 
            self.beta[Nf,2]=2857.0/2.0-5033.0/18.0*Nf+325.0/54.0*Nf**2 
  
        if 'alphaSmode' in conf: 
            alphaSmode = conf['alphaSmode']
        else: 
            alphaSmode ='backward' 
            conf['alphaSmode'] ='backward' 
        
        if alphaSmode=='backward':
            # uses alphaS(mZ)--> backwards evolution
            if 'alphaSMZ' in conf: 
                self.aZ  = conf['alphaSMZ']/(4*np.pi)
            else:
                self.aZ  = conf['aux'].alphaSMZ/(4*np.pi)
            self.ab=self.evolve_a(aux.mZ2,self.aZ,aux.mb2,5)
            self.ac=self.evolve_a(aux.mb2,self.ab,aux.mc2,4)
            self.a0=self.evolve_a(aux.mc2,self.ac,self.Q20,3)
  
        elif alphaSmode=='forward':
            self.a0=conf['aux'].alphaS0/(4*np.pi)
            self.ac=self.evolve_a(self.Q20,self.a0,aux.mc2,3)
            self.ab=self.evolve_a(aux.mc2,self.ac,aux.mb2,4)
  
        elif alphaSmode=='2-loop closed form':
            self.alphaS_cj=ALPHAS_CJ()
  
        # we will store all Q2 values of alphaS 
        self.storage={}
  
    def get_state(self):
        return (self.a0,self.ab,self.ac)
    
    def set_state(self,state):
        self.a0, self.ab, self.ac = state[:]
        self.storage = {}
        
    def get_Nf(self,Q2):
        aux = conf['aux']
        Nf=3
        if Q2>=(aux.mc2): Nf+=1
        if Q2>=(aux.mb2): Nf+=1
        return Nf
  
    def beta_func(self,a,Nf):
        betaf = -self.beta[Nf,0]
        if self.order>=1: betaf+=-a*self.beta[Nf,1]
        if self.order>=2: betaf+=-a*self.beta[Nf,2]
        return betaf*a**2
  
    def evolve_a(self,Q20,a,Q2,Nf):
        # Runge-Kutta implemented in pegasus  
        LR = np.log(Q2/Q20)/20.0
        for k in range(20):
            XK0 = LR * self.beta_func(a,Nf)
            XK1 = LR * self.beta_func(a + 0.5 * XK0,Nf)
            XK2 = LR * self.beta_func(a + 0.5 * XK1,Nf)
            XK3 = LR * self.beta_func(a + XK2,Nf)
            a+= (XK0 + 2.* XK1 + 2.* XK2 + XK3) * 0.166666666666666
        return a
  
    def get_a(self,Q2):
        aux = conf['aux']
  
        if Q2 not in self.storage:
  
            if conf['alphaSmode']=='2-loop closed form':
  
                self.storage[Q2]=self.alphaS_cj.get_a(Q2)
  
            else:
  
                if aux.mb2<=Q2:
                    Q20,a0,Nf=aux.mb2,self.ab,5
                elif aux.mc2<=Q2 and Q2<aux.mb2: 
                    Q20,a0,Nf=aux.mc2,self.ac,4
                elif Q2<aux.mc2:
                    Q20,a0,Nf=self.Q20,self.a0,3
                self.storage[Q2]=self.evolve_a(Q20,a0,Q2,Nf)
  
        return self.storage[Q2]
  
    def get_alphaS(self,Q2):
        return self.get_a(Q2)*4*np.pi
  
class ALPHAS_CJ:
 
  def __init__(self):
    self.xMC=1.3
    self.xMB=4.5
    self.PI=3.14159
    self.ALQCD5=0.226

  def get_a(self,Q2):
    return self.get_alphaS(Q2)/4/np.pi

  def get_alphaS(self,XMU2):
    NEFF=self.get_Nf(XMU2)
    return self.ALFAS5(XMU2,2,NEFF)
    
  def get_Nf(self,mu2):
    Nf=3
    if mu2>self.xMC**2: Nf+=1
    if mu2>self.xMB**2: Nf+=1
    return Nf
        
  def ALFAS5(self,Q2,ILOOP,NEFF):
    A  = 1.00
    AMB=A*self.xMB
    AMC=A*self.xMC
    MU=np.sqrt(Q2)
    ALQCD52=self.ALQCD5**2
    if MU>AMB:
      ALFAS5 = self.ASLOOP(Q2,ALQCD52,5,ILOOP)
      NEFF=5
    elif  MU>AMC:
      AMB2=AMB*AMB
      ALFAS5 = 1 / ( 1 / self.ASLOOP(Q2  ,ALQCD52,4,ILOOP) + \
                     1 / self.ASLOOP(AMB2,ALQCD52,5,ILOOP) - \
                     1 / self.ASLOOP(AMB2,ALQCD52,4,ILOOP) )
      NEFF=4
    else:
      AMB2=AMB**2
      AMC2=AMC**2
      ALFAS5 = 1 / ( 1 / self.ASLOOP(Q2  ,ALQCD52,3,ILOOP) + \
                     1 / self.ASLOOP(AMC2,ALQCD52,4,ILOOP) + \
                     1 / self.ASLOOP(AMB2,ALQCD52,5,ILOOP) - \
                     1 / self.ASLOOP(AMB2,ALQCD52,4,ILOOP) - \
                     1 / self.ASLOOP(AMC2,ALQCD52,3,ILOOP) )
      NEFF=3
    return ALFAS5
            
  def ASLOOP(self,XMU2,XLQCD2,NF,NORDER):
    if NORDER==1:
      B1=(33.-2.*NF)/(12.*self.PI)
      T=XMU2/XLQCD2
      ASLOOP=1/(B1*np.log(T))
    elif NORDER==2:
      B1=(33.-2.*NF)/(12.*self.PI)
      B2=(153.-19.*NF)/(2.*self.PI*(33.-2.*NF))
      T=XMU2/XLQCD2
      F1=B1*np.log(T)
      ASLOOP=(1.-B2*np.log(np.log(T))/F1)/F1
    return ASLOOP

if __name__=='__main__':

    conf['order']='NLO'
    conf['Q20'] = 1.0
    conf['aux']=AUX()
    aS=ALPHAS()

    mc2=conf['aux'].mc2
    mb2=conf['aux'].mb2
    mZ2=conf['aux'].mZ2


    print('========================')
    print('test alphaS evolution')
    print('========================')
    print('Q2=1           alphaS=%0.5f'%aS.get_alphaS(1.0))
    print('Q2=(1+mc2)/2   alphaS=%0.5f'%aS.get_alphaS(0.5*(1.0+mc2)))
    print('Q2=mc2         alphaS=%0.5f'%aS.get_alphaS(mc2))
    print('Q2=(mc2+mb2)/2 alphaS=%0.5f'%aS.get_alphaS(0.5*(mc2+mb2)))
    print('Q2=mb2         alphaS=%0.5f'%aS.get_alphaS(mb2))
    print('Q2=(mb2+mZ2)/2 alphaS=%0.5f'%aS.get_alphaS(0.5*(mb2+mZ2)))
    print('Q2=mZ2         alphaS=%0.5f'%aS.get_alphaS(mZ2))
  










