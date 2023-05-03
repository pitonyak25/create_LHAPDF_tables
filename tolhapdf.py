#!/usr/bin/env python
import sys,os
import numpy as np
import copy
from subprocess import Popen, PIPE, STDOUT
import lhapdf

#--from tools
from tools.tools    import load,save,checkdir,lprint
from tools.config   import conf,load_config

#--from local
from tools.core   import CORE
from qpdlib.aux   import AUX
import qpdlib.pdf0 as pdf0
import qpdlib.pdf1 as pdf1
import qpdlib.ff0  as ff0
import qpdlib.ff1  as ff1

core   = CORE()
aux    = AUX()

cwd = os.getcwd()

#--index conventions:
#--1: down
#--2: up
#--3: strange
#--4: charm
#--5: bottom
#--6: top
#--21: gluon
#--negative values for antiquarks

#iflavs = [-5,-4,-3,-2,-1,1,2,3,4,5,21]
iflavs = [1,2,3,-1,-2,-3]

X1=10**np.linspace(-4,-1)
X2=np.linspace(0.101,0.99)
X=np.append(X1,X2)

def write_lhapdf_conf(wdir):
    script = """
    Verbosity: 1
    Interpolator: logcubic
    Extrapolator: continuation
    ForcePositive: 0
    AlphaS_Type: analytic
    MZ: 91.1876
    MUp: 0.002
    MDown: 0.005
    MStrange: 0.10
    MCharm: 1.29
    MBottom: 4.19
    MTop: 172.9
    Pythia6LambdaV5Compat: true"""
    F=open('%s/data/lhapdf.conf'%wdir,'w')
    F.writelines(script)
    F.close()
    
def rename_tables(wdir,dirname,newname):

    print('\nrenaming LHAPDF tables for %s to %s'%(dirname,newname))
    old = '%s/data/%s'%(wdir,dirname)
    new = '%s/data/%s'%(wdir,newname)
    
    checkdir(new)
    F=os.listdir(old)

    cnt=0
    for f in F:
        cnt+=1
        lprint('progress %d/%d'%(cnt,len(F)))
        cmd=['cp','%s/%s'%(old,f),'%s/%s'%(new,f.replace(dirname,newname))]
        p=Popen(cmd,  stdout=PIPE, stderr=STDOUT)
        output = p.stdout.read()
    print



