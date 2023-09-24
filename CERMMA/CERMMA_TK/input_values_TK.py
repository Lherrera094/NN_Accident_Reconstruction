#!/usr/bin/env python
# coding: utf-8
# %%

# %%


#Esta sección del código se encarga de solicitar al usuario la información del auto para su búsqueda en la
#base de datos. El nombre de la marca y modelo deben llevar la primera letra mayúscula.
def car_info():
    brand = input("Marca: ")
    model = input("Modelo: ")
    year = input("Año: ")
    year = validar(year,5)
    return brand, model, year


# %%


#La función find_coeff busca en la base de datos de Warden si un auto con las características ingresadas se 
#encuentra dentro de la base de datos. De no estar, el programa avisara que no se encuentra y terminará.
def find_coeff(brand, model, year,data):
    find = False
    findModel = False 
    findYear = False
    encontrado = False
    A = 0
    B = 0
    masa = 0
    cs = 0
    yearOpt = []
    modOpt = []

    for i in range(0, len(data)):
        if(data.index[i] == brand):
            find = True
            if(data["MODEL"][i] == model):
                findModel = True
                yearOpt.append(data["YEAR"][i])
                if(data["YEAR"][i] == year):
                    encontrado = True
                    findYear = True
                    A = data["A(N/m)"][i]
                    B = data["B(N/m²)"][i]
                    masa = data["MASS(Kg)"][i]
                    cs = data["SAT"][i]
                    print("El auto se encuentran en la base de datos! \n")
                
        
    if(find == False):
        print("El auto no se encuentra en la base de datos.\n")
    if(findModel == False and find == True):
        print("Este modelo de " + brand + " no se encuentra en la base de datos.\n")
    if(findYear == False and find == True and findModel == True):
        print("Este año de " + brand + " no se encuentra en la base de datos. Años disponibles para esta"
              "marca: ", yearOpt)
    
    return A, B, masa, encontrado


# %%


#En esta función recibe la información del daño estructral para calculo de CE
def damage_info():
    l = input("-Longitud de Abolladura(metros) = ")
    l = validar(l,6)
    n = input("-Número de datos(N) = ")
    n = validar(n,5)
    coef = []
    delx = l/(n-1)
    
    print("-Ingrese los Valores de Abolladura.")
    for i in range(0, n):
        ci = input("--C" + str(i+1) + " = ")
        ci = validar(ci,6)
        coef.append(ci)
    
    return n,l, coef, delx

