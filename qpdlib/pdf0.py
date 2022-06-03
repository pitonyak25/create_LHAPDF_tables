#!/usr/bin/env python
import sys
import os
import numpy as np
import time
from qpdlib.core import CORE
from qpdlib.interpolator import INTERPOLATOR
from tools.config import conf

class PDF(CORE):
    """
    upol PDF for proton. Use SU2 symetry to get for n
    """

    def __init__(self,hadron='p'):
        self.aux = conf['aux']
        self.set_default_params(hadron)
        self.setup(hadron)

    def set_default_params(self,hadron):

        # free params
        if hadron=='p':
            self._widths1_uv  = 0.3
            self._widths1_dv  = 0.3
            self._widths1_sea = 0.3

            self._widths2_uv  = 0
            self._widths2_dv = 0
            self._widths2_sea = 0

        if hadron=='pi-':
            self._widths1_ubv  = 0.3
            self._widths1_dv  = 0.3
            self._widths1_sea = 0.3

            self._widths2_ubv  = 0
            self._widths2_dv = 0
            self._widths2_sea = 0

        # internal
        self.widths1 = np.ones(11)
        self.widths2 = np.ones(11)

    def setup(self,hadron):
        if hadron=='p':
            for i in range(11):
                if   i == 1: self.widths1[i] = self._widths1_uv
                elif i == 3: self.widths1[i] = self._widths1_dv
                else:        self.widths1[i] = self._widths1_sea
            for i in range(11):
                if   i == 1: self.widths2[i] = self._widths2_uv
                elif i == 3: self.widths2[i] = self._widths2_dv
                else:        self.widths2[i] = self._widths2_sea
   
        if hadron=='pi-':
            for i in range(11):
                if   i == 2: self.widths1[i] = self._widths1_ubv
                elif i == 3: self.widths1[i] = self._widths1_dv
                else:        self.widths1[i] = self._widths1_sea
            for i in range(11):
                if   i == 2: self.widths2[i] = self._widths2_ubv
                elif i == 3: self.widths2[i] = self._widths2_dv
                else:        self.widths2[i] = self._widths2_sea

    def get_C(self, x, Q2):
        return self.pdf.get_f(x,Q2)

    def get_state(self):
        return self.widths1,self.widths2

    def set_state(self, state):
        self.widths1 = state[0]
        self.widths2 = state[1]

if __name__ == '__main__':

    from qcdlib.aux import AUX

    conf['aux']  = AUX()
    conf['pdfpi-']  = PDF('pi-')
    conf['pdf']  = PDF('p')

    x = 0.15
    Q2 = 2.4
    print(conf['pdfpi-'].get_C(x, Q2))
    print(conf['pdf'].get_C(x, Q2))
    print(conf['aux'].q2qbar(conf['pdf'].get_C(x, Q2)))


