#!/usr/bin/env python
# coding: utf-8
# %%


from PIL import Image
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
import reportlab
from datetime import datetime
import locale


# %%


def portada(n,marca,modelo,año,folder,canv): #Portada del reporte
    locale.setlocale(locale.LC_ALL, '') 
    date = datetime.now()
    date = date.strftime("%d de %B del %Y (%H:%M:%S)")
    w,h = A4
    text1 = f"Código Reporte: {folder}"  #Número de Reporte
    text2 = "Sección de Reconstrucción de Accidentes"
    text3 = "Reporte Realizado el " + date #Fecha
    if (n == 4):
        text4 = "Resultados CERMMA-M"
    else:
        text4 = "Resultados CERMMA"
    text9 = "Simulación y Reconstrucción Mecánica-Dinámica"
    
    text_width1 = stringWidth(text1, "Helvetica",13)
    text_width2 = stringWidth(text2, "Helvetica",13)
    text_width3 = stringWidth(text3, "Helvetica",13)
    text_width4 = stringWidth(text4, "Helvetica",13)
    
    text_width9 = stringWidth(text9, "Helvetica",13)
    
    if(n==1):
        text5 = "Colisión contra Barrera"  #Tipo de colisión    
        text_width5 = stringWidth(text5, "Helvetica",13)
        canv.drawString((w-text_width5)/2, h - 175, text5) #(PosHorizontal, PosVertical)
        
        text7 = "Vehículo Involucrado:"
        text_width7 = stringWidth(text7, "Helvetica",13)
        canv.drawString((w-text_width7)/2, h - 575, text7) #(PosHorizontal, PosVertical)
        text6 = marca + " " + modelo + " " + str(año)
        text_width6 = stringWidth(text6, "Helvetica",13)
        canv.drawString((w-text_width6)/2, h - 600, text6) #(PosHorizontal, PosVertical)
        
    if(n==2):
        text5 = "Colisión entre Dos Vehículos"  #Tipo de colisión    
        text_width5 = stringWidth(text5, "Helvetica",13)
        canv.drawString((w-text_width5)/2, h - 175, text5) #(PosHorizontal, PosVertical)
        
        text7 = "Vehículos Involucrados:"
        text_width7 = stringWidth(text7, "Helvetica",13)
        canv.drawString((w-text_width7)/2, h - 575, text7) #(PosHorizontal, PosVertical)
        
        text6 = marca[0] + " " + modelo[0] + " " + str(año[0])
        text_width6 = stringWidth(text6, "Helvetica",13)
        canv.drawString((w-text_width6)/2, h - 600, text6) #(PosHorizontal, PosVertical)
        
        text6 = marca[1] + " " + modelo[1] + " " + str(año[1])
        text_width6 = stringWidth(text6, "Helvetica",13)
        canv.drawString((w-text_width6)/2, h - 625, text6) #(PosHorizontal, PosVertical)
        
    if(n==3):
        text5 = "Colisión de Múltiple"  #Tipo de colisión    
        text_width5 = stringWidth(text5, "Helvetica",13)
        canv.drawString((w-text_width5)/2, h - 175, text5) #(PosHorizontal, PosVertical)
        
    if(n==4):
        text5 = "Colisión con Motocicletas"  #Tipo de colisión    
        text_width5 = stringWidth(text5, "Helvetica",13)
        canv.drawString((w-text_width5)/2, h - 175, text5) #(PosHorizontal, PosVertical)
        
        text7 = "Motocicleta Involucrada:"
        text_width7 = stringWidth(text7, "Helvetica",13)
        canv.drawString((w-text_width7)/2, h - 575, text7) #(PosHorizontal, PosVertical)
        
        text6 = marca + " " + modelo + " " + str(año)
        text_width6 = stringWidth(text6, "Helvetica",13)
        canv.drawString((w-text_width6)/2, h - 600, text6) #(PosHorizontal, PosVertical)

    
    canv.drawString((w-text_width1)/2, h - 50, text1) #(PosHorizontal, PosVertical)
    canv.drawString((w-text_width2)/2, h - 400, text2) #(PosHorizontal, PosVertical)
    canv.drawString((w-text_width3)/2, h - 800, text3) #(PosHorizontal, PosVertical)
    canv.drawString((w-text_width4)/2, h - 150, text4) #(PosHorizontal, PosVertical)
    canv.drawString((w-text_width9)/2, h - 425, text9) #(PosHorizontal, PosVertical)
    
    canv.drawImage("Images/Logo.jpg", 115, h - 375, width=360, height=130)
    canv.showPage()


