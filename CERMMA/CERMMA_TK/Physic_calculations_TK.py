#!/usr/bin/env python
# coding: utf-8
# %%
# Developer: Luis Carlos Herrera Quesada
# Date: 20/09/2023
# San José, Costa Rica

# %%
import numpy as np
import math as mp
from plot_functions_TK import *


# %%
#Esta función calcula la relacion entre el radio de giro y la distancia h
def delta(h,K):
    delta = 1 + (h/K)**2
    
    return delta


# %%

def CESpeed(E, m):
    v = mp.sqrt(2*E/m) #Velocidad a partir de Crush Energy
    return v 


# %%

def gamma():
    a = input("Longitud total del auto(m) = ")
    a = validar(a,6)
    b = input("Anchura total del auto(m) = ")
    b = validar(b,6)
    h = input("Distancia h(m)= ")
    h = validar(h,6)
    
    K = gyration_radius(a,b)
    gamma = K/(K + mp.pow(h,2))
    
    return gamma,a,b,h


# %%

def gyration_radius(a,b):
    sqK = (mp.pow(a,2)+mp.pow(b,2))/12
    return sqK


# %%


def massPass(): #Solicita el número de pasajeros y la masa de cada uno
    P = input("Número de Pasajeros: ")
    P = validar(P,5)
    mt = 0
    for i in range(P):
        print("Masa del pasajero ", i+1)
        m = input("Masa (Kg) = ")
        m = validar(m,6)
        mt = mt + m
        
    return mt, P


# %%


def kineticE(v,m):
    K = m*mp.pow(v,2)/2
    return K


# %%


def efectiveMass(Mv,Mb):
    mf = (Mv/(1+(Mv/Mb)))
    return mf


# %%


def cprom(n,coef): #Obtiene el c promedio de los valores de abolladura medidos
    prom_c = 0
    for i in range(0,n-1):
        prom_c = prom_c + coef[i] + coef[i+1]
    
    prom_c = (prom_c/(2*(n-1)))
    return prom_c


# %%


def beta(n,coef,delx,l): #Obtiene el valor de beta, relacionada con la geometría de la abolladura
    beta = 0
    for i in range(0,n-1):
        beta = beta + (coef[i]*coef[i]) + (coef[i]*coef[i+1]) + (coef[i+1]*coef[i+1])
    
    prom_c = cprom(n,coef)
    beta = (beta*delx)/(3*l*mp.pow(prom_c,2))
    return beta


# * Modelos Para Obtención de la Crush Energy (CE)

# %%


#Modelo de C Promedio: Calcula la CE usando los valores de abolladura
def cBeta(n,l,coef, delx, a,b):
    bet = beta(n,coef,delx,l)
    prom_c = cprom(n,coef)
    CE = l*mp.pow(a + (b*bet*prom_c),2)/(2*bet*b)
    return CE


# %%


def segBeta(n,coef,delx,l):
    bet = 0
    for i in range(0,n-1):
        bet = bet + (mp.pow(coef[i],2) + (coef[i]*coef[i+1]) + mp.pow(coef[i+1],2))*delx
    
    prom_c = cprom(n,coef)
    bet = bet/(3*l*mp.pow(prom_c,2))
    return bet


# %%


#Función que encuentra el CE y Ftot para el daño sobre un auto
def SegbySeg(n,coef,delx,l,a,b):
    CEi = 0 #Contribuciones al crush energy
    Fi = [] #Fuerza aplicada a cada sección sobre el auto
    
    prom_c = cprom(n,coef)
    bet = segBeta(n,coef,delx,l)
    G = mp.pow(a,2)/(2*b*bet)
    
    for i in range(0,n-1):
        Ci = (coef[i]+coef[i+1])/2
        CEi = CEi + (((a*coef[i])+G)*delx) + ((b/6)*(mp.pow(coef[i],2) + (coef[i]*coef[i+1]) + mp.pow(coef[i+1],2))*delx)
        Fi.append((a + (b*coef[i]))*delx)
    
    return CEi, Fi


# %%


def narrowObjects(coef,m):
    crm = max(coef)*10
    b11 = 1.53*mp.pow(10,-4)
    b12 = 2.47*mp.pow(10,-4)
    b0 = 8
    v1 = b0 + (b11*crm*m*9.8)
    v2 = b0 + (b12*crm*m*9.8)
    return v1, v2


# %%
def calculoCE(a,b,masa,brand,model,year,sel,L,N,cs,folder):
    v,c = [],[]
    deltax = L/(N-1)
    for i in range(N):
        c.append(cs["C"+str(i+1)])
    #print("Información del daño.\n")
    #N,L,c,deltax = damage_info()    #Se ingresan los datos recolectados de la escena
    csCE = cBeta(N,L,c,deltax,a,b)  #CE por C promedio
    segCE, segFt = SegbySeg(N,c,deltax,L,a,b)          #CE por C segmentado    
    CE = [csCE, segCE]
    FT = [segFt]
                        
    print("------------------------Resultados------------------------- \n")
                        
    print("Modelo de C Promedio: \n"
          "-Energia de Abolladura = " , CE[0] , " J \n")
    print("Modelo de C Segementado: \n"
          "-Energia de Abolladura = " , CE[1] , " J \n"
          "-Fuerza Total = " , np.sum(FT) , " N \n"
          "-Fuerza sobre cada sección de la abolladura = ", FT, " N \n")
    
    if (sel==1):
        plotAB(a,b,brand,model,year,L,c,CE[0],folder)
        
    if (sel ==2):
        print("Colisión con motocicleta, no se produce la gráfica")

    if(sel==3):
        Vcb, Vca = narrowObjects(c,masa)
        print("Modelo Empírico: \n"
              "-Velocidad Inferior = " , Vcb*3.6 , " Km/h \n"
              "-Velocidad Superior= " , Vca*3.6 , " Km/h \n")
            
    return CE,FT,c
