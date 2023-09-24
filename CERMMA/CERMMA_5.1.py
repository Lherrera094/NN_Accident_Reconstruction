# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # CERMMA

import sys
sys.path.append("CERMMA_TK/")
from Physic_calculations_TK import *
from ReportLab_TK import *
from validation_function_TK import *
from input_values_TK import *
from excel_files_TK import *
from Stiffnes_calculo_TK import *
from funciones_motos_TK import *
from Initial_velocities_TK import *
#Importacion de Paquetes
import pandas as pd
import matplotlib.pyplot as pl
import matplotlib.image as plim
from PIL import Image
import numpy as np
import math as mp
import json
import os
from datetime import datetime
import locale

# * Funciones de salidan que guían al usuario

# +


# ## Motorcycle Colissions
def controlMotos():

    print("Ha seleccionado Colisión de motocicleta con vehículo.\n")
    car_data = full_data["Carro 1"]
    moto_data = full_data["Moto"]
    marca, modelo, año, sel = car_data["Marca"], car_data["Modelo"], car_data["Año"], car_data["Zona de Impacto"]
    data = readFile(sel)
    A, B, mcarro, encontrado = find_coeff(marca,modelo,año,data)    
    L, cc, ces = car_data["Longitud de Abolladura(m)"], car_data["Numero de Coeficientes"], car_data["Coeficientes"]
    if (encontrado == True):
        CE,FT,c = calculoCE(A,B,mcarro,marca,modelo,año,2,L,cc,ces)
    else:
        mcarro = car_data["Masa Auto"]
        c = []
        CE = 0
        for i in range(car_data["Numero de Coeficientes"]):
            c.append(car_data["Coeficientes"]["C"+str(i+1)])
    oL, oW, d = car_data["Longitud del Auto(m)"], car_data["Ancho del Auto(m)"], car_data["Distance a Referencia (cm)"]
    p, pmass = car_data["Numero de Pasajeros"], car_data["Masa de Pasajeros(Kg)"]
    mt = 0
    for i in range(len(pmass)):
                    mt += pmass["Mass "+str(i+1)]
    marcamoto, modelomoto, añomoto = moto_data["Marca"], moto_data["Modelo"], moto_data["Año"]
    pmoto, mpassmoto = moto_data["Numero de Pasajeros en Moto"], moto_data["Masa de Pasajeros en Moto(Kg)"]
    mtmoto = 0
    for i in range(len(mpassmoto)):
                    mtmoto += mpassmoto["Mass "+str(i+1)]
    
    
    woodcarbool = True
    woodmotobool = True
    woodcrushbool = True
    empiricbool = True
    
    cscarro = car_data["Coeficientes"]
    dcarro = cscarro["C1"]
    for i in range(car_data["Numero de Coeficientes"]):
        if (dcarro < cscarro["C"+str(i+1)]):
            dcarro = cscarro["C"+str(i+1)]
    dcarro = validar(dcarro,7)
    if ((dcarro == 0) or (dcarro == 0.0)):
        woodcarbool = empiricbool = False    
    energymed = car_data["Energia disipada"]
    energymed = validar(energymed,7)
    if ((energymed == 0) or (energymed == 0.0)):
        woodcrushbool = False
    dwb = moto_data["Delta ejes"]
    dwb = validar(dwb,7)
    if ((dwb == 0) or (dwb == 0.0)):
        print("\n------------------------------------------------")
        print("No se pueden obtener resultados sin el cambio de distancia entre ejes de la motocicleta!!")
        print("------------------------------------------------\n")
        contador = 2
        return contador
    mmot = moto_data["Masa"]
    mmot = validar(mmot,7)
    if ((mmot == 0) or (mmot == 0.0)):
        if empiricbool == False:
            print("\n----------------------------------------------------")
            print("No se pueden obtener resultados sin tantos valores!!")
            print("----------------------------------------------------\n")
            contador = 2
            return contador
        woodcarbool = woodmotobool = woodcrushbool = False
    mcarro = validar(mcarro,7)
    if ((mcarro == 0) or (mcarro == 0.0)):
        if empiricbool == False:
            print("\n----------------------------------------------------")
            print("No se pueden obtener resultados sin tantos valores!!")
            print("----------------------------------------------------\n")
            contador = 2
            return contador
        woodcarbool = woodmotobool = woodcrushbool = False
    lcarro = car_data["Longitud del Auto(m)"]
    lcarro = validar(lcarro,7)
    if ((lcarro == 0) or (lcarro == 0.0)):
        if empiricbool == False:
            print("\n----------------------------------------------------")
            print("No se pueden obtener resultados sin tantos valores!!")
            print("----------------------------------------------------\n")
            contador = 2
            return contador
        woodcarbool = woodmotobool = woodcrushbool = False
    wcarro = car_data["Ancho del Auto(m)"]
    wcarro = validar(wcarro,7)
    if ((wcarro == 0) or (wcarro == 0.0)):
        if empiricbool == False:
            print("\n----------------------------------------------------")
            print("No se pueden obtener resultados sin tantos valores!!")
            print("----------------------------------------------------\n")
            contador = 2
            return contador
        woodcarbool = woodmotobool = woodcrushbool = False
    wbcarro = car_data["Wheelbase"]
    wbcarro = validar(wbcarro,7)
    if ((wbcarro == 0) or (wbcarro == 0.0)):
        if empiricbool == False:
            print("\n----------------------------------------------------")
            print("No se pueden obtener resultados sin tantos valores!!")
            print("----------------------------------------------------\n")
            contador = 2
            return contador
        woodcarbool = woodmotobool = woodcrushbool = False
    trcarro = car_data["Track"]
    trcarro = validar(trcarro,7)
    if ((trcarro == 0) or (trcarro == 0.0)):
        if empiricbool == False:
            print("\n----------------------------------------------------")
            print("No se pueden obtener resultados sin tantos valores!!")
            print("----------------------------------------------------\n")
            contador = 2
            return contador
        woodcarbool = woodmotobool = woodcrushbool = False
    hwood = car_data["Distancia h"]
    hwood = validar(hwood,7)
    if ((hwood == 0) or (hwood == 0.0)):
        if empiricbool == False:
            print("\n----------------------------------------------------")
            print("No se pueden obtener resultados sin tantos valores!!")
            print("----------------------------------------------------\n")
            contador = 2
            return contador
        woodcarbool = woodmotobool = woodcrushbool = False
    
    if (woodcarbool):
        kquad = (lcarro*lcarro+wcarro*wcarro)/12
        Iz = mcarro*kquad
        mcarroef = Iz / (kquad + hwood*hwood)
        moa = mmot*mcarroef / (mmot + mcarroef)
        energym = mmot * (641.7*(dwb + 0.1) ** 1.89)
        energywood = 65305*(dcarro - 0.0576)
        vwood = mp.sqrt(2*(energywood+energym)/moa)
        vcckhwood = vwood * 3.6
    elif ((not woodcarbool) and (woodcrushbool or woodmotobool)):
        energywood = "ND"
        vwood = "ND"
        vcckhwood = "ND"
    else:
        energym = "ND"
        energywood = "ND"
        vwood = "ND"
        vcckhwood = "ND"
    if (woodcrushbool and woodcarbool):
        vmed = mp.sqrt(2*(energymed+energym)/moa)
        vcckhmed = vmed * 3.6
    elif (woodcrushbool and (not woodcarbool)):
        kquad = (lcarro*lcarro+wcarro*wcarro)/12
        Iz = mcarro*kquad
        mcarroef = Iz / (kquad + hwood*hwood)
        moa = mmot*mcarroef / (mmot + mcarroef)
        energym = mmot * (641.7*(dwb + 0.1) ** 1.89)
        vmed = mp.sqrt(2*(energymed+energym)/moa)
        vcckhmed = vmed * 3.6
    else:
        energymed = "ND"
        vmed = "ND"
        vcckhmed = "ND"
    if (woodmotobool and (woodcarbool or woodcrushbool)):
        vmoto = (energym/(moa*0.86)) ** (1/1.6)
        vcckhmoto = vmoto * 3.6
    elif (woodmotobool and (not woodcarbool) and (not woodcrushbool)):
        kquad = (lcarro*lcarro+wcarro*wcarro)/12
        Iz = mcarro*kquad
        mcarroef = Iz / (kquad + hwood*hwood)
        moa = mmot*mcarroef / (mmot + mcarroef)
        energym = mmot * (641.7*(dwb + 0.1) ** 1.89)
        vmoto = (energym/(moa*0.86)) ** (1/1.6)
        vcckhmoto = vmoto * 3.6
    else:
        vmoto = "ND"
        vcckhmoto = "ND"
    if (empiricbool):
        vemp = 7.02 + 35.52 * dwb + 15.5 * dcarro
        vcckhemp = vemp * 3.6
    else:
        vemp = "ND"
        vcckhemp = "ND"
    print("\n----------------------------------------------------")
    print("Se ha obtenido y calculado la información con éxito!")
    print("----------------------------------------------------\n")
    damagePlotMot(sel,marca, modelo, año,c,L,oL,oW,d)
    portada(4,marcamoto,modelomoto,añomoto)
    inputMotos(marca,modelo,año,marcamoto,modelomoto,añomoto,dwb,mmot,pmoto,mtmoto,dcarro,mcarro,p,mt,lcarro,wcarro,wbcarro,trcarro,hwood,energymed,c)
    outputMotos(marca,modelo,año,marcamoto,modelomoto,añomoto,energywood,energym,vwood,vcckhwood,energymed,vmed,vcckhmed,vemp,vcckhemp,vmoto,vcckhmoto)
    
    # -------------------------------------------------------------------------------------------------------------------------
    # Lista de variables de salida de la sección de Motocicletas:
    
    # energym = Energía de la moto calculada con la ecuación original de Wood (única opción por ahora)
    
    # energywood = Energía del auto calculada con la ecuación original de Wood
    # vwood = Rapidez relativa en m/s calculada con la ecuación original de Wood
    # vcckhwood = Rapidez relativa en km/h calculada con la ecuación original de Wood
    
    # energymed = Energía del auto proporcionada por el usuario (obtenida de CERMMA Autos)
    # vmed = Rapidez relativa en m/s calculada con la ecuación de Wood modificada para recibir la energía de CERMMA Autos
    # vcckhmed = Rapidez relativa en km/h calculada con la ecuación de Wood modificada para recibir la energía de CERMMA Autos
    
    # vmoto = Rapidez relativa en m/s calculada con la ecuación de Wood que no conoce la abolladura en el auto
    # vcckhmoto = Rapidez relativa en km/h calculada con la ecuación de Wood que no conoce la abolladura en el auto
    
    # vemp = Rapidez relativa en m/s calculada con la ecuación empírica de Wood que solo ve deformaciones
    # vcckhemp = Rapidez relativa en km/h calculada con la ecuación empírica de Wood que solo ve deformaciones
    # -------------------------------------------------------------------------------------------------------------------------
    
    
    contador = 2

    return contador


