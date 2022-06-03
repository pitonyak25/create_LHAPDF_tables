#!/usr/bin/env python
import sys,os
#sys.path.append(os.path.dirname( os.path.dirname(os.path.abspath(__file__) ) ) )
import numpy as np

cwd = os.getcwd()

import lhapdf
import argparse
#--matplotlib
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
matplotlib.rc('text',usetex=True)
import pylab  as py
from matplotlib.ticker import MultipleLocator

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

X1=10**np.linspace(-4,-1)
X2=np.linspace(0.101,0.99)
X=np.append(X1,X2)

def plot_transversity(wdir,file_name,Q2,mode=0):

    nrows,ncols=1,2
    fig = py.figure(figsize=(ncols*7,nrows*4))
    ax11=py.subplot(nrows,ncols,1)
    ax12=py.subplot(nrows,ncols,2)

    hand = {}

    os.environ["LHAPDF_DATA_PATH"] = '%s/%s/data'%(cwd,wdir)
    QCF = lhapdf.mkPDFs(file_name)
    nrep = len(QCF)

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
                JAM22 ,= ax.plot(X,data[flav][i],color='red',alpha=0.1)
 
        #--plot average and standard deviation
        if mode==1:
            ax.plot(X,mean,color='blue',alpha=1.0,lw=5)
            JAM22 = ax.fill_between(X,mean-std,mean+std,color='blue',alpha=0.6)


    for ax in [ax11,ax12]:
          ax.set_xlim(0,1)
            
          ax.tick_params(axis='both', which='major', top=True, right=True, direction='in',labelsize=30,length=10)
          ax.tick_params(axis='both', which='minor', top=True, right=True, direction='in',labelsize=30,length=5)
          ax.set_xticks([0.2,0.4,0.6,0.8])
          #ax.set_xticklabels([r'$0.01$',r'$0.1$',r'$1$'])
          minorLocator = MultipleLocator(0.1)
          ax.xaxis.set_minor_locator(minorLocator)

    ax11.set_ylim(-0.1,0.6)
    ax12.set_ylim(-0.4,0.1)

    ax11.set_yticks([0,0.2,0.4,0.6])
    ax12.set_yticks([-0.3,-0.2,-0.1,0])

    minorLocator = MultipleLocator(0.05)
    ax11.yaxis.set_minor_locator(minorLocator)
    minorLocator = MultipleLocator(0.05)
    ax12.yaxis.set_minor_locator(minorLocator)

    for ax in [ax11,ax12]:
        ax.set_xlabel(r'\boldmath$x$' ,size=40)
        ax.xaxis.set_label_coords(0.95,0.00)

    ax11.text(0.85 ,0.50  ,r'\boldmath{$u$}'            , transform=ax11.transAxes,size=40)
    ax12.text(0.85 ,0.50  ,r'\boldmath{$d$}'            , transform=ax12.transAxes,size=40)

    ax11.set_ylabel(r'\boldmath$xh_1(x)$',size=30)

    if Q2 == 1.27**2: ax12.text(0.05,0.08,r'$Q^2 = m_c^2$'                                  , transform=ax12.transAxes,size=30)
    else:             ax12.text(0.05,0.08,r'$Q^2 = %s$'%Q2 + ' ' + r'\textrm{GeV}' + r'$^2$', transform=ax12.transAxes,size=30)

    ax11.axhline(0.0,ls='--',color='black',alpha=0.5)
    ax12.axhline(0.0,ls='--',color='black',alpha=0.5)

    handles, labels = [],[]
    handles.append(JAM22)

    labels.append(r'\textrm{\textbf{JAM22}}')

    legend1 = ax11.legend(handles,labels,loc='upper right',fontsize=24,frameon=0,handletextpad=0.5,handlelength=0.9,ncol=1,columnspacing=1.5)


    py.tight_layout()
    py.subplots_adjust(hspace = 0, wspace = 0.20)

    filename = '%s/gallery/lhapdf-transversity-Q2=%3.5f'%(wdir,Q2)
    if mode==1: filename += '-bands'
    filename+='.png'

    py.savefig(filename)
    py.clf()
    print ('Saving figure to %s'%filename)

