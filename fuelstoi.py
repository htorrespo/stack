#!/usr/bin/python
# fuelstoi.py

import sys

class fuelstoic:
    ''' Representa una caldera industrial '''
    ''' Relacion de las siguientes variables/constantes
        b -> contenido de CO2
        c -> contenido de H2O
        d -> contenido de O2
        e -> contenido de N2
        f -> contenido de CO
        g -> contenido de NO
        h -> contenido de NO2
        i -> contenido de CxHy (char)
        j -> contenido de SO2
        k -> contenido de N2O\
        l -> contenido de H2
        m -> contenido de NH3
        n -> contenido de HCN
        o -> contenido de CxtHyt
        p -> contenido de Ar 
        q -> contenido de CO2 en el aire
        r -> contenido de H2O en el aire

    '''
    
    def __init__(self, yc, yh, yo, yn, ys):
        self.YC = yc
        self.YH = yh
        self.YO = yo
        self.YN = yn
        self.YS = ys
    
    def getC(self):
        return self.YC
        
    def getH(self):
        return self.YH

    def getO(self):
        return self.YO
    
    def getN(self):
        return self.YN
    
    def getS(self):
        return self.YS

    ceX2 = (YArAir + YCO2Air)/YO2Air
    ceX8 = 2.*YC + YH/2. + 2.*YS - YO 

    zs = (100.)/*(YN2Air/YO2Air+(YN+2.*YC+2.*YS)/ceX8+ceX2)
    AS = (2.*zs)/ceX8
    bs = AS*YC
    cs = AS*YH
    js = AS*YS
    ps = zs*YArAir/YO2Air
    qs = zs*YCO2Air/YO2Air
    rs = zs*YH2OAir/YO2Air

    e = 100.-bs-zs*ceX2-js


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