# -

def salidaStiffnes():
    print("Obtener los coeficientes de: \n"
          "1. Reportes de la NHTSA para Frontales y Traseros. \n"
          "2. Reportes de la NHTSA para Laterales. \n"
          "3. Publicación Prassad. \n"
          "4. Salir. \n")
    sel = input("Selección: ")
    sel = validar(sel,2)
    
    if(sel == 1):
        A,B,marca,modelo,año,masa,data,encontrado,seccion = frontRearStiffnes()
        
    if(sel == 2):
        A,B,marca,modelo,año,masa,data,encontrado,seccion = sideStiffnes()
        
    if(sel == 3):
        A,B,marca,modelo,año,masa,data,encontrado,seccion = stiffPrassad()
    
    if(encontrado == False):
        print("¿Desea guardar esta información en la base de datos?")
        select = input("1.SI \n"
                       "2.NO \n")
        select = validar(select,3)
        
        if(select == 1):
            writeFile(data,A,B,marca,modelo,año,masa,seccion)
        
    contador = 2
    
    return contador


def salidaDeltaV(CETp,CETs,FT,m,g):
    print("----------------Resultado Total---------------")        
    print("Energía de Abolladura Total: ")
    print("-CE (promedio) = " , CETp, " J")
    print("-CE (segmentado)= " , CETs, " J")
    print("Fuerza Total: ")
    print("-FT = " , FT, " N")
    
    #Se calcula los cambios de velocidad para cada auto
    e = [0.15,0.2,0.25]
    dV1c = []
    dV2c = []
    dV1s = []
    dV2s = []
    r1 = (g[0]*m[0])/(g[1]*m[1])
    r2 = (g[1]*m[1])/(g[0]*m[0])
    
    for i in range(0,len(e)):
        v1s = mp.sqrt((2*CETs*g[0]*(1+e[i]))/(m[0]*(1+r1)*(1-e[i])))*3.6
        v2s = -mp.sqrt((2*CETs*g[1]*(1+e[i]))/(m[1]*(1+r2)*(1-e[i])))*3.6
        v1c = mp.sqrt((2*CETp*g[0]*(1+e[i]))/(m[0]*(1+r1)*(1-e[i])))*3.6
        v2c = -mp.sqrt((2*CETp*g[1]*(1+e[i]))/(m[1]*(1+r2)*(1-e[i])))*3.6
        dV1c.append(v1c)
        dV2c.append(v2c)
        dV1s.append(v1s)
        dV2s.append(v2s)
    
    print("-----Cambios en la velocidad para cada vehículo------")
    print("Coeficiente de Restitución: ", e)
    print("Delta V1 = ", dV1s, " Km/h")
    print("Delta V2 = ", dV2s, " Km/h")
    
    return e,dV1c,dV2c,dV1s,dV2s 