# %%


def inputData(marca,modelo,año,sel,A,B,masa,L,p,mp,cs,oL,oW,h,canv,folder):
    w,h = A4
    text1 = "Vehículo: " + marca + " " + modelo + " " + str(año)
    canv.drawString(50, h - 100, text1) #(PosHorizontal, PosVertical)
    
    text1 = "-Variables de entrada "
    canv.drawString(50, h - 118, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 125
    # Space between rows.
    padding = 18
    max_rows_per_page = 9
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Zona de Impacto"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    if (sel==1):
        text = "Frontal"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    if (sel==2):
        text = "Trasera"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    if (sel==3):
        text = "Lateral"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    
    text = "Longitud de Abolladura"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    text = str(L) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    
    text = "Coeficiente de Rigidez A"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    text = str(round(A,4)) + " N/m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    
    text = "Coeficiente de Rigidez B"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    text = str(round(B,4)) + " N/m^2"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    
    text = "Masa del Vehículo"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
    text = str(round(masa,3)) + " Kg"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
    
    text = "Longitud del Vehículo"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 228, text) #(PosHorizontal, PosVertical)
    text = str(oL) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 228, text) #(PosHorizontal, PosVertical)
        
    text = "Anchura del Vehículo"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 246, text) #(PosHorizontal, PosVertical)
    text = str(oW) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 246, text) #(PosHorizontal, PosVertical)
        
    text = "Cantidad de Pasajeros"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 264, text) #(PosHorizontal, PosVertical)
    text = str(p)
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 264, text) #(PosHorizontal, PosVertical)
        
    text = "Masa Total Pasajeros"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 282, text) #(PosHorizontal, PosVertical)
    text = str(mp) + " Kg"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 282, text) #(PosHorizontal, PosVertical)
        
    text1 = "-Medidas de Abolladura"
    canv.drawString(50, h - 338, text1) #(PosHorizontal, PosVertical)
        
    max_rows_per_page = 6
    # Margin.
    x_offset = 100
    y_offset = 350
    # Space between rows.
    padding = 18
    
    xlist = [x + x_offset for x in [0, 200, 400]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    
    canv.grid(xlist,ylist)
    
    text1 = "C1"
    canv.drawString(185, h - 364, text1) #(PosHorizontal, PosVertical)
    text1 = str(cs[0]) + " m"
    canv.drawString(385, h - 364, text1) #(PosHorizontal, PosVertical)
    
    text2 = "C2"
    canv.drawString(185, h - 382, text2) #(PosHorizontal, PosVertical)
    text1 = str(cs[1]) + " m"
    canv.drawString(385, h - 382, text1) #(PosHorizontal, PosVertical)
    
    text3 = "C3"
    canv.drawString(185, h - 400, text3) #(PosHorizontal, PosVertical)
    text1 = str(cs[2]) + " m"
    canv.drawString(385, h - 400, text1) #(PosHorizontal, PosVertical)
    
    text4 = "C4"
    canv.drawString(185, h - 418, text4) #(PosHorizontal, PosVertical)
    text1 = str(cs[3]) + " m"
    canv.drawString(385, h - 418, text1) #(PosHorizontal, PosVertical)
    
    text5 = "C5"
    canv.drawString(185, h - 436, text5) #(PosHorizontal, PosVertical)
    text1 = str(cs[4]) + " m"
    canv.drawString(385, h - 436, text1) #(PosHorizontal, PosVertical)
    
    text6 = "C6"
    canv.drawString(185, h - 454, text6) #(PosHorizontal, PosVertical)
    text1 = str(cs[5]) + " m"
    canv.drawString(385, h - 454, text1) #(PosHorizontal, PosVertical)
    
    canv.drawImage(f"{folder}/Resultados CERMMA/Daño{marca}{modelo}{año}.png", 100, h - 760, width=400, height=260)
        
    canv.showPage()
    
    canv.drawImage(f'{folder}/Resultados CERMMA/Daño_Veh_{marca}_{modelo}_{año}.png', 45, h - 460, width=500, height=360)
    
    #page = canvas.getPageNumber()
    #text = page
    #canv.drawString(410, h - 810, text) #(PosHorizontal, PosVertical)
    
    canv.showPage()


# %%


def inputMotos(marca,modelo,año,marcamoto,modelomoto,añomoto,dme,mmot,npasajmoto,mpasajmoto,c,mauto,npasaj,mpasaj,l,a,eje,tr,ah,cE,cs,canv):
    w,h = A4
    text1 = "Motocicleta: " + marcamoto + " " + modelomoto + " " + str(añomoto)
    canv.drawString(50, h - 100, text1) #(PosHorizontal, PosVertical)
    
    text1 = "-Variables de entrada: Motocicleta "
    canv.drawString(50, h - 118, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 125
    # Space between rows.
    padding = 18
    max_rows_per_page = 4
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Cambio distancia entre ejes"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    text = str(dme) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    
    text = "Masa de la Motocicleta"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    text = str(round(mmot,4)) + " Kg"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    
    text = "Cantidad de Pasajeros"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    text = str(round(npasajmoto,4))
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    
    text = "Masa Total Pasajeros"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    text = str(round(mpasajmoto,3)) + " Kg"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    
    
    text1 = "-Variables de entrada: Automóvil"
    canv.drawString(50, h - 268, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 275
    # Space between rows.
    padding = 18
    max_rows_per_page = 10
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Máxima Profundidad de Abolladura"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 288, text) #(PosHorizontal, PosVertical)
    text = str(c) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 288, text) #(PosHorizontal, PosVertical)
    
    text = "Masa del Automóvil"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 306, text) #(PosHorizontal, PosVertical)
    text = str(round(mauto,4)) + " Kg"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 306, text) #(PosHorizontal, PosVertical)
    
    text = "Longitud del Automóvil"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 324, text) #(PosHorizontal, PosVertical)
    text = str(round(l,4)) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 324, text) #(PosHorizontal, PosVertical)
    
    text = "Ancho del Automóvil"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 342, text) #(PosHorizontal, PosVertical)
    text = str(round(a,3)) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 342, text) #(PosHorizontal, PosVertical)
    
    text = "Distancia entre Ejes"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 360, text) #(PosHorizontal, PosVertical)
    text = str(round(eje,3)) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 360, text) #(PosHorizontal, PosVertical)
    
    text = "Track"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 378, text) #(PosHorizontal, PosVertical)
    text = str(round(tr,3)) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 378, text) #(PosHorizontal, PosVertical)
    
    text = "h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 396, text) #(PosHorizontal, PosVertical)
    text = str(round(ah,3)) + " m"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 396, text) #(PosHorizontal, PosVertical)
    
    text = "Energía Disipada por Abolladura"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 414, text) #(PosHorizontal, PosVertical)
    if (cE == "ND"):
        text = cE
    else:
        text = str(round(cE,3)) + " J"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 414, text) #(PosHorizontal, PosVertical)
    
    text = "Cantidad de Pasajeros"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 432, text) #(PosHorizontal, PosVertical)
    text = str(npasaj)
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 432, text) #(PosHorizontal, PosVertical)
        
    text = "Masa Total Pasajeros"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 450, text) #(PosHorizontal, PosVertical)
    text = str(mpasaj) + " Kg"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 450, text) #(PosHorizontal, PosVertical)
    
    text1 = "-Medidas de Abolladura"
    canv.drawString(50, h - 506, text1) #(PosHorizontal, PosVertical)
        
    max_rows_per_page = len(cs)
    # Margin.
    x_offset = 100
    y_offset = 513
    # Space between rows.
    padding = 18
    
    xlist = [x + x_offset for x in [0, 200, 400]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    
    canv.grid(xlist,ylist)
    
    for i in range(0, len(cs)):
        text1 = "C" + str(i+1)
        canv.drawString(185, h - 526 - 18*i, text1) #(PosHorizontal, PosVertical)
        text1 = str(cs[i]) + " m"
        canv.drawString(385, h - 526 - 18*i, text1) #(PosHorizontal, PosVertical)
    
    #text2 = "C2"
    #canv.drawString(185, h - 544, text2) #(PosHorizontal, PosVertical)
    #text1 = str(cs[1]) + " m"
    #canv.drawString(385, h - 544, text1) #(PosHorizontal, PosVertical)
    
    #text3 = "C3"
    #canv.drawString(185, h - 562, text3) #(PosHorizontal, PosVertical)
    #text1 = str(cs[2]) + " m"
    #canv.drawString(385, h - 562, text1) #(PosHorizontal, PosVertical)
    
    #text4 = "C4"
    #canv.drawString(185, h - 580, text4) #(PosHorizontal, PosVertical)
    #text1 = str(cs[3]) + " m"
    #canv.drawString(385, h - 580, text1) #(PosHorizontal, PosVertical)
    
    #text5 = "C5"
    #canv.drawString(185, h - 598, text5) #(PosHorizontal, PosVertical)
    #text1 = str(cs[4]) + " m"
    #canv.drawString(385, h - 598, text1) #(PosHorizontal, PosVertical)
    
    #text6 = "C6"
    #canv.drawString(185, h - 616, text6) #(PosHorizontal, PosVertical)
    #text1 = str(cs[5]) + " m"
    #canv.drawString(385, h - 616, text1) #(PosHorizontal, PosVertical)
    
    #text6 = "C7"
    #canv.drawString(185, h - 634, text6) #(PosHorizontal, PosVertical)
    #text1 = str(cs[6]) + " m"
    #canv.drawString(385, h - 634, text1) #(PosHorizontal, PosVertical)
    
    #text6 = "C8"
    #canv.drawString(185, h - 652, text6) #(PosHorizontal, PosVertical)
    #text1 = str(cs[7]) + " m"
    #canv.drawString(385, h - 652, text1) #(PosHorizontal, PosVertical)
    
    canv.showPage()
    
    canv.drawImage(f'{folder}/Resultados CERMMA/Daño_Veh_{marca}_{modelo}_{año}.png', 45, h - 460, width=500, height=360)
    
    #page = canvas.getPageNumber()
    #text = page
    #canv.drawString(410, h - 810, text) #(PosHorizontal, PosVertical)
    
    canv.showPage()


# %%


def outputMotos(marca,modelo,año,marcamoto,modelomoto,añomoto,cE,dE,dv,dv2,rE,dvm,dvm2,dve,dve2,dvn,dvn2,canv):
    w,h = A4
    text1 = "Variables de Salida: Rapideces Relativas del Sistema Auto y Motocicleta"
    canv.drawString(50, h - 100, text1) #(PosHorizontal, PosVertical)

#Método Completo de Wood    
    text1 = "-Resultados: Método Completo de Wood (usando daños en auto y motocicleta)"
    canv.drawString(50, h - 118, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 125
    # Space between rows.
    padding = 18
    max_rows_per_page = 4
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Energía de Abolladura"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    if (cE == "ND"):
        text = cE
    else:
        text = str(round(cE,3)) + " J"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    
    text = "Energía de Deformación"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    if (dE == "ND"):
        text = dE
    else:
        text = str(round(dE,3)) + " J"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    
    text = "Raidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    if (dv == "ND"):
        text = dv
    else:
        text = str(round(dv,3)) + " m/s"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    
    text = "Rapidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    if (dv2 == "ND"):
        text = dv2
    else:
        text = str(round(dv2,3)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    
    
#Método Modificado de Wood     
    text1 = "-Resultados: Método Modificado de Wood (usando energía disipada)"
    canv.drawString(50, h - 243, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 250
    # Space between rows.
    padding = 18
    max_rows_per_page = 3
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Energia de Abolladura Reportada"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 263, text) #(PosHorizontal, PosVertical)
    if (rE == "ND"):
        text = rE
    else:
        text = str(round(rE,3)) + " J"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 263, text) #(PosHorizontal, PosVertical)
    
    text = "Rapidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 281, text) #(PosHorizontal, PosVertical)
    if (dvm == "ND"):
        text = dvm
    else:
        text = str(round(dvm,4)) + " m/s"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 281, text) #(PosHorizontal, PosVertical)
    
    text = "Rapidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 299, text) #(PosHorizontal, PosVertical)
    if (dvm2 == "ND"):
        text = dvm2
    else:
        text = str(round(dvm2,4)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 299, text) #(PosHorizontal, PosVertical)
    
#Método Empírico de Wood    
    text1 = "-Resultados: Método Empírico de Wood (usando daños en auto y motocicleta)"
    canv.drawString(50, h - 343, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 350
    # Space between rows.
    padding = 18
    max_rows_per_page = 2
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Rapidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 363, text) #(PosHorizontal, PosVertical)
    if (dve == "ND"):
        text = dve
    else:
        text = str(round(dve,4)) + " m/s"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 363, text) #(PosHorizontal, PosVertical)
    
    text = "Rapidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 381, text) #(PosHorizontal, PosVertical)
    if (dve2 == "ND"):
        text = dve2
    else:
        text = str(round(dve2,4)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 381, text) #(PosHorizontal, PosVertical)
    
    
#Método Sin Datos del Automóvil    
    text1 = "-Resultados: Método Simplificado de Wood (usando solo daños en la motocicleta)"
    canv.drawString(50, h - 433, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 440
    # Space between rows.
    padding = 18
    max_rows_per_page = 2
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Rapidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 453, text) #(PosHorizontal, PosVertical)
    if (dvn == "ND"):
        text = dvn
    else:
        text = str(round(dvn,4)) + " m/s"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 453, text) #(PosHorizontal, PosVertical)
    
    text = "Rapidez Relativa Inicial"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 471, text) #(PosHorizontal, PosVertical)
    if (dvn2 == "ND"):
        text = dvn2
    else:
        text = str(round(dvn2,4)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 471, text) #(PosHorizontal, PosVertical)
    
    #page = canvas.getPageNumber()
    #text = page
    #canv.drawString(410, h - 810, text) #(PosHorizontal, PosVertical)
    
    canv.showPage()


