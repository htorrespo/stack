#!/usr/bin/python
# moles.py

import sys

class moles:

    def __init__(self):
        self.MC = 12.0107   # peso molecular del carbon (kg/kmol)
        self.MH = 1.00797   # peso molecular del hidrogeno (kg/kmol)
        self.MN = 14.0067   # peso molecular del nitrogeno (kg/kmol) 
        self.MS = 32.0650   # peso molecular del azufre  (kg/kmol)
        self.MO = 15.9994   # peso molecular del oxigeno  (kg/kmol)
        self.MAr = 39.948   # peso molecular del argon   (kg/kmol)



def main():


   i = Industrial('Entrada', 1.0, 27.0)
   print 'Evaluacion de caldera industrial Fiel Oil 6'
   '''(self, name, pbar, tambi, conteS, conteO2, conteCO2, tgases)'''
   fo6 = IndustrialFO6('Caldera 600 BHP', 1.0, 27.0, 0.957, 4.0, 12.0, 100.0)
   print 'CO2 = %s, ' % fo6.getCO2()
   print 'H2O = %s, ' % fo6.getH2O()
   print 'N2 = %s, ' % fo6.getN2()
   print 'total gases humedos de combustion = %s' % fo6.getGash()
   print 'total gases secos de combustion = %s' % fo6.getGass()
   print 'Caudal de gases humedos (ft3/lb Fuel Oil 6) =  %s' % fo6.getQgash()
   print 'Caudal de gases secos (ft3/lb Fuel Oil 6) =  %s' % fo6.getQgass()

if __name__ == '__main__':
   main()

