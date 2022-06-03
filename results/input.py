conf={}

#--setups
conf['bootstrap']=True
conf['flat par']=True
conf['ftol']=1e-6
conf['ncpus']=4
conf['Q20']   = 1.27**2
conf['order'] = 'LO' 
conf['unpol PDF FF fixed']=False

#--datasets

conf['datasets']={}

conf['datasets']['sidis']={}
conf['datasets']['sidis']['filters']=["z>0.2 and z<0.6 and Q2>1.63 and pT>0.2 and pT<0.9"]
conf['datasets']['sidis']['xlsx']={}

#--Unpol multiplicities (HERMES only)
conf['datasets']['sidis']['xlsx'][1010]='sidis/expdata/1010.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1011]='sidis/expdata/1011.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1012]='sidis/expdata/1012.xlsx'  # |  proton | k+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1013]='sidis/expdata/1013.xlsx'  # |  proton | k-   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1014]='sidis/expdata/1014.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1015]='sidis/expdata/1015.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1016]='sidis/expdata/1016.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
conf['datasets']['sidis']['xlsx'][1017]='sidis/expdata/1017.xlsx'  # |  deuteron | k-   | M_Hermes | hermes

#--Collins effect SIDIS
conf["datasets"]["sidis"]["xlsx"][4001]="sidis/expdata/4001.xlsx"  #  compass  deuteron  pi+  pT
conf["datasets"]["sidis"]["xlsx"][4000]="sidis/expdata/4000.xlsx"  #  compass  deuteron  pi+   x
conf["datasets"]["sidis"]["xlsx"][4002]="sidis/expdata/4002.xlsx"  #  compass  deuteron  pi+   z
conf["datasets"]["sidis"]["xlsx"][4004]="sidis/expdata/4004.xlsx"  #  compass  deuteron  pi-   pT
conf["datasets"]["sidis"]["xlsx"][4003]="sidis/expdata/4003.xlsx"  #  compass  deuteron  pi-    x
conf["datasets"]["sidis"]["xlsx"][4005]="sidis/expdata/4005.xlsx"  #  compass  deuteron  pi-    z
conf["datasets"]["sidis"]["xlsx"][3027]="sidis/expdata/3027.xlsx"  #  compass    proton   pi+ pt
conf["datasets"]["sidis"]["xlsx"][3025]="sidis/expdata/3025.xlsx"  #  compass    proton  pi+   x
conf["datasets"]["sidis"]["xlsx"][3010]="sidis/expdata/3010.xlsx"  #  compass    proton  pi+  z
conf["datasets"]["sidis"]["xlsx"][3012]="sidis/expdata/3012.xlsx"  #  compass    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3005]="sidis/expdata/3005.xlsx"  #  compass    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3013]="sidis/expdata/3013.xlsx"  #  compass    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3026]="sidis/expdata/3026.xlsx"  #   HERMES    proton pi+   pt
conf["datasets"]["sidis"]["xlsx"][3000]="sidis/expdata/3000.xlsx"  #   HERMES    proton pi+    x
conf["datasets"]["sidis"]["xlsx"][3003]="sidis/expdata/3003.xlsx"  #   HERMES    proton pi+    z
conf["datasets"]["sidis"]["xlsx"][3016]="sidis/expdata/3016.xlsx"  #   HERMES    proton  pi-   pt
conf["datasets"]["sidis"]["xlsx"][3004]="sidis/expdata/3004.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][3018]="sidis/expdata/3018.xlsx"  #   HERMES    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][3006]="sidis/expdata/3006.xlsx"  #   HERMES    proton  pi0    z
conf["datasets"]["sidis"]["xlsx"][3014]="sidis/expdata/3014.xlsx"  #   HERMES    proton  pi0    x
conf["datasets"]["sidis"]["xlsx"][3015]="sidis/expdata/3015.xlsx"  #   HERMES    proton  pi0   pT

conf["datasets"]["sidis"]["xlsx"][3700]="sidis/expdata/3700.xlsx"  #   HERMES    proton pi+    x
conf["datasets"]["sidis"]["xlsx"][3701]="sidis/expdata/3701.xlsx"  #   HERMES    proton pi+    z
conf["datasets"]["sidis"]["xlsx"][3702]="sidis/expdata/3702.xlsx"  #   HERMES    proton pi+    pT
conf["datasets"]["sidis"]["xlsx"][3703]="sidis/expdata/3703.xlsx"  #   HERMES    proton  pi0   x
conf["datasets"]["sidis"]["xlsx"][3704]="sidis/expdata/3704.xlsx"  #   HERMES    proton  pi0   z
conf["datasets"]["sidis"]["xlsx"][3705]="sidis/expdata/3705.xlsx"  #   HERMES    proton  pi0   pT
conf["datasets"]["sidis"]["xlsx"][3706]="sidis/expdata/3706.xlsx"  #   HERMES    proton  pi-   x
conf["datasets"]["sidis"]["xlsx"][3707]="sidis/expdata/3707.xlsx"  #   HERMES    proton  pi-   z
conf["datasets"]["sidis"]["xlsx"][3708]="sidis/expdata/3708.xlsx"  #   HERMES    proton  pi-   pT
conf["datasets"]["sidis"]["xlsx"][3709]="sidis/expdata/3709.xlsx"  #   HERMES    proton  pi+   x,z,pT
conf["datasets"]["sidis"]["xlsx"][3710]="sidis/expdata/3710.xlsx"  #   HERMES    proton  pi-   x,z,pT


#--Sivers effect SIDIS
conf['datasets']['sidis']['xlsx'][2000]='sidis/expdata/2000.xlsx' # proton   | pi+    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2001]='sidis/expdata/2001.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2002]='sidis/expdata/2002.xlsx' # proton   | pi+    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2003]='sidis/expdata/2003.xlsx' # proton   | pi-    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2004]='sidis/expdata/2004.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2005]='sidis/expdata/2005.xlsx' # proton   | pi-    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2006]='sidis/expdata/2006.xlsx' # proton   | pi0    | AUTsivers  | hermes     | PT
conf['datasets']['sidis']['xlsx'][2007]='sidis/expdata/2007.xlsx' # proton   | pi0    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2008]='sidis/expdata/2008.xlsx' # proton   | pi0    | AUTsivers  | hermes     | z

conf['datasets']['sidis']['xlsx'][2026]='sidis/expdata/2026.xlsx' # deuteron | pi+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2027]='sidis/expdata/2027.xlsx' # deuteron | pi+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2028]='sidis/expdata/2028.xlsx' # deuteron | pi+    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2029]='sidis/expdata/2029.xlsx' # deuteron | pi-    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2030]='sidis/expdata/2030.xlsx' # deuteron | pi-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2031]='sidis/expdata/2031.xlsx' # deuteron | pi-    | AUTsivers  | compass    | z

conf['datasets']['sidis']['xlsx'][2512]='sidis/expdata/2512.xlsx' # proton   | pi+    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2513]='sidis/expdata/2513.xlsx' # proton   | pi+    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2514]='sidis/expdata/2514.xlsx' # proton   | pi+    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2515]='sidis/expdata/2515.xlsx' # proton   | pi-    | AUTsivers  | compass    | x
conf['datasets']['sidis']['xlsx'][2516]='sidis/expdata/2516.xlsx' # proton   | pi-    | AUTsivers  | compass    | z
conf['datasets']['sidis']['xlsx'][2517]='sidis/expdata/2517.xlsx' # proton   | pi-    | AUTsivers  | compass    | PT
conf['datasets']['sidis']['xlsx'][2518]='sidis/expdata/2518.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2519]='sidis/expdata/2519.xlsx' # proton   | pi+    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2520]='sidis/expdata/2520.xlsx' # proton   | pi+    | AUTsivers  | hermes     | pT
conf['datasets']['sidis']['xlsx'][2521]='sidis/expdata/2521.xlsx' # proton   | pi0    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2522]='sidis/expdata/2522.xlsx' # proton   | pi0    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2523]='sidis/expdata/2523.xlsx' # proton   | pi0    | AUTsivers  | hermes     | pT
conf['datasets']['sidis']['xlsx'][2524]='sidis/expdata/2524.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x
conf['datasets']['sidis']['xlsx'][2525]='sidis/expdata/2525.xlsx' # proton   | pi-    | AUTsivers  | hermes     | z
conf['datasets']['sidis']['xlsx'][2526]='sidis/expdata/2526.xlsx' # proton   | pi-    | AUTsivers  | hermes     | pT
conf['datasets']['sidis']['xlsx'][2527]='sidis/expdata/2527.xlsx' # proton   | pi+    | AUTsivers  | hermes     | x,z,pT
conf['datasets']['sidis']['xlsx'][2528]='sidis/expdata/2528.xlsx' # proton   | pi-    | AUTsivers  | hermes     | x,z,pT


