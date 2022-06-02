#!/usr/bin/env python
import sys,os
#sys.path.append(os.path.dirname( os.path.dirname(os.path.abspath(__file__) ) ) )
import numpy as np

os.environ["LHAPDF_DATA_PATH"] = '/work/JAM/ccocuzza/WormGearLHAPDF/lhapdf/sets'


import lhapdf
import argparse
#--matplotlib
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
matplotlib.rc('text',usetex=True)
import pylab  as py

#--index conventions:
#--index conventions:
#--1: down
#--2: up
#--3: strange
#--4: charm
#--5: bottom
#--6: top
#--21: gluon
#--negative values for antiquarks



Q2=[10,1000,10000]
X1=10**np.linspace(-4,-1)
X2=np.linspace(0.101,0.99)
X=np.append(X1,X2)

def get_data(target):
    #--set up dictionary based on target
    data = {_:{} for _ in ['idx','color','label','nrep']}

    if target=='proton':

        tag = 'p'
        tabnames=[        
                   'CT18ptxg'
                  ,'NNPDF31_lo_as_0118_SF'
                  ,'NNPDF31_nnlo_pch_as_0118_NC_Wm_Wp_SF'
                  ,'JAM4EIC_p'
                 ]
        
        data['idx']['CT18ptxg'] = [900,901,902,903,904,905,906,907,908,909,910,930,931,932]
        data['idx']['NNPDF31_lo_as_0118_SF'] = [908,909,910,940,941,942,930,931,932]
        data['idx']['NNPDF31_nnlo_pch_as_0118_NC_Wm_Wp_SF'] = [900,901,902,903,904,905,906,907,908,909,910,940,941,942,930,931,932]
        data['idx']['JAM4EIC_p'] = [900,901,902,903,904,905,906,907,908,909,910,940,941,942,930,931,932]
       
        data['nrep']['CT18ptxg'] =  0
        data['nrep']['NNPDF31_lo_as_0118_SF'] = 100
        data['nrep']['NNPDF31_nnlo_pch_as_0118_NC_Wm_Wp_SF'] = 0
        data['nrep']['JAM4EIC_p'] = 50
 
        data['color']['CT18ptxg'] =  'red'
        data['color']['NNPDF31_lo_as_0118_SF'] = 'blue'
        data['color']['NNPDF31_nnlo_pch_as_0118_NC_Wm_Wp_SF'] = 'orange'
        data['color']['JAM4EIC_p'] = 'green'

        data['label']['CT18ptxg'] =  'CT18'
        data['label']['NNPDF31_lo_as_0118_SF'] = 'NNPDF31 LO'
        data['label']['NNPDF31_nnlo_pch_as_0118_NC_Wm_Wp_SF'] = 'NNPDF31 NNLO'
        data['label']['JAM4EIC_p'] = 'JAM'

    elif target=='deuteron':

        tag = 'd'
        tabnames=[        
                  'JAM4EIC_d'
                 ]
        
        data['idx']['JAM4EIC_d'] = [900,901,902,903,904,905,906,907,908,909,910]
        
        data['nrep']['JAM4EIC_d'] = 50

        data['color']['JAM4EIC_d'] = 'green'

        data['label']['JAM4EIC_d'] = 'JAM'

    elif target=='helium':

        tag = 'h'
        tabnames=[        
                  'JAM4EIC_h'
                 ]
        
        data['idx']['JAM4EIC_h'] = [900,901,902,903,904,905,906,907,908,909,910]
        
        data['nrep']['JAM4EIC_h'] = 50

        data['color']['JAM4EIC_h'] = 'green'
        data['label']['JAM4EIC_h'] = 'JAM'

    else:
        print('Target: %s is not available!'%target)

    return data,tabnames,tag

