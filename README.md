# Source code repository for stack test emission

This repository serve for several purpose, preliminary, intermediate and final calculation for evaluation of stack test emissions. This can be acomplish for technical who know EPA or ISO methods for evaluation of stack tests, and also fluid mechanics, and thermodinamics, is an ideal condition.

************************************************************************
In this site are the EPA methods with several functions arranged in packages for use in personal projects, but can be extended with time.

## Functions or methods

**Velocity**
**
**Absolute temperature**

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




Vej=the replacement stack gas velocity for the Method 1 equal-area sector closest to the wall, i.e., the stack gas point velocity value, adjusted for wall effects, for the jth Method 1 equal-area sector closest to the wall, actual ft/sec (m/sec);
VAVG=the average stack gas velocity that accounts for velocity decay near the wall, actual ft/sec (m/sec);

WAF=the wall effects adjustment factor derived from vavg and VAVG for a single traverse, dimensionless;

vfinal=the final wall effects-adjusted average stack gas velocity that replaces the unadjusted average stack gas velocity obtained using Method 2, 2F, or 2G for a field test consisting of a single traverse, actual ft/sec (m/sec);

WAF'=the wall effects adjustment factor that is applied to the average velocity, unadjusted for wall effects, in order to obtain the final wall effects-adjusted stack gas velocity vfinal or vfinal(k), dimensionless;

vfinal(k)=the final wall effects-adjusted average stack gas velocity that replaces the unadjusted average stack gas velocity obtained using Method 2, 2F, or 2G on run k of a RATA or other multiple-run field test procedure, actual ft/sec (m/sec);

vavg(k)=the average stack gas velocity, obtained on run k of a RATA or other multiple-run procedure, unadjusted for velocity decay near the wall, actual ft/sec (m/sec);

k= index of runs in a RATA or other multiple-run procedure.


### Nomenclature EPA Method 3

Md=peso molecular del gas en chimenea, base seca(ver seccion 8.6), g/g-mol (lb/lb-mol). 

%CO2=Percent CO2 by volume, dry basis.

%O2=Percent O2 by volume, dry basis.

%CO=Percent CO by volume, dry basis.

%N2=Percent N2 by volume, dry basis.

0.280=Molecular weight of N2 or CO, divided by 100.

0.320=Molecular weight of O2 divided by 100.

0.440=Molecular weight of CO2 divided by 100.

### Nomenclature EPA Method 3A - no tiene

### Nomenclature EPA Method 3B


%EA=Percent excess air.

0.264=Ratio of O2 to N2 in air, v/v.

### Nomenclature EPA Method 3C

Bw= contenido de humedad en la muestra, fraccion.

CN2= Measured N2 concentration (by Method 3C), fraction.

CN2Corr= Measured N2 concentration corrected only for dilution, fraction.

Ct= Calculated NMOC concentration, ppmv C equivalent.

Ctm= Measured NMOC concentration, ppmv C equivalent.

Pb= presion barometrica, mm Hg.

Pt= Gas sample tank pressure after sampling, but before pressurizing, mm Hg absolute.

Ptf= Final gas sample tank pressure after pressurizing, mm Hg absolute.

Pti= Gas sample tank pressure after evacuation, mm Hg absolute.

Pw= Vapor pressure of H2O (from Table 25C-1), mm Hg.

r = Total number of analyzer injections of sample tank during analysis (where j = injection number, 1 . . . r).

R = Mean calibration response factor for specific sample component, area/ppm.

Tt= Sample tank temperature at completion of sampling, °K.

Tti= Sample tank temperature before sampling, °K.

Ttf= Sample tank temperature after pressurizing, °K.

### Nomenclature EPA Method 4

Bws=vapor de agua en la corriente gaseosa (metodo 4 o alternativo), fracción de volumen. 

Mw= peso molecular del agua, 18.0 g/g-mol (18.0 lb/lb-mol). 

Pm=Absolute pressure (for this method, same as barometric pressure) at the dry gas meter, mm Hg (in. Hg). 

Pstd=presion absoluta estandar, 760 mm Hg (29.92 in. Hg).

R=Ideal gas constant, 0.06236 (mm Hg)(m3)/(g-mole)(°K) for metric units and 21.85 (in. Hg)(ft3)/(lb-mole)(°R) for English units. 

Tm=Absolute temperature at meter, °K (°R). 

Tstd= temperatura estandar absoluta, 293 °K (528 °R). 

Vf=Final volume of condenser water, ml. 

Vi=Initial volume, if any, of condenser water, ml. 

Vm=Dry gas volume measured by dry gas meter, dcm (dcf). 

