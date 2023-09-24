#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import matplotlib.pyplot as pl
import math as mp
import numpy as np
from PIL import Image


# %%


def damagePlot(brand,model,year,med,long,folder): #Dibuja el contorno del daño con los Cs
    x = [0]
    abo = [0]
    for i in range(len(med)-1): 
        x.append(x[i] + (long/(len(med)-1)))
    
    for i in range(len(med)): 
        abo.append(med[i])
    
    abo.append(0)
    x.append(x[-1]+0.05)
    x.append(-0.05)
    x.insert(0,x.pop())
    
    pl.plot(x,abo, color = 'navy')
    pl.plot(x,abo,'o',color='green', label='Mediciones de Abolladura')
    pl.title("Perfil de Daño Estructural",size=18)
    pl.xlabel('Ancho del Daño(m)', size=16)
    pl.ylabel('Medidas de Profundidad(m)',size=16)
    pl.grid()
    
    for i in range(len(med)):
        pl.text(x=x[i+1], y=abo[i+1], s='C' + str(i+1), color = 'red')
        
    pl.legend()
    pl.savefig(f'{folder}/Resultados CERMMA/Daño{brand}{model}{year}.png', dpi=1000)
    pl.show()


# %%


def damagePlotMot(sec,brand,model,year,med,long,OL,OW,dis,folder): #Utiliza imagen del auto
    long, OL, OW = long*100, OL*100, OW*100
    abo = []
    img = Image.open(f'Images/vehículo.png') 
    
    pl.imshow(img, extent=[-22,OW+22,OL+7,-6])
    if sec == 1:
        for i in range(len(med)):
            abo.append((med[i]*100*((OW-22)/OW)) + 7) #*((200-20)/195)
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1)*((OL-6)/OL)))
        
        pl.plot(x,abo, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(x,abo,'o', ms = 5, color='navy',label = 'Medidas de Abolladura')
        pl.text(x=x[0], y=abo[0], s=' C' + str(1), color = 'green')
        pl.text(x=x[-1], y=abo[-1], s=' C' + str(len(med)), color = 'green')
        
    if sec == 2:
        for i in range(len(med)):
            abo.append(-(med[i]*100*((OW-22)/OW)) + OL)
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1)*((OL-6)/OL)))
        
        pl.plot(x,abo, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(x,abo,'o', ms = 5, color='navy',label = 'Medidas de Abolladura')
        pl.text(x=x[0], y=abo[0], s=' C' + str(1), color = 'green')
        pl.text(x=x[-1], y=abo[-1], s=' C' + str(len(med)), color = 'green')
    
    if sec == 3:
        for i in range(len(med)):
            abo.append((med[i]*100*((OL-6)/OL)))
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1))*((OW-22)/OW))
        
        pl.plot(abo,x, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(abo,x,'o', ms = 5, color='navy',label = 'Medidas de Abolladura')
        pl.text(x=abo[0], y=x[0], s=' C' + str(1), color = 'green')
        pl.text(x=abo[-1], y=x[-1], s=' C' + str(len(med)), color = 'green') 
                
    if sec == 4:
        for i in range(len(med)):
            abo.append(-(med[i]*100*((OL-6)/OL)) + OW)
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1))*((OW-22)/OW))
        
        pl.plot(abo,x, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(abo,x,'o', ms = 5, color='navy',label = 'Medidas de Abolladura')
        pl.text(x=abo[0], y=x[0], s=' C' + str(1), color = 'green', verticalalignment = 'center_baseline')
        pl.text(x=abo[-1], y=x[-1], s=' C' + str(len(med)), color = 'green', verticalalignment = 'center_baseline') 
        
    pl.title(f"Daño sobre el Vehículo {brand} {model} {year}",size=18)
    pl.xlabel('Ancho (cm)', size=16)
    pl.ylabel('Largo (cm)',size=16)
    pl.xlim(-19,550)
    pl.legend(loc='center right')
    pl.grid()
    pl.savefig(f'{folder}/Resultados CERMMA/Daño_Veh_{brand}_{model}_{year}.png', dpi=1000)
    pl.show()


# %%


def damagePlotVeh(sec,brand,model,year,med,long,OL,OW,dis,folder): #Utiliza imagen del auto
    long, OL, OW = long*100, OL*100, OW*70
    abo = []
    img = Image.open(f'Images/vehículo.png') 
    
    pl.imshow(img, extent=[-22,OW+22,OL+7,-6])
    if sec == 1:
        for i in range(len(med)):
            abo.append((med[i]*100*((OW-22)/OW)) + 7) #*((200-20)/195)
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1)*((OL-6)/OL)))
        
        pl.plot(x,abo, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(x,abo,'o',color='navy',label = 'Medidas de Abolladura')
        pl.text(x=x[0], y=abo[0], s='C' + str(1), color = 'green')
        pl.text(x=x[-1], y=abo[-1], s='C' + str(6), color = 'green')
        
    if sec == 2:
        for i in range(len(med)):
            abo.append(-(med[i]*100*((OW-22)/OW)) + OL)
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1)*((OL-6)/OL)))
        
        pl.plot(x,abo, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(x,abo,'o',color='navy',label = 'Medidas de Abolladura')
        pl.text(x=x[0], y=abo[0], s='C' + str(1), color = 'green')
        pl.text(x=x[-1], y=abo[-1], s='C' + str(6), color = 'green')
    
    if sec == 3:
        for i in range(len(med)):
            abo.append((med[i]*100*((OL-6)/OL)))
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1))*((OW-22)/OW))
        
        pl.plot(abo,x, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(abo,x,'o',color='navy',label = 'Medidas de Abolladura')
        pl.text(x=abo[0], y=x[0], s='C' + str(1), color = 'green')
        pl.text(x=abo[-1], y=x[-1], s='C' + str(6), color = 'green') 
                
    if sec == 4:
        for i in range(len(med)):
            abo.append(-(med[i]*100*((OL-6)/OL)) + OW)
    
        x = [dis]
        for i in range(len(med)-1): 
            x.append(x[i] + (long/(len(med)-1))*((OW-22)/OW))
        
        pl.plot(abo,x, color = 'tomato',label = 'Contorno del Daño')
        pl.plot(abo,x,'o',color='navy',label = 'Medidas de Abolladura')
        pl.text(x=abo[0], y=x[0], s='C' + str(1), color = 'green')
        pl.text(x=abo[-1], y=x[-1], s='C' + str(6), color = 'green') 
        
    pl.title("Daño sobre el Vehículo",size=18)
    pl.xlabel('Ancho (cm)', size=16)
    pl.ylabel('Largo (cm)',size=16)
    pl.xlim(-19,550)
    pl.legend(loc='center right')
    pl.grid()
    pl.savefig(f'{folder}/Resultados CERMMA/Daño_Veh_{brand}_{model}_{year}.png', dpi=1000)
    pl.show()


# %%


def plotAB(a,b,brand, model, year,l,c,CEi,folder):
    cave = sum(c)/len(c)
    F = []
    CE = []
    Cteorico = np.arange(0.0,0.6,0.05).tolist()
    for i in range(0,len(Cteorico)):
        F.append((a+b*Cteorico[i])*l)
        CE.append(np.power((a/np.sqrt(b))+ (np.sqrt(b)*Cteorico[i]),2)*l)
    
    pl.plot(cave,CEi*l, 'o',label="Energía del Caso(J)")
    pl.plot(Cteorico,F, 'o',label="Fuerza de Abolladura (N)")
    pl.plot(Cteorico,CE, 'o',label="Energía de Abolladura (J)")
    pl.title("Curva de Fuerza ",size=18)
    pl.xlabel('Medidas de Abolladura Generales(m)', size=16)
    pl.ylabel('Carga Seccional',size=16)
    pl.legend()
    pl.savefig(f'{folder}/Resultados CERMMA/{brand}{model}{year}.png', dpi=600)
    pl.show()