def salidaCE(select,folder): #Información de salida para los calculos de velocidad, energía y fuerza
    salida = 0
    control = 0 
    print("Tipo de Colisión: \n"
          "1. Colisión por un solo auto. \n"
          "2. Colisión entre dos autos. \n")
    
    n = full_data["Tipo de Colision"]
    
    if(n == 1):
        print("Ha seleccionado Colisión por un solo auto.\n")
        car_data = full_data["Carro 1"]
        print("Información del Auto y Zona de Impacto.\n")
        marca, modelo, año, sel = car_data["Marca"], car_data["Modelo"], car_data["Año"], car_data["Zona de Impacto"]
        print("El daño se presenta en la zona \n"
              "1. Frontal. \n"
              "2. Trasera. \n"
              "3. Lateral. \n")
        data = readFile(sel)
        A, B, masa, encontrado = find_coeff(marca,modelo,año,data)
                
        if(encontrado == True):
            L, cc, cs = car_data["Longitud de Abolladura(m)"], car_data["Numero de Coeficientes"], car_data["Coeficientes"]
            v = []
            CE,FT,c = calculoCE(A,B,masa,marca,modelo,año,select,L,cc,cs,folder)
            p, mass = car_data["Numero de Pasajeros"], car_data["Masa de Pasajeros(Kg)"]
            oL, oW, d = car_data["Longitud del Auto(m)"], car_data["Ancho del Auto(m)"], car_data["Distance a Referencia(cm)"]
            mt=0
            for i in range(len(mass)):
                mt += mass["Mass "+str(i+1)]
            
            for i in CE:
                vel = CESpeed(i,masa+mt)
                v.append(vel)
            print("Velocidades: \n")
            print("-V(C Promedio) = " ,v[0]*3.6," Km/h" )
            print("-V(C Segmentado) = " ,v[1]*3.6," Km/h" )
            
            FT = np.sum(FT)
            df = excel_export1(marca,modelo,año,sel,A,B,masa,CE,FT,L,c,p,mt,v,folder)
        
            portada(n,marca,modelo,año,folder,canv)
            
            damagePlot(marca, modelo, año, c, L, folder)
            damagePlotVeh(sel,marca, modelo, año, c, L,oL,oW,d, folder)
            
            inputData(marca,modelo,año,sel,A,B,masa,L,p,mt,c,oL,oW,0,canv,folder) #Escribe en el PDF
            outputData(n,marca,modelo,año,CE,FT,v,canv,folder)
            
            contador = 2
            
        
        
        if(encontrado == False):
            print("¿Desea calcular los coeficientes de Stiffness para este vehículo?")
            salida = input("1. SI \n"
                           "2. NO \n")
            salida = validar(salida,3)
        
            if(salida == 1):
                salida = 4
            else:
                salida = 0
    
    if(n == 2):
        print("Ha seleccionado Colisión entre dos autos.\n")
        CETp, CETs, FTs, ms, gam, hs, hts, sec, Ls, mts = [], [], [], [], [], [], [], [], [], []
        As, Bs, mar, mod, an, sec, masav, cs, pas = [], [], [], [], [], [], [], [], []
        oLs, oWs, deltas, Ks, thetas = [], [], [], [], []
        encont = 0
        alpha = full_data["alpha"]
        print(f"Alpha: {alpha}")
        
        for i in range(2):
            print(f"Información del Auto {i+1} y Zona de Impacto.\n")
            car_data = full_data[f"Carro {i+1}"]
            print("El daño se presenta en la zona \n"
                  "1. Frontal. \n"
                  "2. Trasera. \n"
                  "3. Lateral. \n")
            
            marca, modelo, año, sel = car_data["Marca"], car_data["Modelo"], car_data["Año"], car_data["Zona de Impacto"]
            
            data = readFile(sel)
            A, B, masa, encontrado = find_coeff(marca,modelo,año,data)
            
            if(encontrado == True):
                L, cc, ces = car_data["Longitud de Abolladura(m)"], car_data["Numero de Coeficientes"], car_data["Coeficientes"]
                encont += 1
                CE,FT,c = calculoCE(A,B,masa,marca,modelo,año,select,L,cc,ces,folder)
                oL, oW, h, ht = car_data["Longitud del Auto(m)"], car_data["Ancho del Auto(m)"], car_data["Distancia h"], car_data["Distancia ht"]
                
                if i == 0:
                    theta = car_data["theta"]
                    thetas.append(theta)
                if i == 1:
                    thetas.append(180 - alpha - thetas[0])
                
                K = gyration_radius(oL,oW)
                gama = K/(K + mp.pow(h,2))
                delt = delta(h,K)
                p, mass, d = car_data["Numero de Pasajeros"], car_data["Masa de Pasajeros(Kg)"],  car_data["Distance a Referencia(cm)"]
                mt=0
                for i in range(len(mass)):
                    mt += mass["Mass "+str(i+1)]
                
                mar.append(marca)
                mod.append(modelo)
                an.append(año)
                As.append(A)
                Bs.append(B)
                masav.append(masa)
                Ls.append(L)
                oLs.append(oL)
                oWs.append(oW)
                gam.append(gama)
                pas.append(p)
                mts.append(mt)
                ms.append(mt+masa)
                CETp.append(CE[0])
                CETs.append(CE[1])
                FTs.append(np.sum(FT))
                hs.append(h)
                hts.append(ht)
                cs.append(c)
                sec.append(sel)
                deltas.append(delt)
                Ks.append(K)
                
                damagePlot(marca, modelo, año, c, L,folder)
                damagePlotVeh(sel,marca, modelo, año,c,L,oL,oW,d,folder)
                
            if(encontrado == False):
                i = 2
                print("¿Desea calcular los coeficientes de Stiffness para este vehículo?")
                salida = input("1. SI \n"
                               "2. NO \n")
                salida = validar(salida,3)
        
                if(salida == 1):
                    salida = 3
                elif salida == 2:
                    salida = 0
        
        if encont == 2:
            cetp = CETp[0] + CETp[1]    #Crush energy total modelo promedio       
            cets = CETs[0] + CETs[1]    #Crush energy total modelo segmentado
            ft = FTs[0] + FTs[1]
            e, dv1c,dv2c,dv1s,dv2s = salidaDeltaV(cetp, cets, ft, ms, gam)
            dvc, dvs = [dv1c,dv2c], [dv1s,dv2s]
            df = excel_export2(mar,mod,an,sec,As,Bs,masav,CETp,CETs,FTs,Ls,cs,pas,ms,dvc,dvs,hs,e,folder)
        
            CE0, CE1 = [CETp[0],CETs[0]], [CETp[1],CETs[1]]
            
            #Calculo de velocidades Iniciales
            U_pP = closing_speed_par(cetp,ms[0],ms[1],deltas[0],deltas[1],e)    #Componente paralela de la velocidad modelo promedio
            U_pS = closing_speed_par(cets,ms[0],ms[1],deltas[0],deltas[1],e)    #Componente paralela de la velocidad modelo segmentado
            
            U_tP = closing_speed_trans(dv1c,ms[0],Ks[0],hs[0],hts[0],ms[1],Ks[1],hs[1],hts[1]) #Componente transversal de la velocidad modelo promedio
            U_tS = closing_speed_trans(dv1s,ms[0],Ks[0],hs[0],hts[0],ms[1],Ks[1],hs[1],hts[1]) #Componente transversal de la velocidad modelo segmentado
            
            #Usando resultado del Modelo Promedio
            U_R_C, angle_beta_C = beta_and_resU(U_pP, U_tP)                    
            lamb1_C = [x - thetas[0] for x in angle_beta_C]
            lamb2_C = [180 - alpha - x for x in lamb1_C]
            
            U1_C = initial_speed(U_R_C,alpha,lamb1_C)
            U2_C = initial_speed(U_R_C,alpha,lamb2_C)
            
            #Usando resultado del Modelo Segmentado
            U_R_S, angle_beta_S = beta_and_resU(U_pS, U_tS)                    
            lamb1_S = [x - thetas[0] for x in angle_beta_S]
            lamb2_S = [180 - alpha - x for x in lamb1_S]
            
            U1_S = initial_speed(U_R_S,alpha,lamb1_S)
            U2_S = initial_speed(U_R_S,alpha,lamb2_S)
            
            print(f"---------------------------Velocidades Pre-impacto-----------------------------------\n"
                  f"Resultados Modelo Promedio: \n"
                  f"Velocidad Vehículo 1: {U1_C} Km/h \n"
                  f"Velocidad Vehículo 2: {U2_C} Km\h \n"
                  "\n"
                  "Resultados Modelo Segmentado: \n"
                  f"Velocidad Vehículo 1: {U1_S} Km\h \n"
                  f"Velocidad Vehículo 2: {U2_S} Km\h")
            
            
            
            #Construccion del reporte
            portada(n,mar,mod,an,folder,canv)
        
            inputData(mar[0],mod[0],an[0],sec[0],As[0],Bs[0],masav[0],Ls[0],pas[0],mts[0],cs[0],oLs[0],oWs[0], hs[0],canv,folder) 
            outputData(n,mar[0],mod[0],an[0],CE0,FTs[0],0,canv,folder,alpha)
            inputData(mar[1],mod[1],an[1],sec[1],As[1],Bs[1],masav[1],Ls[1],pas[1],mts[1],cs[1],oLs[1],oWs[1], hs[1],canv,folder) 
            outputData(n,mar[1],mod[1],an[1],CE0,FTs[1],0,canv,folder,alpha)
        
            for i in range(len(e)):
                generalOutput(e[i],cetp,cets,ft,dv1c[i],dv2c[i],dv1s[i],dv2s[i],i+1,canv,folder,
                              U_pP[i],U_pS[i],U_tP[i],U_tS[i],U_R_C[i],U_R_S[i],angle_beta_C[i],
                              angle_beta_S[i],thetas[0],thetas[1])
        
        control = 2
    
    return salida, control