#A_{UT}^{\sin\phi_S}
conf["datasets"]["sidis"]["xlsx"][9011]="sidis/expdata/9011.xlsx"    #   COMPASS    proton  h+    z
conf["datasets"]["sidis"]["xlsx"][9022]="sidis/expdata/9022.xlsx"    #   COMPASS    proton  h-    z
conf["datasets"]["sidis"]["xlsx"][9033]="sidis/expdata/9033.xlsx"    #   COMPASS    proton  h+    x
conf["datasets"]["sidis"]["xlsx"][9044]="sidis/expdata/9044.xlsx"    #   COMPASS    proton  h-    x
conf["datasets"]["sidis"]["xlsx"][9055]="sidis/expdata/9055.xlsx"    #   HERMES    proton  pi+    x
conf["datasets"]["sidis"]["xlsx"][9066]="sidis/expdata/9066.xlsx"    #   HERMES    proton  pi+    z
conf["datasets"]["sidis"]["xlsx"][9077]="sidis/expdata/9077.xlsx"    #   HERMES    proton  pi+    pt
conf["datasets"]["sidis"]["xlsx"][9088]="sidis/expdata/9088.xlsx"    #   HERMES    proton  pi0    x
conf["datasets"]["sidis"]["xlsx"][9099]="sidis/expdata/9099.xlsx"    #   HERMES    proton  pi0    z
conf["datasets"]["sidis"]["xlsx"][10010]="sidis/expdata/10010.xlsx"  #   HERMES    proton  pi0    pt
conf["datasets"]["sidis"]["xlsx"][10021]="sidis/expdata/10021.xlsx"  #   HERMES    proton  pi-    x
conf["datasets"]["sidis"]["xlsx"][10032]="sidis/expdata/10032.xlsx"  #   HERMES    proton  pi-    z
conf["datasets"]["sidis"]["xlsx"][10043]="sidis/expdata/10043.xlsx"  #   HERMES    proton  pi-    pt
conf["datasets"]["sidis"]["xlsx"][10054]="sidis/expdata/10054.xlsx"  #   HERMES    proton  pi+    x,z,pt
conf["datasets"]["sidis"]["xlsx"][10065]="sidis/expdata/10065.xlsx"  #   HERMES    proton  pi-    x,z,pt

conf['datasets']['sidis']['norm']={}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}
#for k in [9011,9022,9033,9044]: conf['datasets']['sidis']['norm'][k]={'value':1.00000e+00,'fixed':True,'min':8.00000e-01,'max':1.20000e+00}

#Sivers effect DY
conf['datasets']['dy']={}
conf['datasets']['dy']['filters']=[]
conf['datasets']['dy']['xlsx']={}
conf['datasets']['dy']['xlsx'][1000]='dy/expdata/1000.xlsx'       # proton-pi- |    | AUTsivers  | compass    | xbeam
conf['datasets']['dy']['xlsx'][1001]='dy/expdata/1001.xlsx'       # proton-pi- |    | AUTsivers  | compass    | xtarget
conf['datasets']['dy']['xlsx'][1002]='dy/expdata/1002.xlsx'       # proton-pi- |    | AUTsivers  | compass    | xF
conf['datasets']['dy']['xlsx'][1003]='dy/expdata/1003.xlsx'       # proton-pi- |    | AUTsivers  | compass    | qT

conf['datasets']['dy']['norm']={}
for k in conf['datasets']['dy']['xlsx']: conf['datasets']['dy']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}

#Sivers effect WZ
conf['datasets']['wz']={}
conf['datasets']['wz']['filters']=[]
conf['datasets']['wz']['xlsx']={}
conf['datasets']['wz']['xlsx'][2000]='wz/expdata/2000.xlsx'       # proton-proton |W+/-| AUTsivers  | star    | pT
conf['datasets']['wz']['xlsx'][2001]='wz/expdata/2001.xlsx'       # proton-proton |W+/-| AUTsivers  | star    | y
conf['datasets']['wz']['xlsx'][2002]='wz/expdata/2002.xlsx'       # proton-proton |Z   | AUTsivers  | star    | y

conf['datasets']['wz']['norm']={}
for k in conf['datasets']['wz']['xlsx']: conf['datasets']['wz']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}

#--Collins effect SIA
conf['datasets']['sia']={}
conf['datasets']['sia']['filters']=[]
#conf['datasets']['sia']['filters'].append("pT/z1<3.5")
#conf['datasets']['sia']['filters'].append("z2<0.7")
conf['datasets']['sia']['xlsx']={}

conf['datasets']['sia']['xlsx'][1000]='sia/expdata/1000.xlsx' # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1001]='sia/expdata/1001.xlsx' # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['datasets']['sia']['xlsx'][1002]='sia/expdata/1002.xlsx' # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1003]='sia/expdata/1003.xlsx' # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['datasets']['sia']['xlsx'][1004]='sia/expdata/1004.xlsx' # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][1005]='sia/expdata/1005.xlsx' # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['datasets']['sia']['xlsx'][2008]='sia/expdata/2008.xlsx' # babar | pi,pi | AUL-0     | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][2009]='sia/expdata/2009.xlsx' # babar | pi,pi | AUC-0     | 16     | z1,z2      |
conf['datasets']['sia']['xlsx'][3000]='sia/expdata/3000.xlsx' # bes3 | pi,pi | AUL-0     | 6     | z1,z2        |
conf['datasets']['sia']['xlsx'][3001]='sia/expdata/3001.xlsx' # bes3 | pi,pi | AUC-0     | 6     | z1,z2        |
conf['datasets']['sia']['xlsx'][3002]='sia/expdata/3002.xlsx' # bes3 | pi,pi | AUL-0     | 5     | z1,z2,pT     |
conf['datasets']['sia']['xlsx'][3003]='sia/expdata/3003.xlsx' # bes3 | pi,pi | AUC-0     | 5     | z1,z2.pT     |

conf['datasets']['sia']['norm']={}
for k in conf['datasets']['sia']['xlsx']: conf['datasets']['sia']['norm'][k]={'value':1.00000e+00,'fixed':False,'min':8.00000e-01,'max':1.20000e+00}


#--AN
conf['datasets']['AN']={}
conf['datasets']['AN']['filters']=[]
conf['datasets']['AN']['xlsx']={}
conf['datasets']['AN']['xlsx'][1000]='AN_pp/expdata/1000.xlsx' # BRAHMS pim 2.3
conf['datasets']['AN']['xlsx'][1001]='AN_pp/expdata/1001.xlsx' # BRAHMS pim 4
conf['datasets']['AN']['xlsx'][1002]='AN_pp/expdata/1002.xlsx' # BRAHMS pip 2.3
conf['datasets']['AN']['xlsx'][1003]='AN_pp/expdata/1003.xlsx' # BRAHMS pip 4
conf['datasets']['AN']['xlsx'][2000]='AN_pp/expdata/2000.xlsx' # STAR piz 04
conf['datasets']['AN']['xlsx'][2001]='AN_pp/expdata/2001.xlsx' # STAR piz 3.3
conf['datasets']['AN']['xlsx'][2002]='AN_pp/expdata/2002.xlsx' # STAR piz 3.68
conf['datasets']['AN']['xlsx'][2003]='AN_pp/expdata/2003.xlsx' # STAR piz 3.7
conf['datasets']['AN']['xlsx'][2004]='AN_pp/expdata/2004.xlsx' # STAR piz 2008 |pT
conf['datasets']['AN']['xlsx'][3000]='AN_pp/expdata/3000.xlsx' # STAR piz 2020 |xF
conf['datasets']['AN']['xlsx'][3001]='AN_pp/expdata/3001.xlsx' # STAR piz 2020 |xF
conf['datasets']['AN']['xlsx'][3002]='AN_pp/expdata/3002.xlsx' # STAR piz 2020 |pT
conf['datasets']['AN']['xlsx'][3003]='AN_pp/expdata/3003.xlsx' # STAR piz 2020 |pT
conf['datasets']['AN']['xlsx'][3004]='AN_pp/expdata/3004.xlsx' # STAR piz 2020 |pT nonisolated
conf['datasets']['AN']['xlsx'][3005]='AN_pp/expdata/3005.xlsx' # STAR piz 2020 |pT nonisolated
conf['datasets']['AN']['xlsx'][4000]='AN_pp/expdata/4000.xlsx' # STAR jet 2020 |xF
conf['datasets']['AN']['xlsx'][4001]='AN_pp/expdata/4001.xlsx' # STAR jet 2020 |xF
conf['datasets']['AN']['xlsx'][4002]='AN_pp/expdata/4002.xlsx' # STAR jet 2020 |xF
conf['datasets']['AN']['xlsx'][4003]='AN_pp/expdata/4003.xlsx' # STAR jet 2020 |xF
conf['datasets']['AN']['xlsx'][4004]='AN_pp/expdata/4004.xlsx' # ANDY jet      |xF

