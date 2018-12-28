# Repositorio para estudios de emisiones en chimenea

Este repositorio sirve para varios propósitos, cálculos preliminares, 
intermedios y finales para la evaluación de las emisiones de chimenea. 
Estas determinaciones las hacen los técnicos que conocen los métodos EPA 
o ISO para la evaluación de emisiones en chimenea. Es necesario tener 
conocimientos basicos en mecanica de fluidos y termodinámica.

En este sitio se encuentran los métodos de la EPA con varias funciones 
organizadas en paquetes para uso en proyectos personales, pero se pueden 
ampliar con el tiempo.

## Functioness o metodos

### Nomenclature EPA Method 1

L=longitud. 

n =numero total de puntos transversales. 

Pi=angulo de inclinación (pitch) en el punto transversal i, grados. 

Ravg=angulo resultante promedio, grados. 

Ri=ángulo resultante en el punto transversal i, grados. 

Sd=desviación estándar, gradoa. 

W=ancho. 

Yi=ángulo de orientación (yaw) en el punto transversal i, grado. 

### Nomenclature EPA Method 1A - No tiene

### Nomenclature EPA Method 2

A=area de la sección transversal de la cimenea, m2(ft2). 

Bws=vapor de agua en la corriente gaseosa (metodo 4 o alternativo), fracción de volumen. 

Cp= coeficiente del tubo pitot, adimensional.

Cp(s)= coeficente del tubo pitot tipo S, adimensional. 

Cp(std)=coeficiente del tubo pitot estandar; usar 0.99 si el coeficiente es desconocido y esta diseñado conforme a los criterios de la seccion 6.7.1 a 6.7.5 de este metodo.

De= diametro equivalente. 

K=0.127 mm H2O (unidades metricas). 0.005 in. H2O (unidades inglesas). 

Kp= constante de la ecuacion de velocidad. 

L=longitud. 

Md= peso molecular del gas en chimenea, base seca(ver seccion 8.6), g/g-mol (lb/lb-mol). 

Ms=peso molecular del gas en chimenea, base humeda, g/g-mol (lb/lb-mol). 

n =numero total de puntos transversales. 

Pbar= presion barometrica en el sitio de medicion, mm Hg (in. Hg). 

Pg= presion estatica en chimenea, mm Hg (in. Hg). 

Ps= presion absoluta en chimenea(Pbar + Pg), mm Hg (in. Hg), 

Pstd= presion absoluta estandar, 760 mm Hg (29.92 in. Hg). 

Qsd= tasa de flujo volumetrico (caudal) del gas seco corregido a condiciones estandar, dscm/hr (dscf/hr).

T= factor de sensibilidad para manometros diferenciales de presion.

Ts(abavg)=  temperatura absoluta promedio en la chimenea, °K (°R).
= 273 + Ts para unidades metricas,
= 460 + Ts para unidades metricas.