def plot_stf(target):
   
    data,tabnames,tag = get_data(target) 
 
    #--collect data from different groups 
    for tabname in tabnames:
        data[tabname] = {}
        nrep = data['nrep'][tabname]
        idxs = data['idx'][tabname]
        for q2 in Q2: data[tabname][q2] = {_:[] for _ in idxs}
        for i in range(nrep+1): 
            stf=lhapdf.mkPDF(tabname,i)
            for q2 in Q2:
                for idx in idxs:
                    F=np.array([x*stf.xfxQ2(idx,x,q2) for x in X])
                    data[tabname][q2][idx].append(F)

    #--plot data
 
    #--all channels 
    nrows,ncols=3,3
    fig = py.figure(figsize=(ncols*5,nrows*3))
    
    cnt=0
    for q2 in Q2:
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 908 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F2=data[tabname][q2][908][i]
                ax.plot(X,F2,label=label,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,2)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==1: ax.legend(loc='lower left',bbox_to_anchor=(0,0.1),frameon=False,fontsize=15)
        if cnt==1: ax.text(0.1,0.7,r'$xF_2^{(%s)}$'%tag,size=35,transform=ax.transAxes)
        if cnt==7: ax.set_xlabel(r'$x$',size=20)
        ax.set_ylabel(r'$Q^2=%0.1f~{\rm GeV^2}$'%q2,size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 909 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                FL=data[tabname][q2][909][i]
                ax.plot(X,FL,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,0.3)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==2: ax.text(0.1,0.7,r'$xF_L^{(%s)}$'%tag,size=35,transform=ax.transAxes)
        if cnt==8: ax.set_xlabel(r'$x$',size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 910 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F3=data[tabname][q2][910][i]
                ax.plot(X,F3,color=data['color'][tabname],alpha=alpha)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        #ax.set_ylim(0,0.9)
        if cnt==3: ax.text(0.1,0.7,r'$xF_3^{(%s)}$'%tag,size=35,transform=ax.transAxes)
        if cnt==9: ax.set_xlabel(r'$x$',size=20)
    
    py.tight_layout()
    filename = 'gallery/%s/FX.png'%target
    py.savefig(filename)
    print('Saving figure to %s'%filename)
    py.clf()
       
    
    
    #--gamma channel
    nrows,ncols=3,2
    fig = py.figure(figsize=(ncols*5,nrows*3))
    
    cnt=0
    for q2 in Q2:
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 900 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F2=data[tabname][q2][900][i]
                ax.plot(X,F2,label=label,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,2)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==1: ax.legend(loc='lower left',bbox_to_anchor=(0,0.1),frameon=False,fontsize=15)
        if cnt==1: ax.text(0.1,0.7,r'$xF_2^{(%s)\gamma}$'%tag,size=35,transform=ax.transAxes)
        if cnt==7: ax.set_xlabel(r'$x$',size=20)
        ax.set_ylabel(r'$Q^2=%0.1f~{\rm GeV^2}$'%q2,size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 901 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                FL=data[tabname][q2][901][i]
                ax.plot(X,FL,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,0.3)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==2: ax.text(0.1,0.7,r'$xF_L^{(%s)\gamma}$'%tag,size=35,transform=ax.transAxes)
        if cnt==8: ax.set_xlabel(r'$x$',size=20)
    
    
    py.tight_layout()
    filename = 'gallery/%s/FXg.png'%target
    py.savefig(filename)
    print('Saving figure to %s'%filename)
    py.clf()
    
    #--Z channel
    nrows,ncols=3,3
    fig = py.figure(figsize=(ncols*5,nrows*3))
    
    cnt=0
    for q2 in Q2:
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 905 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F2=data[tabname][q2][905][i]
                ax.plot(X,F2,label=label,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,2)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==1: ax.legend(loc='lower left',bbox_to_anchor=(0,0.1),frameon=False,fontsize=15)
        if cnt==1: ax.text(0.1,0.7,r'$xF_2^{(%s)Z}$'%tag,size=35,transform=ax.transAxes)
        if cnt==7: ax.set_xlabel(r'$x$',size=20)
        ax.set_ylabel(r'$Q^2=%0.1f~{\rm GeV^2}$'%q2,size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 906 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                FL=data[tabname][q2][906][i]
                ax.plot(X,FL,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,0.3)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==2: ax.text(0.1,0.7,r'$xF_L^{(%s)Z}$'%tag,size=35,transform=ax.transAxes)
        if cnt==8: ax.set_xlabel(r'$x$',size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 907 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F3=data[tabname][q2][907][i]
                ax.plot(X,F3,color=data['color'][tabname],alpha=alpha)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        #ax.set_ylim(0,0.9)
        if cnt==3: ax.text(0.1,0.7,r'$xF_3^{(%s)Z}$'%tag,size=35,transform=ax.transAxes)
        if cnt==9: ax.set_xlabel(r'$x$',size=20)
    
    
    py.tight_layout()
    filename = 'gallery/%s/FXZ.png'%target
    py.savefig(filename)
    print('Saving figure to %s'%filename)
    py.clf()
    
    
    
    
    #--gamma/Z channel
    nrows,ncols=3,3
    fig = py.figure(figsize=(ncols*5,nrows*3))
    
    cnt=0
    for q2 in Q2:
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 902 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F2=data[tabname][q2][902][i]
                ax.plot(X,F2,label=label,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,2)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==1: ax.legend(loc='lower left',bbox_to_anchor=(0,0.1),frameon=False,fontsize=15)
        if cnt==1: ax.text(0.1,0.7,r'$xF_2^{(%s)\gamma Z}$'%tag,size=35,transform=ax.transAxes)
        if cnt==7: ax.set_xlabel(r'$x$',size=20)
        ax.set_ylabel(r'$Q^2=%0.1f~{\rm GeV^2}$'%q2,size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 903 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                FL=data[tabname][q2][903][i]
                ax.plot(X,FL,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,0.3)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==2: ax.text(0.1,0.7,r'$xF_L^{(%s)\gamma Z}$'%tag,size=35,transform=ax.transAxes)
        if cnt==8: ax.set_xlabel(r'$x$',size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 904 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F3=data[tabname][q2][904][i]
                ax.plot(X,F3,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,0.25)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==3: ax.text(0.1,0.7,r'$xF_3^{(%s)\gamma Z}$'%tag,size=35,transform=ax.transAxes)
        if cnt==9: ax.set_xlabel(r'$x$',size=20)
    
    
    py.tight_layout()
    filename = 'gallery/%s/FXgZ.png'%target
    py.savefig(filename)
    print('Saving figure to %s'%filename)
    py.clf()
   
    #--no charged current for deuteron/helium
    if target=='deuteron': return
    if target=='helium':   return

 
    #--W plus
    nrows,ncols=3,3
    fig = py.figure(figsize=(ncols*5,nrows*3))
    
    cnt=0
    for q2 in Q2:
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 940 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F2=data[tabname][q2][940][i]
                ax.plot(X,F2,label=label,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,12)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==1: ax.legend(loc='lower left',bbox_to_anchor=(0,0.1),frameon=False,fontsize=15)
        if cnt==1: ax.text(0.1,0.7,r'$xF_2^{(%s)W^+}$'%tag,size=35,transform=ax.transAxes)
        if cnt==7: ax.set_xlabel(r'$x$',size=20)
        ax.set_ylabel(r'$Q^2=%0.1f~{\rm GeV^2}$'%q2,size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 941 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                FL=data[tabname][q2][941][i]
                ax.plot(X,FL,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,2.5)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==2: ax.text(0.1,0.7,r'$xF_L^{(%s)W^+}$'%tag,size=35,transform=ax.transAxes)
        if cnt==8: ax.set_xlabel(r'$x$',size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 942 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F3=data[tabname][q2][942][i]
                ax.plot(X,F3,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,20)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==3: ax.text(0.1,0.7,r'$xF_3^{(%s)W^+}$'%tag,size=35,transform=ax.transAxes)
        if cnt==9: ax.set_xlabel(r'$x$',size=20)
    
    
    py.tight_layout()
    filename = 'gallery/%s/WXp.png'%target
    py.savefig(filename)
    print('Saving figure to %s'%filename)
    py.clf()
    
    
    #--W minus
    nrows,ncols=3,3
    fig = py.figure(figsize=(ncols*5,nrows*3))
    
    cnt=0
    for q2 in Q2:
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 930 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F2=data[tabname][q2][930][i]
                ax.plot(X,F2,label=label,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,12)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==1: ax.legend(loc='lower left',bbox_to_anchor=(0,0.1),frameon=False,fontsize=15)
        if cnt==1: ax.text(0.1,0.7,r'$xF_2^{(%s)W^-}$'%tag,size=35,transform=ax.transAxes)
        if cnt==7: ax.set_xlabel(r'$x$',size=20)
        ax.set_ylabel(r'$Q^2=%0.1f~{\rm GeV^2}$'%q2,size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 931 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                FL=data[tabname][q2][931][i]
                ax.plot(X,FL,color=data['color'][tabname],alpha=alpha)
        #ax.set_ylim(0,2.5)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        if cnt==2: ax.text(0.1,0.7,r'$xF_L^{(%s)W^-}$'%tag,size=35,transform=ax.transAxes)
        if cnt==8: ax.set_xlabel(r'$x$',size=20)
    
        cnt+=1
        ax=py.subplot(nrows,ncols,cnt)
        ax.tick_params(axis='both',which='both',top=True,right=True,direction='in',labelsize=20)
        for tabname in tabnames:
            if 932 not in data[tabname][q2]: continue
            for i in range(data['nrep'][tabname]+1):
                if i == 0: label, alpha = data['label'][tabname], 1.0
                else:      label, alpha = None, 0.1
                F3=data[tabname][q2][932][i]
                ax.plot(X,F3,color=data['color'][tabname],alpha=alpha)
        ax.semilogx()
        ax.set_xticks([10e-5,10e-4,10e-3,10e-2,10e-1,1])
        ax.axhline(0,0,1,ls='--',color='black',alpha=0.5)
        #ax.set_ylim(0,20)
        if cnt==3: ax.text(0.1,0.7,r'$xF_3^{(%s)W^-}$'%tag,size=35,transform=ax.transAxes)
        if cnt==9: ax.set_xlabel(r'$x$',size=20)
    
    
    py.tight_layout()
    filename = 'gallery/%s/WXm.png'%target
    py.savefig(filename)
    print('Saving figure to %s'%filename)
    py.clf()

def plot_tpdfs(self,wdir,file_name,Q2,mode=0):

    nrows,ncols=1,2
    fig = py.figure(figsize=(ncols*7,nrows*4))
    ax11=py.subplot(nrows,ncols,1)
    ax12=py.subplot(nrows,ncols,2)

    hand = {}

    os.environ["LHAPDF_DATA_PATH"] = '/w/jam-sciwork18/ccocuzza/WormGearLHAPDF/%s/data'%(wdir)
    QCF = lhapdf.mkPDFs(file_name)
    nrep = len(PDF)

    flavs = ['u','d']
    data = {flav: [] for flav in flavs} 

    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        d =  np.array([QCF[i].xfxQ2( 1,x,Q2) for x in X])
        u =  np.array([QCF[i].xfxQ2( 2,x,Q2) for x in X])
        data['d'].append(d)
        data['u'].append(u)
        
    for flav in data:

        if   flav=='u': ax = ax11
        elif flav=='d': ax = ax12

        mean = np.mean(data[flav],axis=0)
        std  = np.std (data[flav],axis=0)

        if mode==0:
            for i in range(nrep-1):
                ax.plot(X,data[flav][i],color='red',alpha=0.1)
 
        #--plot average and standard deviation
        if mode==1:
            ax.fill_between(X,mean-std,mean+std,color='red',alpha=0.9)


    for ax in [ax11,ax12]:
          ax.set_xlim(0,1)
            
          ax.tick_params(axis='both', which='major', top=True, right=True, direction='in',labelsize=30,length=10)
          ax.tick_params(axis='both', which='minor', top=True, right=True, direction='in',labelsize=30,length=5)
          ax.set_xticks([0.2,0.4,0.6,0.8])
          #ax.set_xticklabels([r'$0.01$',r'$0.1$',r'$1$'])

    ax11.set_ylim(-0.1,0.6)
    ax12.set_ylim(-0.3,0.2)

    ax11.set_yticks([0,0.2,0.4])
    ax12.set_yticks([-0.2,-0.1,0])

    minorLocator = MultipleLocator(0.05)
    ax11.yaxis.set_minor_locator(minorLocator)
    ax12.yaxis.set_minor_locator(minorLocator)

    for ax in [ax11,ax12]:
        ax.set_xlabel(r'\boldmath$x$' ,size=30)
        ax.xaxis.set_label_coords(0.90,0.00)

    ax11.text(0.85 ,0.50  ,r'\boldmath{$u$}'            , transform=ax11.transAxes,size=30)
    ax12.text(0.60 ,0.20  ,r'\boldmath{$d$}'            , transform=ax12.transAxes,size=30)

    ax11.set_ylabel(r'$xh_1(x)$',size=30)

    if Q2 == 1.27**2: ax12.text(0.05,0.08,r'$Q^2 = m_c^2$'                                  , transform=ax12.transAxes,size=30)
    else:             ax12.text(0.05,0.08,r'$Q^2 = %s$'%Q2 + ' ' + r'\textrm{GeV}' + r'$^2$', transform=ax12.transAxes,size=30)

    ax11.axhline(0.0,ls='--',color='black',alpha=0.5)
    ax12.axhline(0.0,ls='--',color='black',alpha=0.5)

    py.tight_layout()
    py.subplots_adjust(hspace = 0, wspace = 0.20)

    filename = '%s/gallery/lhapdf-tpdfs-Q2=%3.5f'%(wdir,Q2)
    if mode==1: filename += '-bands'
    filename+='.png'

    py.savefig(filename)
    py.clf()
    print ('Saving figure to %s'%filename)

def plot_f1T(self,wdir,file_name,Q2,mode=0):

    nrows,ncols=1,2
    fig = py.figure(figsize=(ncols*7,nrows*4))
    ax11=py.subplot(nrows,ncols,1)
    ax12=py.subplot(nrows,ncols,2)

    hand = {}

    os.environ["LHAPDF_DATA_PATH"] = '/w/jam-sciwork18/ccocuzza/WormGearLHAPDF/%s/data'%(wdir)
    QCF = lhapdf.mkPDFs(file_name)
    nrep = len(PDF)

    flavs = ['u','d']
    data = {flav: [] for flav in flavs} 

    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        d =  np.array([QCF[i].xfxQ2( 1,x,Q2) for x in X])
        u =  np.array([QCF[i].xfxQ2( 2,x,Q2) for x in X])
        data['d'].append(d)
        data['u'].append(u)
        
    for flav in data:

        if   flav=='u': ax = ax11
        elif flav=='d': ax = ax12

        mean = np.mean(data[flav],axis=0)
        std  = np.std (data[flav],axis=0)

        if mode==0:
            for i in range(nrep-1):
                ax.plot(X,data[flav][i],color='red',alpha=0.1)
 
        #--plot average and standard deviation
        if mode==1:
            ax.fill_between(X,mean-std,mean+std,color='red',alpha=0.9)


    for ax in [ax11,ax12]:
          ax.set_xlim(0,0.8)
            
          ax.tick_params(axis='both', which='major', top=True, right=True, direction='in',labelsize=30,length=10)
          ax.tick_params(axis='both', which='minor', top=True, right=True, direction='in',labelsize=30,length=5)
          ax.set_xticks([0.2,0.4,0.6])
          #ax.set_xticklabels([r'$0.01$',r'$0.1$',r'$1$'])

    ax11.set_ylim(-0.04,0.00)
    ax12.set_ylim( 0.00,0.04)

    ax11.set_yticks([-0.04,-0.02,0.00])
    ax12.set_yticks([ 0.00, 0.02,0.04])

    minorLocator = MultipleLocator(0.005)
    ax11.yaxis.set_minor_locator(minorLocator)
    ax12.yaxis.set_minor_locator(minorLocator)

    for ax in [ax11,ax12]:
        ax.set_xlabel(r'\boldmath$x$' ,size=30)
        ax.xaxis.set_label_coords(0.90,0.00)

    ax11.text(0.85 ,0.50  ,r'\boldmath{$u$}'            , transform=ax11.transAxes,size=30)
    ax12.text(0.60 ,0.20  ,r'\boldmath{$d$}'            , transform=ax12.transAxes,size=30)

    ax11.set_ylabel(r'$xf_{1T}^{\perp(1)}(x)$',size=30)

    if Q2 == 1.27**2: ax12.text(0.05,0.08,r'$Q^2 = m_c^2$'                                  , transform=ax12.transAxes,size=30)
    else:             ax12.text(0.05,0.08,r'$Q^2 = %s$'%Q2 + ' ' + r'\textrm{GeV}' + r'$^2$', transform=ax12.transAxes,size=30)

    #ax11.axhline(0.0,ls='--',color='black',alpha=0.5)
    #ax12.axhline(0.0,ls='--',color='black',alpha=0.5)

    py.tight_layout()
    py.subplots_adjust(hspace = 0, wspace = 0.20)

    filename = '%s/gallery/lhapdf-f1T-Q2=%3.5f'%(wdir,Q2)
    if mode==1: filename += '-bands'
    filename+='.png'

    py.savefig(filename)
    py.clf()
    print ('Saving figure to %s'%filename)

def plot_H1perp(self,wdir,file_name,Q2,mode=0):

    nrows,ncols=1,2
    fig = py.figure(figsize=(ncols*7,nrows*4))
    ax11=py.subplot(nrows,ncols,1)
    ax12=py.subplot(nrows,ncols,2)

    hand = {}

    os.environ["LHAPDF_DATA_PATH"] = '/w/jam-sciwork18/ccocuzza/WormGearLHAPDF/%s/data'%(wdir)
    QCF = lhapdf.mkPDFs(file_name)
    nrep = len(PDF)

    flavs = ['fav','unf']
    data = {flav: [] for flav in flavs} 

    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        fav =  np.array([QCF[i].xfxQ2( 1,x,Q2) for x in X])
        unf =  np.array([QCF[i].xfxQ2( 2,x,Q2) for x in X])
        data['fav']  .append(fav)
        data['unf'].append(unfav)
        
    for flav in data:

        if   flav=='fav': ax = ax11
        elif flav=='unf': ax = ax12

        mean = np.mean(data[flav],axis=0)
        std  = np.std (data[flav],axis=0)

        if mode==0:
            for i in range(nrep-1):
                ax.plot(X,data[flav][i],color='red',alpha=0.1)
 
        #--plot average and standard deviation
        if mode==1:
            ax.fill_between(X,mean-std,mean+std,color='red',alpha=0.9)


    for ax in [ax11,ax12]:
          ax.set_xlim(0,1)
            
          ax.tick_params(axis='both', which='major', top=True, right=True, direction='in',labelsize=30,length=10)
          ax.tick_params(axis='both', which='minor', top=True, right=True, direction='in',labelsize=30,length=5)
          ax.set_xticks([0.2,0.4,0.6,0.8])
          #ax.set_xticklabels([r'$0.01$',r'$0.1$',r'$1$'])

    ax11.set_ylim( 0.0,0.4)
    ax12.set_ylim(-0.7,0.0)

    ax11.set_yticks([0.1,0.2,0.3])
    ax12.set_yticks([-0.4,0.0])

    minorLocator = MultipleLocator(0.05)
    ax11.yaxis.set_minor_locator(minorLocator)
    minorLocator = MultipleLocator(0.1)
    ax12.yaxis.set_minor_locator(minorLocator)

    for ax in [ax11,ax12]:
        ax.set_xlabel(r'\boldmath$z$' ,size=30)
        ax.xaxis.set_label_coords(0.90,0.00)

    ax11.text(0.85 ,0.50  ,r'\textrm{\textbf{fav}}'            , transform=ax11.transAxes,size=30)
    ax12.text(0.60 ,0.20  ,r'\textrm{\textbf{unf}}'            , transform=ax12.transAxes,size=30)

    ax11.set_ylabel(r'$zH_1^{\perp(1)}(z)$',size=30)

    if Q2 == 1.27**2: ax12.text(0.05,0.08,r'$Q^2 = m_c^2$'                                  , transform=ax12.transAxes,size=30)
    else:             ax12.text(0.05,0.08,r'$Q^2 = %s$'%Q2 + ' ' + r'\textrm{GeV}' + r'$^2$', transform=ax12.transAxes,size=30)

    #ax11.axhline(0.0,ls='--',color='black',alpha=0.5)
    #ax12.axhline(0.0,ls='--',color='black',alpha=0.5)

    py.tight_layout()
    py.subplots_adjust(hspace = 0, wspace = 0.20)

    filename = '%s/gallery/lhapdf-H1perp-Q2=%3.5f'%(wdir,Q2)
    if mode==1: filename += '-bands'
    filename+='.png'

    py.savefig(filename)
    py.clf()
    print ('Saving figure to %s'%filename)


if __name__=="__main__":

    ap = argparse.ArgumentParser()
    #--available targets: proton, deuteron, helium
    ap.add_argument('-t','--target',type=str, default='proton')

    args = ap.parse_args()
    plot_stf(args.target) 

    plot_tpdf()







