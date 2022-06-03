#!/usr/bin/env python
import os,sys
import argparse
#--set lhapdf data path
#os.environ["LHAPDF_DATA_PATH"] = '/work/JAM/ccocuzza/WormGearLHAPDF/lhapdf/sets'
#sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from tools.tools import checkdir

#--from qpdlib
from tolhapdf import QCF
QCF = QCF()



if __name__=='__main__':

    ap = argparse.ArgumentParser()

    ap.add_argument('-d'  ,'--directory' ,type=str   ,default=None       ,help='directory name to store results')
    args = ap.parse_args()

    checkdir('%s/data'%args.directory)
    checkdir('%s/gallery'%args.directory)

    #--generate transversity 
    description = '...' 
    index       = '1'
    authors     = '...'
    reference   = '...'
    info = {}
    info['<description>'] = description
    info['<index>']       = index
    info['<authors>']     = authors
    info['reference']     = reference
   
    print('Generating LHAPDF files using directory %s for transversity with the following information \n'%(args.directory))

    name        = 'JAM22-transversity_proton_lo'
    particle    = '2212'
    print('Name:        %s'%name)
    print('Description: %s'%description)
    print('Index:       %s'%index)
    print('Authors:     %s'%authors)
    print('Reference:   %s'%reference)
    print('Particle:    %s'%particle)
    info['particle']      = particle
    QCF.gen_tables(args.directory,'transversity',name,info,info_only=False)

    #--generate collins
    description = '...' 
    index       = '1'
    authors     = '...'
    reference   = '...'
    info = {}
    info['<description>'] = description
    info['<index>']       = index
    info['<authors>']     = authors
    info['reference']     = reference

    print('Generating LHAPDF files using directory %s for Collins pion with the following information \n'%(args.directory))

    name        = 'JAM22-Collins_pion_lo'
    particle    = '211'
    print('Name:        %s'%name)
    print('Description: %s'%description)
    print('Index:       %s'%index)
    print('Authors:     %s'%authors)
    print('Reference:   %s'%reference)
    print('Particle:    %s'%particle)
    info['particle']      = particle
    QCF.gen_tables(args.directory,'collinspi',name,info,info_only=False)











