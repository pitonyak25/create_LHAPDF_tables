#!/usr/bin/env python
import os,sys
import argparse
#--set lhapdf data path
os.environ["LHAPDF_DATA_PATH"] = '/work/JAM/ccocuzza/WormGearLHAPDF/lhapdf/sets'
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from tools.tools import checkdir

#--from qpdlib
from analysis.qpdlib.tolhapdf import QCF

QCF = QCF()

description = '...' 
index       = '1'
authors     = '...'
reference   = '...'


if __name__=='__main__':

    ap = argparse.ArgumentParser()

    ap.add_argument('-d'  ,'--directory' ,type=str   ,default=None       ,help='directory name to store results')
    ap.add_argument('-f'  ,'--function'  ,type=str   ,default='tpdf'     ,help='function to generate LHAPDF files for')
    args = ap.parse_args()

    checkdir('%s/data'%args.directory)
    checkdir('%s/gallery'%args.directory)

    info = {}
    info['<description>'] = description
    info['<index>']       = index
    info['<authors>']     = authors
    info['reference']     = reference
   
    print('Generating LHAPDF files using directory %s for the function %s with the following information \n'%(args.directory,args.function))
 
    if args.function=='tpdf':
        name        = 'JAM22-TPDF_proton_nlo'
        particle    = '2212'
        print('Name:        %s'%name)
        print('Description: %s'%description)
        print('Index:       %s'%index)
        print('Authors:     %s'%authors)
        print('Reference:   %s'%reference)
        print('Particle:    %s'%particle)
        info['particle']      = particle
        QCF.gen_tables(args.directory,'pdf',name,info,info_only=False)












