# Source code repository for stack test emission

This repository serve for several purpose, preliminary, intermediate and final calculation for evaluation of stack test emissions. This can be acomplish for technical who know EPA or ISO methods for evaluation of stack tests, and also fluid mechanics, and thermodinamics, is an ideal condition.

In this site are the EPA methods with several functions arranged in packages for use in personal projects, but can be extended with time.

## Functions or methods

**Velocity**
**
**Absolute temperature**

### Nomenclature EPA Method 1

L=length. 

n =total number of traverse points. 

Pi=pitch angle at traverse point i, degree. 

Ravg=average resultant angle, degree. 

Ri=resultant angle at traverse point i, degree. 

Sd=standard deviation, degree. 

W=width. 

Yi=yaw angle at traverse point i, degree. 

### Nomenclature EPA Method 1A - No tiene

### Nomenclature EPA Method 2

A=Cross-sectional area of stack, m2(ft2). 

Bws=Water vapor in the gas stream (from Method 4 (reference method) or Method 5), proportion by volume. 
Cp=Pitot tube coefficient, dimensionless.

Cp(s)=Type S pitot tube coefficient, dimensionless. 

Cp(std)=Standard pitot tube coefficient; use 0.99 if the coefficient is unknown and the tube is designed according to the criteria of sections 6.7.1 to 6.7.5 of this method. 

De=Equivalent diameter. 

K=0.127 mm H2O (metric units). 0.005 in. H2O (English units). 

Kp=Velocity equation constant. 

L=Length. 

Md=Molecular weight of stack gas, dry basis (see section 8.6), g/g-mole (lb/lb-mole). 

Ms=Molecular weight of stack gas, wet basis, g/g-mole (lb/lb-mole). 

n =Total number of traverse points. 

Pbar=Barometric pressure at measurement site, mm Hg (in. Hg). 

Pg=Stack static pressure, mm Hg (in. Hg). 

Ps=Absolute stack pressure (Pbar+ Pg), mm Hg (in. Hg), 

Pstd=Standard absolute pressure, 760 mm Hg (29.92 in. Hg). 

Qsd=Dry volumetric stack gas flow rate corrected to standard conditions, dscm/hr (dscf/hr). 

T=Sensitivity factor for differential pressure gauges. 

Ts(abavg)= Average absolute stack temperature, °K (°R).
= 273 + Ts for metric units,
= 460 + Ts for English units.