def plot_collinspi(wdir,file_name,Q2,mode=0):

    nrows,ncols=1,2
    fig = py.figure(figsize=(ncols*7,nrows*4))
    ax11=py.subplot(nrows,ncols,1)
    ax12=py.subplot(nrows,ncols,2)

    hand = {}

    os.environ["LHAPDF_DATA_PATH"] = '%s/%s/data'%(cwd,wdir)
    QCF = lhapdf.mkPDFs(file_name)
    nrep = len(QCF)

    flavs = ['u','d']
    data = {flav: [] for flav in flavs} 

    for i in range(nrep):
        #--skip mean value
        if i==0: continue
        d =  np.array([QCF[i].xfxQ2( 1,x,Q2) for x in X])
        u =  np.array([QCF[i].xfxQ2( 2,x,Q2) for x in X])
        data['u'].append(u)
        data['d'].append(d)
        
    for flav in data:

        if   flav=='u': ax = ax11
        elif flav=='d': ax = ax12

        mean = np.mean(data[flav],axis=0)
        std  = np.std (data[flav],axis=0)

        if mode==0:
            for i in range(nrep-1):
                JAM22 ,= ax.plot(X,data[flav][i],color='red',alpha=0.1)
 
        #--plot average and standard deviation
        if mode==1:
            ax.plot(X,mean,color='blue',alpha=1.0,lw=5)
            JAM22 = ax.fill_between(X,mean-std,mean+std,color='blue',alpha=0.6)


    for ax in [ax11,ax12]:
          ax.set_xlim(0.2,1)
            
          ax.tick_params(axis='both', which='major', top=True, right=True, direction='in',labelsize=30,length=10)
          ax.tick_params(axis='both', which='minor', top=True, right=True, direction='in',labelsize=30,length=5)
          ax.set_xticks([0.2,0.4,0.6,0.8])
          #ax.set_xticklabels([r'$0.01$',r'$0.1$',r'$1$'])
          minorLocator = MultipleLocator(0.1)
          ax.xaxis.set_minor_locator(minorLocator)

    ax11.set_ylim( 0.0,0.6)
    ax12.set_ylim(-0.7,0.0)

    ax11.set_yticks([0.2,0.4,0.6])
    ax12.set_yticks([-0.6,-0.4,-0.2,0])

    minorLocator = MultipleLocator(0.05)
    ax11.yaxis.set_minor_locator(minorLocator)
    minorLocator = MultipleLocator(0.1)
    ax12.yaxis.set_minor_locator(minorLocator)

    for ax in [ax11,ax12]:
        ax.set_xlabel(r'\boldmath$z$' ,size=40)
        ax.xaxis.set_label_coords(0.95,0.00)

    ax11.text(0.75 ,0.50  ,r'\textrm{\textbf{fav}}'            , transform=ax11.transAxes,size=40)
    ax12.text(0.75 ,0.50  ,r'\textrm{\textbf{unf}}'            , transform=ax12.transAxes,size=40)

    ax11.set_ylabel(r'\boldmath$zH_1^{\perp(1)}(z)$',size=30)

    if Q2 == 1.27**2: ax12.text(0.05,0.08,r'$Q^2 = m_c^2$'                                  , transform=ax12.transAxes,size=30)
    else:             ax12.text(0.05,0.08,r'$Q^2 = %s$'%Q2 + ' ' + r'\textrm{GeV}' + r'$^2$', transform=ax12.transAxes,size=30)

    #ax11.axhline(0.0,ls='--',color='black',alpha=0.5)
    #ax12.axhline(0.0,ls='--',color='black',alpha=0.5)

    handles, labels = [],[]
    handles.append(JAM22)

    labels.append(r'\textrm{\textbf{JAM22}}')

    legend1 = ax11.legend(handles,labels,loc='upper right',fontsize=24,frameon=0,handletextpad=0.5,handlelength=0.9,ncol=1,columnspacing=1.5)

    py.tight_layout()
    py.subplots_adjust(hspace = 0, wspace = 0.20)

    filename = '%s/gallery/lhapdf-collinspi-Q2=%3.5f'%(wdir,Q2)
    if mode==1: filename += '-bands'
    filename+='.png'

    py.savefig(filename)
    py.clf()
    print ('Saving figure to %s'%filename)

def plot_widths(wdir,file_name):

    nrows,ncols=1,2
    fig = py.figure(figsize=(ncols*7,nrows*4))
    ax11=py.subplot(nrows,ncols,1)
    ax12=py.subplot(nrows,ncols,2)

    hand = {}

    os.environ["LHAPDF_DATA_PATH"] = '%s/%s/data'%(cwd,wdir)
    QCF = lhapdf.mkPDFs(file_name)
    nrep = len(QCF)

    info = lhapdf.getPDFSet(file_name)
    widths_fav = info.get_entry('widths_fav')
    widths_unf = info.get_entry('widths_unf')
    #--the list of widths is saved as a big string
    #--the code below converts that giant string back into a list of floats
    widths_fav = widths_fav[1:][:len(widths_fav)-2]
    widths_unf = widths_fav[1:][:len(widths_unf)-2]
    widths_fav = widths_fav.split(',')
    widths_unf = widths_unf.split(',')

    fav, unf = [],[]
    for i in range(nrep):
        num, exp = widths_fav[i].split('E')
        fav.append(float(num)*10**int(exp))

        num, exp = widths_unf[i].split('E')
        unf.append(float(num)*10**int(exp))
       
    ax11.hist(fav,color='red' ,alpha=0.6,edgecolor='black',bins=40)
    ax12.hist(unf,color='blue',alpha=0.6,edgecolor='black',bins=40)

    for ax in [ax11,ax12]:
          ax.set_xlim(0.0,0.3)
            
          ax.tick_params(axis='both', which='major', top=True, right=True, direction='in',labelsize=20,length=10)
          ax.tick_params(axis='both', which='minor', top=True, right=True, direction='in',labelsize=20,length=5)
          ax.set_xticks([0.05,0.10,0.15,0.20,0.25])
          #minorLocator = MultipleLocator(0.1)
          #ax.xaxis.set_minor_locator(minorLocator)

    ax11.set_ylabel(r'\textrm{\textbf{Yield}}',size=30)

    ax11.set_title(r'\textrm{\textbf{Favored}}',size=25)
    ax12.set_title(r'\textrm{\textbf{Unfavored}}',size=25)

    py.tight_layout()
    py.subplots_adjust(hspace = 0, wspace = 0.20)

    filename = '%s/gallery/lhapdf-collinspi-widths'%(wdir)
    filename+='.png'

    py.savefig(filename)
    py.clf()
    print ('Saving figure to %s'%filename)

if __name__=="__main__":

    wdir      = 'results'
    Q2 = 4.0

    #--plot transversity
    file_name = 'JAM22-transversity_proton_lo'
    plot_transversity(wdir,file_name,Q2,mode=0)
    plot_transversity(wdir,file_name,Q2,mode=1)

    ##--plot Collins pion
    file_name = 'JAM22-Collins_pion_lo'
    plot_collinspi(wdir,file_name,Q2,mode=0)
    plot_collinspi(wdir,file_name,Q2,mode=1)

    #--plot widths for Collins pion
    plot_widths(wdir,file_name)