conf['datasets']['AN']['xlsx'][5000]='AN_pp/expdata/5000.xlsx' # STAR Collins pi0 zem, 200 GeV 
conf['datasets']['AN']['xlsx'][5001]='AN_pp/expdata/5001.xlsx' # STAR Collins pi0 zem, 500 GeV
conf['datasets']['AN']['xlsx'][5002]='AN_pp/expdata/5002.xlsx' # STAR Collins pi0 zem, jTbin1 200 GeV 
conf['datasets']['AN']['xlsx'][5003]='AN_pp/expdata/5003.xlsx' # STAR Collins pi0 zem, jTbin2 200 GeV
conf['datasets']['AN']['xlsx'][5004]='AN_pp/expdata/5004.xlsx' # STAR Collins pi0 zem, jTbin3 200 GeV
conf['datasets']['AN']['xlsx'][5005]='AN_pp/expdata/5005.xlsx' # STAR Collins pi0 zem, jTbin4 200 GeV
conf['datasets']['AN']['xlsx'][5006]='AN_pp/expdata/5006.xlsx' # STAR Collins pi+ pT, z=0.14, 0<eta<1, 500 GeV 
conf['datasets']['AN']['xlsx'][5007]='AN_pp/expdata/5007.xlsx' # STAR Collins pi- pT, z=0.14, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5008]='AN_pp/expdata/5008.xlsx' # STAR Collins pi+ pT, z=0.14, -1<eta<0, 500 GeV 
conf['datasets']['AN']['xlsx'][5009]='AN_pp/expdata/5009.xlsx' # STAR Collins pi- pT, z=0.14, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5010]='AN_pp/expdata/5010.xlsx' # STAR Collins pi+ pT, z=0.24, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5011]='AN_pp/expdata/5011.xlsx' # STAR Collins pi- pT, z=0.24, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5012]='AN_pp/expdata/5012.xlsx' # STAR Collins pi+ pT, z=0.24, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5013]='AN_pp/expdata/5013.xlsx' # STAR Collins pi- pT, z=0.24, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5014]='AN_pp/expdata/5014.xlsx' # STAR Collins pi+ pT, z=0.38, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5015]='AN_pp/expdata/5015.xlsx' # STAR Collins pi- pT, z=0.38, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5016]='AN_pp/expdata/5016.xlsx' # STAR Collins pi+ pT, z=0.38, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5017]='AN_pp/expdata/5017.xlsx' # STAR Collins pi- pT, z=0.38, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5018]='AN_pp/expdata/5018.xlsx' # STAR Collins pi+ z, pT=10.6, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5019]='AN_pp/expdata/5019.xlsx' # STAR Collins pi- z, pT=10.6, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5020]='AN_pp/expdata/5020.xlsx' # STAR Collins pi+ z, pT=10.6, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5021]='AN_pp/expdata/5021.xlsx' # STAR Collins pi- z, pT=10.6, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5022]='AN_pp/expdata/5022.xlsx' # STAR Collins pi+ z, pT=20.6, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5023]='AN_pp/expdata/5023.xlsx' # STAR Collins pi- z, pT=20.6, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5024]='AN_pp/expdata/5024.xlsx' # STAR Collins pi+ z, pT=20.6, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5025]='AN_pp/expdata/5025.xlsx' # STAR Collins pi- z, pT=20.6, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5026]='AN_pp/expdata/5026.xlsx' # STAR Collins pi+ z, pT=31, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5027]='AN_pp/expdata/5027.xlsx' # STAR Collins pi- z, pT=31, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5028]='AN_pp/expdata/5028.xlsx' # STAR Collins pi+ z, pT=31, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5029]='AN_pp/expdata/5029.xlsx' # STAR Collins pi- z, pT=31, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5030]='AN_pp/expdata/5030.xlsx' # STAR Collins pi+ jT, z=0.13, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5031]='AN_pp/expdata/5031.xlsx' # STAR Collins pi- jT, z=0.13, 0<eta<1, 500 GeV 
conf['datasets']['AN']['xlsx'][5032]='AN_pp/expdata/5032.xlsx' # STAR Collins pi+ jT, z=0.13, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5033]='AN_pp/expdata/5033.xlsx' # STAR Collins pi- jT, z=0.13, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5034]='AN_pp/expdata/5034.xlsx' # STAR Collins pi+ jT, z=0.23, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5035]='AN_pp/expdata/5035.xlsx' # STAR Collins pi- jT, z=0.23, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5036]='AN_pp/expdata/5036.xlsx' # STAR Collins pi+ jT, z=0.23, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5037]='AN_pp/expdata/5037.xlsx' # STAR Collins pi- jT, z=0.23, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5038]='AN_pp/expdata/5038.xlsx' # STAR Collins pi+ jT, z=0.37, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5039]='AN_pp/expdata/5039.xlsx' # STAR Collins pi- jT, z=0.37, 0<eta<1, 500 GeV
conf['datasets']['AN']['xlsx'][5040]='AN_pp/expdata/5040.xlsx' # STAR Collins pi+ jT, z=0.37, -1<eta<0, 500 GeV
conf['datasets']['AN']['xlsx'][5041]='AN_pp/expdata/5041.xlsx' # STAR Collins pi- jT, z=0.37, -1<eta<0, 500 GeV

conf['datasets']['AN']['norm']={}
for k in conf['datasets']['AN']['xlsx']: conf['datasets']['AN']['norm'][k]={'value':1.000000,'fixed':False,'min':0.8000000,'max':1.2000000}
for k in [i for i in range(2004,5042)]: conf['datasets']['AN']['norm'][k]={'value':1.00000e+00,'fixed':True,'min':8.00000e-01,'max':1.20000e+00}

#--ANep
conf['datasets']['ANep']={}
conf['datasets']['ANep']['xlsx']={}
conf['datasets']['ANep']['xlsx'][1000]='AN_ep/expdata/1000.xlsx' # HERMES / proton / pi-
conf['datasets']['ANep']['xlsx'][1001]='AN_ep/expdata/1001.xlsx' # HERMES / proton / pi-
conf['datasets']['ANep']['xlsx'][1002]='AN_ep/expdata/1002.xlsx' # HERMES / proton / pi-
conf['datasets']['ANep']['xlsx'][1003]='AN_ep/expdata/1003.xlsx' # EIC / proton / pi-
conf['datasets']['ANep']['xlsx'][1004]='AN_ep/expdata/1004.xlsx' # EIC / proton / pi-
conf['datasets']['ANep']['xlsx'][1005]='AN_ep/expdata/1005.xlsx' # COMPASS / proton / pi-
conf['datasets']['ANep']['xlsx'][1006]='AN_ep/expdata/1006.xlsx' # JLAB12 / proton / pi-
conf['datasets']['ANep']['xlsx'][2000]='AN_ep/expdata/2000.xlsx' # HERMES / proton / pi+
conf['datasets']['ANep']['xlsx'][2001]='AN_ep/expdata/2001.xlsx' # HERMES / proton / pi+
conf['datasets']['ANep']['xlsx'][2002]='AN_ep/expdata/2002.xlsx' # HERMES / proton / pi+
conf['datasets']['ANep']['xlsx'][2003]='AN_ep/expdata/2003.xlsx' # EIC / proton / pi+
conf['datasets']['ANep']['xlsx'][2004]='AN_ep/expdata/2004.xlsx' # EIC / proton / pi+
conf['datasets']['ANep']['xlsx'][2005]='AN_ep/expdata/2005.xlsx' # COMPASS / proton / pi+
conf['datasets']['ANep']['xlsx'][2006]='AN_ep/expdata/2006.xlsx' # JLAB12 / proton / pi+
conf['datasets']['ANep']['xlsx'][3000]='AN_ep/expdata/3000.xlsx' # EIC / proton / pi

conf['datasets']['ANep']['norm']={}
for k in conf['datasets']['ANep']['xlsx']: conf['datasets']['ANep']['norm'][k]={'value':1.000000,'fixed':False,'min':0.8000000,'max':1.2000000}
for k in [1000,1001,1002,1003,1004,1005,1006,2000,2001,2002,2003,2004,2005,2006,3000]: conf['datasets']['ANep']['norm'][k]={'value':1.000000,'fixed':True,'min':0.8000000,'max':1.2000000}
    
#--lattice data for tensor charge
conf['datasets']['moments']={}
conf['datasets']['moments']['filters']=[]
conf['datasets']['moments']['xlsx']={}
conf['datasets']['moments']['xlsx'][2000]='lattice/expdata/2000.xlsx' # gT(u-d)
conf['datasets']['moments']['xlsx'][2001]='lattice/expdata/2001.xlsx' # gTu
conf['datasets']['moments']['xlsx'][2002]='lattice/expdata/2002.xlsx' # gTd
#conf['datasets']['moments']['xlsx'][2003]='lattice/expdata/2003.xlsx' # gTs

conf['datasets']['moments']['norm']={}
for k in conf['datasets']['moments']['xlsx']: conf['datasets']['moments']['norm'][k]={'value':1.000000,'fixed':True,'min':0.8000000,'max':1.2000000}

#--Soffer Bound
conf['datasets']['SB']={}
conf['datasets']['SB']['filters']=[]
conf['datasets']['SB']['xlsx']={}
conf['datasets']['SB']['xlsx'][1000]='Soffer_Bound/expdata/1000.xlsx' # SB u quark
conf['datasets']['SB']['xlsx'][2000]='Soffer_Bound/expdata/2000.xlsx' # SB d quark

conf['datasets']['SB']['norm']={}
for k in conf['datasets']['SB']['xlsx']: conf['datasets']['SB']['norm'][k]={'value':1.000000,'fixed':True,'min':0.8000000,'max':1.2000000}

#--parameters
conf['params']={}


