#!/usr/bin/env python
import os,sys
import argparse
#--set lhapdf data path
#os.environ["LHAPDF_DATA_PATH"] = '/work/JAM/ccocuzza/WormGearLHAPDF/lhapdf/sets'
#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from tools.tools import checkdir

#--from qpdlib
from tolhapdf import QCF, rename_tables
QCF = QCF()

from plot import plot_transversity,plot_collinspi,plot_widths,plot_Htildepi,plot_sivers

def gen_lhapdf(wdir,dist,name,particle,description,index,authors,reference):

    print('Generating LHAPDF files using directory %s for %s with the following information \n'%(args.directory,dist))

    print('Name:        %s'%name)
    print('Description: %s'%description)
    print('Index:       %s'%index)
    print('Authors:     %s'%authors)
    print('Reference:   %s'%reference)
    print('Particle:    %s'%particle)
    info['particle']      = particle
    QCF.gen_tables(args.directory,dist,name,info,info_only=False)

if __name__=='__main__':

    ap = argparse.ArgumentParser()

    ap.add_argument('-d'  ,'--directory' ,type=str   ,default=None                 ,help='directory name to get/store results')
    ap.add_argument('-f'  ,'--function'  ,type=str   ,default='transversity'       ,help='function to generate')
    args = ap.parse_args()

    checkdir('%s/data'%args.directory)
    checkdir('%s/gallery'%args.directory)

    #rename_tables(args.directory,'JAM22-transversity_proton_lo','JAM22-transversity_proton_lo_nolat')
    #sys.exit()

    #--generate transversity
    if args.function=='transversity':
        dist='transversity'
        name        = 'JAM23-transversity_proton_lo'
        #name        = 'JAM23-transversity_proton_lo_nolat'
        particle    = '2212'
        description = '...' 
        index       = '1'
        authors     = '...'
        reference   = '...'
        info = {}
        info['<description>'] = description
        info['<index>']       = index
        info['<authors>']     = authors
        info['reference']     = reference

        gen_lhapdf(args.directory,dist,name,particle,description,index,authors,reference)   

        plot_transversity(args.directory,name,Q2=4.0,mode=0)
        plot_transversity(args.directory,name,Q2=4.0,mode=1)

    #--generate collins
    elif args.function=='collinspi':
        dist = 'collinspi'
        name        = 'JAM22-Collins_pion_lo'
        particle    = '211'
        description = '...' 
        index       = '1'
        authors     = '...'
        reference   = '...'
        info = {}
        info['<description>'] = description
        info['<index>']       = index
        info['<authors>']     = authors
        info['reference']     = reference

        gen_lhapdf(args.directory,dist,name,particle,description,index,authors,reference)   


        plot_collinspi(args.directory,name,Q2=4.0,mode=0)
        plot_collinspi(args.directory,name,Q2=4.0,mode=1)

        plot_widths(args.directory,name)

    #--generate Htildepi
    elif args.function=='Htildepi':
        dist = 'Htildepi'
        name        = 'JAM22-Htilde_pion_lo'
        particle    = '211'
        description = '...' 
        index       = '1'
        authors     = '...'
        reference   = '...'
        info = {}
        info['<description>'] = description
        info['<index>']       = index
        info['<authors>']     = authors
        info['reference']     = reference

        gen_lhapdf(args.directory,dist,name,particle,description,index,authors,reference)   

        plot_Htildepi(args.directory,name,Q2=4.0,mode=0)
        plot_Htildepi(args.directory,name,Q2=4.0,mode=1)


    #--generate Htildepi
    elif args.function=='sivers':
        dist = 'sivers'
        name        = 'JAM22-sivers_lo'
        particle    = '211'
        description = '...' 
        index       = '1'
        authors     = '...'
        reference   = '...'
        info = {}
        info['<description>'] = description
        info['<index>']       = index
        info['<authors>']     = authors
        info['reference']     = reference

        #gen_lhapdf(args.directory,dist,name,particle,description,index,authors,reference)   

        plot_sivers(args.directory,name,Q2=4.0,mode=0)
        plot_sivers(args.directory,name,Q2=4.0,mode=1)


    else:
        print('Function %s not available.'%args.function)
        print('Available functions are transversity, collinspi, Htildepi, sivers')





