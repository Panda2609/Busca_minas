# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 19:49:57 2016

@author: banda
"""
#------------------------bibliotecas-------------------------------
from random import randint 
from time import *
#------------------------funciones---------------------------------
def menu():#funcion que imprime el menu
    print("|-----------MENÚ-----------|")
    print("|[1] Nivel Principiante    |")
    print("|[2] Nivel Intermedio      |")
    print("|[3] Nivel Experto         |")
    print("|[4] Nivel  Perzonalizado  |")
    print("|--------------------------|")
    nivel=0
    termino=0
    while termino != 1:
        nivel=int(raw_input("nivel:"))
        if nivel >= 1 and nivel <= 4:
            termino=1
    if nivel == 1:#nivel de dificultad principiante
        TABLERO=crear_tablero(8,8)
        Tablero_jugador=tablero_del_jugador(8,8)
        n_minas=10
        posicionar_minas(TABLERO,n_minas)
        revisa_minas(TABLERO)
    elif nivel == 2:#nivel de dificultad avanzada
        TABLERO=crear_tablero(16,16)
        Tablero_jugador=tablero_del_jugador(16,16)
        n_minas=20
        posicionar_minas(TABLERO,n_minas)
        revisa_minas(TABLERO)
    elif nivel == 3:#nivel de dificultad experto
        TABLERO=crear_tablero(32,32)
        Tablero_jugador=tablero_del_jugador(32,32)
        n_minas=30
        posicionar_minas(TABLERO,n_minas)
        revisa_minas(TABLERO)
    elif nivel == 4:#nivel de dificultad perzonalizado
        filas=int(raw_input("filas del tablero:"))
        columnas=int(raw_input("columnas del tablero:"))
        TABLERO=crear_tablero(filas,columnas)
        Tablero_jugador=tablero_del_jugador(filas, columnas)
        n_minas=int(raw_input("cantidad de minas:"))
        posicionar_minas(TABLERO,n_minas)
        revisa_minas(TABLERO)
    return TABLERO, Tablero_jugador    
def revisa_minas(M):#funcion que revisa la casilla circundante en busca de minas
    i=0
    cant_minas=0
    while i < len(M):
        j=0
        while j < len(M[0]):
            if M[i][j] == 0:
                if i-1 >= 0 and M[i-1][j] == '*':#arriba
                    cant_minas+=1
                if i-1 >= 0 and j+1 < len(M[0]) and M[i-1][j+1] == '*':#esquina sup derecha
                    cant_minas+=1
                if j+1 < len(M[0]) and M[i][j+1] == '*':#derecha
                    cant_minas+=1
                if i+1 < len(M) and j+1< len(M[0]) and M[i+1][j+1] == '*':#esquina inf derecha
                    cant_minas+=1
                if i+1 < len(M) and M[i+1][j] == '*':#abajo
                    cant_minas+=1
                if i+1 <len(M) and j-1 >= 0 and M[i+1][j-1] == '*':#esquina inf izquerda
                    cant_minas+=1
                if j-1>= 0 and M[i][j-1] == '*':#izquerda
                    cant_minas+=1
                if i-1 >= 0 and j-1 >= 0 and M[i-1][j-1] == '*':#esquina sup izquerda
                    cant_minas+=1
                M[i][j]=cant_minas
                cant_minas=0
            j+=1
        i+=1
def imprime_tablero(M):#Imprime el tablero en formato
    i=0
    while i < len(M):
        j=0
        while j < len(M[0]):
            print "[",M[i][j],"]",
            j+=1
        print
        i+=1
def crear_tablero(filas,columnas):#crea tablero relleno de 0 
    M=[]
    i=0
    while i < filas:
        a=[0]*columnas
        M.append(a)
        i+=1
    return M
def tablero_del_jugador(filas,columnas):#crea tablero relleno de 0 
    M=[]
    i=0
    while i < filas:
        a=['#']*columnas
        M.append(a)
        i+=1
    return M
def posicionar_minas(M,n_minas):#posiciona las minas dentro del rango de la matriz
    i=0
    while i < n_minas:
        pos_i=randint(0,len(M)-1)
        pos_j=randint(0,len(M[0])-1)
        if M[pos_i][pos_j] != '*':
            M[pos_i][pos_j]='*' #el numero 9 indicará una mina
            i+=1
#def destape(TABLERO, Tablero_jugador, pos_i, pos_j):
    
    
'''def destape(TABLERO, Tablero_jugador,pos_i,pos_j):#funcion de backtracking que destapa las casillas
        Tablero_jugador=TABLERO[pos_i][pos_j]
        
        if pos_i -1 >= 0 and TABLERO[pos_i-1][pos_j] != 0:#arriba
            destape(TABLERO, Tablero_jugador,pos_i-1,pos_j)
            
        if pos_i -1 >= 0 and pos_j+1 < len(TABLERO[0]) and TABLERO[pos_i-1][pos_j+1] != 0:#esquina sup derecha
            destape(TABLERO, Tablero_jugador,pos_i-1,pos_j+1)
            
        if pos_j +1 < len(TABLERO[0]) and TABLERO[pos_i][pos_j+1] != 0:#derecha
            destape(TABLERO, Tablero_jugador,pos_i,pos_j+1)
            
        if pos_j +1 < len(TABLERO[0]) and pos_i + 1 < len(TABLERO) and TABLERO[pos_i+1][pos_j+1] != 0:#esquina inf derecha
            destape(TABLERO, Tablero_jugador,pos_i+1,pos_j+1)
            
        if pos_i +1 < len(TABLERO) and TABLERO[pos_i+1][pos_j] != 0:#abajo
            destape(TABLERO, Tablero_jugador,pos_i+1,pos_j)
            
        if pos_i +1 < len(TABLERO) and pos_j -1 >= 0 and TABLERO[pos_i+1][pos_j-1] != 0:#esquina inf izquerda
            destape(TABLERO, Tablero_jugador,pos_i+1,pos_j-1)
            
        if pos_j -1 >= 0 and TABLERO[pos_i][pos_j-1] != 0:#izquerda
            destape(TABLERO, Tablero_jugador,pos_i,pos_j-1)
            
        if pos_i -1 >= 0 and pos_j -1 >= 0 and TABLERO[pos_i-1][pos_j-1] != 0:#esquina sup izquerda 
            destape(TABLERO, Tablero_jugador,pos_i-1,pos_j-1)'''
#-------------------------programa principal----------------------------
TABLERO, Tablero_jugador=menu() #contiene el tablero dependiendo del nivel
imprime_tablero(Tablero_jugador)
final=0
while final == 0:
    pos_i=int(raw_input("posicion i:"))#variables de posicion dentro de la matriz
    pos_j=int(raw_input("posicion j:"))
    if TABLERO[pos_i][pos_j] != '*':#mientras la posiscion no sea una mina imprime segun corresponda
        if TABLERO[pos_i][pos_j] == 0:#hace el destape recursivo en caso de ser 0
            destape(TABLERO, Tablero_jugador, pos_i, pos_j)
            imprime_tablero(Tablero_jugador)
        else:#solo imprime la casilla en caso de que esta tenga número
            Tablero_jugador[pos_i][pos_j]=TABLERO[pos_i][pos_j]
            imprime_tablero(Tablero_jugador)
    else:#si la posicion es una mina, cambia la variable y se sale del juego
        final=1
        Tablero_jugador[pos_i][pos_j]=TABLERO[pos_i][pos_j]
        imprime_tablero(Tablero_jugador)
        print("has perdido!")