class QCF:

    def __init__(self):
        pass

    def gen_cj_grid(self):
    
        Q2=[1.30000E+00,1.50159E+00,1.75516E+00,2.07810E+00\
                ,2.49495E+00,3.04086E+00,3.76715E+00,4.50000E+00\
                ,4.75000E+00,6.23113E+00,8.37423E+00,1.15549E+01\
                ,1.64076E+01,2.40380E+01,3.64361E+01,5.73145E+01\
                ,9.38707E+01,1.60654E+02,2.88438E+02,5.45587E+02\
                ,1.09231E+03,2.32646E+03,5.30043E+03,1.29956E+04\
                ,3.45140E+04,1.00000E+05]
    
        X=[1.00000E-06,1.28121E-06,1.64152E-06,2.10317E-06\
               ,2.69463E-06,3.45242E-06,4.42329E-06,5.66715E-06\
               ,7.26076E-06,9.30241E-06,1.19180E-05,1.52689E-05\
               ,1.95617E-05,2.50609E-05,3.21053E-05,4.11287E-05\
               ,5.26863E-05,6.74889E-05,8.64459E-05,1.10720E-04\
               ,1.41800E-04,1.81585E-04,2.32503E-04,2.97652E-04\
               ,3.80981E-04,4.87518E-04,6.26039E-04,8.00452E-04\
               ,1.02297E-03,1.30657E-03,1.66759E-03,2.12729E-03\
               ,2.71054E-03,3.44865E-03,4.37927E-03,5.54908E-03\
               ,7.01192E-03,8.83064E-03,1.10763E-02,1.38266E-02\
               ,1.71641E-02,2.11717E-02,2.59364E-02,3.15062E-02\
               ,3.79623E-02,4.53425E-02,5.36750E-02,6.29705E-02\
               ,7.32221E-02,8.44039E-02,9.64793E-02,1.09332E-01\
               ,1.23067E-01,1.37507E-01,1.52639E-01,1.68416E-01\
               ,1.84794E-01,2.01731E-01,2.19016E-01,2.36948E-01\
               ,2.55242E-01,2.73927E-01,2.92954E-01,3.12340E-01\
               ,3.32036E-01,3.52019E-01,3.72282E-01,3.92772E-01\
               ,4.13533E-01,4.34326E-01,4.55495E-01,4.76836E-01\
               ,4.98342E-01,5.20006E-01,5.41818E-01,5.63773E-01\
               ,5.85861E-01,6.08077E-01,6.30459E-01,6.52800E-01\
               ,6.75387E-01,6.98063E-01,7.20830E-01,7.43683E-01\
               ,7.66623E-01,7.89636E-01,8.12791E-01,8.35940E-01\
               ,8.59175E-01,8.82485E-01,9.05866E-01,9.29311E-01\
               ,9.52817E-01,9.76387E-01,1.00000E+00]
    
        return X,Q2
    
    def gen_grid(self,dist):
        if    dist=='transversity' : return self.gen_cj_grid()
        if    dist=='collinspi' :    return self.gen_cj_grid()
        if    dist=='Htildepi' :     return self.gen_cj_grid()
        if    dist=='sivers' :       return self.gen_cj_grid()
    
    def _gen_table(self,dist):
    
        X,Q2=self.gen_grid(dist)
        qpd=conf[dist]
    
        nx=len(X)
        nQ2=len(Q2)
    
        #--fill table
        table={iflav:[]  for iflav in iflavs}  
        npts=nQ2*nx
        #--note that one has the corresponding indices
        #--u:   2 -> 1
        #--ub: -2 -> 2
        #--d:   1 -> 3
        #--db: -1 -> 4
        #--s:   2 -> 5
        #--sb: -2 -> 6
        for iQ2 in range(nQ2):
            for ix in range(nx):
                table[ 1].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[3])
                table[ 2].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[1])
                if dist in ['transversity','sivers']:
                    table[ 3].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[5])
                    table[-1].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[4])
                    table[-2].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[2])
                    table[-3].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[6])
                if dist in ['collinspi','Htildepi']:
                    table[ 3].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[3])
                    table[-1].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[1])
                    table[-2].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[3])
                    table[-3].append(X[ix]*qpd.get_C(X[ix],Q2[iQ2])[3])

        #--remap tables to match with lhapdf format
        for iflav in iflavs: 
            new_list=[]
            for ix in range(nx):
                for inQ2 in range(nQ2):
                    idx=ix+inQ2*nx
                    new_list.append(table[iflav][idx])
            table[iflav]=new_list

        return X,Q2,table
    
    def gen_lhapdf_dat_file(self,X,Q2,table, wdir, file_name,setlabel):
        lines=[]  
        lines.append('PdfType: replica')
        lines.append('Format: lhagrid1')
        lines.append('---')
        line=''
        for _ in X: line+=('%10.5e '%_).upper()
        lines.append(line)
        line=''
        for _ in Q2: line+=('%10.5e '%_**0.5).upper()
        lines.append(line)
        line = ''
        for i in iflavs: line += str(i) + ' '
        lines.append(line)
 
        nx=len(X)
        nQ2=len(Q2)
    
        for i in range(nx*nQ2):
            line=''
            for iflav in iflavs:
                line+=('%10.5e '%table[iflav][i]).upper()
            lines.append(line)
        lines.append('---')
        lines=[l+'\n' for l in lines]
        idx=str(setlabel).zfill(4)
        tab=open('%s/data/%s/%s_%s.dat'%(wdir, file_name, file_name,idx),'w')
        tab.writelines(lines)
        tab.close()
    
    def gen_lhapdf_info_file(self,X,Q2,nrep,wdir,dist,file_name,info):
    
        from qpdlib.alphaS import ALPHAS
        alphas = ALPHAS()
        aS=[alphas.get_alphaS(_) for _ in Q2]
        mZ=conf['aux'].mZ
        mb=conf['aux'].mb
        mc=conf['aux'].mc
        alphaSMZ=conf['aux'].alphaSMZ
        xmin=X[0]
        xmax=X[-1]
        Qmin=Q2[0]**0.5
        Qmax=Q2[-1]**0.5
    
    
        lines=[]
        lines.append('SetDesc:         "<description>"')
        lines.append('SetIndex:        <index>')
        lines.append('Authors:         <authors>')
        lines.append('Reference:       reference')
        lines.append('Format:          lhagrid1')
        lines.append('DataVersion:     1')
        lines.append('NumMembers:      %d'%nrep)
        lines.append('Particle:        particle')
        #lines.append('Flavors:         [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 21]')
        lines.append('Flavors:         [1, 2, 3, -1, -2, -3]')
        lines.append('OrderQCD:        1')
        lines.append('FlavorScheme:    variable')
        lines.append('NumFlavors:      5')
        lines.append('ErrorType:       replicas')
        lines.append('XMin:            %0.2e'%xmin)
        lines.append('XMax:            %0.2e'%xmax)
        lines.append('QMin:            %0.2e'%Qmin)
        lines.append('QMax:            %0.2e'%Qmax)
        lines.append('MZ:              %f'%mZ)
        lines.append('MUp:             0.0')
        lines.append('MDown:           0.0')
        lines.append('MStrange:        0.0')
        lines.append('MCharm:          %f'%mc)
        lines.append('MBottom:         %f'%mb)
        lines.append('MTop:            180.0')
        lines.append('AlphaS_MZ:       %f'%alphaSMZ)
        lines.append('AlphaS_OrderQCD: 1')
        lines.append('AlphaS_Type:     ipol')
        line='AlphaS_Qs: ['
        for _ in Q2: line+=('%10.5e, '%_**0.5).upper()
        line=line.rstrip(',')+']'
        lines.append(line)
        line='AlphaS_Vals: ['
        for _ in aS: line+=('%10.5e, '%_).upper()
        line=line.rstrip(',')+']'
        lines.append(line)
        lines.append('AlphaS_Lambda4: 0')
        lines.append('AlphaS_Lambda5: 0')
        if dist=='transversity':
            line='widths_uv: ['
            for _ in self.widths_uv: line+=('%10.5e, '%_**0.5).upper()
            line=line.rstrip(',')+']'
            lines.append(line)
        if dist=='collinspi':
            line='widths_fav: ['
            for _ in self.widths_fav: line+=('%10.5e, '%_).upper()
            line=line.rstrip(',')+']'
            lines.append(line)
            line='widths_unf: ['
            for _ in self.widths_unf: line+=('%10.5e, '%_).upper()
            line=line.rstrip(',')+']'
            lines.append(line)

 
        for i in range(len(lines)):
            for _ in info:
                lines[i]=lines[i].replace(_,info[_])
    
    
        lines=[l+'\n' for l in lines]
        tab=open('%s/data/%s/%s.info'%(wdir, file_name, file_name),'w')
        tab.writelines(lines)
        tab.close()
    
    def gen_tables(self,wdir,dist, file_name,info,info_only=False):
   
        print('\ngenerating QCF LHAPDF tables for %s using %s'%(dist,wdir))
    
        write_lhapdf_conf(wdir)
        load_config('%s/input.py'%wdir)
        istep=core.get_istep()
        core.mod_conf(istep) #--set conf as specified in istep

        #--LO analysis
        conf['order'] = 'LO'
        conf['aux']   = aux

        #--load jar file, or generate if it does not exist
        jarname = '%s/data/jar-%d.dat'%(wdir,istep)
        try:
            jar=load(jarname)
        except:
            core.gen_jar_file(wdir)
            jar=load(jarname)
        replicas=jar['replicas']

 
        #print(list(conf['params'])) 
        parman = PARMAN() 
 
        #--check order consistency
        order=jar['order']
        parman.order = order
    
        #--create output dir
        checkdir(wdir + '/data/')
        checkdir(wdir + '/data/%s/' % file_name)

        if dist=='transversity': self.widths_uv = []
        if dist=='collinspi':    self.widths_fav,self.widths_unf = [],[]
        if dist=='sivers':       self.widths_uv = []
        for i in range(len(order)):
            if order[i][0] != 1: continue
            if order[i][1] != dist: continue
            if order[i][2] == 'widths1_uv':   uv_idx  = i
            if order[i][2] == 'widths1_fav':  fav_idx = i
            if order[i][2] == 'widths1_ufav': unf_idx = i



        #--gen lhapdf_data_files
        TABLE = {}
        for iflav in iflavs:
            TABLE[iflav] = []
        if info_only==False:
            cnt=0
            for par in replicas:
                lprint('progress: %d/%d'%(cnt+1,len(replicas)))
                parman.set_new_params(par,initial=False)
                core.set_passive_params(istep,par)
                X,Q2,table = self._gen_table(dist)
                for iflav in iflavs:
                    TABLE[iflav].append(table[iflav])
                self.gen_lhapdf_dat_file(X,Q2,table, wdir, file_name,cnt+1)
                if dist=='transversity':
                    self.widths_uv.append(par[uv_idx])
                if dist=='collinspi':
                    self.widths_fav.append(par[fav_idx])
                    self.widths_unf.append(par[unf_idx])
                if dist=='sivers':
                    self.widths_uv.append(par[uv_idx])
                cnt+=1
            print()
      
        #--save mean value with index 0000 
        for iflav in iflavs:
            TABLE[iflav] = np.mean(TABLE[iflav],axis=0)
        self.gen_lhapdf_dat_file(X,Q2,TABLE, wdir, file_name,0)

        #--gen_lhapdf_info_file
        X,Q2=self.gen_grid(dist)
        nrep=len(replicas)
        self.gen_lhapdf_info_file(X,Q2,nrep,wdir,dist,file_name,info)

        print('Saving LHAPDF table to %s/data/%s'%(wdir,file_name))

      





