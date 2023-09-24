#!/usr/bin/env python
# coding: utf-8
# %%
import pandas as pd

# %%


def readFile(nc): #Se encarga de leer el archivo solicitado
    directory = "CERMMA_Database"
    if(nc==1):
        data = pd.read_excel(f"{directory}/Coeficientes de Stiffness Frontales.xlsx", index_col=0) #Lee la base de datos frontales
        data = pd.DataFrame(data) #Convierte el archivo en data frame
    if(nc==2):
        data = pd.read_excel(f"{directory}/Coeficientes de Stiffness Traseros.xlsx", index_col=0) #Lee la base de datos trasera
        data = pd.DataFrame(data) #Convierte el archivo en data frame 
    if(nc==3 or nc==4):
        data = pd.read_excel(f"{directory}/Coeficientes de Stiffness Laterales.xlsx", index_col=0) #Lee la base de datos laterales
        data = pd.DataFrame(data) #Convierte el archivo en data frame 
    return data


# %%


def writeFile(file,a,b,brand,model,year,mass,tipo): #Guarda la información de los stiffness en la base de datos
    directory = "CERMMA_Database"
    new_data = pd.DataFrame({'MODEL': [model],
                             'YEAR': [year],
                             'A(N/m)': [a],
                             'B(N/m²)': [b],
                             'MASS(Kg)': [mass]},
                          index=[brand])
    
    new_file = file.append(new_data)
    if(tipo == 1):
        new_file.to_excel(f"{directory}/Coeficientes de Stiffness Frontales.xlsx")
    if(tipo == 2):
        new_file.to_excel(f"{directory}/Coeficientes de Stiffness Traseros.xlsx")
    if(tipo == 3):
        new_file.to_excel(f"{directory}/Coeficientes de Stiffness Laterales.xlsx")


# %%


#Esta función pasa a Excel todos los datos de entrada y salida
def excel_export1(mar,mod,an,sec,A,B,m,CE,FT,L,c,pasaj,mt,vel,folder):
    if sec==1:
        sec = 'Frontal'
    elif sec == 2:
        sec = 'Trasero'
    elif sec == 3:
        sec = 'Lateral'
    
    marca, modelo, ano, sec, m, L, p = [mar], [mod], [an], [sec], [m], [L], [pasaj]
    A, B, mt,FT = [A], [B], [mt], [FT]
        
    lmar,lmod,lan,lsec,lA,lB,lm = len(marca),len(modelo),len(ano), len(sec),len(A),len(B),len(m)
    lCE,lFT,lL,lc,lp,lmt,lvel = len(CE),len(FT),len(L), len(c),len(p),len(mt),len(vel)
    # now find the max
    max_len = max(lmar,lmod,lan,lsec,lCE,lFT,lc,lvel)
    
    if not max_len == lmar:
        marca.extend(['']*(max_len-lmar))
    if not max_len == lmod:
        modelo.extend(['']*(max_len-lmod))
    if not max_len == lan:
        ano.extend(['']*(max_len-lan))
    if not max_len == lsec:
        sec.extend(['']*(max_len-lsec))
    if not max_len == lA:
        A.extend(['']*(max_len-lA))
    if not max_len == lB:
        B.extend(['']*(max_len-lB))
    if not max_len == lm:
        m.extend(['']*(max_len-lm))
    if not max_len == lCE:
        CE.extend(['']*(max_len-lCE))
    if not max_len == lFT:
        FT.extend(['']*(max_len-lFT))
    if not max_len == lL:
        L.extend(['']*(max_len-lL))
    if not max_len == lc:
        c.extend(['']*(max_len-lc))
    if not max_len == lp:
        p.extend(['']*(max_len-lp))
    if not max_len == lmt:
        mt.extend(['']*(max_len-lmt))
    if not max_len == lvel:
        vel.extend(['']*(max_len-lvel))
    
    df = pd.DataFrame({'Marca':mar, 'Modelo':mod, 'Año': an, 'Sección':sec,
                       'A': A, 'B': B, 'Masa_Vehiculo': m,
                       'Energía_Abolladura': CE,'Fuerza_Total': FT, 'Longitud_Abolladura': L,
                       'Coeficientes': c, 'Pasajeros': pasaj, 'masa_total': mt, 'Velocidad': vel})
        
    df.to_csv(f'{folder}/Resultados CERMMA/Datos {mar}{mod}{an}.csv')
    return df


# %%


#Esta función pasa a Excel todos los datos de entrada y salida
def excel_export2(marca,modelo,ano,sec,A,B,m,CEp,CEs,FT,L,c,p,mt,dvc,dvs,h,e,folder):
    
    lmar,lmod,lan,lsec,lA,lB,lm = len(marca),len(modelo),len(ano), len(sec),len(A),len(B),len(m)
    lCEs,lCEp,lFT,lL,lc,lp,lmt = len(CEs),len(CEp),len(FT),len(L), len(c),len(p),len(mt)
    lh, ldvc, ldvs, le = len(h), len(dvc), len(dvs), len(e)
    # now find the max
    max_len = max(lmar,lmod,lan,lsec,lCEs,lCEp,lFT,lc,lp,ldvs, ldvc,lh, lmt,le,lA,lB)
    
    if not max_len == lmar:
        marca.extend(['']*(max_len-lmar))
    if not max_len == lmod:
        modelo.extend(['']*(max_len-lmod))
    if not max_len == lan:
        ano.extend(['']*(max_len-lan))
    if not max_len == lsec:
        sec.extend(['']*(max_len-lsec))
    if not max_len == lA:
        A.extend(['']*(max_len-lA))
    if not max_len == lB:
        B.extend(['']*(max_len-lB))
    if not max_len == lm:
        m.extend(['']*(max_len-lm))
    if not max_len == lCEs:
        CEs.extend(['']*(max_len-lCEs))
    if not max_len == lCEp:
        CEp.extend(['']*(max_len-lCEp))
    if not max_len == lFT:
        FT.extend(['']*(max_len-lFT))
    if not max_len == lL:
        L.extend(['']*(max_len-lL))
    if not max_len == lc:
        c.extend(['']*(max_len-lc))
    if not max_len == lp:
        p.extend(['']*(max_len-lp))
    if not max_len == lmt:
        mt.extend(['']*(max_len-lmt))
    if not max_len == ldvc:
        dvc.extend(['']*(max_len-ldvc))
    if not max_len == ldvs:
        dvs.extend(['']*(max_len-ldvs))
    if not max_len == lh:
        h.extend(['']*(max_len-lh))
    if not max_len == le:
        e.extend(['']*(max_len-le))
    
    
    df = pd.DataFrame({'Marca':marca, 'Modelo':modelo, 'Año': ano, 'Sección':sec,
                       'A': A, 'B': B, 'Masa_Vehiculo': m, 'h': h,
                       'Energía_Abolladura_s': CEs,'Energía_Abolladura_p': CEp,'Fuerza_Total': FT, 'Longitud_Abolladura': L,
                       'Coeficientes': c, 'Pasajeros': p, 'masa_total': mt, 'Velocidad_promedio': dvc,
                       'Velocidad_Segmentado': dvs, 'e':e})
        
    df.to_csv(f'{folder}/Resultados CERMMA/Full_Datos.csv')
    return df

