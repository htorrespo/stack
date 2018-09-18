#!/usr/bin/python
# fuel.py

import sys

class fuel:
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

    ceX1 = d + f + g + h + i + k + l + m + n + o
    ceX2 = (YArAir + YCO2Air)/YO2Air
    ceX4 = f + i*x + n + o*xt
    ceX5 = i*y + 2.*l +3.*m + n + o*yt
    ceX6 = g + h + 2.*k + m + n
    ceX7 = 2.*d + f + g + 2.*h + k
    ceX8 = 2.*YC + YH/2. + 2.*YS - YO 
    ceX9 = 2.*ceX4 + ceX5/2. - ceX7 

    z = (100.-ceX1+ceX4+ceX6/2.-ceX9/ceX8*(YC+YN/2.+YS))/*(YN2Air/YO2Air+(YN+2.YC+2.YS)/ceX8+ceX2)
    a = (2.*z+ceX9)/ceX8
    b = a*YC-ceX4
    c = (a*YH-ceX5)/2.
    j = a*YS
    p = z*YArAir/YO2Air
    q = z*YCO2Air/YO2Air
    r = z*YH2OAir/YO2Air

    e = 100.-ceX1-b-z*ceX2-j


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

