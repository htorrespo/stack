#!/usr/bin/python
# Chimenea.py
import sys

class Chimenea:
    ''' determina el # puntos en chimeneas circulares o rectangulares'''

    npc_p = 0              # numero de puntos c. circular xa particulas
    npc_g = 0              # numero de puntos c. circular xa gases
    npr_p = 0              # numero de puntos c. rectangular xa particulas
    npr_g = 0              # numero de puntos c. rectangular xa gases

    npupc_p = 0            # numero de puntos c. circular upstream xa particulas
    npdwc_p = 0            # numero de puntos c. circular dwonstream xa particulas
    npupc_g = 0            # numero de puntos c. circular upstream xa gases
    npdwc_g = 0            # numero de puntos c. circular dwonstream xa gases

    npupr_p = 0            # numero de puntos c. rectangular upstream xa particulas
    npdwr_p = 0            # numero de puntos c. rectangular dwonstream xa particulas
    npupr_g = 0            # numero de puntos c. rectangular upstream xa gases
    npdwr_g = 0            # numero de puntos c. rectangular dwonstream xa gases

    def __init__(self, diametro, d_upstream, d_downstream): 
        self.d = diametro
        self.du = d_upstream / self.d
        self.dd = d_downstream / self.d
        self.description = "Metodo EPA 1, # de puntos"
        self.author = "Henry Torres P."

    def setPuntos(self):
        # la chimenea esta entre 12 y 24 pulgadas (30.5 y 61.0 m)
        if  ((self.d > 30.5) and (self.d < 61.0)):
            Chimenea.npc_p, Chimenea.npc_g = 8, 8
            Chimenea.npr_p, Chimenea.npr_g = 9, 8
        # el sitio esta a 2 diametros del disturbio inferior ?
        # el sitio esta a 0.5 diametros del disturbio superior ?
        if  ((self.dd < 2.0) or (self.du < 0.5)):
            print ("No se recomienda utilizar este método ...")
        #else:
        # el sitio esta entre 2 y 5 diametros del disturbio inferior ?
        # el sitio esta entre 0.5 a 1.25 del disturbio superior ?
        if  ((self.dd < 5.0) or (self.du < 1.25)):
            Chimenea.npdwc_p, Chimenea.npupc_p = 24, 24
            Chimenea.npdwr_p = 25
            Chimenea.npdwc_g, Chimenea.npdwr_g, Chimenea.npupc_g, = 16, 16, 16
        # el sitio esta entre 1.25 a 1.50 del disturbio superior ?
        if  ((self.du >= 1.25) and (self.du < 1.50)):
            Chimenea.npupc_p, Chimenea.npdwr_p = 20, 20
            Chimenea.npupc_g, Chimenea.npdwr_g = 16, 16
        # el sitio esta entre 1.50 a 1.75 del disturbio superior ?
        if  ((self.du >= 1.50) and (self.du < 1.75)):
            Chimenea.npupc_p, Chimenea.npupc_g, Chimenea.npdwr_p, Chimenea.npdwr_g = 16, 16, 16, 16
        # el sitio esta entre 1.75 y > 2.5 del disturbio superior ?
        # el sitio esta entre 7 y 10 diametros del disturbio inferior ?
        if  ((self.du >= 1.75) or (self.dd >= 7.0)):
            Chimenea.npupc_p, Chimenea.npupc_g, Chimenea.npdwr_p, Chimenea.npdwr_g = 12, 12, 12, 12
            Chimenea.npdwc_p, Chimenea.npdwc_g, Chimenea.npdwr_p, Chimenea.npdwr_g = 12, 12, 12, 12
        # el sitio esta entre 5 y 6 diametros del disturbio inferior ?
        if  ((self.dd >= 5.0) and (self.dd < 6.0)):
            Chimenea.npdwc_p, Chimenea.npdwr_p = 20, 20
            Chimenea.npdwc_g, Chimenea.npdwr_g = 16, 16
        # el sitio esta entre 6 y 7 diametros del disturbio inferior ?
        if  ((self.dd >= 6.0) and (self.dd < 7.0)):
            Chimenea.npdwc_p, Chimenea.npdwr_p = 16, 16
            Chimenea.npdwc_g, Chimenea.npdwr_g = 12, 12


    def printText(texto, puntos):
        pt = puntos
        txt = texto 
        if pt != 0:
            print pt

    def getPuntos(self):
        self.printText("numero de puntos c. circular xa particulas   :"  + str(Chimenea.npc_p) )
        self.printText("numero de puntos c. circular xa gases        :" + str(Chimenea.npc_g) )
        self.printText("numero de puntos c. rectangular xa particulas:" + str(Chimenea.npr_p) )
        self.printText("numero de puntos c. rectangular xa gases     :" + str(Chimenea.npr_g) )

        self.printText("numero de puntos c. circular upstream xa particulas   :" + str(Chimenea.npupc_p) )
        self.printText("numero de puntos c. circular dwonstream xa particulas :" + str(Chimenea.npdwc_p) )
        self.printText("numero de puntos c. circular upstream xa gases        :" + str(Chimenea.npupc_g) )
        self.printText("numero de puntos c. circular dwonstream xa gases      :" + str(Chimenea.npdwc_g) )

        self.printText("numero de puntos c. rectangular upstream xa particulas   :" + str(Chimenea.npupr_p) )
        self.printText("numero de puntos c. rectangular dwonstream xa particulas :" + str(Chimenea.npdwr_p) )
        self.printText("numero de puntos c. rectangular upstream xa gases        :" + str(Chimenea.npupr_g) )
        self.printText("numero de puntos c. rectangular dwonstream xa gases      :" + str(Chimenea.npdwr_g) )


c = Chimenea(0.5036, 2.0, 3.0)
c.description
c.author
c.setPuntos()
c.getPuntos()
