#!/usr/bin/env python
# coding: utf-8
# %%

# %%


def validar(valor,tipo):
    #Validar control
    if(tipo == 1):
        sel = ["1", "2", "3", "4", "5"]
        if valor not in sel:
            while(valor not in sel):
                print("Ingrese el valor correcto.")
                valor = input("Selección: ")
        valor = int(valor)
    
    if(tipo == 2):
        sel = ["1", "2", "3","4"]
        if valor not in sel:
            while(valor not in sel):
                print("Ingrese el valor correcto.")
                valor = input("Selección: ")
        valor = int(valor)
                
    if(tipo == 3):
        sel = ["1", "2"]
        if valor not in sel:
            while(valor not in sel):
                print("Ingrese el valor correcto.")
                valor = input("Selección: ")
        valor = int(valor)
                
    if(tipo == 4):
        sel = ["1", "2","3"]
        if valor not in sel:
            while(valor not in sel):
                print("Ingrese el valor correcto.")
                valor = input("Selección: ")
        valor = int(valor)
                
    #Validar si un dato es un entero
    if(tipo == 5):
        valid = val_int(valor)
        if(valid == False):
            while(valid == False):
                valor = input("Ingrese un valor válido: ")
                valid = val_int(valor)
        valor = int(valor)
                
    #Validar si un dato es tipo flotante
    if(tipo == 6):
        valid = val_float(valor)
        if(valid == False):
            while(valid == False):
                valor = input("Ingrese un valor válido: ")
                valid = val_float(valor)
        valor = float(valor)
    
    #Validar si el valor es nulo (motocicletas)
    if(tipo == 7):
        validint = val_int(valor)
        validflo = val_float(valor)
        if((validint == False) and (validflo == False) and (valor != "ND")):
            while((validint == False) and (validflo == False) and (valor != "ND")):
                valor = input("Ingrese un valor válido: ")
                validint = val_int(valor)
                validflo = val_float(valor)
        if validflo == True:
            valor = float(valor)
        elif validint == True:
            valor = int(float(valor))
    
    return valor


# %%


def val_int(value): #Revisa que los valores ingresados sean enteros
    try:
        int(value)
        return True
    except ValueError:
        return False


# %%


def val_float(value): #Revisa que los valores ingresados sean flotantes
    try:
        float(value)
        return True
    except ValueError:
        return False