Vm(std)=Dry gas volume measured by the dry gas meter, corrected to standard conditions, dscm (dscf). 

Vwc(std)=Volume of water vapor condensed, corrected to standard conditions, scm (scf). 

Vwsg(std)=Volume of water vapor collected in silica gel, corrected to standard conditions, scm (scf). 

Wf=Final weight of silica gel or silica gel plus impinger, g. 

Wi=Initial weight of silica gel or silica gel plus impinger, g. 

Y=Dry gas meter calibration factor. 

ΔVm=Incremental dry gas volume measured by dry gas meter at each traverse point, dcm (dcf).

ρw=Density of water, 0.9982 g/ml (0.002201 lb/ml). 

### Nomenclature EPA Method 5

An = Cross-sectional area of nozzle, m2(ft2).

Bws=vapor de agua en la corriente gaseosa (metodo 4 o alternativo), fracción de volumen.

Ca=Acetone blank residue concentration, mg/mg.

cs=Concentration of particulate matter in stack gas, dry basis, corrected to standard conditions, g/dscm (gr/dscf).

I=Percent of isokinetic sampling.

L1=Individual leakage rate observed during the leak-check conducted prior to the first component change, m3/min (ft3/min).

La=Maximum acceptable leakage rate for either a pretest leak-check or for a leak-check following a component change; equal to 0.00057 m3/min (0.020 cfm) or 4 percent of the average sampling rate, whichever is less.

Li=Individual leakage rate observed during the leak-check conducted prior to the “ith” component change (i=1, 2, 3 . . . n), m3/min (cfm).

Lp=Leakage rate observed during the post-test leak-check, m3/min (cfm).

ma=Mass of residue of acetone after evaporation, mg.

mn=Total amount of particulate matter collected, mg.

Mw= peso molecular del agua, 18.0 g/g-mol (18.0 lb/lb-mol).

Pbar= presion barometrica en el sitio de medicion, mm Hg (in. Hg).

Ps= presion absoluta en chimenea(Pbar + Pg), mm Hg (in. Hg), 

Pstd= presion absoluta estandar, 760 mm Hg (29.92 in. Hg).

R=Ideal gas constant, 0.06236 ((mm Hg)(m3))/((K)(g-mole)) {21.85 ((in. Hg) (ft3))/((°R) (lb-mole))}.

Tm=Absolute average DGM temperature (see Figure 5-3), K (°R).

Ts=Absolute average stack gas temperature (see Figure 5-3), K (°R).

Tstd= temperatura estandar absoluta, 293 °K (528 °R).

Va=Volume of acetone blank, ml.

Vaw=Volume of acetone used in wash, ml.

V1c=Total volume of liquid collected in impingers and silica gel (see Figure 5-6), ml.

Vm=Volume of gas sample as measured by dry gas meter, dcm (dcf).

Vm(std)=Volume of gas sample measured by the dry gas meter, corrected to standard conditions, dscm (dscf).

Vw(std)=Volume of water vapor in the gas sample, corrected to standard conditions, scm (scf).

Vs= velocidad promedio en chimenea, determinada por el Metodo 2, ecuacion 2-7, con datos obtenidos por el Metodo 5, m/s (ft/s).

Wa=Weight of residue in acetone wash, mg.

Y=Dry gas meter calibration factor.

ΔH=Average pressure differential across the orifice meter (see Figure 5-4), mm H2O (in. H2O).

ρa=Density of acetone, mg/ml (see label on bottle).

ρw=Density of water, 0.9982 g/ml. (0.002201 lb/ml).

θ=Total sampling time, min.

θ1=Sampling time interval, from the beginning of a run until the first component change, min.

θi=Sampling time interval, between two successive component changes, beginning with the interval between the first and second changes, min.

θp=Sampling time interval, from the final (nth) component change until the end of the sampling run, min.

13.6= gravedad especifica del mercurio. factor de conversion de mm H2O (in. H2O) a mm Hg (in. Hg).

60= s/min.

100= conversion a percentaje.

It is possible to have math written with the LaTeX syntax rendered using [KaTeX](https://github.com/Khan/KaTeX). See Github [site](https://docs.gitlab.com/ee/user/markdown.html).

This math is inline $`a^2+b^2=c^2`$.

This is on a separate line
```math
a^2+b^2=c^2
```

graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;

# TODO

- [ ] Determine the tasks or functions name used in all methods. Cross references

- [ ] Build use cases for methods

- [ ] Build image for interrelation of methods

- [ ] Define the packages contents

- [ ] Start coding class, methods and files

- [ ] More ...