class PARMAN:

    def __init__(self):

        self.setup_core()
        self.get_ordered_free_params()

    def setup_core(self):


        if 'version' in conf: version=conf['version']
        else: version=0 #--for back compatibility

        if 'pdf'           in conf['params']: conf['pdf']          = pdf0.PDF()
        if 'pdfpi-'        in conf['params']: conf['pdfpi-']       = pdf0.PDF('pi-')
        if 'transversity'  in conf['params']:
            if version == 0:  conf['transversity'] = pdf1.PDF()
            if version == 'JAM20+':  conf['transversity'] = pdf2.PDF('h1')
        if 'sivers'        in conf['params']:
            if version == 0:
                conf['sivers']       = pdf1.PDF()
                conf['dsivers']      = pdf1.PDF('deriv')
            if version == 'JAM20+':
                conf['sivers']       = pdf2.PDF('Siv')
                conf['dsivers']      = pdf2.PDF('Siv','deriv')
        if 'boermulders' in conf['params']:
            if version == 0:
                conf['boermulders']  = pdf1.PDF()
                conf['dboermulders'] = pdf1.PDF('deriv')
            if version == 'JAM20+':
                conf['boermulders']  = pdf2.PDF('BM')
                conf['dboermulders'] = pdf2.PDF('BM','deriv')
        if 'ffpi'          in conf['params']: conf['ffpi']         = ff0.FF('pi')
        if 'ffk'           in conf['params']: conf['ffk']          = ff0.FF('k')
        if 'ffh'           in conf['params']: conf['ffh']          = ff0.FF('h') #ffpi still has the same class as the original ff0
        if 'collinspi'     in conf['params']:
            if version == 0:
                conf['collinspi']    = ff1.FF('pi')
                conf['dcollinspi']   = ff1.FF('pi','deriv')
            if version == 'JAM20+':
                conf['collinspi']    = ff2.FF('Col','pi')
                conf['dcollinspi']   = ff2.FF('Col','pi','deriv')
        if 'collinsk'      in conf['params']:
            if version == 0:
                conf['collinsk']     = ff1.FF('k')
                conf['dcollinsk']    = ff1.FF('k','deriv')
            if version == 'JAM20+':
                conf['collinsk']     = ff2.FF('Col','k')
                conf['dcollinsk']    = ff2.FF('Col','k','deriv')
        if 'Htildepi'      in conf['params']:
            if version == 0:
                conf['Htildepi']     = ff1.FF('pi')
            if version == 'JAM20+':
                conf['Htildepi']    = ff2.FF('Col','pi')  # Htilde (using same splitting functions as Collins)
        if 'Htildek'       in conf['params']:
            if version == 0:
                conf['Htildek']      = ff1.FF('k')
            if version == 'JAM20+':
                conf['Htildek']     = ff2.FF('Col','k')  # Htilde (using same splitting functions as Collins)

    def get_ordered_free_params(self):
        self.par=[]
        self.order=[]
        self.pmin=[]
        self.pmax=[]

        if 'check lims' not in conf: conf['check lims']=False

        for k in conf['params']:
            #print('parman:',k)
            for kk in conf['params'][k]:
                if  conf['params'][k][kk]['fixed']==False:
                    p=conf['params'][k][kk]['value']
                    pmin=conf['params'][k][kk]['min']
                    pmax=conf['params'][k][kk]['max']
                    self.pmin.append(pmin)
                    self.pmax.append(pmax)
                    if p<pmin or p>pmax:
                       if conf['check lims']: raise ValueError('par limits are not consistent with central: %s %s'%(k,kk))

                    self.par.append(p)
                    self.order.append([1,k,kk])
                    #print('order:',[1,k,kk])

        if 'datasets' in conf:
            for k in conf['datasets']:
                for kk in conf['datasets'][k]['norm']:
                    if  conf['datasets'][k]['norm'][kk]['fixed']==False:
                        p=conf['datasets'][k]['norm'][kk]['value']
                        pmin=conf['datasets'][k]['norm'][kk]['min']
                        pmax=conf['datasets'][k]['norm'][kk]['max']
                        self.pmin.append(pmin)
                        self.pmax.append(pmax)
                        if p<pmin or p>pmax:
                           if conf['check lims']: raise ValueError('par limits are not consistend with central: %s %s'%(k,kk))
                        self.par.append(p)
                        self.order.append([2,k,kk])

        self.pmin=np.array(self.pmin)
        self.pmax=np.array(self.pmax)
        self.par=np.array(self.par)
        self.set_new_params(self.par,initial=True)

    def gen_flat(self,setup=True):
        r=uniform(0,1,len(self.par))
        par=self.pmin + r * (self.pmax-self.pmin)
        if setup: self.set_new_params(par,initial=True)
        return par
        #while 1:
        #  r=uniform(0,1,len(self.par))
        #  par=self.pmin + r * (self.pmax-self.pmin)
        #  self.set_new_params(par,initial=True)
        #  flag=False
        #  if 'pdf' in conf and conf['pdf'].params['g1'][0]<0: flag=True
        #  if 'pdf' in conf and conf['pdf'].params['s1'][0]<0: flag=True
        #  if flag==False: break
        #return par

    def check_lims(self):
        flag=True
        for k in conf['params']:
            for kk in conf['params'][k]:
                if  conf['params'][k][kk]['fixed']==False:
                    p=conf['params'][k][kk]['value']
                    pmin=conf['params'][k][kk]['min']
                    pmax=conf['params'][k][kk]['max']
                    if  p<pmin or p>pmax:
                        print(k,kk, p,pmin,pmax)
                        flag=False

        if  'datasets' in conf:
            for k in conf['datasets']:
                for kk in conf['datasets'][k]['norm']:
                    if  conf['datasets'][k]['norm'][kk]['fixed']==False:
                        p=conf['datasets'][k]['norm'][kk]['value']
                        pmin=conf['datasets'][k]['norm'][kk]['min']
                        pmax=conf['datasets'][k]['norm'][kk]['max']
                        if p<pmin or p>pmax:
                          flag=False
                          print(k,kk, p,pmin,pmax)

        return flag

    def set_new_params(self,parnew,initial=False):
        self.par=parnew
        self.shifts=0
        semaphore={}

        for i in range(len(self.order)):
            ii,k,kk=self.order[i]
            if  ii==1:
                if k not in semaphore: semaphore[k]=0
                if conf['params'][k][kk]['value']!=parnew[i]:
                  conf['params'][k][kk]['value']=parnew[i]
                  semaphore[k]=1
                  self.shifts+=1
            elif ii==2:
                if conf['datasets'][k]['norm'][kk]['value']!=parnew[i]:
                  conf['datasets'][k]['norm'][kk]['value']=parnew[i]
                  self.shifts+=1

        if  initial:
            for k in conf['params']: 
                semaphore[k]=1

        #--This is needed so the pion widths get updated
        #--when they are set equal to the proton widths
        try:
            semaphore['pdf']
            if semaphore['pdf']==1 and 'pdfpi-' in conf['params']: semaphore['pdfpi-']=1
        except KeyError: pass
        try: 
            semaphore['ffpi']
            if semaphore['ffpi']==1 and 'ffk' in conf['params']: semaphore['ffk']=1
        except KeyError: pass
        try: 
            semaphore['ffpi']
            if semaphore['ffpi']==1 and 'ffh' in conf['params']: semaphore['ffh']=1
        except KeyError: pass

        self.propagate_params(semaphore)

    def gen_report(self):
        L=[]
        cnt=0
        for k in conf['params']:
            for kk in sorted(conf['params'][k]):
                if  conf['params'][k][kk]['fixed']==False:
                    cnt+=1
                    if  conf['params'][k][kk]['value']<0:
                        L.append('%d %10s  %10s  %10.5e'%(cnt,k,kk,conf['params'][k][kk]['value']))
                    else:
                        L.append('%d %10s  %10s   %10.5e'%(cnt,k,kk,conf['params'][k][kk]['value']))

        for k in conf['datasets']:
            for kk in conf['datasets'][k]['norm']:
                if  conf['datasets'][k]['norm'][kk]['fixed']==False:
                    cnt+=1
                    L.append('%d %10s %10s %10d  %10.5e'%(cnt,'norm',k,kk,conf['datasets'][k]['norm'][kk]['value']))
        return L

    def propagate_params(self,semaphore):

      if 'version' in conf: version=conf['version']
      else: version=0 #--for back compatibility

      flag=False
      if 'pdf'          in semaphore and semaphore['pdf']          == 1: self.set_pdf_params()
      if 'pdfpi-'       in semaphore and semaphore['pdfpi-']       == 1: self.set_pdfpi_params()
      if 'transversity' in semaphore and semaphore['transversity'] == 1: self.set_transversity_params(version)
      if 'sivers'       in semaphore and semaphore['sivers']       == 1: self.set_sivers_params(version)
      if 'boermulders'  in semaphore and semaphore['boermulders']  == 1: self.set_boermulders_params(version)
      if 'ffpi'         in semaphore and semaphore['ffpi']         == 1: self.set_ffpi_params()
      if 'ffk'          in semaphore and semaphore['ffk']          == 1: self.set_ffk_params()
      if 'ffh'          in semaphore and semaphore['ffh']          == 1: self.set_ffh_params()
      if 'collinspi'    in semaphore and semaphore['collinspi']    == 1: self.set_collinspi_params(version)
      if 'collinsk'     in semaphore and semaphore['collinsk']     == 1: self.set_collinsk_params(version)
      if 'Htildepi'     in semaphore and semaphore['Htildepi']     == 1: self.set_Htildepi_params(version)
      if 'Htildek'      in semaphore and semaphore['Htildek']      == 1: self.set_Htildek_params(version)

    def set_constraits(self,dist,FLAV=None,PAR=None,version=0):

        if (dist in ['pdf','pdfpi-','ffpi','ffk']) or (version==0):
            parkind=dist
            for k in conf['params'][parkind]:
                if conf['params'][parkind][k]['fixed'] == True:  continue
                elif conf['params'][parkind][k]['fixed'] == False: continue
                elif 'proton widths uv' in conf['params'][parkind][k]['fixed']:
                    conf['params'][parkind][k]['value'] = conf['params']['pdf']['widths1_uv']['value']
                elif 'proton widths sea' in conf['params'][parkind][k]['fixed']:
                    conf['params'][parkind][k]['value'] = conf['params']['pdf']['widths1_sea']['value']
                elif 'sivers' in conf['params'][parkind][k]['fixed']:
                    ref_par = conf['params'][parkind][k]['fixed'].replace('sivers','').strip()
                    conf['params'][parkind][k]['value'] = conf['params']['sivers'][ref_par]['value']
                elif '-' in conf['params'][parkind][k]['fixed']:
                    ref_par = conf['params'][parkind][k]['fixed'].replace('-','').strip()
                    conf['params'][parkind][k]['value'] = -conf['params'][parkind][ref_par]['value']
                else:
                    ref_par = conf['params'][parkind][k]['fixed']
                    conf['params'][parkind][k]['value'] = conf['params'][parkind][ref_par]['value']

        elif version=='JAM20+':
            for flav in FLAV:
                for par in PAR:
                    for s in ['1','2']:
                        if flav+' '+par+' '+s not in conf['params'][dist]: continue
                        if conf['params'][dist][flav+' '+par+' '+s]['fixed']==True: continue
                        if conf['params'][dist][flav+' '+par+' '+s]['fixed']==False: continue
                        reference_flav=conf['params'][dist][flav+' '+par+' '+s]['fixed']
                        conf['params'][dist][flav+' '+par+' '+s]['value']=conf['params'][dist][reference_flav]['value']

    def set_params(self,dist,FLAV,PAR,version,dist2=None):

        if version==0:
            iflav=0
            for flav in FLAV:
                iflav+=1
                ipar=-1
                for par in PAR:
                    ipar+=1
                    if '%s %s 1'%(flav,par) in conf['params'][dist]:
                        conf[dist].shape1[iflav][ipar] = conf['params'][dist]['%s %s 1'%(flav,par)]['value']
                        if 'd'+dist in conf: conf['d'+dist].shape1[iflav][ipar] = conf['params'][dist]['%s %s 1'%(flav,par)]['value']
                    if '%s %s 2'%(flav,par) in conf['params'][dist]:
                        conf[dist].shape2[iflav][ipar] = conf['params'][dist]['%s %s 2'%(flav,par)]['value']
                        if 'd'+dist in conf: conf['d'+dist].shape2[iflav][ipar] = conf['params'][dist]['%s %s 2'%(flav,par)]['value']

            conf[dist].setup()

        elif version=='JAM20+':
            #--update values at the class
            for flav in FLAV:
                idx=0
                for s in ['1','2']:
                    for par in PAR:
                        if  flav+' '+par+' '+s in conf['params'][dist]:
                            conf[dist].params[flav][idx]=conf['params'][dist][flav+' '+par+' '+s]['value']
                        else:
                            conf[dist].params[flav][idx]=0
                        idx+=1

            conf[dist].setup()

            #--update values at conf
            for flav in FLAV:
                idx=0
                for s in ['1','2']:
                    for par in PAR:
                        if  flav+' '+par+' '+s in conf['params'][dist]:
                            conf['params'][dist][flav+' '+par+' '+s]['value']= conf[dist].params[flav][idx]
                        idx+=1

    def set_pdf_params(self):
        self.set_constraits('pdf')
        hadron='p'
        conf['pdf']._widths1_uv  = conf['params']['pdf']['widths1_uv' ]['value']
        conf['pdf']._widths1_dv  = conf['params']['pdf']['widths1_dv' ]['value']
        conf['pdf']._widths1_sea = conf['params']['pdf']['widths1_sea']['value']
        conf['pdf']._widths2_uv  = conf['params']['pdf']['widths2_uv' ]['value']
        conf['pdf']._widths2_dv  = conf['params']['pdf']['widths2_dv' ]['value']
        conf['pdf']._widths2_sea = conf['params']['pdf']['widths2_sea']['value']
        conf['pdf'].setup(hadron)

    def set_pdfpi_params(self):
        self.set_constraits('pdfpi-')
        hadron='pi-'
        conf['pdfpi-']._widths1_ubv = conf['params']['pdfpi-']['widths1_ubv' ]['value']
        conf['pdfpi-']._widths1_dv  = conf['params']['pdfpi-']['widths1_dv' ]['value']
        conf['pdfpi-']._widths1_sea = conf['params']['pdfpi-']['widths1_sea']['value']
        conf['pdfpi-']._widths2_ubv = conf['params']['pdfpi-']['widths2_ubv' ]['value']
        conf['pdfpi-']._widths2_dv  = conf['params']['pdfpi-']['widths2_dv' ]['value']
        conf['pdfpi-']._widths2_sea = conf['params']['pdfpi-']['widths2_sea']['value']
        conf['pdfpi-'].setup(hadron)

    def set_transversity_params(self,version):
        self.set_constraits('transversity')
        conf['transversity']._widths1_uv  = conf['params']['transversity']['widths1_uv']['value']
        conf['transversity']._widths1_dv  = conf['params']['transversity']['widths1_dv']['value']
        conf['transversity']._widths1_sea = conf['params']['transversity']['widths1_sea']['value']

        conf['transversity']._widths2_uv  = conf['params']['transversity']['widths2_uv']['value']
        conf['transversity']._widths2_dv  = conf['params']['transversity']['widths2_dv']['value']
        conf['transversity']._widths2_sea = conf['params']['transversity']['widths2_sea']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='transversity'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','uv1','dv1','sea1','sea2','db1','ub1','s1','sb1']
            PAR=['N','a','b','c','d']
            dist='transversity'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_sivers_params(self,version):
        self.set_constraits('sivers')
        conf['sivers']._widths1_uv  = conf['params']['sivers']['widths1_uv']['value']
        conf['sivers']._widths1_dv  = conf['params']['sivers']['widths1_dv']['value']
        conf['sivers']._widths1_sea = conf['params']['sivers']['widths1_sea']['value']

        conf['sivers']._widths2_uv  = conf['params']['sivers']['widths2_uv']['value']
        conf['sivers']._widths2_dv  = conf['params']['sivers']['widths2_dv']['value']
        conf['sivers']._widths2_sea = conf['params']['sivers']['widths2_sea']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='sivers'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','uv1','dv1','sea1','sea2','db1','ub1','s1','sb1']
            PAR=['N','a','b','c','d']
            dist='sivers'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)
            conf['dsivers'].BC3=conf['sivers'].BC3
            conf['dsivers'].BC4=conf['sivers'].BC4
            conf['dsivers'].BC5=conf['sivers'].BC5
            conf['dsivers'].storage={}

    def set_boermulders_params(self,version):
        self.set_constraits('boermulders')
        conf['boermulders']._widths1_uv  = conf['params']['boermulders']['widths1_uv']['value']
        conf['boermulders']._widths1_dv  = conf['params']['boermulders']['widths1_dv']['value']
        conf['boermulders']._widths1_sea = conf['params']['boermulders']['widths1_sea']['value']

        conf['boermulders']._widths2_uv  = conf['params']['boermulders']['widths2_uv']['value']
        conf['boermulders']._widths2_dv  = conf['params']['boermulders']['widths2_dv']['value']
        conf['boermulders']._widths2_sea = conf['params']['boermulders']['widths2_sea']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='boermulders'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','uv1','dv1','sea1','sea2','db1','ub1','s1','sb1']
            PAR=['N','a','b','c','d']
            dist='boermulders'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_ffpi_params(self):
        self.set_constraits('ffpi')
        conf['ffpi']._widths1_fav  = conf['params']['ffpi']['widths1_fav']['value']
        conf['ffpi']._widths1_ufav = conf['params']['ffpi']['widths1_ufav']['value']
        conf['ffpi']._widths2_fav  = conf['params']['ffpi']['widths2_fav']['value']
        conf['ffpi']._widths2_ufav = conf['params']['ffpi']['widths2_ufav']['value']
        conf['ffpi'].setup()

    def set_ffk_params(self):
        self.set_constraits('ffk')
        conf['ffk']._widths1_fav   = conf['params']['ffk']['widths1_fav']['value']
        conf['ffk']._widths1_ufav  = conf['params']['ffk']['widths1_ufav']['value']
        conf['ffk']._widths2_fav   = conf['params']['ffk']['widths2_fav']['value']
        conf['ffk']._widths2_ufav  = conf['params']['ffk']['widths2_ufav']['value']
        conf['ffk'].setup()

    def set_ffh_params(self):
        self.set_constraits('ffh')
        conf['ffh']._widths1_fav   = conf['params']['ffh']['widths1_fav']['value']
        conf['ffh']._widths1_ufav  = conf['params']['ffh']['widths1_ufav']['value']
        conf['ffh']._widths2_fav   = conf['params']['ffh']['widths2_fav']['value']
        conf['ffh']._widths2_ufav  = conf['params']['ffh']['widths2_ufav']['value']
        conf['ffh'].setup()

    def set_collinspi_params(self,version):
        self.set_constraits('collinspi')
        conf['collinspi']._widths1_fav  = conf['params']['collinspi']['widths1_fav']['value']
        conf['collinspi']._widths1_ufav = conf['params']['collinspi']['widths1_ufav']['value']
        conf['collinspi']._widths2_fav  = conf['params']['collinspi']['widths2_fav']['value']
        conf['collinspi']._widths2_ufav = conf['params']['collinspi']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='collinspi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='collinspi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)
            conf['dcollinspi'].BC3=conf['collinspi'].BC3
            conf['dcollinspi'].BC4=conf['collinspi'].BC4
            conf['dcollinspi'].BC5=conf['collinspi'].BC5
            conf['dcollinspi'].storage={}

    def set_collinsk_params(self):
        self.set_constraits('collinsk')
        conf['collinsk']._widths1_fav   = conf['params']['collinsk']['widths1_fav']['value']
        conf['collinsk']._widths1_ufav  = conf['params']['collinsk']['widths1_ufav']['value']
        conf['collinsk']._widths2_fav   = conf['params']['collinsk']['widths2_fav']['value']
        conf['collinsk']._widths2_ufav  = conf['params']['collinsk']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='collinsk'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='collinsk'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_Htildepi_params(self,version):
        self.set_constraits('Htildepi')
        conf['Htildepi']._widths1_fav  = conf['params']['Htildepi']['widths1_fav']['value']
        conf['Htildepi']._widths1_ufav = conf['params']['Htildepi']['widths1_ufav']['value']
        conf['Htildepi']._widths2_fav  = conf['params']['Htildepi']['widths2_fav']['value']
        conf['Htildepi']._widths2_ufav = conf['params']['Htildepi']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='Htildepi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='Htildepi'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

    def set_Htildek_params(self,version):
        self.set_constraits('Htildek')
        conf['Htildek']._widths1_fav   = conf['params']['Htildek']['widths1_fav']['value']
        conf['Htildek']._widths1_ufav  = conf['params']['Htildek']['widths1_ufav']['value']
        conf['Htildek']._widths2_fav   = conf['params']['Htildek']['widths2_fav']['value']
        conf['Htildek']._widths2_ufav  = conf['params']['Htildek']['widths2_ufav']['value']

        if version == 0:
            FLAV = ['u','ub','d','db','s','sb']
            PAR = ['N0','a0','b0','c0','d0','N1','a1','b1','c1','d1']
            dist='Htildek'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)

        if version == 'JAM20+':
            FLAV=['g1','u1','d1','s1','c1','b1','ub1','db1','sb1','cb1','bb1']
            PAR=['N','a','b','c','d']
            dist='Htildek'
            self.set_constraits(dist,FLAV,PAR,version)
            self.set_params(dist,FLAV,PAR,version)





