#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import math as mp


# In[ ]:


#Información de la abolladura al vehículo o barrera
def testData():
    l = input("-Longitud de la abolladura(metros) = ")
    l = validar(l,6)
    v0 = input("-Velocidad de Impacto(Km/h) = ")
    v0 = validar(v0,6)
    m = input("-Masa del Cuerpo(Kg) = ")
    m = validar(m,6)
    n = input("-Número de Medidas de Abolladura (N) = ")
    n = validar(n,5)
    v0 = v0*10/36
    coef = []
    delx = l/(n-1)
    
    print("-Valores de Abolladura:")
    for i in range(0, n):
        ci = input("--C" + str(i+1) + " = ")
        ci = validar(ci,6)
        coef.append(ci)
    
    return l, coef, v0, m, delx


# In[ ]:


def McHenry(l,coef,v0,masa): #Obtiene los coeficientes A y B
    ci = 0
    b0 = 55/18 #Speed of zero permanent damage Vzd
    vel0 = v0 #velocidad de impacto en m/s
    
    for i in range(1,len(coef)-1):
        ci = ci + coef[i]
    
    Csr = ((coef[0]/2)+(coef[-1]/2) + ci)/(len(coef)-1) #coeficiente de abolladura efectivo
    b1 = (vel0-b0)/Csr
    
    a = (masa*b1*b0)/l
    b = (masa*b1*b1)/l
    
    return a,b


# In[ ]:


def ECFs(bet,ce,lv,lb,mef):
    ECF = mp.sqrt((2*bet*ce)/lv)
    ECF0 = 10.75670326*mp.sqrt(mef*(1-np.power(0.25,2))/lb)*0.156464
    return ECF, ECF0


# In[ ]:


def crush(L,c,delx,A,B):
    coefi = []
    area = 0
    CEi = 0
    coeffi = 0
    for i in range(0,len(c)-1): 
        ci = (c[i]+c[i+1])/2
        area = area + (ci*delx)
        coef = (mp.pow(c[i],2)+(c[i]*c[i+1])+mp.pow(c[i+1],2))*delx
        coefi.append(coef)
        coeffi = coeffi + coef
    
    Cavg = area/L
    beta = (coeffi)/(3*L*mp.pow(Cavg,2))
    G = (mp.pow(A,2))/(2*B*beta)
    for i in range(0,len(c)-1):
        ci = (c[i]+c[i+1])/2
        CE = (((A*ci)+G)*delx)+(B*coefi[i]/6)
        CEi = CEi + CE
        print(CE)
        
    return CEi


# In[ ]:


def frontRearStiffnes():
    marca, modelo, año = car_info()
    print("El daño se presenta en la zona \n"
          "1. Frontal. \n"
          "2. Trasera. \n")
    tipo = input("Selección: ")
    tipo = validar(tipo,3)
    data = readFile(tipo)
    A,B,M,encontrado = find_coeff(marca,modelo,año,data)
    
    if(encontrado == False):
        L,c,V,M,delx = testData()
        A,B = McHenry(L,c,V,M)
        CE = cBeta(len(c),L,c, delx,A,B)
        CEs, Ftot = SegbySeg(len(c),c,delx,L,A,B)
        v = CESpeed(CE,M)
        vs = CESpeed(CEs,M)
        errorv = (abs(V-v)/V)*100
        errorvs = (abs(V-vs)/V)*100
    
        print("----------------Resultados---------------")
        print("-Coeficiente A = ", A, "N/m \n"
              "-Coeficiente B = ", B, "N/m^2 \n")
        plotAB(A,B,marca,modelo,año,L,c,CEs)
        
        print("-----Prueba con los Coeficientes Obtenidos-----")
        print("-Velocida de Prueba = ", V*3.6, "Km/h")
        print("-Velocidad por Modelo Promedio C = ", v*3.6, "Km/h")
        print("-Error = ", errorv, "%")
        print("-Velocidad por Modelo C Segmentado = ", vs*3.6, "Km/h")
        print("-Error = ", errorvs, "%")
        
    return A,B,marca,modelo,año,M,data,encontrado,tipo


# In[ ]:


def sideStiffnes():
    print("Para el Vehículo ingrese: ")
    marca, modelo, año = car_info()
    data = readFile(3)
    A,B,masa,encontrado,cs = find_coeff(marca,modelo,año,data)
    tipo = 3
    
    if(encontrado == False):
        LV,cV,V0V,MV,delxV = testData()
        VfV = input("-Velocidad después del Impacto (Km/h) = ")
        V = validar(VfV,6)
        V = V/3.6
        print("Para la Barrera ingrese: ")
        LB,cB,V0B,MB,delxB = testData()
        VfB = input("-Velocidad después del Impacto (Km/h) = ")
        VB = validar(VfB,6)
        VB = VB/3.6
        print("-Coeficientes de Stiffness de la Barrera:")
        A = input("--A = ")
        A = validar(A,6)
        B = input("--B = ")
        B = validar(B,6)
        KiV = kineticE(V0V,MV) #Cinetica inicial vehículo
        KiB = kineticE(V0B,MB) #Cinética inicial barrera
        KfB = kineticE(VB,MB)  #Cinética final barrera
        KfV = kineticE(V,MV)   #cinética final vehículo
        Ei = KiV + KiB         #Energía inicial
        Ef = KfB + KfV         #Energía Final
        CE = Ei-Ef             #Crush energy total
        CEB = crush(LB,cB,delxB,A,B) #nueva función para laterales
        CEV = CE-CEB           #Crush energy vehículo
        Mef = efectiveMass(MV,MB)
        
        area = 0
        coeffi = 0
        for i in range(0,len(cV)-1): 
            ci = (cV[i]+cV[i+1])/2
            area = area + (ci*delxV)
            coeffi = coeffi + (mp.pow(cV[i],2)+(cV[i]*cV[i+1])+mp.pow(cV[i+1],2))*delxV
        
        prom_c = area/LV
        bet = (coeffi)/(3*LV*mp.pow(prom_c,2))
        
        ECF, ECF0 = ECFs(bet,CEV,LV,LB,Mef)
        m = (ECF-ECF0)/(bet*prom_c)
        b = ECF0
        A = m*b
        B = m*m
        print("m = ",m)
        print("b = ",b)
        print("beta = ",bet)
        print("C = ",prom_c)
        print(marca," ", modelo, " '", año,":")
        print("A = ", A)
        print("B = ", B)
    
    return A,B,marca,modelo,año,MV,data,encontrado,tipo


# In[ ]:


def stiffPrassad():
    marca, modelo, año = car_info()
    print("Coeficientes para la zona: \n"
          "1. Frontal. \n"
          "2. Trasera. \n")
    tipo = input("Selección: ")
    tipo = validar(tipo,3)
    data = readFile(tipo)
    a,b,masa, encontrado, cs = find_coeff(marca,modelo,año,data)
    
    if(encontrado == False):
        masa = input("Masa del Vehículo (Kg): ")
        masa = validar(masa,6)
        d0 = input("d0 = ")
        d0 = validar(d0,6)
        d1 = input("d1 = ")
        d1 = validar(d1,6)
        a = d0*d1*175.126835758
        b = d1*d1*6894.7573133
        print("Coeficiente A = ", a, "N/m \n"
              "Coeficiente B = ", b, "N/m^2 \n")
    
    return a,b,marca,modelo,año,masa,data,encontrado,tipo