Ts=Stack temperature, °C (( °deg;F). 
=273 + Ts for metric units, 
=460 + Ts for English units. 

Tstd=Standard absolute temperature, 293 °K (528 °R). 

Vs=Average stack gas velocity, m/sec (ft/sec). 

W=Width.

Δp=Velocity head of stack gas, mm H2O (in. H20).

Δpi=Individual velocity head reading at traverse point “i”, mm (in.) H2O. 

Δpstd=Velocity head measured by the standard pitot tube, cm (in.) H2O.

Δps=Velocity head measured by the Type S pitot tube, cm (in.) H2O. 

3600=Conversion Factor, sec/hr. 

18.0=Molecular weight of water, g/g-mole (lb/lb-mole). 

### Nomenclature EPA Method 2A

f=Final reading.

i=Initial reading. 

Pbar=Barometric pressure, mm Hg. 

Pg=Average static pressure in volume meter, mm Hg. 

Qs=Gas flow rate, m3/min, standard conditions.

s =Standard conditions, 20 °C and 760 mm Hg

Tr=Reference meter average temperature, °K (°R). 

Tm=Test meter average temperature, °K (°R).

Vr=Reference meter volume reading, m3. 

Vm=Test meter volume reading, m3. 

Ym=Test meter calibration coefficient, dimensionless. 

θ=Elapsed test period time, min.

### Nomenclature EPA Method 2B

COe= Mean carbon monoxide concentration in system exhaust, ppm.

(CO2)a= Ambient carbon dioxide concentration, ppm (if not measured during the test period, may be assumed to equal 380 ppm).

(CO2)e= Mean carbon dioxide concentration in system exhaust, ppm.

HCe= Mean organic concentration in system exhaust as defined by the calibration gas, ppm.

Hci= Mean organic concentration in system inlet as defined by the calibration gas, ppm.

Ke= Hydrocarbon calibration gas factor for the exhaust hydrocarbon analyzer, unitless (equal to the number of carbon atoms per molecule of the gas used to calibrate the analyzer (2 for ethane, 3 for propane, etc.)).

Ki= Hydrocarbon calibration gas factor for the inlet hydrocarbon analyzer, unitless.

Ves= Exhaust gas volume, m3.

Vis= Inlet gas volume, m3.

Qes= Exhaust gas volume flow rate, m3/min.

Qis= Inlet gas volume flow rate, m3/min.

Ө= Sample run time, min.

S = Standard conditions: 20 °C, 760 mm Hg.

### Nomenclature EPA Method 2C - No tiene

### Nomenclature EPA Method 2D

Pbar=Barometric pressure, mm Hg (in. Hg). 

Pm=Test meter average static pressure, mm Hg (in. Hg). 

Qr=Reference meter volume flow rate reading, m3/min (ft3/min). 

Qm=Test meter volume flow rate reading, m3/min (ft3/min). 

Tr=Absolute reference meter average temperature, °K (°R). 

Tm=Absolute test meter average temperature, °K (°R). 

Kl=0.3855 °K/mm Hg for metric units,=17.65 °R/in. Hg for English units

### Nomenclature EPA Method 2E

A=Age of landfill, yr.

Aavg=Average age of the refuse tested, yr.

Ai=Age of refuse in the ith fraction, yr.

Ar=Acceptance rate, Mg/yr.

CNMOC=NMOC concentration, ppmv as hexane (CNMOC=Ct/6).

Co=Concentration of N2at the outlet, ppmv.

Ct=NMOC concentration, ppmv (carbon equivalent) from Method 25C.

Cw=Concentration of N2at the wellhead, ppmv.

D=Depth affected by the test wells, m.

Dst=Depth affected by the test wells in the short-term test, m.

### Nomenclature EPA Method 2F

A=Cross-sectional area of stack or duct, m2(ft2).

Bws=Water vapor in the gas stream (from Method 4 or alternative), proportion by volume.

Kp_metric = 34.97 # m/s ({(g/g-mole)(mmHg)}/{(K)(mmH2O)})^1/2

Kp_english = 85.49 # ft/s ({(lb/bl-mole)(in.Hg)}/{(R)(in.H2O)})^1/2

Md=Molecular weight of stack or duct gas, dry basis (see section 8.13), g/g-mole (lb/lb-mole).

Ms=Molecular weight of stack or duct gas, wet basis, g/g-mole (lb/lb-mole).

Pbar=Barometric pressure at measurement site, mm Hg (in. Hg).

Pg=Stack or duct static pressure, mm H2O (in. H2O).

Ps=Absolute stack or duct pressure, mm Hg (in. Hg).

Pstd=Standard absolute pressure, 760 mm Hg (29.92 in. Hg).

13.6=Conversion from mm H2O (in. H2O) to mm Hg (in. Hg).

Qsd=Average dry-basis volumetric stack or duct gas flow rate corrected to standard conditions, dscm/hr (dscf/hr).

Qsw=Average wet-basis volumetric stack or duct gas flow rate corrected to standard conditions, wscm/hr (wscf/hr).

Ts(avg)=Average absolute stack or duct gas temperature across all traverse points.

ts(i)=Stack or duct gas temperature, C (F), at traverse point i.

Ts(i)=Absolute stack or duct gas temperature, K (R), at traverse point i.

Tstd=Standard absolute temperature, 293°K (528°R).

F1(i)=Pitch angle ratio, applicable at traverse point i, dimensionless.

F2(i)=3-D probe velocity calibration coefficient, applicable at traverse point i, dimensionless.

(P4-P5)I=Pitch differential pressure of stack or duct gas flow, mm H2O (in. H2O), at traverse point i.

(P1-P2)I =Velocity head (differential pressure) of stack or duct gas flow, mm H2O (in. H2O), at traverse point i.

va(i)=Reported stack or duct gas axial velocity, m/sec (ft/sec), at traverse point i.

va(avg)=Average stack or duct gas axial velocity, m/sec (ft/sec), across all traverse points.

3,600=Conversion factor, sec/hr.

18.0=Molecular weight of water, g/g-mole (lb/lb-mole).

θy(i)=Yaw angle, degrees, at traverse point i.

θp(i)=Pitch angle, degrees, at traverse point i.

n=Number of traverse points.

### Nomenclature EPA Method 2G

A=Cross-sectional area of stack or duct at the test port location, m2(ft2).

Bws=Water vapor in the gas stream (from Method 4 or alternative), proportion by volume.

Cp=Pitot tube calibration coefficient, dimensionless.

F2(i)=3-D probe velocity coefficient at 0 pitch, applicable at traverse point i.

Kp_metric = 34.97 # m/s ({(g/g-mole)(mmHg)}/{(K)(mmH2O)})^1/2

Kp_english = 85.49 # ft/s ({(lb/bl-mole)(in.Hg)}/{(R)(in.H2O)})^1/2

Md=Molecular weight of stack or duct gas, dry basis (see section 8.13), g/g-mole (lb/lb-mole).

Ms=Molecular weight of stack or duct gas, wet basis, g/g-mole (lb/lb-mole).

Pbar=Barometric pressure at velocity measurement site, mm Hg (in. Hg).

Pg=Stack or duct static pressure, mm H2O (in. H2O).

Ps=Absolute stack or duct pressure, mm Hg (in. Hg),

Pstd=Standard absolute pressure, 760 mm Hg (29.92 in. Hg)

13.6=Conversion from mm H2O (in. H2O) to mm Hg (in. Hg).

Qsd=Average dry-basis volumetric stack or duct gas flow rate corrected to standard conditions, dscm/hr (dscf/hr).

Qsw=Average wet-basis volumetric stack or duct gas flow rate corrected to standard conditions, wscm/hr (wscf/hr).

ts(i)=Stack or duct temperature, °C (°F), at traverse point i.

Ts(i)=Absolute stack or duct temperature, °K (°R), at traverse point i.

Ts(avg)=Average absolute stack or duct gas temperature across all traverse points.

Tstd=Standard absolute temperature, 293°K (528°R).

va(i)=Measured stack or duct gas impact velocity, m/sec (ft/sec), at traverse point i.

va(avg)=Average near-axial stack or duct gas velocity, m/sec (ft/sec) across all traverse points.

ΔPi=Velocity head (differential pressure) of stack or duct gas, mm H2O (in. H2O), applicable at traverse point i.

(P1-P2)=Velocity head (differential pressure) of stack or duct gas measured by a 3-D probe, mm H2O (in. H2O), applicable at traverse point i.

3,600=Conversion factor, sec/hr.

18.0=Molecular weight of water, g/g-mole (lb/lb-mole).

θy(i)=Yaw angle of the flow velocity vector, at traverse point i.

n=Number of traverse points.

### Nomenclature EPA Method 2H

vavg=the average stack gas velocity, unadjusted for wall effects, actual ft/sec (m/sec);

viI=stack gas point velocity value at Method 1 interior equal-area sectors, actual ft/sec (m/sec);

vej=stack gas point velocity value, unadjusted for wall effects, at Method 1 exterior equal-area sectors, actual ft/sec (m/sec);

i =index of Method 1 interior equal-area traverse points;

j =index of Method 1 exterior equal-area traverse points;

n =total number of traverse points in the Method 1 traverse;

vdecd=the wall effects decay velocity for a sub-sector located between the traverse points at distances d−1 (in metric units, d−2.5 ) and d from the wall, actual ft/sec (m/sec);

vd=the measured stack gas velocity at distance d from the wall, actual ft/sec(m/sec); Note: v 0=0;

d =the distance of a 1-in. incremented wall effects traverse point from the wall, for traverse points d 1through dlast, in. (cm);

Ad=the cross-sectional area of a sub-sector located between the traverse points at distances d−1 (in metric units, d−2.5 ) and d from the wall, in.2(cm2) (e.g., sub-sector A2 shown in Figures 2H–3 and 2H–4);

r =the stack or duct radius, in. (cm);

Qd=the stack gas volumetric flow rate for a sub-sector located between the traverse points at distances d−1 (in metric units, d−2.5 ) and d from the wall, actual ft-in.2/sec (m-cm2/sec);

Qd1->dlast=the total stack gas volumetric flow rate for all sub-sectors located between the wall and dlast, actual ft-in.2/sec (m-cm2sec);

dlast=the distance from the wall of the last 1-in. incremented wall effects traverse point, in. (cm);

Adrem=the cross-sectional area of the sub-sector located between dlast and the interior edge of the Method 1 equal-area sector closest to the wall, in.2(cm2)(see Figure 2H–4);

p =the number of Method 1 traverse points per diameter, p ≥8 (e.g., for a 16-point traverse, p =8);

drem=the distance from the wall of the centroid of the area between dlast and the interior edge of the Method 1 equal-area sector closest to the wall, in. (cm);

Qdrem=the total stack gas volumetric flow rate for the sub-sector located between dlast and the interior edge of the Method 1 equal-area sector closest to the wall, actual ft-in.2/sec (m-cm2/sec);

vdrem=the measured stack gas velocity at distance drem from the wall, actual ft/sec (m/sec);

QT=the total stack gas volumetric flow rate for the Method 1 equal-area sector closest to the wall, actual ft-in.2/sec (m-cm2/sec);

Vej=the replacement stack gas velocity for the Method 1 equal-area sector closest to the wall, i.e., the stack gas point velocity value, adjusted for wall effects, for the jth Method 1 equal-area sector closest to the wall, actual ft/sec (m/sec);
VAVG=the average stack gas velocity that accounts for velocity decay near the wall, actual ft/sec (m/sec);

WAF=the wall effects adjustment factor derived from vavg and VAVG for a single traverse, dimensionless;

vfinal=the final wall effects-adjusted average stack gas velocity that replaces the unadjusted average stack gas velocity obtained using Method 2, 2F, or 2G for a field test consisting of a single traverse, actual ft/sec (m/sec);

WAF'=the wall effects adjustment factor that is applied to the average velocity, unadjusted for wall effects, in order to obtain the final wall effects-adjusted stack gas velocity vfinal or vfinal(k), dimensionless;

vfinal(k)=the final wall effects-adjusted average stack gas velocity that replaces the unadjusted average stack gas velocity obtained using Method 2, 2F, or 2G on run k of a RATA or other multiple-run field test procedure, actual ft/sec (m/sec);

vavg(k)=the average stack gas velocity, obtained on run k of a RATA or other multiple-run procedure, unadjusted for velocity decay near the wall, actual ft/sec (m/sec);

k= index of runs in a RATA or other multiple-run procedure.


### Nomenclature EPA Method 3

Md=Dry molecular weight, g/g-mole (lb/lb-mole).

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

Bw= Moisture content in the sample, fraction.

CN2= Measured N2 concentration (by Method 3C), fraction.

CN2Corr= Measured N2 concentration corrected only for dilution, fraction.

Ct= Calculated NMOC concentration, ppmv C equivalent.

Ctm= Measured NMOC concentration, ppmv C equivalent.

Pb= Barometric pressure, mm Hg.

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

Bws=Proportion of water vapor, by volume, in the gas stream. 

Mw=Molecular weight of water, 18.0 g/g-mole (18.0 lb/lb-mole). 

Pm=Absolute pressure (for this method, same as barometric pressure) at the dry gas meter, mm Hg (in. Hg). 

Pstd=Standard absolute pressure, 760 mm Hg (29.92 in. Hg). 

R=Ideal gas constant, 0.06236 (mm Hg)(m3)/(g-mole)(°K) for metric units and 21.85 (in. Hg)(ft3)/(lb-mole)(°R) for English units. 

Tm=Absolute temperature at meter, °K (°R). 

Tstd=Standard absolute temperature, 293°K (528°R). 

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

Bws=Water vapor in the gas stream, proportion by volume.

Ca=Acetone blank residue concentration, mg/mg.

cs=Concentration of particulate matter in stack gas, dry basis, corrected to standard conditions, g/dscm (gr/dscf).

I=Percent of isokinetic sampling.

L1=Individual leakage rate observed during the leak-check conducted prior to the first component change, m3/min (ft3/min).

La=Maximum acceptable leakage rate for either a pretest leak-check or for a leak-check following a component change; equal to 0.00057 m3/min (0.020 cfm) or 4 percent of the average sampling rate, whichever is less.

Li=Individual leakage rate observed during the leak-check conducted prior to the “ith” component change (i=1, 2, 3 . . . n), m3/min (cfm).

Lp=Leakage rate observed during the post-test leak-check, m3/min (cfm).

ma=Mass of residue of acetone after evaporation, mg.

mn=Total amount of particulate matter collected, mg.

Mw=Molecular weight of water, 18.0 g/g-mole (18.0 lb/lb-mole).

Pbar=Barometric pressure at the sampling site, mm Hg (in. Hg).

Ps=Absolute stack gas pressure, mm Hg (in. Hg).

Pstd=Standard absolute pressure, 760 mm Hg (29.92 in. Hg).

R=Ideal gas constant, 0.06236 ((mm Hg)(m3))/((K)(g-mole)) {21.85 ((in. Hg) (ft3))/((°R) (lb-mole))}.

Tm=Absolute average DGM temperature (see Figure 5-3), K (°R).

Ts=Absolute average stack gas temperature (see Figure 5-3), K (°R).

Tstd=Standard absolute temperature, 293 K (528 °R).

Va=Volume of acetone blank, ml.

Vaw=Volume of acetone used in wash, ml.

V1c=Total volume of liquid collected in impingers and silica gel (see Figure 5-6), ml.

Vm=Volume of gas sample as measured by dry gas meter, dcm (dcf).

Vm(std)=Volume of gas sample measured by the dry gas meter, corrected to standard conditions, dscm (dscf).

Vw(std)=Volume of water vapor in the gas sample, corrected to standard conditions, scm (scf).

Vs=Stack gas velocity, calculated by Method 2, Equation 2-7, using data obtained from Method 5, m/sec (ft/sec).

Wa=Weight of residue in acetone wash, mg.

Y=Dry gas meter calibration factor.

ΔH=Average pressure differential across the orifice meter (see Figure 5-4), mm H2O (in. H2O).

ρa=Density of acetone, mg/ml (see label on bottle).

ρw=Density of water, 0.9982 g/ml. (0.002201 lb/ml).

θ=Total sampling time, min.

θ1=Sampling time interval, from the beginning of a run until the first component change, min.

θi=Sampling time interval, between two successive component changes, beginning with the interval between the first and second changes, min.

θp=Sampling time interval, from the final (nth) component change until the end of the sampling run, min.

13.6=Specific gravity of mercury.

60=Sec/min.

100=Conversion to percent.

It is possible to have math written with the LaTeX syntax rendered using [KaTeX](https://github.com/Khan/KaTeX). See Github [site](https://docs.gitlab.com/ee/user/markdown.html).

This math is inline $`a^2+b^2=c^2`$.

This is on a separate line
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