Ts= temperatura en la chimenea, °C (( °deg;F). 
=273 + Ts para unidades metricas, 
=460 + Ts para unidades metricas. 

Tstd= temperatura estandar absoluta, 293 °K (528 °R). 

Vs= velocidad promedio en chimenea, m/s (ft/s). 

W=ancho.

Δp= cabeza de velocidad del gas en chimenea, mm H2O (in. H20).

Δpi= lectura de cabeza de velocidad individual en el punto transversal "i", mm (in.) H2O. 

Δpstd= cabeza de velocidad medida con el tubo pitot estandar, cm (in.) H2O.

Δps= cabeza de velocidad medida con el tubo pitot Tipo S, cm (in.) H2O. 

3600= factor de conversion, sec/hr. 

18.0= peso molecular del agua, g/g-mol (lb/lb-mol). 

### Nomenclature EPA Method 2A

f= lectura final.

i= lectura inicial. 

Pbar= presion barometrica en el sitio de medicion, mm Hg (in. Hg). 

Pg= presion estatica en chimenea, mm Hg (in. Hg).

Qs= tasa del flujo (caudal) del gas, m3/min, condiciones standar.

s = condiciones estandar, 20 °C y 760 mm Hg

Tr= temperatura promedio en el medidor de referencia., °K (°R). 

Tm= temperatura promedio en el medidor, °K (°R).

Vr= volumen (lectura) en el medidor de referencia, m3. 

Vm= volumen (lectura) en el medidor, m3. 

Ym= coeficiente de calibracion en el medidor, adimensional. 

θ= periodo (tiempo) transcurrido, min.

### Nomenclature EPA Method 2B

COe= Concentración media de monóxido de carbono en el sistema de escape, ppm.

(CO2)a= Concentración de dióxido de carbono ambiental, ppm (si se mide durante la prueba, se puede asumir es 380 ppm).

(CO2)e= Concentración media de dióxido de carbono en el sistema de escape, ppm.

HCe= Concentración orgánica media en el sistema de escape según lo definido por el gas de calibración, en ppm.

Hci= Concentración orgánica media en la entrada del sistema según lo definido por el gas de calibración, en ppm.

Ke= factor de calibracion del gas (hidrocarburos) para la salida del analizador de hidrocarburos, adimensional (igual al número de átomos de carbono por molécula del gas utilizado para calibrar el analizador (2 para etano, 3 para propano, etc.))

Ki= factor de calibracion del gas (hidrocarburos) para la entrada del analizador de hidrocarburos, adimensonal

Ves= volumen del gas de escape, m3.

Vis= volumen del gas de entrada, m3.

Qes= tasa volumetrica del flujo del gas a la salida, m3/min.

Qis= tasa volumetrica del flujo del gas a la entrada, m3/min.

Ө= tiempo de ejecucion del muestreo, min.

S = condiciones estandar, 20 °C y 760 mm Hg

### Nomenclature EPA Method 2C - No tiene

### Nomenclature EPA Method 2D

Pbar= presion barometrica en el sitio de medicion, mm Hg (in. Hg). 

Pm= presion estatica promedio en el medidor, mm Hg (in. Hg). 

Qr= lectura de la tasa de flujo volumetrica en el medidor de referencia, m3/min (ft3/min). 

Qm= lectura de la tasa de flujo volumetrica en el medidor, m3/min (ft3/min). 

Tr= temperatura absoluta promedio en el medidor de referencia, °K (°R). 

Tm= temperatura absoluta promedio en el medidor, °K (°R). 

Kl=0.3855 °K/mm Hg para unidades metricas,=17.65 °R/in. Hg para unidades inglesas

### Nomenclature EPA Method 2E

A= edad del rellemo sanitario, yr.

Aavg= edad promedio de los residuos analizados, yr.

Ai= edad del desecho en la fraccion i, yr.

Ar= tasa de aceptacion / recibo, Mg/yr.

CNMOC=NMOC concentracion, ppmv como hexano (CNMOC=Ct/6).

Co= Concentracion de N2 a la salida, ppmv.

Ct= concentracion de NMOC, ppmv (carbon equivalente) del Metodo 25C.

Cw=concentracion de N2 en el pozo, ppmv.

D= Profundidad afectada por los pozos de prueba, m.

Dst= Profundidad afectada por los pozos de prueba en la prueba de corto plazo, m.

### Nomenclature EPA Method 2F

A= area transversal de la chimenea o ducto, m2(ft2).

Bws= vapor de agua en la corriente gaseosa (metodo 4 o alternativo), fracción de volumen.

Kp_metric = 34.97 # m/s ({(g/g-mol)(mm Hg)}/{(K)(mm H2O)})^1/2

Kp_english = 85.49 # ft/s ({(lb/bl-mol)(in.Hg)}/{(R)(in.H2O)})^1/2

Md= peso molecular del gas en chimenea, base seca (ver seccion 8.6), g/g-mol (lb/lb-mol). 

Ms= peso molecular del gas en chimenea, base humeda, g/g-mol (lb/lb-mol).

Pbar= presion barometrica en el sitio de medicion, mm Hg (in. Hg).

Pg= presion estatica en chimenea, mm Hg (in. Hg).

Ps= presion absoluta en chimenea(Pbar + Pg), mm Hg (in. Hg), 

Pstd= presion absoluta estandar, 760 mm Hg (29.92 in. Hg).

13.6= factor de conversion de mm H2O (in. H2O) a mm Hg (in. Hg).

Qsd= tasa de flujo volumetrico (caudal) del gas seco corregido a condiciones estandar, dscm/hr (dscf/hr).

Qsw= tasa de flujo volumetrico (caudal) del gas humedo corregido a condiciones estandar, wscm/hr (wscf/hr).

Ts(avg)= temperatura absoluta promedio en la chimenea o ducto de todos los puntos transversales.

ts(i)= temperatura del gas en chimenea o ducto, C (F), en el punto transversal i.

Ts(i)= temperatura absoluta del gas en chimenea o ducto, en el punto transversal i.

Tstd= temperatura estandar absoluta, 293 °K (528 °R).

F1(i)= cociente del ángulo de inclinación (pitch), aplicable en el punto transversal i, adimensional.

F2(i)= coeficiente de calibración de la velocidad de la sonda 3-D, aplicable en el punto transversal i, adimensional.

(P4-P5)I= Presión diferencial del flujo de gas en la chimenea o ducto para el angulo de inclinación (pitch), mm H2O (pulg. H2O), en el punto transversal i.

(P1-P2)I = cabeza de velocidad (presion diferencial) del flujo del gas en chimenea o ducto, en el punto transversal i.

va(i)= velocidad axial reportada en chimenea o ducto,  m/sec (ft/sec), en el punto transversal i.

va(avg)= velocidad axial promedio en chimenea o ducto,  m/sec (ft/sec), en todos los puntos transversales.

3,600= factor de conversion, s/hr.

18.0= peso molecular del agua, g/g-mol (lb/lb-mol).

θy(i)= Ángulo de desviación (yaw), grados, en el punto transversal i.

θp(i)= Ángulo de inclinación (pitch), grados, en el punto transversal i.

n=numero total de puntos transversales.

### Nomenclature EPA Method 2G

A=Cross-sectional area of stack or duct at the test port location, m2(ft2).

Bws=vapor de agua en la corriente gaseosa (metodo 4 o alternativo), fracción de volumen.

Cp=coeficiente del tubo pitot, adimensional.

F2(i)= coeficiente de calibración de la velocidad de la sonda 3-D (al angulo de inclinacion - pitch - 0 grados), aplicable en el punto transversal i, adimensional.

Kp_metric = 34.97 # m/s ({(g/g-mol)(mmHg)}/{(K)(mmH2O)})^1/2

Kp_english = 85.49 # ft/s ({(lb/bl-mol)(in.Hg)}/{(R)(in.H2O)})^1/2

Md= peso molecular del gas en chimenea, base seca(ver seccion 8.6), g/g-mol (lb/lb-mol). 

Ms= peso molecular del gas en chimenea, base humeda, g/g-mol (lb/lb-mol).

Pbar= presion barometrica en el sitio de medicion, mm Hg (in. Hg).

Pg= presion estatica en chimenea, mm Hg (in. Hg).

Ps= presion absoluta en chimenea(Pbar + Pg), mm Hg (in. Hg), 

Pstd= presion absoluta estandar, 760 mm Hg (29.92 in. Hg).

13.6= factor de conversion de mm H2O (in. H2O) a mm Hg (in. Hg).

Qsd= tasa de flujo volumetrico (caudal) del gas seco corregido a condiciones estandar, dscm/hr (dscf/hr).

Qsw= tasa de flujo volumetrico (caudal) del gas humedo corregido a condiciones estandar, wscm/hr (wscf/hr).

ts(i)= temperatura en chimenea o ducto, °C (°F), en el punto transversal i.

Ts(i)= temperatura absoluta en chimenea o ducto, °K (°R), en el punto transversal i.

Ts(avg)= temperatura absoluta promedio en chimenea o ducto de todos los puntos transversales

Tstd= temperatura estandar absoluta, 293 °K (528 °R).

va(i)= velocidad axial reportada en chimenea o ducto,  m/sec (ft/sec), en el punto transversal i.

va(avg)= velocidad axial promedio en chimenea o ducto,  m/sec (ft/sec), en todos los puntos transversales.

Δpi= lectura de cabeza de velocidad individual en el punto transversal "i", mm (in.) H2O. 

(P1-P2)= cabeza de velocidad (presion diferencial) en chimenea o ducto, medido con una sonda 3D, mm H2O (in. H2O), aplicable al punto transversal i.

Δpstd= cabeza de velocidad medida con el tubo pitot estandar, cm (in.) H2O.

3,600= factor de conversion, s/h.

18.0= peso molecular del agua, g/g-mol (lb/lb-mol).

θy(i)= Ángulo de desviación (yaw), grados, en el punto transversal i.

n=numero total de puntos transversales.

### Nomenclature EPA Method 2H

vavg= velocidad promedio del gas en chimenea, ajustado por efecto de las paredes, ft/s (m/s) actuales.

viI= valor puntual de velocidad del gas en chimenea por el Metodo 1 en sectores interiores de igual area, ft/s (m/s) actual;

vej= valor puntual de velocidad del gas en chimenea, ajustado por efecto de paredes, por el Metodo 1 en sectores exteriores de igual area, ft/s (m/s) actual;

i = indice del Metodo 1, puntos transversales interiores de igual area;

j = indice del Metodo 1, puntos transversales exteriores de igual area;

n =numero total de puntos transversales;

vdecd= decaimiento de velocidad por efecto pared para un sub-sector localizado entre el punto transversal a la distancia d-1 (en unidades metricas d-2.5) y d en la pared, ft/s (m/s) actual;

vd= velocidad del gas en chimenea medida a la distancia d en la pared, ft/s (m/s) actual; Nota: v0=0;

d = the distance of a 1-in. incremented wall effects traverse point from the wall, for traverse points d 1through dlast, in. (cm);

Ad= the cross-sectional area of a sub-sector located between the traverse points at distances d−1 (in metric units, d−2.5 ) and d from the wall, in.2(cm2) (e.g., sub-sector A2 shown in Figures 2H–3 and 2H–4);

r = radio de la chimenea o ducto, in. (cm);

Qd= tasa de flujo volumetrica (caudal) del gas para el sub-sector localizado entre el punto transversal a la distancia d-1 (en unidades metricas d-2.5) y d de la pared, ft-in.2/s (m-cm2/s) actuales

Qd1->dlast= tasa de flujo volumetrica (caudal) del gas para todos los sub-sectores localizados entre la pared y dlast, ft-in.2/s (m-cm2/s) actuales

dlast= la distancia entre la pared y el ultimo 1-in. punto incrementado por efecto de la pared, in. (cm); 

Adrem= area de la seccion transversal del sub-sector localizado entre dlast y el borde interior del sector mas cercano a la pared del Metodo 1, in.2(cm2)(ver Figura 2H–4);


p = numero de puntos transversales por diametro del Metodo 1, p ≥8 (e.g., para una travbesia de 16 puntos, p =8);

drem= distancia desde la pared del centroide del área entre la d-last y el borde interior del sector más cercano a la pared del Método 1 , in. (cm);

Qdrem= fluo volumetrico (caudal) total del gas en chimenea para el subsector ubicado entre el d-last y el borde interior del sector más cercano a la pared, ft-in2 / s (m-cm2 / s);

vdrem= velocidad del gas en chimenea medida a una distancia drem desde la pared, ft/s (m/s) actual;

QT= tasa de flujo volumetrica (caudal) total del gas en chimenea para el sector mas cercano a la pared por el Metodo 1, ft-in2 / s (m-cm2 / s);

Vej= reemplazo de la velocidad en chimenea para el Metodo 1 del sector mas
cercano a la pared, i.e., velocidad puntual en la chimenea, ajustado por 
efectos de pared, para el sector j-esimo mas cercano a la pared, 
ft/s (m/s) actual.

VAVG=  velocidad promedio en chimenea que tiene en cuenta el decaimiento 
de la velocidad cerca a las paredes, ft/s (m/s) actual.

WAF= factor de ajuste por efecto de paredes derivado de vavg y VAVG para 
un unico punto transversal, adimensional

vfinal= velocidad promedio en chimenea final ajustado por efecto de 
paredes, que reemplaza la velocidad promedio en chimenea sin ajuste 
obtenido con el Metodo 2, 2F, o 2G para pruebas de campo empleando un 
unico punto transversal, ft/s (m/s) actual.

WAF'= factor de ajuste por efecto de paredes que se aplica a la velocidad 
promedio, sin ajuste por efecto de paredes, para obtener la velocidad 
promedio en chimenea final ajustado por efecto de paredes vfinal o 
vfinal(k), adimensional

vfinal(k)= velocidad promedio en chimenea final ajustado por efectos de 
pared que reemplaza la velocidad promedio en chimenea sin auste obtenido 
con el Metodo 2, 2F, o 2G en una ejecucion k de una prueba RATA u otros 
procedimientos de ejecuciones de muestreo multiples, ft/s (m/s) actual.

vavg(k)= velocidad promedio en chimenea, obtenida en el procedimiento de 
muestreo k de una prueba RATA u u otros procedimientos de ejecuciones de 
muestreo multiples, sin ajuste por decaimiento de velocidad cerca a las 
paredes, ft/s (m/s) actual.

k= indice de ejecuciones en un RATA u otro procedimiento de ejecuciones multiples


### Nomenclature EPA Method 3

Md=peso molecular del gas en chimenea, base seca( ver seccion 8.6), g/g-mol (lb/lb-mol). 

%CO2=porcentaje de CO2 en volumen, base seca.

%O2= porcentaje de O2 en volumen, base seca.

%CO= porcentaje de CO en volumen, base seca.

%N2= porcentaje de N2 en volumen, base seca.

0.280= peso molecular de N2 or CO, dividido en 100.

0.320= peso molecular de O2 dividido en 100.

0.440= peso molecular de CO2 dividido en 100.

### Nomenclature EPA Method 3A - no tiene

### Nomenclature EPA Method 3B


%EA= porcentaje exceso de aire.

0.264= cociente O2 a N2 en aire, v/v.

### Nomenclature EPA Method 3C

Bw= contenido de humedad en la muestra, fraccion.

CN2= concentracion de N2 medida (por Method 3C), fraccion.

CN2Corr= concentracion de N2 medida corregida solamente por dilucion, fraccion.

Ct= concentracion de NMOC calculada, ppmv C equivalente.

Ctm= concentracion de NMOC medida, ppmv C equivalente.

Pb= presion barometrica, mm Hg.

Pt= presion absoluta en el tanque, pero antes de presurizacion, mm Hg absoluta.

Ptf= presion absoluta en el taque de muestreo despues de presurizacion, mm Hg absoluta.

Pti= presion absoluta en el tanque de muestreo despues de evacuacipn, mm Hg absoluta.

Pw= presion de vapor del H2O (de Tabla 25C-1), mm Hg.

r = numero total de inyecciones al analizador (tanque de muestra) durante el analisis (donde J = numero de inyecciones, 1, ...r)

R = factor de respuesta de calibracion media para un componente de muestra especifica, area/ppm.

Tt= temperatura en el tanque al completar el muestreo, °K.

Tti= temperatura en el tanque antes del muestreo, °K.

Ttf= temperatura en el tanque despues de presurizar, °K.

### Nomenclature EPA Method 4

Bws=vapor de agua en la corriente gaseosa (metodo 4 o alternativo), fracción de volumen. 

Mw= peso molecular del agua, 18.0 g/g-mol (18.0 lb/lb-mol). 

Pm= presion absoluta en medidor de gas seco ( para este metodo, igual a la presion barometrica), mm Hg (in. Hg). 

Pstd=presion absoluta estandar, 760 mm Hg (29.92 in. Hg).

R= constante del gas ideal, 0.06236 ((mm Hg)(m3))/((K)(g-mole)) {21.85 ((in. Hg) (ft3))/((°R) (lb-mole))}.

Tm= temperatura absoluta en medidor, °K (°R). 

Tstd= temperatura estandar absoluta, 293 °K (528 °R). 

Vf= volumen final de agua condensada, ml. 

Vi= volumen inicial, si existe, de agua condensada, ml. 

Vm= volumen de gas seco registrado por el medidor de gas seco, dcm (dcf). 

Vm(std)= volumen de gas seco medido en medidor de gas seco, corregido a condiciones estandar, dscm (dscf). 

Vwc(std)= volumen de vapor de agua condensado, corregido a condiciones estandar, scm (scf). 

Vwsg(std)= volumen de vapor de agua recogido en silica gel, corregido a condiciones estandar, scm (scf). 

Wf= peso final de la silica gel o silica gel mas burbujeador, g. 

Wi= peso inicial de la silica gel o silica gel mas burbujeador, g. 

Y= factor de calibración del medidor de gas seco. 

ΔVm= incremento de volumen de gas seco medido por el medidor de gas seco en cada punto transversal, dcm (dcf).

ρw= densidad del agua, 0.9982 g/ml (0.002201 lb/ml). 

### Nomenclature EPA Method 5

An = area transversal de la boquilla, m2(ft2).

Bws=vapor de agua en la corriente gaseosa (metodo 4 o alternativo), fracción de volumen.

Ca= concentracion residuo de la acetona blanco, mg/mg.

cs= concentracion de material particulado en chimenea, base seca, corregida a condiciones estandar, g/dscm (gr/dscf).

I= Porcentaje de isocinetismo de muestreo.

L1= tasa de fuga individual observada durante prueba de fugas realizada antes del cambio del primer componente, m3/min (ft3/min).

La= tasa de fuga maxima aceptable para una prueba de fugas antes de un estudio y despues del cambio de un componente; igual a 0.00057 m3/min (0.020 cfm) o 4 porciento de la tasa de muestre promedio, o el que sea menor.

Li= tasa de fuga individual observada durante prueba de fugas realizada antes de iesimo cambio de componente del tren de muestreo (i=1, 2, 3 . . . n), m3/min (cfm).

Lp= tasa de fuga observada durante prueba de fugas realizada posterior al muestreo, m3/min (cfm).

ma= masa de residuo en acetona despues de evaporacion, mg.

mn= cantidad total de material particulado recogido, mg.

Mw= peso molecular del agua, 18.0 g/g-mol (18.0 lb/lb-mol).

Pbar= presion barometrica en el sitio de medicion, mm Hg (in. Hg).

Ps= presion absoluta en chimenea(Pbar + Pg), mm Hg (in. Hg), 

Pstd= presion absoluta estandar, 760 mm Hg (29.92 in. Hg).

R= constante del gas ideal, 0.06236 ((mm Hg)(m3))/((K)(g-mole)) {21.85 ((in. Hg) (ft3))/((°R) (lb-mole))}.

Tm= temperatura absoluta promedio en el DGM (ver Figura 5-3), K (°R).

Ts= Ts(avg)= temperatura absoluta promedio en chimenea o ducto (ver Figura 5-3), K (°R).

Tstd= temperatura estandar absoluta, 293 °K (528 °R).

Va= volumen de acetona blanco, ml.

Vaw= volumen de acetona utilizado en lavado, ml.

V1c= volumen total de liquido recogido en burbujeadores y silica gel (ver Figura 5-6), ml.

Vm= volume  de gas registrado por el medidor de gas seco, dcm (dcf).

Vm(std)= volumen de gas registrado por el medidor de gas seco, corregido a condiciones estandar, dscm (dscf).

Vw(std)= volumen de vapor de agua en el agua, corregido a condiciones estandar, scm (scf).

Vs= velocidad promedio en chimenea, determinada por el Metodo 2, ecuacion 2-7, con datos obtenidos por el Metodo 5, m/s (ft/s).

Wa= peso del residuo en la acetona de lavado, mg.

Y= factor de calibracion del medidor de gas seco.

ΔH= presion diferencial promedio en el orificio, (ver  Figura 5-4), mm H2O (in. H2O).

ρa= densidad de la acetona, mg/ml (ver nivel de la botella).

ρw= densidad del agua, 0.9982 g/ml. (0.002201 lb/ml).

θ= tiempo e muestreo total, min.

θ1= intervalo de tiempo de muestreo, desde el principio hasta el primer cambio, min.

θi= intervalo de tiempo de muestreo, entre cambios sucesivos, comenzando con el intervalo entre el primero y segundo cambio, min. 

θp= intervalo de tiempo de muestreo, desde el último cambio hasta el final del tiempo de muestreo, min.

13.6= gravedad especifica del mercurio. factor de conversion de mm H2O (in. H2O) a mm Hg (in. Hg).

60= s/min.

100= conversion a percentaje.

It is possible to have math written with the LaTeX syntax rendered using [KaTeX](https://github.com/Khan/KaTeX). See Github [site](https://docs.gitlab.com/ee/user/markdown.html).

This math is inline `a^2+b^2=c^2`.


```math
a^2+b^2=c^2
```

# TODO

- [ ] Determine the tasks or functions name used in all methods. Cross references

- [ ] Build use cases for methods

- [ ] Build image for interrelation of methods

- [ ] Define the packages contents

- [ ] Start coding class, methods and files

- [ ] More ...