# %%


def outputData(n,marca,modelo,año,CE,F,V,canv,folder,alpha):
    w,h = A4
    text1 = "-Variables de Salida"
    canv.drawString(50, h - 118, text1) #(PosHorizontal, PosVertical)
    
    # Margin.
    x_offset = 50
    y_offset = 125
    # Space between rows.
    padding = 18
    
    if(n==1):
        max_rows_per_page = 6
        xlist = [x + x_offset for x in [0, 250, 500]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
        canv.grid(xlist,ylist)
    
        text = "Energía de Abolladura(C prom.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
        text = str(round(CE[0],4)) + " J"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
        
        text = "Velocidad Inicial(C prom.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
        text = str(round(V[0]*3.6,4)) + " Km/h"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
        
        text = "Energía de Abolladura(C Seg.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
        text = str(round(CE[1],4)) + " J"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
        
        text = "Fuerza sobre el Vehículo(C Seg.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
        text = str(round(F,4)) + " N"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
        
        text = "Tiempo de Colisión(C Seg.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
        text = str(round(CE[1]/F,4)) + " s"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
        
        text = "Velocidad Inicial(C Seg.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 228, text) #(PosHorizontal, PosVertical)
        text = str(round(V[1]*3.6,4)) + " Km/h"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 228, text) #(PosHorizontal, PosVertical)
    
        canv.drawImage(f"{folder}/Resultados CERMMA/{marca}{modelo}{año}.png", 100, h - 580, width=400, height=260)
    
    if(n>1):
        max_rows_per_page = 5
        xlist = [x + x_offset for x in [0, 250, 500]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
        canv.grid(xlist,ylist)
    
        text = "Energía de Abolladura(C prom.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
        text = str(round(CE[0],4)) + " J"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
        
        text = "Energía de Abolladura(C Seg.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
        text = str(round(CE[1],4)) + " J"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
        
        text = "Fuerza sobre el Vehículo(C Seg.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
        
        text = str(round(F,4)) + " N"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
        
        text = "Tiempo de Colisión(C Seg.)"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
        text = str(round(CE[1]/F,4)) + " s"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
        
        text = f"Angulo entre Vehículos."
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((360-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
        text = f"{round(alpha,4)} grados"
        text_width = stringWidth(text, "Helvetica",13)
        canv.drawString((860-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
    
        canv.drawImage(f"{folder}/Resultados CERMMA/{marca}{modelo}{año}.png", 100, h - 580, width=400, height=260)
    
    #text6 = "-Observaciones"
    #canv.drawString(50, h - 538, text6) #(PosHorizontal, PosVertical)
    #canv.roundRect(50, h - 750, 500, 200, 10)
    
    #page = canvas.getPageNumber()
    #text = page
    #canv.drawString(410, h - 810, text) #(PosHorizontal, PosVertical)
    
    canv.showPage()


# %%


def generalOutput(e,CEc,CEs,FT,V1c,V2c,V1s,V2s,i,canv,folder,UpP,UpS,UtP,UtS,URP,URS,BC,BS,
                  theta1,theta2):
    w,h = A4
    text1 = f"-Variables de Salida: Generales. Coeficiente de Fricción {i}."
    canv.drawString(50, h - 118, text1) #(PosHorizontal, PosVertical)
        
    max_rows_per_page = 9
    # Margin.
    x_offset = 50
    y_offset = 125
    # Space between rows.
    padding = 18
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Coeficiente de Resitución"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    text = str(e)
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 138, text) #(PosHorizontal, PosVertical)
    
    text = "Energía de Abolladura(C prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    text = str(round(CEc,4)) + " J"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 156, text) #(PosHorizontal, PosVertical)
    
    text = "Energía de Abolladura(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    text = str(round(CEs,4)) + " J"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 174, text) #(PosHorizontal, PosVertical)
    
    text = "Fuerza Total"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    text = str(round(FT,4)) + " N"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 192, text) #(PosHorizontal, PosVertical)
    
    text = "Tiempo de Colisión Total"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
    text = str(round(CEs/FT,4)) + " s"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 210, text) #(PosHorizontal, PosVertical)
        
    text = "Cambio Velocidad Vehículo 1 (C prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 228, text) #(PosHorizontal, PosVertical)
    text = str(round(V1c,4)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 228, text) #(PosHorizontal, PosVertical)
    
    text = "Cambio Velocidad Vehículo 1 (C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 246, text) #(PosHorizontal, PosVertical)
    text = str(round(V1s,4)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 246, text) #(PosHorizontal, PosVertical)
    
    text = "Cambio Velocidad Vehículo 2 (C prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 264, text) #(PosHorizontal, PosVertical)
    text = str(round(V2c,4)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 264, text) #(PosHorizontal, PosVertical)
    
    text = "Cambio Velocidad Vehículo 2 (C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 282, text) #(PosHorizontal, PosVertical)
    text = str(round(V2s,4)) + " Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 282, text) #(PosHorizontal, PosVertical)
    
    #-------------------------------------------------------------------------------------------
    text1 = "-Variables de Salida: Velocidades Pre-impacto"
    canv.drawString(50, h - 343, text1) #(PosHorizontal, PosVertical)
    x_offset = 50
    y_offset = 350
        
    max_rows_per_page = 18
    xlist = [x + x_offset for x in [0, 250, 500]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
    canv.grid(xlist,ylist)
    
    text = "Velocidad de Cierre Paralela(C prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 363, text) #(PosHorizontal, PosVertical)
    text = f"{round(UpP,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 363, text) #(PosHorizontal, PosVertical)
        
    text = "Velocidad de Cierre Paralela(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 381, text) #(PosHorizontal, PosVertical)
    text = f"{round(UpS,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 381, text) #(PosHorizontal, PosVertical)
        
    text = "Velocidad de Cierre Perpendicular(C Prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 399, text) #(PosHorizontal, PosVertical)
    text = f"{round(UtP,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 399, text) #(PosHorizontal, PosVertical)
        
    text = "Velocidad de Cierre Perpendicular(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 417, text) #(PosHorizontal, PosVertical)
    text = f"{round(UtS,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 417, text) #(PosHorizontal, PosVertical)
        
    text = f"Velocidad de Cierre Resultante(C Prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 435, text) #(PosHorizontal, PosVertical)
    text = f"{round(URP,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 435, text) #(PosHorizontal, PosVertical)
    
    text = f"Velocidad de Cierre Resultante(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 453, text) #(PosHorizontal, PosVertical)
    text = f"{round(URS,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 453, text) #(PosHorizontal, PosVertical)
    
    text = r"Ángulo Resultant Beta(C Prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 471, text) #(PosHorizontal, PosVertical)
    text = f"{round(BC,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 471, text) #(PosHorizontal, PosVertical)
    
    text = f"Ángulo Resultant Beta(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 489, text) #(PosHorizontal, PosVertical)
    text = f"{round(BS,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 489, text) #(PosHorizontal, PosVertical)
    
    text = f"Ángulo Theta 1"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 507, text) #(PosHorizontal, PosVertical)
    text = f"{round(theta1,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 507, text) #(PosHorizontal, PosVertical)
    
    text = f"Ángulo Theta 2"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 525, text) #(PosHorizontal, PosVertical)
    text = f"{round(theta2,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 525, text) #(PosHorizontal, PosVertical)
    
    text = r"Ángulo Lambda 1(C Prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 579, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 579, text) #(PosHorizontal, PosVertical)
    
    text = r"Ángulo Lambda 1(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 597, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 597, text) #(PosHorizontal, PosVertical)
    
    text = r"Ángulo Lambda 2(C Prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 615, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 615, text) #(PosHorizontal, PosVertical)
    
    text = r"Ángulo Lambda 2(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 633, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} grados"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 633, text) #(PosHorizontal, PosVertical)
    
    text = f"Velocidad Pre-impacto Vehículo 1(C Prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 651, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 651, text) #(PosHorizontal, PosVertical)
    
    text = r"Velocidad Pre-impacto Vehículo 1(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 669, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 669, text) #(PosHorizontal, PosVertical)
    
    text = f"Velocidad Pre-impacto Vehículo 2(C Prom.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 687, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 687, text) #(PosHorizontal, PosVertical)
    
    text = r"Velocidad Pre-impacto Vehículo 2(C Seg.)"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((360-text_width)/2, h - 705, text) #(PosHorizontal, PosVertical)
    text = f"{round(CEc,4)} Km/h"
    text_width = stringWidth(text, "Helvetica",13)
    canv.drawString((860-text_width)/2, h - 705, text) #(PosHorizontal, PosVertical)
    
    #text6 = "-Observaciones"
    #canv.drawString(50, h - 538, text6) #(PosHorizontal, PosVertical)
    #canv.roundRect(50, h - 750, 500, 200, 10)
    
    #page = canvas.getPageNumber()
    #text = page
    #canv.drawString(410, h - 810, text) #(PosHorizontal, PosVertical)
    
    canv.showPage()
