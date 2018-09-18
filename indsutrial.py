#!/usr/bin/python
# Industrial.py

import sys

class Industrial:
    ''' Representa una caldera industrial '''
    
    def __init__(self, name, pbar, tambi):
        self.name = name
        self.pbar = pbar
        self.tambi = tambi
        print '(Inicializando la caldera industrial: %s)' % self.name

class IndustrialFO6(Industrial):
    ''' Representa ... '''
    def __init__(self, name, pbar, tambi, conteS, conteO2, conteCO2, tgases):
        Industrial.__init__(self, name, pbar, tambi)
        self.fos = conteS/32.06
        self.conteO2 = conteO2
        self.conteCO2 = conteCO2
        self.tambi = tambi
        self.tgases = tgases
        self.foO2 = 0.20
        self.foh2 = 12.70
        self.foc = 86.40
        self.fo_exc = 0.00
        
    def getO2mol(self):
        return (self.foO2/32.0)
    
    def getH2O(self):
        return (self.foh2/2.016)
    
    def getCO2(self):
        return (self.foc/12.01)
    
    def getO2exc(self):
        return self.fo_exc
    
    def getTgas(self):
        return ((self.tgases * 1.8 + 32) + 460.0)
    
    def getSO2(self):
        return self.fos
        
    def getPbar(self):
        return self.pbar
        
    def getO2exceso(self):
        return (self.getO2() + self.getO2() * (self.getO2exc() ))
        
    def getO2(self):
        return ( self.getCO2() + (self.getH2O()/2.0) + self.getSO2() - self.getO2mol() )
    
    def getN2(self):
        return (0.79/0.21)*(self.getCO2() + self.getH2O()/2 + self.getSO2() - self.getO2mol() )
    
    def getGass(self):
        return (self.getCO2() + self.getSO2()  + self.getN2())
    
    def getGash(self):
        return (self.getCO2() + self.getH2O() + self.getSO2() + self.getN2())
    
    def getQgass(self):
        return ((self.getGass()/100.0)*0.7302*self.getTgas()/self.getPbar())
        
    def getQgash(self):
        return ((self.getGash()/100.0)*0.7302*self.getTgas()/self.getPbar())

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