def control(folder):
    if not os.path.exists(folder+"/Resultados CERMMA"):
        os.makedirs(folder+"/Resultados CERMMA")
    
    control = 1
    cont = 1
    
    n = full_data["Analisis"]
    
    while(control == 1):
        print("Análisis a Realizar: \n"
              "1. Colisión entre autos. \n"
              "2. Colisión con motocicletas. \n"
              "3. Obtener Coeficientes de Stiffness. \n")
        
        #n = input("Selección: ")
        #n = validar(n,1)
        
        print("---------------------------------------------------------------------------- \n")
        
        if(n == 1): #Colisiones vehiculos
            print("-Se realizará un análisis de colisión entre autos. \n")
            cont = 1
            while(cont == 1):  
                n, cont = salidaCE(n,folder)      
                      
        if(n == 2): #Colisiones Motocicletas
            print("-Se realizará un análisis de colisión con Motocicletas. \n")
            cont = 1
            while(cont == 1):
                cont = controlMotos(folder)
                
                
        if(n == 3): #Obtencion Coeficientes de Abolladura
            print("Se realizará una obtención de coeficientes. \n")
            cont = 1
            while(cont == 1):
                cont = salidaStiffnes()
        
        canv.save()
        
        print("---------------------------------------------------------------------------- \n")
        print("El programa ha terminado.")
        control = 2

folder = input("Código del caso: ")
json_file = open(f'{folder}/input.json')
full_data = json.load(json_file)
code = full_data["Code"]
if(folder == code):
    canv = canvas.Canvas(f'{folder}/Resultados CERMMA/{folder}.pdf', pagesize=A4)
    control(folder)
else:
    print("El código de los casos no coincide! Revise.")