#--Parameters in gaussian approximation, parton model:
#--TMD PDF:
conf['params']['pdf']={}
conf['params']['pdf']['widths1_uv']  ={'value':    5.51292e-01,'min': 0.1,'max':0.8,'fixed':False}
conf['params']['pdf']['widths2_uv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['widths1_dv']  ={'value':    5.40344e-01,'min': 0.1,'max':0.8,'fixed':'widths1_uv'}
conf['params']['pdf']['widths2_dv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}
conf['params']['pdf']['widths1_sea'] ={'value':    5.43879e-01,'min': 0.1,'max':0.8,'fixed':False}
conf['params']['pdf']['widths2_sea'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}

conf['params']['pdfpi-']={}
conf['params']['pdfpi-']['widths1_ubv'] ={'value':    5.51292e-01,'min': 0.1,'max':0.8,'fixed':'proton widths uv'}
conf['params']['pdfpi-']['widths2_ubv'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdfpi-']['widths1_dv']  ={'value':    5.51292e-01,'min': 0.1,'max':0.8,'fixed':'widths1_ubv'}
conf['params']['pdfpi-']['widths2_dv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_ubv'}
conf['params']['pdfpi-']['widths1_sea'] ={'value':    5.43879e-01,'min': 0.1,'max':0.8,'fixed':'proton widths sea'}
conf['params']['pdfpi-']['widths2_sea'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_ubv'}

#--TMD FF:
conf['params']['ffpi']={}
conf['params']['ffpi']['widths1_fav']  ={'value':    1.22011e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffpi']['widths2_fav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffpi']['widths1_ufav'] ={'value':    1.43665e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffpi']['widths2_ufav'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}

conf['params']['ffk']={}
conf['params']['ffk']['widths1_fav']   ={'value':    1.32333e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffk']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffk']['widths1_ufav']  ={'value':    2.02660e-01,'min': 0.05,'max':0.3,'fixed':False}
conf['params']['ffk']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}

conf['params']['ffh']={}
conf['params']['ffh']['widths1_fav']   ={'value':    1.24050e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffh']['widths1_ufav']  ={'value':    1.43730e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_fav'}


# Transversity
conf['params']['transversity']={}
conf['params']['transversity']['widths1_uv']  ={'value':    0.5, 'min':0.1, 'max':3.0, 'fixed':False}
conf['params']['transversity']['widths1_dv']  ={'value':    3.12697e-01, 'min':0.2, 'max':0.8, 'fixed': 'widths1_uv'}
conf['params']['transversity']['widths1_sea'] ={'value':    8.35004e-01, 'min':0.05, 'max':2.0, 'fixed': True}
conf['params']['transversity']['widths2_uv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': True}
conf['params']['transversity']['widths2_dv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}
conf['params']['transversity']['widths2_sea'] ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}

conf['params']['transversity']['u N0 1'] ={'value':    0.25, 'min': 0.15, 'max': 0.6, 'fixed':False}
conf['params']['transversity']['u N1 1'] ={'value':    -0.0175e+00, 'min': -0.02, 'max': -0.015, 'fixed':False}
conf['params']['transversity']['u a0 1'] ={'value':    0.000, 'min': -0.5, 'max':3, 'fixed':False}
conf['params']['transversity']['u a1 1'] ={'value':    0, 'min':0, 'max':0.5, 'fixed':True}
conf['params']['transversity']['u b0 1'] ={'value':    4.5e+00, 'min':0, 'max':12, 'fixed':False}
conf['params']['transversity']['u b1 1'] ={'value':    0.65e+00, 'min': 0.5, 'max':0.75, 'fixed':False}
conf['params']['transversity']['u c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 0.0, 'fixed': True}
conf['params']['transversity']['u c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['u c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['u d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['transversity']['d N0 1'] ={'value':   -0.15, 'min': -0.2, 'max':0.1, 'fixed':False}
conf['params']['transversity']['d N1 1'] ={'value':    0.0175e+00, 'min': 0.015, 'max': 0.02, 'fixed':False}
conf['params']['transversity']['d a0 1'] ={'value':    0.5e+00, 'min': -0.5, 'max': 4.0, 'fixed':False} ###
conf['params']['transversity']['d a1 1'] ={'value':    0.00000e+00, 'min':0, 'max': 0.5, 'fixed':'u a1 1'}
conf['params']['transversity']['d b0 1'] ={'value':    6.0e+00, 'min': 0, 'max':12, 'fixed':'u b0 1'}
conf['params']['transversity']['d b1 1'] ={'value':    1e+00, 'min': 0.5, 'max':1.125, 'fixed':'u b1 1'}
conf['params']['transversity']['d c0 1'] ={'value':    0.00000e+00, 'min':-1000.0, 'max': 0.0, 'fixed':True}
conf['params']['transversity']['d c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['d c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['d d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}

conf['params']['transversity']['s N0 1'] ={'value':    0.00000e+00, 'min': -0.1, 'max': 0.1, 'fixed': True}
conf['params']['transversity']['s N1 1'] ={'value':    0.00000e+00, 'min': -1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s a0 1'] ={'value':    1.00000e+00, 'min': 0.5, 'max':5, 'fixed': True}
conf['params']['transversity']['s a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':2.0, 'fixed': True}
conf['params']['transversity']['s b0 1'] ={'value':    10.00000e+00, 'min': 0, 'max':20.0, 'fixed': True}
conf['params']['transversity']['s b1 1'] ={'value':    0.00000e+00, 'min': -2.0, 'max':2.0, 'fixed':True}
conf['params']['transversity']['s c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['transversity']['s c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['transversity']['s d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['transversity']['ub N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['transversity']['ub N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['transversity']['ub a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['transversity']['ub a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['transversity']['ub b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['transversity']['ub b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['transversity']['ub c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['transversity']['ub c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['transversity']['ub d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['transversity']['ub d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['transversity']['ub N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['transversity']['ub N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['transversity']['ub a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['transversity']['ub a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['transversity']['ub b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['transversity']['ub b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['transversity']['ub c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['transversity']['ub c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['transversity']['ub d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['transversity']['ub d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['transversity']['db N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['transversity']['db N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['transversity']['db a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['transversity']['db a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['transversity']['db b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['transversity']['db b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['transversity']['db c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['transversity']['db c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['transversity']['db d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['transversity']['db d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['transversity']['db N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['transversity']['db N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['transversity']['db a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['transversity']['db a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['transversity']['db b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['transversity']['db b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['transversity']['db c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['transversity']['db c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['transversity']['db d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['transversity']['db d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['transversity']['sb N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['transversity']['sb N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['transversity']['sb a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['transversity']['sb a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['transversity']['sb b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['transversity']['sb b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['transversity']['sb c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['transversity']['sb c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['transversity']['sb d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['transversity']['sb d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['transversity']['sb N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['transversity']['sb N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['transversity']['sb a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['transversity']['sb a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['transversity']['sb b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['transversity']['sb b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['transversity']['sb c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['transversity']['sb c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['transversity']['sb d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['transversity']['sb d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}



# Collins TMD FF:
conf['params']['collinspi']={}

conf['params']['collinspi']['widths1_fav']   ={'value':    1.22288e-01,'min':0.025, 'max':0.25, 'fixed':False}
conf['params']['collinspi']['widths1_ufav'] ={'value':    6.11536e-02,'min':0.01, 'max':0.15, 'fixed':False}
conf['params']['collinspi']['widths2_fav']   ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['collinspi']['widths2_ufav'] ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':'widths2_fav'}

conf['params']['collinspi']['u N0 1'] ={'value':    0.2e+00,'min': -0.05, 'max':0.5, 'fixed':False}
conf['params']['collinspi']['u N1 1'] ={'value':    0e+0,'min': -0.0015, 'max': 0, 'fixed':False}
conf['params']['collinspi']['u a0 1'] ={'value':    2.5,'min':-1, 'max':7, 'fixed':False}
conf['params']['collinspi']['u a1 1'] ={'value':    0.00000e+00,'min':0, 'max': 0.25, 'fixed':False}
conf['params']['collinspi']['u b0 1'] ={'value':    2.5e+00,'min': 0.5, 'max': 5, 'fixed':False}
conf['params']['collinspi']['u b1 1'] ={'value':    0.0e+00,'min': 0.0, 'max':1, 'fixed':False}
conf['params']['collinspi']['u c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u N0 2'] ={'value':    1000,'min': 0, 'max': 1000, 'fixed':True}
conf['params']['collinspi']['u N1 2'] ={'value':    0.00000e+00,'min': -2, 'max': 0, 'fixed':True}
conf['params']['collinspi']['u a0 2'] ={'value':    0,'min':-0.1, 'max': 0.1, 'fixed':True}
conf['params']['collinspi']['u a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 0, 'fixed':True}
conf['params']['collinspi']['u b0 2'] ={'value':    11,'min':6, 'max':15, 'fixed':False} ###
conf['params']['collinspi']['u b1 2'] ={'value':    0.00e+00,'min': -0.5, 'max':0.5, 'fixed':False}
conf['params']['collinspi']['u c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['u d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['d N0 1'] ={'value':   -0.4,'min': -0.75, 'max':0.05, 'fixed':False}
conf['params']['collinspi']['d N1 1'] ={'value':    0e+00,'min': 0, 'max': 0.0015, 'fixed':False}
conf['params']['collinspi']['d a0 1'] ={'value':    0.5e+00,'min':-1, 'max': 3, 'fixed':False}
conf['params']['collinspi']['d a1 1'] ={'value':    0.00000e+00,'min':0, 'max':0.25, 'fixed':False}
conf['params']['collinspi']['d b0 1'] ={'value':    3.41000e+00,'min': 1, 'max':5, 'fixed':False}
conf['params']['collinspi']['d b1 1'] ={'value':    0.000e+00,'min': 0, 'max':1, 'fixed':False}
conf['params']['collinspi']['d c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d N0 2'] ={'value':    200,'min':0, 'max':200, 'fixed':True}
conf['params']['collinspi']['d N1 2'] ={'value':    0.00000e+00,'min': -2, 'max': 0, 'fixed':True}
conf['params']['collinspi']['d a0 2'] ={'value':    0,'min': -0.1, 'max': 0.1, 'fixed':True}
conf['params']['collinspi']['d a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 0, 'fixed':True}
conf['params']['collinspi']['d b0 2'] ={'value':    10.80e+00,'min': 5, 'max':25, 'fixed':False}
conf['params']['collinspi']['d b1 2'] ={'value':    0.00000e+00,'min': -0.5, 'max':0.5, 'fixed':False}
conf['params']['collinspi']['d c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['collinspi']['d d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['collinspi']['s N0 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10, 'fixed':'d N0 1'}
conf['params']['collinspi']['s N1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 1'}
conf['params']['collinspi']['s a0 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20, 'fixed':'d a0 1'}
conf['params']['collinspi']['s a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 1'}
conf['params']['collinspi']['s b0 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10, 'fixed':'d b0 1'}
conf['params']['collinspi']['s b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 1'}
conf['params']['collinspi']['s c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 1'}
conf['params']['collinspi']['s c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 1'}
conf['params']['collinspi']['s d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 1'}
conf['params']['collinspi']['s d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 1'}
conf['params']['collinspi']['s N0 2'] ={'value':   -3.06065e+02,'min': 0, 'max': 1, 'fixed':'d N0 2'}
conf['params']['collinspi']['s N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 2'}
conf['params']['collinspi']['s a0 2'] ={'value':    8.69912e-01,'min':-2, 'max': 2, 'fixed':'d a0 2'}
conf['params']['collinspi']['s a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 2'}
conf['params']['collinspi']['s b0 2'] ={'value':    1.39667e+01,'min': 0, 'max':10, 'fixed':'d b0 2'}
conf['params']['collinspi']['s b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 2'}
conf['params']['collinspi']['s c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 2'}
conf['params']['collinspi']['s c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 2'}
conf['params']['collinspi']['s d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 2'}
conf['params']['collinspi']['s d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 2'}


conf['params']['collinspi']['ub N0 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10,  'fixed':'d N0 1'}
conf['params']['collinspi']['ub N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['collinspi']['ub a0 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20,  'fixed':'d a0 1'}
conf['params']['collinspi']['ub a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['collinspi']['ub b0 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10,    'fixed':'d b0 1'}
conf['params']['collinspi']['ub b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['collinspi']['ub c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['collinspi']['ub c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['collinspi']['ub d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['collinspi']['ub d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['collinspi']['ub N0 2'] ={'value':   -3.06065e+02,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['collinspi']['ub N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['collinspi']['ub a0 2'] ={'value':    8.69912e-01,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['collinspi']['ub a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['collinspi']['ub b0 2'] ={'value':    1.39667e+01,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['collinspi']['ub b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['collinspi']['ub c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['collinspi']['ub c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['collinspi']['ub d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['collinspi']['ub d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

conf['params']['collinspi']['db N0 1'] ={'value':    1.56490e+00,'min': -15, 'max': 15,  'fixed':'u N0 1'}
conf['params']['collinspi']['db N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'u N1 1'}
conf['params']['collinspi']['db a0 1'] ={'value':    1.23346e-01,'min':-0.228, 'max': 5,  'fixed':'u a0 1'}
conf['params']['collinspi']['db a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'u a1 1'}
conf['params']['collinspi']['db b0 1'] ={'value':    2.90807e+00,'min': 0.9, 'max':15,    'fixed':'u b0 1'}
conf['params']['collinspi']['db b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 1'}
conf['params']['collinspi']['db c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 1'}
conf['params']['collinspi']['db c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 1'}
conf['params']['collinspi']['db d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 1'}
conf['params']['collinspi']['db d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 1'}
conf['params']['collinspi']['db N0 2'] ={'value':    2.93621e+00,'min': -15, 'max': 15, 'fixed':'u N0 2'}
conf['params']['collinspi']['db N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'u N1 2'}
conf['params']['collinspi']['db a0 2'] ={'value':    7.95023e-01,'min':-0.228, 'max': 20,   'fixed':'u a0 2'}
conf['params']['collinspi']['db a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'u a1 2'}
conf['params']['collinspi']['db b0 2'] ={'value':    5.72097e+00,'min': 1.20, 'max':10,    'fixed':'u b0 2'}
conf['params']['collinspi']['db b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 2'}
conf['params']['collinspi']['db c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 2'}
conf['params']['collinspi']['db c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 2'}
conf['params']['collinspi']['db d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 2'}
conf['params']['collinspi']['db d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 2'}

conf['params']['collinspi']['sb N0 1'] ={'value':   -5.94721e+00,'min': -15, 'max': 10,  'fixed':'d N0 1'}
conf['params']['collinspi']['sb N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['collinspi']['sb a0 1'] ={'value':    4.25846e+00,'min':-1, 'max': 20,  'fixed':'d a0 1'}
conf['params']['collinspi']['sb a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['collinspi']['sb b0 1'] ={'value':    4.19000e+00,'min': 2.19, 'max':10,    'fixed':'d b0 1'}
conf['params']['collinspi']['sb b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['collinspi']['sb c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['collinspi']['sb c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['collinspi']['sb d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['collinspi']['sb d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['collinspi']['sb N0 2'] ={'value':   -3.06065e+02,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['collinspi']['sb N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['collinspi']['sb a0 2'] ={'value':    8.69912e-01,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['collinspi']['sb a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['collinspi']['sb b0 2'] ={'value':    1.39667e+01,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['collinspi']['sb b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['collinspi']['sb c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['collinspi']['sb c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['collinspi']['sb d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['collinspi']['sb d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

#mimic Collins, widths not required, but only 1 shape
conf['params']['Htildepi']={}
conf['params']['Htildepi']['widths1_fav']   ={'value':    1.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths1_ufav'] ={'value':    1.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths2_fav']   ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}
conf['params']['Htildepi']['widths2_ufav'] ={'value':    0.00000e+00,'min':0, 'max':1, 'fixed':True}

conf['params']['Htildepi']['u N0 1'] ={'value':    0.0e+00,'min': -0.5, 'max': 0.5, 'fixed':False}
conf['params']['Htildepi']['u N1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 0.15, 'fixed':False}
conf['params']['Htildepi']['u a0 1'] ={'value':    4.0e+00,'min':1.0, 'max': 5, 'fixed':False}
conf['params']['Htildepi']['u a1 1'] ={'value':    0.00000e+00,'min':0, 'max': 0.25, 'fixed':False}
conf['params']['Htildepi']['u b0 1'] ={'value':    2.44590e+00,'min': 1, 'max':10, 'fixed':False}
conf['params']['Htildepi']['u b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':1, 'fixed':False}
conf['params']['Htildepi']['u c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed': True}
conf['params']['Htildepi']['u N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20, 'fixed':True}
conf['params']['Htildepi']['u a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':True}
conf['params']['Htildepi']['u b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['u b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['u c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['u d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['Htildepi']['d N0 1'] ={'value':    0.0e+00,'min': -0.5, 'max': 0.5, 'fixed':False}
conf['params']['Htildepi']['d N1 1'] ={'value':    0.00000e+00,'min': -0.01, 'max': 0, 'fixed':False} ###
conf['params']['Htildepi']['d a0 1'] ={'value':    3.0e+00,'min':1.0, 'max': 5, 'fixed':'u a0 1'}
conf['params']['Htildepi']['d a1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'u a1 1'}
conf['params']['Htildepi']['d b0 1'] ={'value':    4.13470e+00,'min': 1, 'max':10, 'fixed':'u b0 1'} ###
conf['params']['Htildepi']['d b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':1, 'fixed':'u b1 1'}
conf['params']['Htildepi']['d c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':True}
conf['params']['Htildepi']['d N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 5, 'fixed':True}
conf['params']['Htildepi']['d a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':True}
conf['params']['Htildepi']['d b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['d b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':True}
conf['params']['Htildepi']['d c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}
conf['params']['Htildepi']['d d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':True}

conf['params']['Htildepi']['s N0 1'] ={'value':    5.68651e+00,'min': 0, 'max': 1, 'fixed':'d N0 1'}
conf['params']['Htildepi']['s N1 1'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 1'}
conf['params']['Htildepi']['s a0 1'] ={'value':    1.79259e+00,'min':-2, 'max': 2, 'fixed':'d a0 1'}
conf['params']['Htildepi']['s a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 1'}
conf['params']['Htildepi']['s b0 1'] ={'value':    4.13470e+00,'min': 0, 'max':10, 'fixed':'d b0 1'}
conf['params']['Htildepi']['s b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 1'}
conf['params']['Htildepi']['s c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 1'}
conf['params']['Htildepi']['s c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 1'}
conf['params']['Htildepi']['s d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 1'}
conf['params']['Htildepi']['s d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 1'}
conf['params']['Htildepi']['s N0 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N0 2'}
conf['params']['Htildepi']['s N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1, 'fixed':'d N1 2'}
conf['params']['Htildepi']['s a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a0 2'}
conf['params']['Htildepi']['s a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2, 'fixed':'d a1 2'}
conf['params']['Htildepi']['s b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b0 2'}
conf['params']['Htildepi']['s b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10, 'fixed':'d b1 2'}
conf['params']['Htildepi']['s c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c0 2'}
conf['params']['Htildepi']['s c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d c1 2'}
conf['params']['Htildepi']['s d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d0 2'}
conf['params']['Htildepi']['s d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1, 'fixed':'d d1 2'}


conf['params']['Htildepi']['ub N0 1'] ={'value':    5.68651e+00,'min': -15, 'max': 2,  'fixed':'d N0 1'}
conf['params']['Htildepi']['ub N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['Htildepi']['ub a0 1'] ={'value':    1.79259e+00,'min':-2.5, 'max': 5,  'fixed':'d a0 1'}
conf['params']['Htildepi']['ub a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['Htildepi']['ub b0 1'] ={'value':    4.13470e+00,'min': 0, 'max':10,    'fixed':'d b0 1'}
conf['params']['Htildepi']['ub b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['Htildepi']['ub c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['Htildepi']['ub c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['Htildepi']['ub d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['Htildepi']['ub d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['Htildepi']['ub N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['Htildepi']['ub N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['Htildepi']['ub a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['Htildepi']['ub a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['Htildepi']['ub b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['Htildepi']['ub b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['Htildepi']['ub c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['Htildepi']['ub c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['Htildepi']['ub d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['Htildepi']['ub d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

conf['params']['Htildepi']['db N0 1'] ={'value':   -6.31163e+00,'min': -15, 'max': 2,  'fixed':'u N0 1'}
conf['params']['Htildepi']['db N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'u N1 1'}
conf['params']['Htildepi']['db a0 1'] ={'value':    5.33063e+00,'min':-2.5, 'max': 5,  'fixed':'u a0 1'}
conf['params']['Htildepi']['db a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'u a1 1'}
conf['params']['Htildepi']['db b0 1'] ={'value':    1.44590e+00,'min': 0, 'max':10,    'fixed':'u b0 1'}
conf['params']['Htildepi']['db b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 1'}
conf['params']['Htildepi']['db c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 1'}
conf['params']['Htildepi']['db c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 1'}
conf['params']['Htildepi']['db d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 1'}
conf['params']['Htildepi']['db d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 1'}
conf['params']['Htildepi']['db N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'u N0 2'}
conf['params']['Htildepi']['db N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'u N1 2'}
conf['params']['Htildepi']['db a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'u a0 2'}
conf['params']['Htildepi']['db a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'u a1 2'}
conf['params']['Htildepi']['db b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b0 2'}
conf['params']['Htildepi']['db b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'u b1 2'}
conf['params']['Htildepi']['db c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c0 2'}
conf['params']['Htildepi']['db c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u c1 2'}
conf['params']['Htildepi']['db d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d0 2'}
conf['params']['Htildepi']['db d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'u d1 2'}

conf['params']['Htildepi']['sb N0 1'] ={'value':    5.68651e+00,'min': -15, 'max': 2,  'fixed':'d N0 1'}
conf['params']['Htildepi']['sb N1 1'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N1 1'}
conf['params']['Htildepi']['sb a0 1'] ={'value':    1.79259e+00,'min':-2.5, 'max': 5,  'fixed':'d a0 1'}
conf['params']['Htildepi']['sb a1 1'] ={'value':    0.00000e+00,'min':-2, 'max': 5,    'fixed':'d a1 1'}
conf['params']['Htildepi']['sb b0 1'] ={'value':    4.13470e+00,'min': 0, 'max':10,    'fixed':'d b0 1'}
conf['params']['Htildepi']['sb b1 1'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 1'}
conf['params']['Htildepi']['sb c0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 1'}
conf['params']['Htildepi']['sb c1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 1'}
conf['params']['Htildepi']['sb d0 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 1'}
conf['params']['Htildepi']['sb d1 1'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 1'}
conf['params']['Htildepi']['sb N0 2'] ={'value':    0.00000e+00,'min': -10, 'max': 10, 'fixed':'d N0 2'}
conf['params']['Htildepi']['sb N1 2'] ={'value':    0.00000e+00,'min': 0, 'max': 1,    'fixed':'d N1 2'}
conf['params']['Htildepi']['sb a0 2'] ={'value':    0.00000e+00,'min':-2, 'max': 20,   'fixed':'d a0 2'}
conf['params']['Htildepi']['sb a1 2'] ={'value':    0.00000e+00,'min':-2, 'max': 2,    'fixed':'d a1 2'}
conf['params']['Htildepi']['sb b0 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b0 2'}
conf['params']['Htildepi']['sb b1 2'] ={'value':    0.00000e+00,'min': 0, 'max':10,    'fixed':'d b1 2'}
conf['params']['Htildepi']['sb c0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c0 2'}
conf['params']['Htildepi']['sb c1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d c1 2'}
conf['params']['Htildepi']['sb d0 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d0 2'}
conf['params']['Htildepi']['sb d1 2'] ={'value':    0.00000e+00,'min':-1, 'max': 1,    'fixed':'d d1 2'}

#Sivers function
conf['params']['sivers']={}
conf['params']['sivers']['widths1_uv']  ={'value':    2.47890e-01, 'min':0.1, 'max':1.0, 'fixed': False}
conf['params']['sivers']['widths1_dv']  ={'value':    3.27437e-01, 'min':0, 'max':2, 'fixed': 'widths1_uv'}
conf['params']['sivers']['widths1_sea'] ={'value':    4.88407e-01, 'min':0.1, 'max':2.0, 'fixed': True}
conf['params']['sivers']['widths2_uv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': True}
conf['params']['sivers']['widths2_dv']  ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}
conf['params']['sivers']['widths2_sea'] ={'value':    0.00000e+00, 'min':0, 'max':1, 'fixed': 'widths2_uv'}

conf['params']['sivers']['u N0 1'] ={'value':   -0.023648e+00, 'min': -0.075, 'max': 0, 'fixed': False}
conf['params']['sivers']['u N1 1'] ={'value':    0.005e+00, 'min': 0.001, 'max': 0.005, 'fixed':False}
conf['params']['sivers']['u a0 1'] ={'value':    7.58691e-01, 'min': -1.0, 'max':2.0, 'fixed': False}
conf['params']['sivers']['u a1 1'] ={'value':    0.0000e+00, 'min':0, 'max':1.0, 'fixed':True}
conf['params']['sivers']['u b0 1'] ={'value':    1.16529e+01, 'min': 0.5, 'max':17.0, 'fixed': False}
conf['params']['sivers']['u b1 1'] ={'value':    1.0000e+00, 'min': 0.5, 'max':1.5, 'fixed':False}
conf['params']['sivers']['u c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['u c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['u d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['sivers']['d N0 1'] ={'value':    0.01373e+00, 'min': 0, 'max': 0.075, 'fixed': False}
conf['params']['sivers']['d N1 1'] ={'value':    -0.005e+00, 'min': -0.025, 'max': -0.005, 'fixed':False}
conf['params']['sivers']['d a0 1'] ={'value':    1.19070e+00, 'min': -1.0, 'max':2, 'fixed': False}
conf['params']['sivers']['d a1 1'] ={'value':    0.00000e+00, 'min':0, 'max':1.0, 'fixed': 'u a1 1'}
conf['params']['sivers']['d b0 1'] ={'value':    1.95150e+01, 'min': 0, 'max':17.0, 'fixed': 'u b0 1'}
conf['params']['sivers']['d b1 1'] ={'value':    0.50000e+00, 'min': 0.5, 'max':1.0, 'fixed': 'u b1 1'}
conf['params']['sivers']['d c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['d c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['d d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['sivers']['s N0 1'] ={'value':    0.00000e+00, 'min': -0.05, 'max': 0.05, 'fixed': True}
conf['params']['sivers']['s N1 1'] ={'value':    0.00000e+00, 'min': -1.0, 'max': 0.0, 'fixed': True}
conf['params']['sivers']['s a0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max':10, 'fixed': True}
conf['params']['sivers']['s a1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max':0.0, 'fixed': True}
conf['params']['sivers']['s b0 1'] ={'value':    0.00000e+00, 'min': 0, 'max':20.0, 'fixed': True}
conf['params']['sivers']['s b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':1.0, 'fixed': True}
conf['params']['sivers']['s c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': True}
conf['params']['sivers']['s c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}
conf['params']['sivers']['s d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': True}


conf['params']['sivers']['ub N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['sivers']['ub N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['sivers']['ub a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['sivers']['ub a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['sivers']['ub b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['sivers']['ub b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['sivers']['ub c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['sivers']['ub c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['sivers']['ub d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['sivers']['ub d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['sivers']['ub N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['sivers']['ub N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['sivers']['ub a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['sivers']['ub a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['sivers']['ub b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['sivers']['ub b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['sivers']['ub c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['sivers']['ub c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['sivers']['ub d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['sivers']['ub d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['sivers']['db N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['sivers']['db N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['sivers']['db a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['sivers']['db a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['sivers']['db b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['sivers']['db b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['sivers']['db c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['sivers']['db c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['sivers']['db d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['sivers']['db d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['sivers']['db N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['sivers']['db N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['sivers']['db a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['sivers']['db a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['sivers']['db b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['sivers']['db b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['sivers']['db c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['sivers']['db c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['sivers']['db d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['sivers']['db d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}

conf['params']['sivers']['sb N0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 10 , 'fixed': 's N0 1'}
conf['params']['sivers']['sb N1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 1'}
conf['params']['sivers']['sb a0 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 1'}
conf['params']['sivers']['sb a1 1'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 1'}
conf['params']['sivers']['sb b0 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 1'}
conf['params']['sivers']['sb b1 1'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 1'}
conf['params']['sivers']['sb c0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 1'}
conf['params']['sivers']['sb c1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 1'}
conf['params']['sivers']['sb d0 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 1'}
conf['params']['sivers']['sb d1 1'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 1'}
conf['params']['sivers']['sb N0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N0 2'}
conf['params']['sivers']['sb N1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max': 1.0, 'fixed': 's N1 2'}
conf['params']['sivers']['sb a0 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a0 2'}
conf['params']['sivers']['sb a1 2'] ={'value':    0.00000e+00, 'min':-2.0, 'max':10.0, 'fixed': 's a1 2'}
conf['params']['sivers']['sb b0 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b0 2'}
conf['params']['sivers']['sb b1 2'] ={'value':    0.00000e+00, 'min': 0.0, 'max':10.0, 'fixed': 's b1 2'}
conf['params']['sivers']['sb c0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c0 2'}
conf['params']['sivers']['sb c1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's c1 2'}
conf['params']['sivers']['sb d0 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d0 2'}
conf['params']['sivers']['sb d1 2'] ={'value':    0.00000e+00, 'min':-1.0, 'max': 1.0, 'fixed': 's d1 2'}


#--steps
conf['steps']={}


##--unpol + (sidis Sivers) + (sia Collins) + (sidis Collins) + (pp A_N)
conf['steps'][3]={}
conf['steps'][3]['dep']=[] #[1,6] #[2,4]
conf['steps'][3]['active distributions']=['pdf','pdfpi-','ffpi','sivers','collinspi','transversity','ffk','Htildepi']
#conf['steps'][3]['active distributions']=['pdf','pdfpi-','ffpi','sivers','ffk']
#conf['steps'][3]['active distributions']=['pdf', 'pdfpi-','ffpi','collinspi', 'transversity','ffk']
#conf['steps'][3]['active distributions']=['pdf','pdfpi-','ffpi','sivers','collinspi','transversity','ffk']
conf['steps'][3]['datasets']={}

conf['steps'][3]['datasets']['sidis']=[]
conf['steps'][3]['datasets']['sidis'].append(1010) #'sidis/expdata/1010.xlsx'  # |  proton   | pi+   | M_Hermes | hermes
conf['steps'][3]['datasets']['sidis'].append(1011) #'sidis/expdata/1011.xlsx'  # |  proton   | pi-   | M_Hermes | hermes
conf['steps'][3]['datasets']['sidis'].append(1012) #'sidis/expdata/1012.xlsx'  # |  proton   | k+   | M_Hermes | hermes
conf['steps'][3]['datasets']['sidis'].append(1013) #'sidis/expdata/1013.xlsx'  # |  proton   | k-   | M_Hermes | hermes
conf['steps'][3]['datasets']['sidis'].append(1014) #'sidis/expdata/1014.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes
conf['steps'][3]['datasets']['sidis'].append(1015) #'sidis/expdata/1015.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes
conf['steps'][3]['datasets']['sidis'].append(1016) #'sidis/expdata/1016.xlsx'  # |  deuteron | k+   | M_Hermes | hermes
conf['steps'][3]['datasets']['sidis'].append(1017) #'sidis/expdata/1017.xlsx'  # |  deuteron | k-   | M_Hermes | hermes

# conf['steps'][3]['datasets']['sidis'].append(2000) # proton   | pi+    | AUTsivers  | hermes  | PT
# conf['steps'][3]['datasets']['sidis'].append(2001) # proton   | pi+    | AUTsivers  | hermes  | x
# conf['steps'][3]['datasets']['sidis'].append(2002) # proton   | pi+    | AUTsivers  | hermes  | z
# conf['steps'][3]['datasets']['sidis'].append(2003) # proton   | pi-    | AUTsivers  | hermes | PT
# conf['steps'][3]['datasets']['sidis'].append(2004) # proton   | pi-    | AUTsivers  | hermes  | x
# conf['steps'][3]['datasets']['sidis'].append(2005) # proton   | pi-    | AUTsivers  | hermes  | z
# conf['steps'][3]['datasets']['sidis'].append(2006) # proton   | pi0    | AUTsivers  | hermes | PT
# conf['steps'][3]['datasets']['sidis'].append(2007) # proton   | pi0    | AUTsivers  | hermes  | x
# conf['steps'][3]['datasets']['sidis'].append(2008) # proton   | pi0    | AUTsivers  | hermes  | z
conf['steps'][3]['datasets']['sidis'].append(2026) # deuteron | pi+    | AUTsivers  | compass| PT
conf['steps'][3]['datasets']['sidis'].append(2027) # deuteron | pi+    | AUTsivers  | compass | x
conf['steps'][3]['datasets']['sidis'].append(2028) # deuteron | pi+    | AUTsivers  | compass | z
conf['steps'][3]['datasets']['sidis'].append(2029) # deuteron | pi-    | AUTsivers  | compass| PT
conf['steps'][3]['datasets']['sidis'].append(2030) # deuteron | pi-    | AUTsivers  | compass | x
conf['steps'][3]['datasets']['sidis'].append(2031) # deuteron | pi-    | AUTsivers  | compass | z
conf['steps'][3]['datasets']['sidis'].append(2512) # proton   | pi+    | AUTsivers  | compass    | x
conf['steps'][3]['datasets']['sidis'].append(2513) # proton   | pi+    | AUTsivers  | compass    | z
conf['steps'][3]['datasets']['sidis'].append(2514) # proton   | pi+    | AUTsivers  | compass    | PT
conf['steps'][3]['datasets']['sidis'].append(2515) # proton   | pi-    | AUTsivers  | compass    | x
conf['steps'][3]['datasets']['sidis'].append(2516) # proton   | pi-    | AUTsivers  | compass    | z
conf['steps'][3]['datasets']['sidis'].append(2517) # proton   | pi-    | AUTsivers  | compass    | PT
#conf['steps'][3]['datasets']['sidis'].append(2518) # proton   | pi+    | AUTsivers  | hermes  | x
#conf['steps'][3]['datasets']['sidis'].append(2519) # proton   | pi+    | AUTsivers  | hermes  | z
#conf['steps'][3]['datasets']['sidis'].append(2520) # proton   | pi+    | AUTsivers  | hermes  | pT
conf['steps'][3]['datasets']['sidis'].append(2521) # proton   | pi0    | AUTsivers  | hermes  | x
conf['steps'][3]['datasets']['sidis'].append(2522) # proton   | pi0    | AUTsivers  | hermes  | z
conf['steps'][3]['datasets']['sidis'].append(2523) # proton   | pi0    | AUTsivers  | hermes  | pT
#conf['steps'][3]['datasets']['sidis'].append(2524) # proton   | pi-    | AUTsivers  | hermes  | x
#conf['steps'][3]['datasets']['sidis'].append(2525) # proton   | pi-    | AUTsivers  | hermes  | z
#conf['steps'][3]['datasets']['sidis'].append(2526) # proton   | pi-    | AUTsivers  | hermes  | pT
conf['steps'][3]['datasets']['sidis'].append(2527) # proton   | pi+    | AUTsivers  | hermes  | x,z,pT
conf['steps'][3]['datasets']['sidis'].append(2528) # proton   | pi-    | AUTsivers  | hermes  | x,z,pT

conf['steps'][3]['datasets']['sidis'].append(4001)  #  compass  AUTcollins deuteron  pi+  pT
conf['steps'][3]['datasets']['sidis'].append(4000)  #  compass  AUTcollins deuteron  pi+   x
conf['steps'][3]['datasets']['sidis'].append(4002)  #  compass  AUTcollins deuteron  pi+   z
conf['steps'][3]['datasets']['sidis'].append(4004)  #  compass  AUTcollins deuteron  pi-  pT
conf['steps'][3]['datasets']['sidis'].append(4003)  #  compass  AUTcollins deuteron  pi-   x
conf['steps'][3]['datasets']['sidis'].append(4005)  #  compass  AUTcollins deuteron  pi-   z
conf['steps'][3]['datasets']['sidis'].append(3027)  #  compass  AUTcollins  proton   pi+ pt
conf['steps'][3]['datasets']['sidis'].append(3025)  #  compass  AUTcollins  proton  pi+   x
conf['steps'][3]['datasets']['sidis'].append(3010)  #  compass  AUTcollins  proton  pi+   z
conf['steps'][3]['datasets']['sidis'].append(3012)  #  compass  AUTcollins  proton  pi-  pt
conf['steps'][3]['datasets']['sidis'].append(3005)  #  compass  AUTcollins  proton  pi-   x
conf['steps'][3]['datasets']['sidis'].append(3013)  #  compass  AUTcollins  proton  pi-   z
# conf['steps'][3]['datasets']['sidis'].append(3026)  #   HERMES  AUTcollins  proton pi+   pt
# conf['steps'][3]['datasets']['sidis'].append(3000)  #   HERMES  AUTcollins  proton pi+    x
# conf['steps'][3]['datasets']['sidis'].append(3003)  #   HERMES  AUTcollins  proton pi+    z
# conf['steps'][3]['datasets']['sidis'].append(3016)  #   HERMES  AUTcollins  proton  pi-  pt
# conf['steps'][3]['datasets']['sidis'].append(3004)  #   HERMES  AUTcollins  proton  pi-   x
# conf['steps'][3]['datasets']['sidis'].append(3018)  #   HERMES  AUTcollins  proton  pi-   z
# conf['steps'][3]['datasets']['sidis'].append(3006)  #   HERMES  AUTcollins  proton  pi0   z
# conf['steps'][3]['datasets']['sidis'].append(3014)  #   HERMES  AUTcollins  proton  pi0   x
# conf['steps'][3]['datasets']['sidis'].append(3015)  #   HERMES  AUTcollins  proton  pi0  pt
#conf['steps'][3]['datasets']['sidis'].append(3700)  #   HERMES  AUTcollins  proton pi+    x
#conf['steps'][3]['datasets']['sidis'].append(3701)  #   HERMES  AUTcollins  proton pi+    z
#conf['steps'][3]['datasets']['sidis'].append(3702)  #   HERMES  AUTcollins  proton pi+    pt
conf['steps'][3]['datasets']['sidis'].append(3703)  #   HERMES  AUTcollins  proton  pi0   x
conf['steps'][3]['datasets']['sidis'].append(3704)  #   HERMES  AUTcollins  proton  pi0   z
conf['steps'][3]['datasets']['sidis'].append(3705)  #   HERMES  AUTcollins  proton  pi0   pT
#conf['steps'][3]['datasets']['sidis'].append(3706)  #   HERMES  AUTcollins  proton  pi-   x
#conf['steps'][3]['datasets']['sidis'].append(3707)  #   HERMES  AUTcollins  proton  pi-   z
#conf['steps'][3]['datasets']['sidis'].append(3708)  #   HERMES  AUTcollins  proton  pi-   pt
conf['steps'][3]['datasets']['sidis'].append(3709)  #   HERMES  AUTcollins  proton  pi+   x,z,pt
conf['steps'][3]['datasets']['sidis'].append(3710)  #   HERMES  AUTcollins  proton  pi-   x,z,pt

#conf['steps'][3]['datasets']['sidis'].append(9011)  #   COMPASS  AUTsinphiS  proton  h+    z
#conf['steps'][3]['datasets']['sidis'].append(9022)  #   COMPASS  AUTsinphiS  proton  h-    z
#conf['steps'][3]['datasets']['sidis'].append(9033)  #   COMPASS  AUTsinphiS  proton  h+    x
#conf['steps'][3]['datasets']['sidis'].append(9044)  #   COMPASS  AUTsinphiS  proton  h-    x
conf['steps'][3]['datasets']['sidis'].append(9055)  #   HERMES   AUTsinphiS  proton  pi+   x
conf['steps'][3]['datasets']['sidis'].append(9066)  #   HERMES   AUTsinphiS  proton  pi+   z
# #conf['steps'][3]['datasets']['sidis'].append(9077)  #   HERMES   AUTsinphiS  proton  pi+   pt
conf['steps'][3]['datasets']['sidis'].append(9088)  #   HERMES   AUTsinphiS  proton  pi0   x
conf['steps'][3]['datasets']['sidis'].append(9099)  #   HERMES   AUTsinphiS  proton  pi0   z
# #conf['steps'][3]['datasets']['sidis'].append(10010) #   HERMES   AUTsinphiS  proton  pi0   pt
conf['steps'][3]['datasets']['sidis'].append(10021) #   HERMES   AUTsinphiS  proton  pi-   x
conf['steps'][3]['datasets']['sidis'].append(10032) #   HERMES   AUTsinphiS  proton  pi-   z
#conf['steps'][3]['datasets']['sidis'].append(10043) #   HERMES   AUTsinphiS  proton  pi-   pt
#conf['steps'][3]['datasets']['sidis'].append(10054) #   HERMES   AUTsinphiS  proton  pi+   x,z,pt
#conf['steps'][3]['datasets']['sidis'].append(10065) #   HERMES   AUTsinphiS  proton  pi-   x,z,pt


conf['steps'][3]['datasets']['dy']=[]
conf['steps'][3]['datasets']['dy'].append(1000)       # proton-pi- |    | AUTsivers  | compass    | xbeam
conf['steps'][3]['datasets']['dy'].append(1001)       # proton-pi- |    | AUTsivers  | compass    | xtarget
conf['steps'][3]['datasets']['dy'].append(1002)       # proton-pi- |    | AUTsivers  | compass    | xF
conf['steps'][3]['datasets']['dy'].append(1003)       # proton-pi- |    | AUTsivers  | compass    | qT

conf['steps'][3]['datasets']['wz']=[]
conf['steps'][3]['datasets']['wz'].append(2000)       # proton-proton |W+/-| AUTsivers  | star    | pT
conf['steps'][3]['datasets']['wz'].append(2001)       # proton-proton |W+/-| AUTsivers  | star    | y
conf['steps'][3]['datasets']['wz'].append(2002)       # proton-proton |Z   | AUTsivers  | star    | y

conf['steps'][3]['datasets']['sia']=[]
conf['steps'][3]['datasets']['sia'].append(1000) # babar | pi,pi | AUL-0     | 9      | z1,z2,pT0  |
conf['steps'][3]['datasets']['sia'].append(1001) # babar | pi,pi | AUC-0     | 9      | z1,z2,pT0  |
conf['steps'][3]['datasets']['sia'].append(1002) # babar | pi,pi | AUC-0     | 36     | z1,z2      |
conf['steps'][3]['datasets']['sia'].append(1003) # babar | pi,pi | AUL-0     | 36     | z1,z2      |
conf['steps'][3]['datasets']['sia'].append(1004) # belle | pi,pi | AUT-0-CCP | 16     | z1,z2,qT   |
conf['steps'][3]['datasets']['sia'].append(1005) # belle | pi,pi | AUT-0     | 16     | z1,z2,qT   |
conf['steps'][3]['datasets']['sia'].append(2008) # babar | pi,pi | AUL-0     | 16     | z1,z2      |
conf['steps'][3]['datasets']['sia'].append(2009) # babar | pi,pi | AUC-0     | 16     | z1,z2      |
conf['steps'][3]['datasets']['sia'].append(3000) # bes3 | pi,pi | AUL-0     | 6     | z1,z2        |
conf['steps'][3]['datasets']['sia'].append(3001) # bes3 | pi,pi | AUC-0     | 6     | z1,z2        |
conf['steps'][3]['datasets']['sia'].append(3002) # bes3 | pi,pi | AUL-0     | 5     | z1,z2,pT     |
conf['steps'][3]['datasets']['sia'].append(3003) # bes3 | pi,pi | AUC-0     | 5     | z1,z2.pT     |

conf['steps'][3]['datasets']['AN']=[]
conf['steps'][3]['datasets']['AN'].append(1000) # BRAHMS pim 2.3
conf['steps'][3]['datasets']['AN'].append(1001) # BRAHMS   pim 4
conf['steps'][3]['datasets']['AN'].append(1002) # BRAHMS pip 2.3
conf['steps'][3]['datasets']['AN'].append(1003) # BRAHMS   pip 4
conf['steps'][3]['datasets']['AN'].append(2000) # STAR    piz 04
conf['steps'][3]['datasets']['AN'].append(2001) # STAR   piz 3.3
conf['steps'][3]['datasets']['AN'].append(2002) # STAR  piz 3.68
conf['steps'][3]['datasets']['AN'].append(2003) # STAR   piz 3.7
conf['steps'][3]['datasets']['AN'].append(2004) # STAR   piz 2008 |pT
conf['steps'][3]['datasets']['AN'].append(3000) # STAR    piz 2020 |xF
conf['steps'][3]['datasets']['AN'].append(3001) # STAR   piz 2020  |xF
conf['steps'][3]['datasets']['AN'].append(3002) # STAR  piz 2020   |pT
conf['steps'][3]['datasets']['AN'].append(3003) # STAR   piz 2020  |pT
#conf['steps'][3]['datasets']['AN'].append(3004) # STAR  piz 2020   |pT nonisolated
#conf['steps'][3]['datasets']['AN'].append(3005) # STAR   piz 2020  |pT nonisolated
#conf['steps'][3]['datasets']['AN'].append(4000) # STAR    jet 2020 |xF
#conf['steps'][3]['datasets']['AN'].append(4001) # STAR   jet 2020  |xF
conf['steps'][3]['datasets']['AN'].append(4002) # STAR   jet 2020  |xF
conf['steps'][3]['datasets']['AN'].append(4003) # STAR   jet 2020  |xF
conf['steps'][3]['datasets']['AN'].append(4004) # ANDY   jet       |xF

conf['steps'][3]['datasets']['AN'].append(5000) # STAR Collins pi0 zem, 200 GeV 
conf['steps'][3]['datasets']['AN'].append(5001) # STAR Collins pi0 zem, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5002) # STAR Collins pi0 zem, jTbin1 200 GeV 
conf['steps'][3]['datasets']['AN'].append(5003) # STAR Collins pi0 zem, jTbin2 200 GeV
conf['steps'][3]['datasets']['AN'].append(5004) # STAR Collins pi0 zem, jTbin3 200 GeV
conf['steps'][3]['datasets']['AN'].append(5005) # STAR Collins pi0 zem, jTbin4 200 GeV
conf['steps'][3]['datasets']['AN'].append(5006) # STAR Collins pi+ pT, z=0.14, 0<eta<1, 500 GeV 
conf['steps'][3]['datasets']['AN'].append(5007) # STAR Collins pi- pT, z=0.14, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5008) # STAR Collins pi+ pT, z=0.14, -1<eta<0, 500 GeV 
conf['steps'][3]['datasets']['AN'].append(5009) # STAR Collins pi- pT, z=0.14, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5010) # STAR Collins pi+ pT, z=0.24, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5011) # STAR Collins pi- pT, z=0.24, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5012) # STAR Collins pi+ pT, z=0.24, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5013) # STAR Collins pi- pT, z=0.24, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5014) # STAR Collins pi+ pT, z=0.38, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5015) # STAR Collins pi- pT, z=0.38, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5016) # STAR Collins pi+ pT, z=0.38, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5017) # STAR Collins pi- pT, z=0.38, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5018) # STAR Collins pi+ z, pT=10.6, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5019) # STAR Collins pi- z, pT=10.6, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5020) # STAR Collins pi+ z, pT=10.6, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5021) # STAR Collins pi- z, pT=10.6, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5022) # STAR Collins pi+ z, pT=20.6, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5023) # STAR Collins pi- z, pT=20.6, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5024) # STAR Collins pi+ z, pT=20.6, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5025) # STAR Collins pi- z, pT=20.6, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5026) # STAR Collins pi+ z, pT=31, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5027) # STAR Collins pi- z, pT=31, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5028) # STAR Collins pi+ z, pT=31, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5029) # STAR Collins pi- z, pT=31, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5030) # STAR Collins pi+ jT, z=0.13, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5031) # STAR Collins pi- jT, z=0.13, 0<eta<1, 500 GeV 
conf['steps'][3]['datasets']['AN'].append(5032) # STAR Collins pi+ jT, z=0.13, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5033) # STAR Collins pi- jT, z=0.13, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5034) # STAR Collins pi+ jT, z=0.23, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5035) # STAR Collins pi- jT, z=0.23, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5036) # STAR Collins pi+ jT, z=0.23, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5037) # STAR Collins pi- jT, z=0.23, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5038) # STAR Collins pi+ jT, z=0.37, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5039) # STAR Collins pi- jT, z=0.37, 0<eta<1, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5040) # STAR Collins pi+ jT, z=0.37, -1<eta<0, 500 GeV
conf['steps'][3]['datasets']['AN'].append(5041) # STAR Collins pi- jT, z=0.37, -1<eta<0, 500 GeV

conf['steps'][3]['datasets']['ANep']=[]
conf['steps'][3]['datasets']['ANep'].append(1000) # HERMES / proton / pi-
conf['steps'][3]['datasets']['ANep'].append(1001) # HERMES / proton / pi-
conf['steps'][3]['datasets']['ANep'].append(1002) # HERMES / proton / pi-
conf['steps'][3]['datasets']['ANep'].append(1003) # EIC / proton / pi-
conf['steps'][3]['datasets']['ANep'].append(1004) # EIC / proton / pi-
conf['steps'][3]['datasets']['ANep'].append(1005) # COMPASS / proton / pi-
conf['steps'][3]['datasets']['ANep'].append(1006) # JLAB12 / proton / pi-
conf['steps'][3]['datasets']['ANep'].append(2000) # HERMES / proton / pi+
conf['steps'][3]['datasets']['ANep'].append(2001) # HERMES / proton / pi+
conf['steps'][3]['datasets']['ANep'].append(2002) # HERMES / proton / pi+
conf['steps'][3]['datasets']['ANep'].append(2003) # EIC / proton / pi+
conf['steps'][3]['datasets']['ANep'].append(2004) # EIC / proton / pi+
conf['steps'][3]['datasets']['ANep'].append(2005) # COMPASS / proton / pi+
conf['steps'][3]['datasets']['ANep'].append(2006) # JLAB12 / proton / pi+
conf['steps'][3]['datasets']['ANep'].append(3000) # EIC / proton / pi

# --Lattice Data
conf['steps'][3]['datasets']['moments']=[]
conf['steps'][3]['datasets']['moments'].append(2000) # gT(u-d)
conf['steps'][3]['datasets']['moments'].append(2001) # gTu
conf['steps'][3]['datasets']['moments'].append(2002) # gTd
# #conf['steps'][3]['datasets']['moments'].append(2003) # gTs

#--Soffer Bound
conf['steps'][3]['datasets']['SB']=[]
conf['steps'][3]['datasets']['SB'].append(1000) # SB u quark
conf['steps'][3]['datasets']['SB'].append(2000)  # SB d quark