#!/usr/bin/python
# file.py

import sys

class Chimenea:
    ''' Representa una caldera industrial '''

    
    def __init__(self, name, pbar, tambi):
        self.name = name
        self.pbar = pbar
        self.tambi = tambi
        print '(Inicializando la caldera industrial: %s)' % self.name
    
    def __init__(self, l_upstream, l_downstream):
        self.name = name
        self.l_upstream = l_upstream
        self.l_downstream = l_downstream
        print '(Inicializando la chimenea : %s)' % self.name

class Circular(Chimenea):
    ''' Representa ... '''
    def __init__(self, name, l_upstream, l_downstream, stack_dist1, stack_dist2, stack_dia):
        Industrial.__init__(self, name, l_upstream, l_downstream)
        self.l_upstream = l_upstream
        self.l_downstream = l_downstream
        self.stack_dist1 = stack_dist1
        self.stack_dist2 = stack_dist2
        self.stack_dia = stack_dia
        
    def getlupstream(self):
        return (self.l_upstream)
    
    def getldownstream(self):
        return (self.l_downstream)
    
    def getStackDist1(self):
        return (self.stack_dist1)
    
    def getStackDist2(self):
        return (self.stack_dist2)
    
    def getDiaUpstream(self):
        return (l_upstream/self.stack_dia)
    
    def getDiaDownstream(self):
        return (l_downstream/self.stack_dia)

    def getNoParticula(self):
        if (dia_up >= 2.0 & dia_up < 4.99):
            self.np_parti_r = 24
        elif (dia_up >= 5.0 & dia_up < 5.99):
            self.np_parti_r = 20
        elif (dia_up >= 6.0 & dia_up < 6.99):
            self.np_parti_r = 16
        elif (dia_up >= 7.0 & dia_up < 7.99):
            self.np_parti_r = 12
        elif (dia_up >= 8 & self.stack_dia >= 20.3 & self.stack_dia <= 50.8):
            self.np_parti_r = 8
        else:
            self.np_parti_r = 12
        return (self.np_parti_r)


    def getNovelocidad(self):
        if (dia_down >= 0.5 & dia_down < 1.4):
            self.np_gases_r = 16
        elif (dia_down >= 1.25 & dia_down < 1.49):
            self.np_gases_r = 16
        elif (dia_down >= 1.50 & dia_down < 1.74):
            self.np_gases_r = 12
        elif (dia_down >= 1.75 & dia_down < 1.99):
            self.np_gases_r = 12
        elif (dia_down >= 2 & self.stack_dia >= 20.3 & self.stack_dia <= 50.8):
            self.np_gases_r = 8
        else:
            self.np_gases_r = 12
        return (self.np_gases_r)


np_parti_r # puntos requeridos para particulas,
np_gases_r

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


