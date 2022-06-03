#!/usr/bin/env python
import os,sys
import subprocess
import numpy as np
import scipy as sp
import pandas as pd
import copy
import random
import itertools as it

from scipy import interpolate

#--from tools
from tools.tools     import load,save,checkdir,lprint
from tools.config    import conf,load_config

class CORE:

    def get_istep(self):
        #--pick last step
        return sorted(conf['steps'])[-1] 

    def get_replicas(self,wdir):
        """
        load the msr files
        """
        replicas=sorted(os.listdir('%s/msr-inspected'%wdir))
        replicas=[load('%s/msr-inspected/%s'%(wdir,_)) for _ in replicas]
        #print(replicas)
        return replicas

    def set_passive_distributions(self,conf,istep):
        print('setting passive for istep ',istep)
        step=conf['steps'][istep]
        for dist in step['passive distributions']:
            for par in conf['params'][dist]:
                #print(dist, par)
                conf['params'][dist][par]['fixed']=True
        return conf

    def fix_parameters(self,conf,istep):
        step=conf['steps'][istep]
        for dist in step['fix parameters']:
            for par in step['fix parameters'][dist]:
                conf['params'][dist][par]['fixed']=True
        return conf

    def set_passive_params(self,istep,prior):
        step=conf['steps'][istep]
        if 'passive distributions' not in step: return
        for dist in step['passive distributions']:
            for par in conf['params'][dist]:
                #conf['params'][dist][par]['fixed']=True
                for idep in step['dep']:
                    for i in range(len(prior['order'][idep])):
                        _,_dist,_par = prior['order'][idep][i]
                        if  dist==_dist and par==_par:
                            conf['params'][dist][par]['value']=prior['params'][idep][i]

            if dist=='pdf'    : self.parman.set_pdf_params()
            if dist=='pdfpi'    : self.parman.set_pdfpi_params()
            if dist=='ppdf'   : self.parman.set_ppdf_params()
            if dist=='ffpi' : self.parman.set_ffpion_params()
            if dist=='ffkaon' : self.parman.set_ffkaon_params()

    def get_conf(self,_conf,istep,hooks=None):
        conf=copy.deepcopy(_conf)
        step=conf['steps'][istep]

        #--keep only actice distributions  that is not in the step
        params=conf['params'].keys()  #--pdf,ppdf,ffpion,ffkaon,...
        for param in list(params):
            if  param in step['active distributions']:
                continue
            else:
                del conf['params'][param]

        #--set fixed==True for passive distributions
        if 'passive distributions' in step:
            conf.update(self.set_passive_distributions(conf,istep))

        #--fix parameters
        if 'fix parameters' in step:
            conf.update(self.fix_parameters(conf,istep))

        #--isolate a reaction from step
        if hooks!=None:
            if 'reaction' in hooks and hooks['reaction']!='all':
                reaction=hooks['reaction']
                veto=[_ for _ in conf['steps'][istep]['datasets'] if _!=reaction]
                for  _ in veto:
                    del conf['steps'][istep]['datasets'][_]

            if  'sidis-pdf-flav' in hooks and hooks['sidis-pdf-flav']!=None:
                conf['sidis-pdf-flav']=hooks['sidis-pdf-flav']

            if  'sidis-ff-flav' in  hooks and hooks['sidis-ff-flav']!=None:
                conf['sidis-ff-flav']=hooks['sidis-ff-flav']

        #--remove datasets not in the step
        datasets=conf['datasets'].keys() #--idis,dy,....
        for dataset in list(datasets):
            if  dataset in step['datasets']:

                #--remove entry from xlsx
                xlsx=conf['datasets'][dataset]['xlsx'].keys()
                xlsx=conf['datasets'][dataset]['xlsx'].keys()
                for idx in list(xlsx):
                    if  idx in step['datasets'][dataset]:
                        continue
                    else:
                        del conf['datasets'][dataset]['xlsx'][idx]

                #--remove entry from norm
                norm=conf['datasets'][dataset]['norm'].keys()
                for idx in list(norm):
                    if  idx in step['datasets'][dataset]:
                        continue
                    else:
                        del conf['datasets'][dataset]['norm'][idx]
            else:
                del conf['datasets'][dataset]

        return conf

    def mod_conf(self, istep, replica=None):
    
        step=conf['steps'][istep]
    
        #--remove pdf/ff that is not in the step
        distributions=list(conf['params'])  #--pdf,ppdf,ffpion,ffkaon,...
        for dist in distributions:
            if  dist in step['active distributions']:  continue
            elif 'passive distributions' in step and dist in step['passive distributions']:  continue
            else:
                del conf['params'][dist] 
    
        if np.any(replica)!=None:
            #--set fixed==True for passive distributions
            if 'passive distributions' in step:
                for dist in step['passive distributions']:
                    for par in conf['params'][dist]:
                        if conf['params'][dist][par]['fixed']==False:
                            conf['params'][dist][par]['fixed']=True
    
                        #--set prior parameters values for passive distributions
                        for _istep in step['dep']:
                            prior_order=replica['order'][_istep]
                            prior_params=replica['params'][_istep]
                            for i in range(len(prior_order)):
                                _,_dist,_par = prior_order[i]
                                if  dist==_dist and par==_par:
                                    #--update values in conf
                                    conf['params'][dist][par]['value']=prior_params[i]
                                    #--update values at class
                                    if dist not in conf: continue
                                    PAR  = conf[dist].PAR
                                    idx = conf[dist].PAR.index(par.split()[1])
                                    flav = par.split()[0]
                                    conf[dist].params[flav][idx] = prior_params[i]
                                    conf[dist].setup()
    
        #--remove datasets not in the step
        datasets=list(conf['datasets']) #--idis,dy,....
        for dataset in datasets:
            if  dataset in step['datasets']:  
    
                #--remove entry from xlsx
                xlsx=list(conf['datasets'][dataset]['xlsx'])
                for idx in xlsx:
                    if  idx in step['datasets'][dataset]:
                        continue
                    else:
                        del conf['datasets'][dataset]['xlsx'][idx]
    
                #--remove entry from norm
                norm=list(conf['datasets'][dataset]['norm'])
                for idx in norm:
                    if  idx in step['datasets'][dataset]:
                        continue
                    else:
                        del conf['datasets'][dataset]['norm'][idx]
            else:
                del conf['datasets'][dataset]  
    
        if 'passive distributions' in conf['steps'][istep] and replica != None:
            if len(conf['steps'][istep]['passive distributions']) > 0: 
                get_passive_data(istep,replica)

    def gen_jar_file(self,wdir):
    
        print('\ngen jar file using (best cluster) %s\n'%wdir)
    
        replicas=self.get_replicas(wdir)
        conf={}
        load_config('%s/input.py'%wdir)
        istep=self.get_istep()
        self.mod_conf(istep,replicas[0]) #--set conf as specified in istep   
    
        conf['order']=replicas[0]['order'][istep]
        conf['replicas']=[]
    
        cnt=0
        for i in range(len(replicas)):
            replica=replicas[i]
            cnt+=1
            conf['replicas'].append(replica['params'][istep])
        print('number of  replicas = %d'%cnt)
      
        checkdir('%s/data'%wdir)
        save(conf,'%s/data/jar-%d.dat'%(wdir,istep))


