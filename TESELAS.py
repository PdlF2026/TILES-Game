# Copyright (c) 2026 Pablo de la Fuente Sancho - Licensed under the MIT License

import random
import time
import os
import winsound as win

# Algunas variables como fawly, Dev, laurus, YaVes, Kantwa o Trew tienen nombres poco descriptivos.

RUTAniveles="NNN.txt" # Archivos que crea
RUTAusuario="UST.txt"

def clear():
    """Limpia la pantalla en cualquier sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Cuando sin seleccionar nada copias da error de teclado. Estas funciones lo cubren parcialmente.
def KEYinput(text: str):
    q=True
    fawly=True
    while q:
        try:
            Dev=str(input(text))
            q=False
        except KeyboardInterrupt:
            print("")
            if fawly:
                text=text+" (No hagas Ctrl+C sin seleccionar nada)"+str(text[len(text)-1])
                fawly=False
    return Dev

def KEYsleep(t):
    q=True
    while q:
        try:
            time.sleep(t)
            q=False
        except KeyboardInterrupt:
            print("> (No hagas Ctrl+C sin seleccionar nada)")
    return None

# Guarda en los txt la info, controlando excepciones.
def Guardar():
    global RUTAusuario
    global RUTAniveles
    global NumUsuario
    global NumNiveles
    global Cero
    global Tes1NumNiveles
    global Tes2NumNiveles
    global Tes3NumNiveles
    global NumeroTotaldeNiveles
    global Niveles01
    if True:
        laurus=0
        Tes1NumNiveles=0
        while laurus<18:
            if (Niveles01[laurus])=="1":
                Tes1NumNiveles=Tes1NumNiveles+1
            laurus=laurus+1
        Tes2NumNiveles=0
        while laurus<36:
            if (Niveles01[laurus])=="1":
                Tes2NumNiveles=Tes2NumNiveles+1
            laurus=laurus+1
        Tes3NumNiveles=0
        try:
            while laurus<56:
                if (Niveles01[laurus])=="1":
                    Tes3NumNiveles=Tes3NumNiveles+1
                laurus=laurus+1
            NumNiveles=Tes1NumNiveles+Tes2NumNiveles+Tes3NumNiveles
        except:
            win.MessageBeep()
            while laurus<55:
                if (Niveles01[laurus])=="1":
                    Tes3NumNiveles=Tes3NumNiveles+1
                laurus=laurus+1
                NumNiveles=Tes1NumNiveles+Tes2NumNiveles+Tes3NumNiveles
    if True:
        if True:
            Archivo=open(RUTAusuario,"w")
            YaVes=str("Us66PPCCode3451028Seguridad45322Qi5454igbkjew458763PINQwertyLaurusUsuario") # 0 posicionales
            YaVes=YaVes+(str(NumUsuario))+"N"
            Extra=int(3-(len(str(NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(NumNiveles))+"N1"
            Extra=int(3-(len(str(Tes1NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(Tes1NumNiveles))+"N2"
            Extra=int(3-(len(str(Tes2NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(Tes2NumNiveles))+"N3"
            Extra=int(3-(len(str(Tes3NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(Tes3NumNiveles))+"beg56AnemonaCoral34"
            Archivo.write(YaVes)
            Archivo.close()
            # Archivo niveles:
            Niveles=open(RUTAniveles,"w")
            Retaila=""
            i=0
            while i<(NumeroTotaldeNiveles):
                L=str(Niveles01[i])
                Retaila=Retaila+L
                i=i+1
            Niveles.write(Retaila)
            Niveles.close()
    return None

# Para cada Teselas hay las mismas funciones. inputs para la entrada de comandos, Code para los códigos binarios y Tablero para la imagen.
# Control se expllica cuando aparece por primera vez.
################################  TESELAS 1
def CinputT1(text=str):
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="i")or(W=="d")or(W=="I")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="0")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("comando no válido")
def C2inputT1(text=str):
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="i")or(W=="d")or(W=="I")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("comando no válido")
def TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C):
    print("")
    print("           I\\            A |                B |                 C |             /D")
    print("")
    i=0
    while i<7:
        i=i+1
        print("")
        if i==4:
            print("             1--   ",end="")
        else:
            print("                   ",end="")
        if A_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if A_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if A_C:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("")
    i=0
    while i<7:
        i=i+1
        print("")
        if i==4:
            print("             2--   ",end="")
        else:
            print("                   ",end="")
        if B_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if B_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if B_C:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("")
    i=0
    while i<7:
        i=i+1
        print("")
        if i==4:
            print("             3--   ",end="")
        else:
            print("                   ",end="")
        if C_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if C_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if C_C:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("")
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def ControlT1(Acc=str):
    global A_A
    global A_B
    global A_C
    global B_A
    global B_B
    global B_C
    global C_A
    global C_B
    global C_C
    if Acc=="1":
        A_A=not(A_A)
        A_B=not(A_B)
        A_C=not(A_C)
    if Acc=="2":
        B_A=not(B_A)
        B_B=not(B_B)
        B_C=not(B_C)
    if Acc=="3":
        C_A=not(C_A)
        C_B=not(C_B)
        C_C=not(C_C)
    if (Acc=="A")or(Acc=="a"):
        A_A=not(A_A)
        B_A=not(B_A)
        C_A=not(C_A)
    if (Acc=="B")or(Acc=="b"):
        A_B=not(A_B)
        B_B=not(B_B)
        C_B=not(C_B)
    if (Acc=="C")or(Acc=="c"):
        A_C=not(A_C)
        B_C=not(B_C)
        C_C=not(C_C)
    if (Acc=="I")or(Acc=="i"):
        A_A=not(A_A)
        B_B=not(B_B)
        C_C=not(C_C)
    if (Acc=="D")or(Acc=="d"):
        A_C=not(A_C)
        B_B=not(B_B)
        C_A=not(C_A)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def CodeT1(yn=str,CC=str):
    """  si tienes o no código (1/0) y el mismo  """
    global A_A
    global A_B
    global A_C
    global B_A
    global B_B
    global B_C
    global C_A
    global C_B
    global C_C
    T=""
    if yn=="0":
        if A_A:
            T=T+("1")
        else:
            T=T+("0")
        if A_B:
            T=T+("1")
        else:
            T=T+("0")
        if A_C:
            T=T+("1")
        else:
            T=T+("0")
        if B_A:
            T=T+("1")
        else:
            T=T+("0")
        if B_B:
            T=T+("1")
        else:
            T=T+("0")
        if B_C:
            T=T+("1")
        else:
            T=T+("0")
        if C_A:
            T=T+("1")
        else:
            T=T+("0")
        if C_B:
            T=T+("1")
        else:
            T=T+("0")
        if C_C:
            T=T+("1")
        else:
            T=T+("0")
        return T
    if yn=="1":
        A_A=bool(False)
        A_B=bool(False)
        A_C=bool(False)
        B_A=bool(False)
        B_B=bool(False)
        B_C=bool(False)
        C_A=bool(False)
        C_B=bool(False)
        C_C=bool(False)
        i=0
        L=CC[i]
        if L=="1":
            A_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            A_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            A_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_C=True
        i=i+1
        print("")
        print("CÓDIGO PROCESADO")
        return None
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
################################


################################  TESELAS 2
def CinputT2(text=str): # Con carga de código
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="q")or(W=="Q")or(W=="w")or(W=="W")or(W=="r")or(W=="R")or(W=="4")or(W=="i")or(W=="d")or(W=="I")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="0")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("comando no válido")
def C2inputT2(text=str): # Sin carga de código
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="q")or(W=="Q")or(W=="w")or(W=="W")or(W=="r")or(W=="R")or(W=="4")or(W=="i")or(W=="d")or(W=="I")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("comando no válido")
def TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D):
    print("")
    print("            I\\           A |                 B |                 C |                 D |            /R")
    print("")
    i=0
    while i<6:
        i=i+1
        print("")
        if i==3:
            print("             1--   ",end="")
        else:
            print("                   ",end="")
        if A_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if A_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if A_C:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if A_D:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("")
    i=0
    while i<6:
        i=i+1
        print("")
        if i==3:
            print("             2--   ",end="")
        else:
            print("                   ",end="")
        if B_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if B_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if B_C:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if B_D:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if i==4:
            print("                  Centro: W",end="")
    print("")
    print("")
    i=0
    while i<6:
        i=i+1
        print("")
        if i==3:
            print("             3--   ",end="")
        else:
            print("                   ",end="")
        if C_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if C_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if C_C:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if C_D:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if i==4:
            print("                  Esquinas: Q",end="")
    print("")
    print("")
    i=0
    while i<6:
        i=i+1
        print("")
        if i==3:
            print("             4--   ",end="")
        else:
            print("                   ",end="")
        if D_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if D_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if D_C:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if D_D:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("")
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def ControlT2(Acc=str):
    global A_A
    global A_B
    global A_C
    global A_D
    global B_A
    global B_B
    global B_C
    global B_D
    global C_A
    global C_B
    global C_C
    global C_D
    global D_A
    global D_B
    global D_C
    global D_D
    if Acc=="1":
        A_A=not(A_A)
        A_B=not(A_B)
        A_C=not(A_C)
        A_D=not(A_D)
    if Acc=="2":
        B_A=not(B_A)
        B_B=not(B_B)
        B_C=not(B_C)
        B_D=not(B_D)
    if Acc=="3":
        C_A=not(C_A)
        C_B=not(C_B)
        C_C=not(C_C)
        C_D=not(C_D)
    if Acc=="4":
        D_A=not(D_A)
        D_B=not(D_B)
        D_C=not(D_C)
        D_D=not(D_D)
    if (Acc=="A")or(Acc=="a"):
        A_A=not(A_A)
        B_A=not(B_A)
        C_A=not(C_A)
        D_A=not(D_A)
    if (Acc=="B")or(Acc=="b"):
        A_B=not(A_B)
        B_B=not(B_B)
        C_B=not(C_B)
        D_B=not(D_B)
    if (Acc=="C")or(Acc=="c"):
        A_C=not(A_C)
        B_C=not(B_C)
        C_C=not(C_C)
        D_C=not(D_C)
    if (Acc=="D")or(Acc=="d"):
        A_D=not(A_D)
        B_D=not(B_D)
        C_D=not(C_D)
        D_D=not(D_D)
    if (Acc=="I")or(Acc=="i"):
        A_A=not(A_A)
        B_B=not(B_B)
        C_C=not(C_C)
        D_D=not(D_D)
    if (Acc=="R")or(Acc=="r"):
        A_D=not(A_D)
        B_C=not(B_C)
        C_B=not(C_B)
        D_A=not(D_A)
    if (Acc=="Q")or(Acc=="q"):
        A_A=not(A_A)
        A_D=not(A_D)
        D_A=not(D_A)
        D_D=not(D_D)
    if (Acc=="W")or(Acc=="w"):
        B_B=not(B_B)
        B_C=not(B_C)
        C_B=not(C_B)
        C_C=not(C_C)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def CodeT2(yn=str,CC=str):
    """  si tienes o no código (1/0) y el mismo  """
    global A_A
    global A_B
    global A_C
    global A_D
    global B_A
    global B_B
    global B_C
    global B_D
    global C_A
    global C_B
    global C_C
    global C_D
    global D_A
    global D_B
    global D_C
    global D_D
    T=""
    if yn=="0":
        if A_A:
            T=T+("1")
        else:
            T=T+("0")
        if A_B:
            T=T+("1")
        else:
            T=T+("0")
        if A_C:
            T=T+("1")
        else:
            T=T+("0")
        if A_D:
            T=T+("1")
        else:
            T=T+("0")
        if B_A:
            T=T+("1")
        else:
            T=T+("0")
        if B_B:
            T=T+("1")
        else:
            T=T+("0")
        if B_C:
            T=T+("1")
        else:
            T=T+("0")
        if B_D:
            T=T+("1")
        else:
            T=T+("0")
        if C_A:
            T=T+("1")
        else:
            T=T+("0")
        if C_B:
            T=T+("1")
        else:
            T=T+("0")
        if C_C:
            T=T+("1")
        else:
            T=T+("0")
        if C_D:
            T=T+("1")
        else:
            T=T+("0")
        if D_A:
            T=T+("1")
        else:
            T=T+("0")
        if D_B:
            T=T+("1")
        else:
            T=T+("0")
        if D_C:
            T=T+("1")
        else:
            T=T+("0")
        if D_D:
            T=T+("1")
        else:
            T=T+("0")
        return T
    if yn=="1":
        A_A=bool(False)
        A_B=bool(False)
        A_C=bool(False)
        A_D=bool(False)
        B_A=bool(False)
        B_B=bool(False)
        B_C=bool(False)
        B_D=bool(False)
        C_A=bool(False)
        C_B=bool(False)
        C_C=bool(False)
        C_D=bool(False)
        D_A=bool(False)
        D_B=bool(False)
        D_C=bool(False)
        D_D=bool(False)
        i=0
        L=CC[i]
        if L=="1":
            A_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            A_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            A_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            A_D=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_D=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_D=True
        i=i+1
        L=CC[i]
        if L=="1":
            D_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            D_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            D_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            D_D=True
        print("")
        print("CÓDIGO PROCESADO")
        return None
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
################################


################################  TESELAS 3
def CinputT3(text=str):
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="i")or(W=="d")or(W=="I")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="0")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("comando no válido")
def C2inputT3(text=str):
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="i")or(W=="d")or(W=="I")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("comando no válido")
def TableroT3(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C):
    global a1a
    global a1b
    global a1c
    global b1a
    global b1b
    global b1c
    global c1a
    global c1b
    global c1c
    print("")
    print("        I\\           A |                B |                 C |           /D  ")
    print("")
    i=0
    while i<7:
        i=i+1
        print("")
        if i==4:
            print("         1--   ",end="")
        else:
            print("               ",end="")
        if A_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if A_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if A_C:
            print("MMMMMMMMMMMMMMMM       ||    ",end="")
        else:
            print("._ _ _ _ _ _ _ _       ||    ",end="")
        if a1a:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if a1b:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if a1c:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("                                                                            ||")
    i=0
    while i<7:
        i=i+1
        print("")
        if i==4:
            print("         2--   ",end="")
        else:
            print("               ",end="")
        if B_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if B_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if B_C:
            print("MMMMMMMMMMMMMMMM       ||    ",end="")
        else:
            print("._ _ _ _ _ _ _ _       ||    ",end="")
        if b1a:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if b1b:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if b1c:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("                                                                            ||")
    i=0
    while i<7:
        i=i+1
        print("")
        if i==4:
            print("         3--   ",end="")
        else:
            print("               ",end="")
        if C_A:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if C_B:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if C_C:
            print("MMMMMMMMMMMMMMMM       ||    ",end="")
        else:
            print("._ _ _ _ _ _ _ _       ||    ",end="")
        if c1a:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if c1b:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
        if c1c:
            print("MMMMMMMMMMMMMMMM",end="")
        else:
            print("._ _ _ _ _ _ _ _",end="")
        print("   ",end="")
    print("")
    print("")
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def ControlT3(Acc=str):
    global A_A
    global A_B
    global A_C
    global B_A
    global B_B
    global B_C
    global C_A
    global C_B
    global C_C
    if Acc=="1":
        A_A=not(A_A)
        A_B=not(A_B)
        A_C=not(A_C)
    if Acc=="2":
        B_A=not(B_A)
        B_B=not(B_B)
        B_C=not(B_C)
    if Acc=="3":
        C_A=not(C_A)
        C_B=not(C_B)
        C_C=not(C_C)
    if (Acc=="A")or(Acc=="a"):
        A_A=not(A_A)
        B_A=not(B_A)
        C_A=not(C_A)
    if (Acc=="B")or(Acc=="b"):
        A_B=not(A_B)
        B_B=not(B_B)
        C_B=not(C_B)
    if (Acc=="C")or(Acc=="c"):
        A_C=not(A_C)
        B_C=not(B_C)
        C_C=not(C_C)
    if (Acc=="I")or(Acc=="i"):
        A_A=not(A_A)
        B_B=not(B_B)
        C_C=not(C_C)
    if (Acc=="D")or(Acc=="d"):
        A_C=not(A_C)
        B_B=not(B_B)
        C_A=not(C_A)
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def CodeT3(yn=str,CC=str):
    """  si tienes o no código (1/0) y el mismo  """
    global A_A
    global A_B
    global A_C
    global B_A
    global B_B
    global B_C
    global C_A
    global C_B
    global C_C
    global a1a
    global a1b
    global a1c
    global b1a
    global b1b
    global b1c
    global c1a
    global c1b
    global c1c
    T=""
    if yn=="0":
        if A_A:
            T=T+("1")
        else:
            T=T+("0")
        if A_B:
            T=T+("1")
        else:
            T=T+("0")
        if A_C:
            T=T+("1")
        else:
            T=T+("0")
        if B_A:
            T=T+("1")
        else:
            T=T+("0")
        if B_B:
            T=T+("1")
        else:
            T=T+("0")
        if B_C:
            T=T+("1")
        else:
            T=T+("0")
        if C_A:
            T=T+("1")
        else:
            T=T+("0")
        if C_B:
            T=T+("1")
        else:
            T=T+("0")
        if C_C:
            T=T+("1")
        else:
            T=T+("0")
        ###################################
        if a1a:
            T=T+("1")
        else:
            T=T+("0")
        if a1b:
            T=T+("1")
        else:
            T=T+("0")
        if a1c:
            T=T+("1")
        else:
            T=T+("0")
        if b1a:
            T=T+("1")
        else:
            T=T+("0")
        if b1b:
            T=T+("1")
        else:
            T=T+("0")
        if b1c:
            T=T+("1")
        else:
            T=T+("0")
        if c1a:
            T=T+("1")
        else:
            T=T+("0")
        if c1b:
            T=T+("1")
        else:
            T=T+("0")
        if c1c:
            T=T+("1")
        else:
            T=T+("0")
        return T
    if yn=="1":
        A_A=bool(False)
        A_B=bool(False)
        A_C=bool(False)
        B_A=bool(False)
        B_B=bool(False)
        B_C=bool(False)
        C_A=bool(False)
        C_B=bool(False)
        C_C=bool(False)
        a1a=bool(False)
        a1b=bool(False)
        a1c=bool(False)
        b1a=bool(False)
        b1b=bool(False)
        b1c=bool(False)
        c1a=bool(False)
        c1b=bool(False)
        c1c=bool(False)
        i=0
        L=CC[i]
        if L=="1":
            A_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            A_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            A_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            B_C=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_A=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_B=True
        i=i+1
        L=CC[i]
        if L=="1":
            C_C=True
        #############################
        i=i+1
        L=CC[i]
        if L=="1":
            a1a=True
        i=i+1
        L=CC[i]
        if L=="1":
            a1b=True
        i=i+1
        L=CC[i]
        if L=="1":
            a1c=True
        i=i+1
        L=CC[i]
        if L=="1":
            b1a=True
        i=i+1
        L=CC[i]
        if L=="1":
            b1b=True
        i=i+1
        L=CC[i]
        if L=="1":
            b1c=True
        i=i+1
        L=CC[i]
        if L=="1":
            c1a=True
        i=i+1
        L=CC[i]
        if L=="1":
            c1b=True
        i=i+1
        L=CC[i]
        if L=="1":
            c1c=True
        i=i+1
        print("")
        print("CÓDIGO PROCESADO")
        return None
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
################################

# Comienzo del juego
# Hecho por Pablo de la Fuente
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("                                                  TESELAS")
print("")
KEYsleep(1)
clear()
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("                                           ¡Comparte el juego con tus amigos!")
print("")
KEYsleep(1)
clear()
Cero=str("0") # Cero como texto
NumeroTotaldeNiveles=56
Niveles01=list(["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""])
# Niveles01 almacena temporalmente (durante le juego, antes de pasar a los txt) la info de los niveles hechos. Es necesaria ya que optimmiza
# el código, al no tener que buscar en el txt todo el tiempo. También se usa para almacenar la info sacada de los txt

# Abajo chequea el estado de los txt, si no existen los crea (try - excepts). Se crean 2 txt.
# Comprueba unos parámetros de seguridad que demuestran que no se han editado los txt (puedes probar a editar a ver si te pilla, a efectos prácticos, no sumarte niveles sin hacerlos)
FNFE=False
try:
    Archivo=open(RUTAusuario,"r")
    Archivo.close()
except FileNotFoundError:
    FNFE=True
if FNFE:
    NumUsuario=1
    NumNiveles=0
    Tes1NumNiveles=0
    Tes2NumNiveles=0
    Tes3NumNiveles=0
    Archivo=open(RUTAusuario,"w")
    Archivo.write("Us66PPCCode3451028Seguridad45322Qinijrigbkjew458763PINQwertyLaurusUsuario1N000N1000N2000N3000beg66")
    Archivo.close()
    print("Nuevo usuario.")
else:
    Archivo=open(RUTAusuario,"r")
    InfoUsuar=Archivo.read()
    Archivo.close()
    InfoUsuario=InfoUsuar[66:93]
    print(InfoUsuario)
    NumUsuario=int(InfoUsuario[7:8])
    NumNiveles=int(InfoUsuario[9:12])
    Tes1NumNiveles=int(InfoUsuario[14:17])
    Tes2NumNiveles=int(InfoUsuario[19:22])
    Tes3NumNiveles=int(InfoUsuario[24:27])
    if NumNiveles==(Tes1NumNiveles+Tes2NumNiveles+Tes3NumNiveles):
        print("Bien todo")
    else:
        print("Los archivos del juego tiene un problema, puede haber sido editado.")
        while True:
            win.Beep(300,500)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print('1) Para que se inicie bien, busca en tu ordenador ')
            print('los archivos "NNN.txt" y "UST.txt"')
            print("2) Elimina esos archivos. No los toques o podrían dar problemas.")
            print("3) Consulta con pablo.aufhause@gmail.com o diego.herasmiguez@gmail.com")
            c=KEYinput("Se para el juego, da igual que continues. >>>")
#########
FNFE=False
try:
    Niveles=open(RUTAniveles,"r")
    Niveles.close()
except FileNotFoundError:
    FNFE=True
if FNFE:
    w=0
    while w<(NumeroTotaldeNiveles):
        Niveles01[w]="0"
        w=w+1
    Niveles=open(RUTAniveles,"w")
    Niveles.write(str(NumeroTotaldeNiveles*Cero))
    Niveles.close()
    print("Nuevo usuario.")
else:
    print("Recopilando información de los niveles...")
    Niveles=open(RUTAniveles,"r")
    InfoNiveSH=Niveles.read()
    Niveles.close()
    InfoNiveles=str(InfoNiveSH)
    print(InfoNiveles)
    Nniveles1=0
    kantwa=0
    while kantwa<(NumeroTotaldeNiveles):
        L=InfoNiveles[kantwa]
        Niveles01[kantwa]=L
        if L=="1":
            Nniveles1=Nniveles1+1
        kantwa=kantwa+1
    if NumNiveles==Nniveles1:
        print("Bien todo")
    else:
        print("El archivo del juego tiene un problema, puede haber sido editado.")
        while True:
            win.Beep(300,500)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print('1) Para que se inicie bien, busca en tu ordenador ')
            print('los archivos "NNN.txt" y "UST.txt"')
            print("2) Elimina esos archivos. No los toques o podría dar problemas.")
            print("3) Consulta con pablo.aufhause@gmail.com o diego.herasmiguez@gmail.com")
            print("")
            c=KEYinput("Se para el juego, da igual que continues. >>>")
c=KEYinput("Clica primero en cualquier punto de la pantalla  ---->>> ")

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

if True: # Copyright (c) 2026 Pablo de la Fuente Sancho - Licensed under the MIT License
    clear()
    print("")
    print("")
    print("                                        TESELAS")
    print("")
    print("")
    print("                    Te vas a sumergir en la experiencia del juego TESELAS.")
    print("")
    print("")
    print("                             Correos de los creadores: ")
    print("")
    print("                pablo.aufhause@gmail.com             diego.herasmiguez@gmail.com")
    print("")
    print("")
    print("                                            INFORMACIÓN")
    print("")
    print("Para ejecutar este juego como archivo de Python es aconsejable hacerlo en Visual Studio Code, o similares." )
    print("Esta es la versión definitiva del juego TESELAS. En un principio, era un juego para jugar con cachitos de papel," )
    print("inventado por Pablo de la Fuente Sancho en torno al 2019. Una tarde de Abril de 2025 programó, por primera vez," )
    print("un tablero de TESELAS. Este programa inicial sólo tenía un tablero, que ni siquiera interpretaba victorias, solo movías." )
    print("Con el tiempo, el programa fue haciéndose mejor, hasta llegar a TESELAS 1, el primer lanzamiento oficial." )
    print("Tutorial y niveles hechos por Diego Heras y Pablo de la Fuente. Más tarde, el tablero se expandió del 3x3 original" )
    print("al 4x4. Este es TESELAS 2. El objetivo, como en el 1, es igualar las teselas con los movimientos permitidos," )
    print("que se explican en el tutorial. La siguiente versión es TESELAS 3, donde se vuelve al tablero 3x3, pero con el objetivo" )
    print("de imitar el tablero de la derecha. En todas las versiones Diego Heras ha escrito tutoriales y preparado niveles." )
    print("" )
    print("Los derechos de distribución son de Pablo de la Fuente Sancho. Siempre que no sea con fines comerciales" )
    print("se puede distribuir, contactando primero con pablo.aufhause@gmail.com o diego.herasmiguez@gmail.com." )
    print("Contactar también para obtener las versiones individualmente como archivo de Python o cualquier otra cosa." )
    print("")
    print("              Sitio web de TESELAS: https://sites.google.com/view/teselas/inicio")
    print("")
    print("Este texto es el inicio del programa. Lo verás cuando abras el juego. Para navegar por la aplicación, " )
    print('ahora viene un tutorial. Puedes acceder a esta y más información desde el menú general en "Información"' )
    KEYsleep(1)
    print("" )
    print("                                      NAVEGACIÓN POR EL JUEGO" )
    print("" )
    print("Este programa consta, además del tablero, de un TUTORIAL, de niveles precargados, de un modo desafío para retar" )
    print("a amigos y de un generador de posiciones aleatorias. Para cargar una posición, se copia el código en binario" )
    print("y se pega donde se quiera cargar. La navegación es muy intuitiva, con un índice en el que se selecciona por número." )
    print("Al salir de una sección, se vuelve a este índice-menú, común a todas las versiones. Ahí eliges a qué TESELAS jugar" )
    print("y gestionas tu usuario, la cuenta en la que se guarda tu información como jugador. Dentro de un juego, este es el menú:")
    print("")
    print("       EXPLICACIÓN DEL MENÚ:" )
    print("" )
    print("             1) TUTORIAL: Explica cómo jugar." )
    print("" )
    print("             2) NIVELES: Aquí están los códigos de los niveles." )
    print("" )
    print("             3) TABLERO LIBRE: Aquí no hay victoria, sólo el tablero interactivo." )
    print("                               Puedes cargar aquí códigos." )
    print("" )
    print("             4) MODO DESAFÍO: Cargas un código y ganas cuando resuelves el mosaico." )
    print("" )
    print("             5) GENERADOR DE CÓDIGOS: Genera un código aleatorio que puedes copiar." )
    print("" )
    print("             6) SALIR: Te permite sair de una versión determinada de TESELAS e ir" )
    print("                       al menú para elegir versión." )
    print("" )
    print("Cualquier orden tiene una longitud de 1 caracter (una letra o un número). Para hacerla, escribes" )
    print("el caracter de la orden y pulsas Enter en el teclado del ordenador. Esta es una versión de consola para " )
    print("ordenador, pero en un futuro habrá nuevos lanzamientos con interfaces y nuevas versiones. Para tener" )
    print("las últimas versiones escribe a pablo.aufhause@gmail.com o diego.herasmiguez@gmail.com que son" )
    print("los contactos de los creadores. En un plazo de 1 semana prometemos haber contestado. ¡O antes!")
    print("Es importante que para que se guarde la información de lo que has hecho guardes información, en el apartado")
    print("de usuario del menú de versiones.")
    print("")
    print("Siempre en tu pantalla aparecerán las indicaciones de lo que puedes hacer; si te despistas, lee. Encima de")
    print("los tableros te aparecen el número de movimientos y el código del tablero en ese momento. Esos códigos,")
    print("en binario, guardan información de las teselas del tablero. Los niveles están en forma de código. Explicado antes,")
    print("para hacer un nivel copias (Ctrl+C) un código y lo pegas (Ctrl+V) donde quieras. Puedes pegarlo directamente en")
    print("el modo desafío, o entrar en tablero libre y elegir cargar un código (0). Para que un nivel se te marque como hecho")
    print("lo tienes que haber resuelto en el modo desafío. IMPORTANTE: que no se te olvide guardar información del usuario")
    print("antes de salir del juego, en el menú principal. En el tablero libre tienes un tablero a tu disposición, para")
    print("que pruebes movimientos o lo que quieras. Como siempre en los tableros, tienes el código de tu posición actual")
    print("en la esquina superior derecha, para que lo guardes para jugar en otro momento o lo compartas para retar a tus amigos.")
    print("")
    print("                                    ¡Ahora a jugar!")
    KEYsleep(1)
    print("")
    c=KEYinput("                              Enter para comenzar >>>  ")
while True: # BUCLE JUEGO
    TOTAL="dentro"
    if True: # MENÚ DE VERSIONES
        clear()
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("        Usuario ",NumUsuario)
        print("")
        print("                                                MENÚ GENERAL")
        print("")
        print("")
        print("                                Escribe el número de la versión que quieras.")
        print("")
        print("                       --   1) TESELAS 1    Juego original 3x3.")
        print("")
        print("                       --   2) TESELAS 2    Extensión a 4x4, con nuevos movimientos.")
        print("")
        print("                       --   3) TESELAS 3    Tienes que imitar lo del tablero de la derecha.")
        print("")
        print("                       --   4) USUARIO      Ajustes de cuenta de usuario.")
        print("")
        print("                       --   5) INFORMACIÓN  Lo que quieras saber de TESELAS.")
        print("")
        print("")
        print("                          Empieza por la primera versión y ve avanzando, es mejor así para aprender.")
        print("")
        print("")
        KEYsleep(0.5)
    Juego=str(KEYinput("                          Escribe el número del juego >>>  "))
    if Juego=="1":
        A_A=bool(False)
        A_B=bool(False)
        A_C=bool(False)
        B_A=bool(False)
        B_B=bool(False)
        B_C=bool(False)
        C_A=bool(False)
        C_B=bool(False)
        C_C=bool(False)
        ###############################################################
        clear()
        print("")
        print("                        JUEGO DE LAS TESELAS 1")
        print("")
        print("")
        print("       El juego original. En un tablero 3x3 con el objetivo")
        print("       de igualar todas las teselas. Sienta las bases de las futuras versiones.")
        print("")
        KEYsleep(0.5)
        c=KEYinput("                         Enter para comenzar  >>>  ")
        while TOTAL=="dentro":
            clear()
            print("")
            print("                     JUEGO DE LAS TESELAS 1")
            print("")
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            print("")
            TableroT1(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            KEYsleep(1)
            clear()
            print("")
            print("                                   MENÚ")
            print("")
            print("          1) Tutorial")
            print("")
            print("          2) Niveles")
            print("")
            print("          3) Tablero libre")
            print("")
            print("          4) Modo desafío")
            print("")
            print("          5) Generar código aleatorio")
            print("")
            print("          6) Salir de TESELAS 1")
            print("")
            print("")
            KEYsleep(0.5)
            Ellec=str(KEYinput("                                            Tu elección: "))
            KEYsleep(0.5)
            if Ellec=="1": # tutorial
                A_A=bool(False)
                A_B=bool(False)
                A_C=bool(False)
                B_A=bool(False)
                B_B=bool(False)
                B_C=bool(False)
                C_A=bool(False)
                C_B=bool(False)
                C_C=bool(False)
                clear()
                print("")
                print("                                              TUTORIAL")
                print("")
                print("                         ¡Bienvenido al tutorial de Teselas! Veamos cómo se juega:")
                print("")
                KEYsleep(1)
                clear()
                print("     ESTE ES EL TABLERO, CON 3 FILAS, 3 COLUMNAS Y 2 DIAGONALES, CON ALGUNAS TESELAS DE UN TIPO Y OTRAS DE OTRO:")
                TableroT1(A_A,not(A_B),A_C,not(B_A),not(B_B),B_C,C_A,C_B,not(C_C)) # MUESTRA EL TABLERO CON UNA DETERMINADA CONFIGURACIÓN
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                print("")
                TableroT1(A_A,not(A_B),A_C,not(B_A),not(B_B),B_C,C_A,C_B,not(C_C))
                print("")
                print("Como puedes ver, hay una combinación aleatoria de teselas de diferentes colores, unas teselas son blancas y otras negras. Tu objetivo es que todas ellas acaben siendo de un mismo color, da igual cual.")
                print("Veamos como hacerlo.")
                print("")
                print("Puedes mover columnas (A, B, C), filas (1, 2, 3) o las dos diagonales del tablero (I, D). Alrededor del tablero están las indicaciones. Cuando eliges hacer un movimiento, cambias el estado de las teselas de toda la línea, entre claro y oscuro.")
                print("Afecta a todas a la vez. Es con estos movimientos con los que se tiene que llegar a la posición ganadora.")
                print("Es importante que, cada vez que se quiera cambiar alguna línea, se ponga solo un caracter y se de al Enter, es decir, solo un movimiento cada vez que se pulse Enter.")
                print("")
                print("     ¡Veamos un ejemplo sencillo!")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                print("")
                print("             EJEMPLO")
                print("")
                TableroT1(not(A_A),A_B,not(A_C),B_A,not(B_B),B_C,not(C_A),C_B,not(C_C))
                print("")
                print("Vemos el tablero con las teselas de forma aleatoria, debemos conseguir que sean todas blancas o negras.")
                print("Si pulsamos, por ejemplo, 1, y le damos al Enter, se verá que las teselas de la primera fila se han invertido:")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                print("")
                TableroT1(A_A,not(A_B),A_C,B_A,not(B_B),B_C,not(C_A),C_B,not(C_C))
                print("")
                print("Si pulsamos ahora 3 y le damos al Enter, se cambiarán todas las teselas de la tercera fila.")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT1(A_A,not(A_B),A_C,B_A,not(B_B),B_C,C_A,not(C_B),C_C)
                print("")
                print("Ya lo tenemos, si pulsamos ahora B (se ve la indicación encima de esa columna), tendremos todo el tablero de un color, habríamos ganado.")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                print("")
                print("Hubieramos ganado, ya que tenemos todo el tablero de un mismo color.")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                print('Si hubieramos querido mover una diagonal, habríamos escrito "I" y dado al Enter. Este sería el efecto:')
                print("")
                TableroT1(not(A_A),A_B,A_C,B_A,not(B_B),B_C,C_A,C_B,not(C_C))
                print("")
                print("Se puede ver que se ha volteado esa diagonal.")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                print("")
                print("Ya has visto como funciona un poco el juego, ya le irás cogiendo el truco.")
                print("Al principio, puede parecer un poco confuso, por ello, se recomienda usar la funcionalidad TABLERO LIBRE para probar movimientos y demás.")
                print("")
                print("Ten cuidado, es fácil frustarse si ves que algo no sale, pero piensa que siempre puedes cargar otro código para enfrentarte a otro reto.")
                print("")
                print('Por último, se recomienda "memorizar" algunas posiciones a partir de las cuales se puede ganar, los llamados ATAJOS. Así, en vez de tener ')
                print("que visualizar la victoria, puedes ver una posición que ya conoces, y desde ahí resolverlo. No es necesario estudiar atajos, con un poco de")
                print("práctica verás que hay posiciones que ya has jugado, y te sonará cómo resolverlas. Para jugadores avanzados, son muy prácticos.")
                print("Conforme juegues, te darás cuenta de ellos, ¡así que trata de recordarlos para futuras partidas!")
                print("")
                print("")
                print("Y hasta aquí el tutorial del juego, desde el menú podrás acceder a niveles ya cargados, además del modo TABLERO LIBRE y de un generador de códigos aleatorio. Los códigos deberán cargarse en el Modo Desafío o en el Tablero Libre.")
                print("Suerte y ¡DISFRUTA!")
                print("")
                KEYsleep(4)
                print("")
                cont=str(KEYinput("   Para ver un tutorial más en detalle, pulsa la letra K, otra cosa para acabar con los tutoriales.    >>>"))
                if (cont=="K")or(cont=="k"):
                    clear()
                    print("")
                    print("                                              TUTORIAL AVANZADO")
                    print("")
                    print("Este es un juego muy entretenido, inventado por Pablo de la Fuente Sancho en torno al 2019. Consiste en poner todas las teselas del mosaico de 3 por 3 de un mismo tipo, claras u oscuras, da igual.  Se parte de una configuración inicial (obviamente no todas las teselas estarás igual) para intentar llegar a tener todas las teselas iguales con los movimientos permitidos, que ahora se explicarán.")
                    print("")
                    KEYsleep(6)
                    print("     ESTE ES EL TABLERO, CON ALGUNAS TESELAS DE UN TIPO Y OTRAS DE OTRO:        ")
                    TableroT1(A_A,not(A_B),A_C,not(B_A),not(B_B),B_C,C_A,C_B,not(C_C))
                    KEYsleep(5)
                    clear()
                    print("")
                    print("  ::::::::::::::::::::::::::::::::::::::::::::: A PARTIR DE AQUÍ LEE :::::::::::::::::::::::::::::::::::::::")
                    print("")
                    print("Este es un juego muy entretenido, inventado por Pablo de la Fuente Sancho en torno al 2019. Consiste en poner todas las teselas del mosaico de 3 por 3 de un mismo tipo, claras u oscuras, da igual. Se parte de una configuración inicial (obviamente no todas las teselas estarás igual) para intentar llegar a tener todas las teselas iguales con los movimientos permitidos, que ahora se explicarán.")
                    print("Ahora ya te has familiarizado con el tablero; vamos a los movimientos.")
                    print("  Puedes mover columnas (verticales), filas (horizontales) o diagonales (sólo las dos que van de esquina a esquina). Cuando eliges hacer un movimiento, cambias el estado de las teselas a las que afecta, entre claro y oscuro. Afecta a todas a la vez. Es con estos movimientos con los que se tiene que llegar a la posición ganadora.")
                    print("")
                    print("Para jugar en el ordenador, escribes en la terminal el comando del movimiento. Letras A, B y C para las columnas; del 1 al 3 para las filas; I o D para las diagonales que parten desde la esquina superior izquierda o derecha, respectivamente. No te preocupes, que siempre aparecerán las indicaciones en el tablero.")
                    print("     ¡Veamos un ejemplo!")
                    print("")
                    KEYsleep(14)
                    TableroT1(not(A_A),A_B,not(A_C),B_A,not(B_B),B_C,not(C_A),C_B,not(C_C))
                    print("")
                    print("Vemos que no son todas las teselas iguales. ¿Cómo ponerlas de la misma cara? En este caso es sencillo, ya verás que después de haber jugado un poco te parece más que evidente.")
                    print("Lo primero sería voltear dos laterales. Como en este caso el tablero es simétrico, da igual que sean las columnas o las filas. En este ejemplo, se darán la vuelta las filas. Mandamos la instrucción de darle la vuelta a una fila de las que interesan, por ejemplo a la 1. Escribimos el 1 y damos al Enter.")
                    print("")
                    TableroT1(A_A,not(A_B),A_C,B_A,not(B_B),B_C,not(C_A),C_B,not(C_C))
                    print("")
                    print("Se puede ver que las de la fila 1 se han invertido. También podríamos haber hecho lo mismo (por lo de la simetría) con una columna lateral, poniendo A en ese caso, por la columna A, o igualmente la C. Ahora hacemos lo mismo con la otra fila lateral, continuando con el ejemplo.")
                    print("")
                    TableroT1(A_A,not(A_B),A_C,B_A,not(B_B),B_C,C_A,not(C_B),C_C)
                    print("")
                    print("     Y pasa lo mismo que con la otra, se invierten las teselas. ¿Qué haríamos ahora?")
                    print("Muy fácil. Tenemos la columna central de un tipo, y todo lo demás del otro. Basta con dar la vuelta a esa columna. Para hacerlo, como cada vez que queremos hacer un movimiento, escribimos el comando (en este caso, por la columna, la letra B) y pulsamos Enter.")
                    print("")
                    print("          ¡ MAGIA !")
                    print("")
                    TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    print("Ya está terminado, todas están de un tipo. RECAPITULAMOS: no todos los movimientos son directos para dar la vuelta a alguna y ya. La maryoría de las veces (casi todas, y más en los un poco más difíciles) consiste en hacer movimientos que lo preparen. Hay que tener visión espacial para prever movimientos. Para el futuro, con configuraciones iniciales más complicadas, verás que es muy útil saber 'atajos'. Un atajo es una posición a partir de la cual sabes solucionarlo. A veces puede ser más sencillo de ver llegar a un atajo que a la solución final. Un ejemplo de atajo sería con una sola tesela dada la vuelta en el centro. Moviendo fila y columna centrales se llega a la configuración del ejemplo, ¿te acuerdas de lo fácil que era solucionarlo? Como ves, un atajo es simplemente una posición que sabes solucionar.")
                    print("")
                    print("Al principio puede parecer difícil, desafiante o casi imposible. Puede que no sepas por dónde empezar. Si te pasa algo de esto, ¡mueve al azar! Acabarás llegando a una posición más fácil, o a un atajo. Con práctica dominarás el juego, y puedes competir con alguien para ver quién necesita menos movimientos.")
                    print("En el menú tienes algunos niveles precargados, están muy bien para practicar. También puedes crear los tuyos propios con el tablero libre, copiando el código que aparece.")
                    print("")
                    print("                 :::( SUBE PARA LEER ^^^ ):::")
                    KEYsleep(5)
                    print("")
                    c=KEYinput("                    PARA TERMINAR EL TUTORIAL, PULSA ENTER                       >>>      ")
                    KEYsleep(0.5)
                    clear()
            elif Ellec=="2": # niveles
                clear()
                print("")
                print("                              NIVELES")
                print("")
                print("            Copia el código del nivel (en binario) y cárgalo donde desees.")
                print("            Puedes cargarlo en el tablero libre o en el modo desafío.")
                print("")
                print("        1)  101010010     ",end="")
                if ((Niveles01[0])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        2)  101010101     ",end="")
                if ((Niveles01[1])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("hecho")
                else:
                    print(" ")
                print("        3)  110111011     ",end="")
                if ((Niveles01[2])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        4)  101011111     ",end="")
                if ((Niveles01[3])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        5)  111100101     ",end="")
                if ((Niveles01[4])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        6)  101111010     ",end="")
                if ((Niveles01[5])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        7)  100101110     ",end="")
                if ((Niveles01[6])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        8)  001011110     ",end="")
                if ((Niveles01[7])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        9)  010110000     ",end="")
                if ((Niveles01[8])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       10)  010100000     ",end="")
                if ((Niveles01[9])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       11)  110010011     ",end="")
                if ((Niveles01[10])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       12)  001110110     ",end="")
                if ((Niveles01[11])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       13)  101100111     ",end="")
                if ((Niveles01[12])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       14)  010101101     ",end="")
                if ((Niveles01[13])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       15)  111110010     ",end="")
                if ((Niveles01[14])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       16)  100011011     ",end="")
                if ((Niveles01[15])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       17)  010000101     ",end="")
                if ((Niveles01[16])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       18)  110011110     ",end="")
                if ((Niveles01[17])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.3)
                c=KEYinput("          Enter para salir   >>>")
                KEYsleep(0.5)
            elif Ellec=="3": # tablero libre
                exit=0
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          TABLERO LIBRE       ||  ",mov," movimientos  ||  Código: ",CodeT1("0"))
                    print("")
                    print("Con esta función, tienes un tablero a tu disposición, para que muevas teselas o carges códigos.")
                    print("Para cargar un código, escribe el número 0. Para salir escribe E.")
                    print("")
                    TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(CinputT1("            >>>  "))
                    mov=mov+1
                    ControlT1(JJJ) # Ejecuta la acción correspondiente.
                    print("")
                    print("                Has movido ",JJJ)
                    KEYsleep(0.4)
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("SALIENDO DEL TABLERO LIBRE")
                        print("")
                        KEYsleep(1)
                    if JJJ=="0":
                        mov=0
                        clear()
                        print("")
                        print("")
                        print("      CARGAR UN CÓDIGO DE TABLERO       ||  Tu código actual: ",CodeT1("0"))
                        print("")
                        print("De esta manera puedes guardar y cargar la información del tablero. Para guardarla, copia el código que aparece")
                        print("al lado del número de movimientos en el tablero libre. Esto te permite desafiar a tus amigos a ver")
                        print("si resuelven el puzle. El código representa el estado del tablero, reiniciándose el número de movimientos si cargas un código.")
                        print("   El código está sólo formado por los dígitos binarios, no copies espacios, puntos, comas o cualquier otra cosa, o no se interpretará correctamente.")
                        print("   (Para cancelar, escribe la letra E)")
                        print("")
                        KEYsleep(0.5)
                        cunt=0
                        while cunt==0:
                            Www=str(KEYinput("         Escribe tu código (9 cifras)    >>>   "))
                            if (Www=="e")or(Www=="E")or((len(Www))==9):
                                cunt=1
                                Kods=str(Www)
                            else:
                                print("Parece que el código que has puesto tiene un problema, inténtalo de nuevo.")
                        if (Kods=="E")or(Kods=="e"):
                            print("Se cancela la carga de código")
                        else:
                            CodeT1("1",Kods)
                        KEYsleep(0.5)
            elif Ellec=="4": # modo desafío
                exit=0
                clear()
                print("")
                print("")
                print("      CARGAR UN CÓDIGO PARA EL MODO DESAFÍO            (Para cancelar, la letra E)")
                print("")
                print("Puedes cargar el código que quieras o copiar (Ctrl+C) y pegar (Ctrl+V)")
                print("de los códigos de niveles de abajo.   1- Copia el código. 2- Pégalo.")
                print("COPIA SÓLO LOS NÚMEROS Truco: doble click sobre el código, cuando está en blanco, Ctrl+C.")
                print("")
                print("        1)  101010010     ",end="")
                if ((Niveles01[0])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        2)  101010101     ",end="")
                if ((Niveles01[1])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("hecho")
                else:
                    print(" ")
                print("        3)  110111011     ",end="")
                if ((Niveles01[2])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        4)  101011111     ",end="")
                if ((Niveles01[3])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        5)  111100101     ",end="")
                if ((Niveles01[4])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        6)  101111010     ",end="")
                if ((Niveles01[5])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        7)  100101110     ",end="")
                if ((Niveles01[6])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        8)  001011110     ",end="")
                if ((Niveles01[7])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        9)  010110000     ",end="")
                if ((Niveles01[8])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       10)  010100000     ",end="")
                if ((Niveles01[9])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       11)  110010011     ",end="")
                if ((Niveles01[10])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       12)  001110110     ",end="")
                if ((Niveles01[11])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       13)  101100111     ",end="")
                if ((Niveles01[12])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       14)  010101101     ",end="")
                if ((Niveles01[13])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       15)  111110010     ",end="")
                if ((Niveles01[14])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       16)  100011011     ",end="")
                if ((Niveles01[15])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       17)  010000101     ",end="")
                if ((Niveles01[16])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       18)  110011110     ",end="")
                if ((Niveles01[17])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.5)
                cunt=0
                while cunt==0:
                    Www=str(KEYinput("         Escribe tu código (9 cifras)    >>>   "))
                    if (Www=="e")or(Www=="E")or((len(Www))==9):
                        cunt=1
                        Kods=str(Www)
                    else:
                        print("Parece que el código que has puesto tiene un problema, inténtalo de nuevo.")
                if (Kods=="E")or(Kods=="e"):
                    print("Se cancela la carga de código")
                    exit=1
                else:
                    CodeT1("1",Kods)
                    Trew=CodeT1("0")
                KEYsleep(0.5)
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          MODO DESAFÍO       ||  ",mov," movimientos  ||  Código: ",CodeT1("0"))
                    print("")
                    print("Intenta llegar a tener todas las teselas de un tipo. Para salir la letra E.")
                    print("")
                    TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(C2inputT1("            >>>  "))
                    mov=mov+1
                    ControlT1(JJJ)
                    print("")
                    print("                Has movido ",JJJ)
                    KEYsleep(0.4)
                    if ((A_A)and(A_B)and(A_C)and(B_A)and(B_B)and(B_C)and(C_A)and(C_B)and(C_C))or((not(A_A))and(not(A_B))and(not(A_C))and(not(B_A))and(not(B_B))and(not(B_C))and(not(C_A))and(not(C_B))and(not(C_C))):
                        clear()
                        print("")
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        KEYsleep(0.2)
                        print("")
                        print("                ¡¡¡ Has ganado !!!")
                        print("")
                        KEYsleep(0.5)
                        clear()
                        if Trew=="101010010":
                            Niveles01[0]="1"
                        if Trew=="101010101":
                            Niveles01[1]="1"
                        if Trew=="110111011":
                            Niveles01[2]="1"
                        if Trew=="101011111":
                            Niveles01[3]="1"
                        if Trew=="111100101":
                            Niveles01[4]="1"
                        if Trew=="101111010":
                            Niveles01[5]="1"
                        if Trew=="100101110":
                            Niveles01[6]="1"
                        if Trew=="001011110":
                            Niveles01[7]="1"
                        if Trew=="010110000":
                            Niveles01[8]="1"
                        if Trew=="010100000":
                            Niveles01[9]="1"
                        if Trew=="110010011":
                            Niveles01[10]="1"
                        if Trew=="001110110":
                            Niveles01[11]="1"
                        if Trew=="101100111":
                            Niveles01[12]="1"
                        if Trew=="010101101":
                            Niveles01[13]="1"
                        if Trew=="111110010":
                            Niveles01[14]="1"
                        if Trew=="100011011":
                            Niveles01[15]="1"
                        if Trew=="010000101":
                            Niveles01[16]="1"
                        if Trew=="110011110":
                            Niveles01[17]="1"
                        print("")
                        print("                 VICTORIA")
                        print("")
                        print("        Has conseguido poner igual todas las teselas, usando ",mov," movimientos.")
                        print("        Código original: ",Trew)
                        print("")
                        TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                        KEYsleep(1)
                        c=KEYinput("                Enter para continuar    >>>   ")
                        exit=1
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("SALIENDO DEL MODO DESAFÍO")
                        print("")
                        KEYsleep(1)
                Guardar() #TO DO
            elif Ellec=="5": # generar código aleatorio
                clear()
                print("")
                print("          CÓDIGO ALEATORIO")
                print("")
                bb=str("")
                u=0
                while u<9:
                    sup=str(random.randint(0,1))
                    bb=bb+sup
                    u=u+1
                print("Tu código de tablero: ",bb,"     (es posible que sea muy difícil)")
                print("")
                KEYsleep(0.5)
                c=KEYinput("   Copia el código, luego pulsa Enter.          >>>")
            elif Ellec=="6": # salida
                TOTAL="fuera"
                clear()
                print("")
                print("")
                print("     Se sale de TESELAS 1")
                KEYsleep(1)
            else:
                clear()
                print("")
                print("       LO QUE HAS HECHO NO ES UNA ELECCIÓN")
                KEYsleep(1)
        ################################################################################
        ################################################################################
    elif Juego=="2":
        A_A=bool(False)
        A_B=bool(False)
        A_C=bool(False)
        A_D=bool(False)
        B_A=bool(False)
        B_B=bool(False)
        B_C=bool(False)
        B_D=bool(False)
        C_A=bool(False)
        C_B=bool(False)
        C_C=bool(False)
        C_D=bool(False)
        D_A=bool(False)
        D_B=bool(False)
        D_C=bool(False)
        D_D=bool(False)
        clear()
        print("")
        print("                        JUEGO DE LAS TESELAS 2")
        print("")
        print("")
        print("       Actualización del juego. En un tablero 4x4 con el objetivo de igualar ")
        print("       todas las teselas. La expansión de TESELAS 1. Nuevos movimientos.")
        print("")
        KEYsleep(0.5)
        c=KEYinput("                         Enter para comenzar  >>>  ")
        while TOTAL=="dentro":
            clear()
            print("")
            print("                     JUEGO DE LAS TESELAS 2")
            print("")
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            print("")
            TableroT2(A_A,not(A_B),A_C,A_D,not(B_A),not(B_B),B_C,B_D,C_A,C_B,not(C_C),C_D,not(D_A),D_B,D_C,not(D_D))
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            KEYsleep(0.5)
            clear()
            print("")
            print("                                     MENÚ")
            print("")
            print("")
            print("          1) Tutorial")
            print("")
            print("          2) Niveles")
            print("")
            print("          3) Tablero libre")
            print("")
            print("          4) Modo desafío")
            print("")
            print("          5) Generar código aleatorio")
            print("")
            print("          6) Salir de TESELAS 2")
            print("")
            print("")
            KEYsleep(0.5)
            Ellec=str(KEYinput("                                            Tu elección: "))
            KEYsleep(0.5)
            if Ellec=="1": # tutorial
                A_A=bool(False)
                A_B=bool(False)
                A_C=bool(False)
                A_D=bool(False)
                B_A=bool(False)
                B_B=bool(False)
                B_C=bool(False)
                B_D=bool(False)
                C_A=bool(False)
                C_B=bool(False)
                C_C=bool(False)
                C_D=bool(False)
                D_A=bool(False)
                D_B=bool(False)
                D_C=bool(False)
                D_D=bool(False)
                clear()
                print("")
                print("                            TUTORIAL DE TESELAS 2")
                print("")
                print("     ESTE ES EL TABLERO, CON 4 FILAS, 4 COLUMNAS Y 2 DIAGONALES, CON ALGUNAS TESELAS DE UN TIPO Y OTRAS DE OTRO:")
                TableroT2(A_A,A_B,not(A_C),not(A_D),not(B_A),not(B_B),B_C,B_D,C_A,C_B,not(C_C),not(C_D),not(D_A),not(D_B),D_C,D_D)
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                print("Como puedes ver, hay una combinación aleatoria de teselas de diferentes colores, unas teselas son blancas y otras negras. Tu objetivo es que todas ellas acaben siendo de un mismo color, da igual cual.")
                print("Veamos como hacerlo.")
                print("")
                print("Puedes mover columnas (A, B, C, D), filas (1, 2, 3, 4), las dos diagonales del tablero (I, R), las cuatro esquinas (Q) y las cuatro teselas del centro (W). Alrededor del tablero están las indicaciones. Cuando eliges hacer un movimiento, cambias el estado de las teselas de toda la línea, entre claro y oscuro.")
                print("Afecta a todas a la vez. Es con estos movimientos con los que se tiene que llegar a la posición ganadora.")
                print("Es importante que, cada vez que se quiera cambiar alguna línea, se ponga solo un caracter y se de al Enter, es decir, solo un movimiento cada vez que se pulse Enter.")
                print("")
                print("     ¡Veamos un ejemplo sencillo!")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                print("")
                print("             EJEMPLO")
                print("")
                TableroT2(A_A,A_B,not(A_C),not(A_D),not(B_A),not(B_B),B_C,B_D,C_A,C_B,not(C_C),not(C_D),not(D_A),not(D_B),D_C,D_D)
                print("")
                print("Vemos el tablero con las teselas de forma aleatoria, debemos conseguir que sean todas blancas o negras.")
                print("Si pulsamos, por ejemplo, 1, y le damos al Enter, se verá que las teselas de la primera fila se han invertido:")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT2(not(A_A),not(A_B),A_C,A_D,not(B_A),not(B_B),B_C,B_D,C_A,C_B,not(C_C),not(C_D),not(D_A),not(D_B),D_C,D_D)
                print("")
                print("Se han invertido los colores de la primera fila. Como siguiente paso, le daremos al 3 para invertir la tercera fila")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT2(not(A_A),not(A_B),A_C,A_D,not(B_A),not(B_B),B_C,B_D,not(C_A),not(C_B),C_C,C_D,not(D_A),not(D_B),D_C,D_D)
                print("")
                print("Genial, ya lo tenemos sencillo. Vamos a invertir la tercera columna dándole a la C")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT2(not(A_A),not(A_B),not(A_C),A_D,not(B_A),not(B_B),not(B_C),B_D,not(C_A),not(C_B),not(C_C),C_D,not(D_A),not(D_B),not(D_C),D_D)
                print("")
                print("Ya solo nos queda invertir la columna D, así que le damos a la D y veremos el resultado")
                print("")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT2(not(A_A),not(A_B),not(A_C),not(A_D),not(B_A),not(B_B),not(B_C),not(B_D),not(C_A),not(C_B),not(C_C),not(C_D),not(D_A),not(D_B),not(D_C),not(D_D))
                print("")
                print("¡Victoria!")
                print("Ya has visto como funciona un poco el juego, ya le irás cogiendo el truco.")
                print("Al principio, puede parecer un poco confuso, por ello, se recomienda usar la funcionalidad TABLERO LIBRE para probar movimientos y demás.")
                print("")
                print("Ten cuidado, es fácil frustarse si ves que algo no sale, pero piensa que siempre puedes cargar otro código para enfrentarte a otro reto.")
                print("")
                print('Por último, se recomienda "memorizar" algunas posiciones a partir de las cuales se puede ganar, los llamados ATAJOS. Así, en vez de tener ')
                print("que visualizar la victoria, puedes ver una posición que ya conoces, y desde ahí resolverlo. No es necesario estudiar atajos, con un poco de")
                print("práctica verás que hay posiciones que ya has jugado, y te sonará cómo resolverlas. Para jugadores avanzados, son muy prácticos.")
                print("Conforme juegues, te darás cuenta de ellos, ¡así que trata de recordarlos para futuras partidas!")
                print("")
                print("")
                print("Y hasta aquí el tutorial del juego, desde el menú podrás acceder a niveles ya cargados, además del modo TABLERO LIBRE y de un generador de códigos aleatorios. Los códigos deberán cargarse en el Modo Desafío o en el TableroT1 Libre.")
                print("Suerte y ¡DISFRUTA!")
                print("")
                print("")
                c=KEYinput("                        ENTER PARA TERMINAR EL TUTORIAL  >>>")
                KEYsleep(0.5)
                clear()
            elif Ellec=="2": # niveles
                clear()
                print("")
                print("          NIVELES")
                print("")
                print("     Copia el código del nivel (en binario) y cárgalo donde desees.")
                print("     Puedes cargarlo en el tablero libre o en el modo desafío.")
                print("")
                print("        1)  1001011001101001     ",end="")
                if ((Niveles01[18])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        2)  0001010000101000     ",end="")
                if ((Niveles01[19])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("hecho")
                else:
                    print(" ")
                print("        3)  0000100110010000     ",end="")
                if ((Niveles01[20])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        4)  1011001011011011     ",end="")
                if ((Niveles01[21])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        5)  0011111110011010     ",end="")
                if ((Niveles01[22])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        6)  1010000010010011     ",end="")
                if ((Niveles01[23])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        7)  1101100011100100     ",end="")
                if ((Niveles01[24])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        8)  1101111001110100     ",end="")
                if ((Niveles01[25])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        9)  0010100000010100     ",end="")
                if ((Niveles01[26])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       10)  1010100100000011     ",end="")
                if ((Niveles01[27])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       11)  0101101001010101     ",end="")
                if ((Niveles01[28])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       12)  0111010011011110     ",end="")
                if ((Niveles01[29])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       13)  1011111001111101     ",end="")
                if ((Niveles01[30])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       14)  0101110011001010     ",end="")
                if ((Niveles01[31])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       15)  1011111010000010     ",end="")
                if ((Niveles01[32])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       16)  1100100111110101     ",end="")
                if ((Niveles01[33])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       17)  0011100111110101     ",end="")
                if ((Niveles01[34])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       18)  0010100011101011     ",end="")
                if ((Niveles01[35])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.3)
                c=KEYinput("          Enter para salir   >>>")
                KEYsleep(0.5)
            elif Ellec=="3": # tablero libre
                exit=0
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          TABLERO LIBRE       ||  ",mov," movimientos  ||  Código: ",CodeT2("0"))
                    print("")
                    print("Con esta función, tienes un tablero a tu disposición, para que muevas teselas o carges códigos.")
                    print("Para cargar un código, escribe el número 0. Para salir escribe E.")
                    print("")
                    TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D)
                    JJJ=str(CinputT2("            >>>  "))
                    mov=mov+1
                    ControlT2(JJJ)
                    print("")
                    print("                Has movido ",JJJ)
                    KEYsleep(0.4)
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("SALIENDO DEL TABLERO LIBRE")
                        print("")
                        KEYsleep(1)
                    if JJJ=="0":
                        mov=0
                        clear()
                        print("")
                        print("")
                        print("      CARGAR UN CÓDIGO DE TABLERO       ||  Tu código actual: ",CodeT2("0"))
                        print("")
                        print("De esta manera puedes guardar y cargar la información del tablero. Para guardarla, copia el código que aparece al lado")
                        print("del número de movimientos en el tablero libre. Esto te permite desafiar a tus amigos a ver si resuelven el puzle.")
                        print("El código representa el estado del tablero, reiniciándose el número de movimientos si cargas un código.")
                        print("El código está sólo formado por los dígitos binarios, no copies espacios, puntos, comas o cualquier otra cosa, o no se interpretará correctamente.")
                        print("        (Para cancelar la carga de código escribe la letra E)")
                        print("")
                        KEYsleep(0.5)
                        cunt=0
                        while cunt==0:
                            Www=str(KEYinput("         Escribe tu código (16 cifras)    >>>   "))
                            if (Www=="e")or(Www=="E")or((len(Www))==16):
                                cunt=1
                                Kods=str(Www)
                            else:
                                print("Parece que el código que has puesto tiene un problema, inténtalo de nuevo.")
                        if (Kods=="E")or(Kods=="e"):
                            print("Se cancela la carga de código")
                        else:
                            CodeT2("1",Kods)
                        KEYsleep(0.5)
            elif Ellec=="4": # modo desafío
                exit=0
                clear()
                print("")
                print("")
                print("      CARGAR UN CÓDIGO PARA EL MODO DESAFÍO            (Para cancelar, la letra E)")
                print("")
                print("Puedes cargar el código que quieras o copiar (Ctrl+C) y pegar (Ctrl+V)")
                print("de los códigos de niveles de abajo.   1- Copia el código. 2- Pégalo.")
                print("COPIA SÓLO LOS NÚMEROS Truco: doble click sobre el código, cuando está en blanco, Ctrl+C.")
                print("")
                print("        1)  1001011001101001     ",end="")
                if ((Niveles01[18])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        2)  0001010000101000     ",end="")
                if ((Niveles01[19])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("hecho")
                else:
                    print(" ")
                print("        3)  0000100110010000     ",end="")
                if ((Niveles01[20])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        4)  1011001011011011     ",end="")
                if ((Niveles01[21])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        5)  0011111110011010     ",end="")
                if ((Niveles01[22])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        6)  1010000010010011     ",end="")
                if ((Niveles01[23])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        7)  1101100011100100     ",end="")
                if ((Niveles01[24])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        8)  1101111001110100     ",end="")
                if ((Niveles01[25])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        9)  0010100000010100     ",end="")
                if ((Niveles01[26])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       10)  1010100100000011     ",end="")
                if ((Niveles01[27])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       11)  0101101001010101     ",end="")
                if ((Niveles01[28])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       12)  0111010011011110     ",end="")
                if ((Niveles01[29])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       13)  1011111001111101     ",end="")
                if ((Niveles01[30])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       14)  0101110011001010     ",end="")
                if ((Niveles01[31])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       15)  1011111010000010     ",end="")
                if ((Niveles01[32])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       16)  1100100111110101     ",end="")
                if ((Niveles01[33])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       17)  0011100111110101     ",end="")
                if ((Niveles01[34])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       18)  0010100011101011     ",end="")
                if ((Niveles01[35])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.5)
                cunt=0
                while cunt==0:
                    Www=str(KEYinput("         Escribe tu código (16 cifras)    >>>   "))
                    if (Www=="e")or(Www=="E")or((len(Www))==16):
                        cunt=1
                        Kods=str(Www)
                    else:
                        print("Parece que el código que has puesto tiene un problema, inténtalo de nuevo.")
                if (Kods=="E")or(Kods=="e"):
                    print("Se cancela la carga de código")
                    exit=1
                else:
                    CodeT2("1",Kods)
                    Trew=CodeT2("0")
                KEYsleep(0.5)
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          MODO DESAFÍO       ||  ",mov," movimientos  ||  Código: ",CodeT2("0"))
                    print("")
                    print("Intenta llegar a tener todas las teselas de un tipo. Para salir la letra E.")
                    print("")
                    TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D)
                    JJJ=str(C2inputT2("            >>>  "))
                    mov=mov+1
                    ControlT2(JJJ)
                    print("")
                    print("                Has movido ",JJJ)
                    KEYsleep(0.4)
                    if ((A_A)and(A_B)and(A_C)and(A_D)and(B_A)and(B_B)and(B_C)and(B_D)and(C_A)and(C_B)and(C_C)and(C_D)and(D_A)and(D_B)and(D_C)and(D_D))or((not(A_A))and(not(A_B))and(not(A_C))and(not(A_D))and(not(B_A))and(not(B_B))and(not(B_C))and(not(B_D))and(not(C_A))and(not(C_B))and(not(C_C))and(not(C_D))and(not(D_A))and(not(D_B))and(not(D_C))and(not(D_D))):
                        clear()
                        print("")
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        KEYsleep(0.2)
                        print("")
                        print("                ¡¡¡ Has ganado !!!")
                        print("")
                        KEYsleep(0.5)
                        clear()
                        if Trew=="1001011001101001":
                            Niveles01[18]="1"
                        if Trew=="0001010000101000":
                            Niveles01[19]="1"
                        if Trew=="0000100110010000":
                            Niveles01[20]="1"
                        if Trew=="1011001011011011":
                            Niveles01[21]="1"
                        if Trew=="0011111110011010":
                            Niveles01[22]="1"
                        if Trew=="1010000010010011":
                            Niveles01[23]="1"
                        if Trew=="1101100011100100":
                            Niveles01[24]="1"
                        if Trew=="1101111001110100":
                            Niveles01[25]="1"
                        if Trew=="0010100000010100":
                            Niveles01[26]="1"
                        if Trew=="1010100100000011":
                            Niveles01[27]="1"
                        if Trew=="0101101001010101":
                            Niveles01[28]="1"
                        if Trew=="0111010011011110":
                            Niveles01[29]="1"
                        if Trew=="1011111001111101":
                            Niveles01[30]="1"
                        if Trew=="0101110011001010":
                            Niveles01[31]="1"
                        if Trew=="1011111010000010":
                            Niveles01[32]="1"
                        if Trew=="1100100111110101":
                            Niveles01[33]="1"
                        if Trew=="0011100111110101":
                            Niveles01[34]="1"
                        if Trew=="0010100011101011":
                            Niveles01[35]="1"
                        print("")
                        print("                 VICTORIA")
                        print("")
                        print("        Has conseguido poner igual todas las teselas, usando ",mov," movimientos.")
                        print("        Código original: ",Trew)
                        print("")
                        TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D)
                        KEYsleep(1)
                        c=KEYinput("                Enter para continuar    >>>   ")
                        exit=1
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("SALIENDO DEL MODO DESAFÍO")
                        print("")
                        KEYsleep(1)
                Guardar() #TO DO
            elif Ellec=="5": # generar código aleatorio
                clear()
                print("")
                print("          CÓDIGO ALEATORIO")
                print("")
                bb=str("")
                u=0
                while u<16:
                    sup=str(random.randint(0,1))
                    bb=bb+sup
                    u=u+1
                print("Tu código de tablero: ",bb,"     (es posible que sea muy difícil)")
                print("")
                KEYsleep(0.5)
                c=KEYinput("   Copia el código, luego pulsa Enter.          >>>")
            elif Ellec=="6": # salida
                TOTAL="fuera"
                clear()
                print("")
                print("")
                print("     Se sale de TESELAS 2")
                KEYsleep(1)
            else:
                clear()
                print("")
                print("       LO QUE HAS HECHO NO ES UNA ELECCIÓN")
                KEYsleep(1)
        ################################################################################
        ################################################################################
    elif Juego=="3":
        A_A=bool(False)
        A_B=bool(False)
        A_C=bool(False)
        B_A=bool(False)
        B_B=bool(False)
        B_C=bool(False)
        C_A=bool(False)
        C_B=bool(False)
        C_C=bool(False)
        a1a=bool(False)
        a1b=bool(False)
        a1c=bool(False)
        b1a=bool(False)
        b1b=bool(False)
        b1c=bool(False)
        c1a=bool(False)
        c1b=bool(False)
        c1c=bool(False)
        ###############################################################
        clear()
        print("")
        print("                        JUEGO DE LAS TESELAS 3")
        print("")
        print("")
        print("       Cambia el enfoque del juego. Ahora el objetivo es imitar")
        print("       el tablero de la derecha. Tablero 3x3, mismos movimientos.")
        print("")
        KEYsleep(0.5)
        c=KEYinput("                         Enter para comenzar  >>>  ")
        while TOTAL=="dentro":
            clear()
            print("")
            print("                     JUEGO DE LAS TESELAS 3")
            print("")
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            print("")
            TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            KEYsleep(1)
            clear()
            print("")
            print("                                   MENÚ")
            print("")
            print("          1) Tutorial")
            print("")
            print("          2) Niveles")
            print("")
            print("          3) Tablero libre")
            print("")
            print("          4) Modo desafío")
            print("")
            print("          5) Generar código aleatorio")
            print("")
            print("          6) Salir de TESELAS 3")
            print("")
            print("")
            KEYsleep(0.5)
            Ellec=str(KEYinput("                                            Tu elección: "))
            KEYsleep(0.5)
            if Ellec=="1": # tutorial
                A_A=bool(False)
                A_B=bool(False)
                A_C=bool(False)
                B_A=bool(False)
                B_B=bool(False)
                B_C=bool(False)
                C_A=bool(False)
                C_B=bool(False)
                C_C=bool(False)
                a1a=bool(False)
                a1b=bool(False)
                a1c=bool(True)
                b1a=bool(False)
                b1b=bool(False)
                b1c=bool(False)
                c1a=bool(False)
                c1b=bool(False)
                c1c=bool(False)
                clear()
                print("")
                print("                            TUTORIAL DE TESELAS 3")
                print("")
                print("TENEOS 2 TABLEROS DIFERENTES, EL DE LA IZQUIERDA Y EL DE LA DERECHA")
                TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                print("Nuestro tablero es de la izquierda, y nuestro objetivo imitar el de la derecha.")
                print("Los movimietos son los mismos que los de Teselas 1, por lo que se recomienda entender el primer juego antes de jugar a este.")
                print("Si has entendido Teselas 1 sabrás jugar a este. En caso de no saber jugar, dirígete al tutorial de Teselas 1.")
                print("")
                print("Veamos un ejemplo del TESELAS 3 ...")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
                print("")
                print("El objetivo es llegar a la posición del tablero de la derecha.")
                print("Vamos a darle al 3, para invertir la tercera fila.")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,not(C_A),C_B,C_C)
                print("")
                print("Lo siguiente será invertir la primera columna, le damos a la A.")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT3(not(A_A),not(A_B),A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                print("")
                print("Lo tenemos a un solo movimiento ya, si le damos al 1, ganaríamos.")
                c=KEYinput("                        Pulse Enter para continuar con el tutorial  >>>")
                clear()
                TableroT3(A_A,A_B,not(A_C),B_A,B_B,B_C,C_A,C_B,C_C)
                print("")
                print("¡Victoria! Hemos conseguido tener el mismo patrón que en la derecha.")
                print("Este juego es más complejo que los dos anteriores, se recomienda entender los anteriores antes de jugar a esta versión")
                print("")
                c=KEYinput("                        ENTER PARA TERMINAR EL TUTORIAL  >>>")
                KEYsleep(0.5)
                clear()
            elif Ellec=="2": # niveles
                clear()
                print("")
                print("                              NIVELES")
                print("")
                print("            Copia el código del nivel (en binario) y cárgalo donde desees.")
                print("            Puedes cargarlo en el tablero libre o en el modo desafío.")
                print("")
                print("        1)  110101001111111010     ",end="")
                if ((Niveles01[36])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        2)  000001010001110110     ",end="")
                if ((Niveles01[37])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("hecho")
                else:
                    print(" ")
                print("        3)  101111100010101100     ",end="")
                if ((Niveles01[38])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        4)  100101011111000010     ",end="")
                if ((Niveles01[39])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        5)  011010011000111101     ",end="")
                if ((Niveles01[40])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        6)  101100000100011011     ",end="")
                if ((Niveles01[41])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        7)  100011011011000110     ",end="")
                if ((Niveles01[42])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        8)  011000000011010000     ",end="")
                if ((Niveles01[43])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        9)  101000100100111000     ",end="")
                if ((Niveles01[44])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       10)  010110101001001011     ",end="")
                if ((Niveles01[45])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       11)  110001010110011101     ",end="")
                if ((Niveles01[46])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       12)  011100010000101110     ",end="")
                if ((Niveles01[47])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       13)  001010101101000011     ",end="")
                if ((Niveles01[48])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       14)  111110011011111000     ",end="")
                if ((Niveles01[49])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       15)  111101110100100101     ",end="")
                if ((Niveles01[50])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       16)  011001101111010110     ",end="")
                if ((Niveles01[51])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       17)  011011101011011010     ",end="")
                if ((Niveles01[52])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       18)  010011000001111100     ",end="")
                if ((Niveles01[53])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       19)  101010011110100000     ",end="")
                if ((Niveles01[54])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       20)  101000100000011011     ",end="")
                if ((Niveles01[55])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.3)
                c=KEYinput("          Enter para salir   >>>")
                KEYsleep(0.5)
            elif Ellec=="3": # tablero libre
                exit=0
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          TABLERO LIBRE       ||  ",mov," movimientos  ||  Código: ",CodeT3("0"))
                    print("")
                    print("Con esta función, tienes un tablero a tu disposición, para que muevas teselas o carges códigos.")
                    print("Para cargar un código, escribe el número 0. Para salir escribe E.")
                    print("")
                    TableroT3(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(CinputT3("            >>>  "))
                    mov=mov+1
                    ControlT3(JJJ)
                    print("")
                    print("                Has movido ",JJJ)
                    KEYsleep(0.4)
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("SALIENDO DEL TABLERO LIBRE")
                        print("")
                        KEYsleep(1)
                    if JJJ=="0":
                        mov=0
                        clear()
                        print("")
                        print("")
                        print("      CARGAR UN CÓDIGO DE TABLERO       ||  Tu código actual: ",CodeT3("0"))
                        print("")
                        print("De esta manera puedes guardar y cargar la información del tablero. Para guardarla, copia el código que aparece al lado del número de movimientos en el tablero libre. Esto te permite desafiar a tus amigos a ver si resuelven el puzle. El código representa el estado del tablero, reiniciándose el número de movimientos si cargas un código.")
                        print("   El código está sólo formado por los dígitos binarios, no copies espacios, puntos, comas o cualquier otra cosa, o no se interpretará correctamente.")
                        print("   (Para cancelar, escribe la letra E)")
                        print("")
                        KEYsleep(0.5)
                        cunt=0
                        while cunt==0:
                            Www=str(KEYinput("         Escribe tu código (18 cifras)    >>>   "))
                            if (Www=="e")or(Www=="E")or((len(Www))==18):
                                cunt=1
                                Kods=str(Www)
                            else:
                                print("Parece que el código que has puesto tiene un problema, inténtalo de nuevo.")
                        if (Kods=="E")or(Kods=="e"):
                            print("Se cancela la carga de código")
                        else:
                            CodeT3("1",Kods)
                        KEYsleep(0.5)
            elif Ellec=="4": # modo desafío
                exit=0
                clear()
                print("")
                print("")
                print("      CARGAR UN CÓDIGO PARA EL MODO DESAFÍO            (Para cancelar, la letra E)")
                print("")
                print("Puedes cargar el código que quieras o copiar (Ctrl+C) y pegar (Ctrl+V)")
                print("de los códigos de niveles de abajo.   1- Copia el código. 2- Pégalo.")
                print("COPIA SÓLO LOS NÚMEROS Truco: doble click sobre el código, cuando está en blanco, Ctrl+C.")
                print("")
                print("        1)  110101001111111010     ",end="")
                if ((Niveles01[36])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        2)  000001010001110110     ",end="")
                if ((Niveles01[37])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("hecho")
                else:
                    print(" ")
                print("        3)  101111100010101100     ",end="")
                if ((Niveles01[38])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        4)  100101011111000010     ",end="")
                if ((Niveles01[39])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        5)  011010011000111101     ",end="")
                if ((Niveles01[40])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        6)  101100000100011011     ",end="")
                if ((Niveles01[41])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        7)  100011011011000110     ",end="")
                if ((Niveles01[42])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        8)  011000000011010000     ",end="")
                if ((Niveles01[43])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("        9)  101000100100111000     ",end="")
                if ((Niveles01[44])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       10)  010110101001001011     ",end="")
                if ((Niveles01[45])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       11)  110001010110011101     ",end="")
                if ((Niveles01[46])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       12)  011100010000101110     ",end="")
                if ((Niveles01[47])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       13)  001010101101000011     ",end="")
                if ((Niveles01[48])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       14)  111110011011111000     ",end="")
                if ((Niveles01[49])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       15)  111101110100100101     ",end="")
                if ((Niveles01[50])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       16)  011001101111010110     ",end="")
                if ((Niveles01[51])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       17)  011011101011011010     ",end="")
                if ((Niveles01[52])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       18)  010011000001111100     ",end="")
                if ((Niveles01[53])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       19)  101010011110100000     ",end="")
                if ((Niveles01[54])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("       20)  101000100000011011     ",end="")
                if ((Niveles01[55])=="1"):
                    print("hecho")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.5)
                cunt=0
                while cunt==0:
                    Www=str(KEYinput("         Escribe tu código (18 cifras)    >>>   "))
                    if (Www=="e")or(Www=="E")or((len(Www))==18):
                        cunt=1
                        Kods=str(Www)
                    else:
                        print("Parece que el código que has puesto tiene un problema, inténtalo de nuevo.")
                if (Kods=="E")or(Kods=="e"):
                    print("Se cancela la carga de código")
                    exit=1
                else:
                    CodeT3("1",Kods)
                    Trew=CodeT3("0")
                KEYsleep(0.5)
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          MODO DESAFÍO       ||  ",mov," movimientos  ||  Código: ",CodeT3("0"))
                    print("")
                    print("Intenta imitar en tu tablero lo del de la derecha. Tú mueves en el izquierdo.")
                    print("Para salir la letra E.")
                    print("")
                    TableroT3(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(C2inputT3("            >>>  "))
                    mov=mov+1
                    ControlT3(JJJ)
                    print("")
                    print("                Has movido ",JJJ)
                    KEYsleep(0.4)
                    if ((A_A==a1a)and(A_B==a1b)and(A_C==a1c)and(B_A==b1a)and(B_B==b1b)and(B_C==b1c)and(C_A==c1a)and(C_B==c1b)and(C_C==c1c)):
                        clear()
                        print("")
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORIA")
                        KEYsleep(0.2)
                        print("")
                        print("                ¡¡¡ Has ganado !!!")
                        print("")
                        KEYsleep(0.5)
                        clear()
                        if Trew=="110101001111111010":
                            Niveles01[36]="1"
                        if Trew=="000001010001110110":
                            Niveles01[37]="1"
                        if Trew=="101111100010101100":
                            Niveles01[38]="1"
                        if Trew=="100101011111000010":
                            Niveles01[39]="1"
                        if Trew=="011010011000111101":
                            Niveles01[40]="1"
                        if Trew=="101100000100011011":
                            Niveles01[41]="1"
                        if Trew=="100011011011000110":
                            Niveles01[42]="1"
                        if Trew=="011000000011010000":
                            Niveles01[43]="1"
                        if Trew=="101000100100111000":
                            Niveles01[44]="1"
                        if Trew=="010110101001001011":
                            Niveles01[45]="1"
                        if Trew=="110001010110011101":
                            Niveles01[46]="1"
                        if Trew=="011100010000101110":
                            Niveles01[47]="1"
                        if Trew=="001010101101000011":
                            Niveles01[48]="1"
                        if Trew=="111110011011111000":
                            Niveles01[49]="1"
                        if Trew=="111101110100100101":
                            Niveles01[50]="1"
                        if Trew=="011001101111010110":
                            Niveles01[51]="1"
                        if Trew=="011011101011011010":
                            Niveles01[52]="1"
                        if Trew=="010011000001111100":
                            Niveles01[53]="1"
                        if Trew=="101010011110100000":
                            Niveles01[54]="1"
                        if Trew=="101000100000011011":
                            Niveles01[55]="1"
                        print("")
                        print("                 VICTORIA")
                        print("")
                        print("        Has conseguido imitar el otro tablero, usando ",mov," movimientos.")
                        print("        Código original: ",Trew)
                        print("")
                        TableroT3(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                        KEYsleep(1)
                        c=KEYinput("                Enter para continuar    >>>   ")
                        exit=1
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("SALIENDO DEL MODO DESAFÍO")
                        print("")
                        KEYsleep(1)
                Guardar() #TO DO
            elif Ellec=="5": # generar código aleatorio
                clear()
                print("")
                print("          CÓDIGO ALEATORIO")
                print("")
                bb=str("")
                u=0
                while u<18:
                    sup=str(random.randint(0,1))
                    bb=bb+sup
                    u=u+1
                print("Tu código de tablero: ",bb,"     (es posible que sea muy difícil)")
                print("")
                KEYsleep(0.5)
                c=KEYinput("   Copia el código, luego pulsa Enter.          >>>")
            elif Ellec=="6": # salida
                TOTAL="fuera"
                clear()
                print("")
                print("")
                print("     Se sale de TESELAS 3")
                KEYsleep(1)
            else:
                clear()
                print("")
                print("       LO QUE HAS HECHO NO ES UNA ELECCIÓN")
                KEYsleep(1)
        ################################################################################
        ################################################################################
    elif Juego=="4": # USUARIO (primero recaba unos pocos datos, contando cuántos niveles has hecho de cada apartado)
        clear()
        laurus=0
        Tes1NumNiveles=0
        while laurus<18:
            if (Niveles01[laurus])=="1":
                Tes1NumNiveles=Tes1NumNiveles+1
            laurus=laurus+1
        Tes2NumNiveles=0
        while laurus<36:
            if (Niveles01[laurus])=="1":
                Tes2NumNiveles=Tes2NumNiveles+1
            laurus=laurus+1
        Tes3NumNiveles=0
        try:
            while laurus<56:
                if (Niveles01[laurus])=="1":
                    Tes3NumNiveles=Tes3NumNiveles+1
                laurus=laurus+1
            NumNiveles=Tes1NumNiveles+Tes2NumNiveles+Tes3NumNiveles
        except:
            win.MessageBeep()
            while laurus<55:
                if (Niveles01[laurus])=="1":
                    Tes3NumNiveles=Tes3NumNiveles+1
                laurus=laurus+1
                NumNiveles=Tes1NumNiveles+Tes2NumNiveles+Tes3NumNiveles
        print("")
        print("           USUARIO")
        print("")
        print("       Usuario número ",NumUsuario)
        print("")
        print("       ",NumNiveles," niveles completados")
        print("")
        print("           TESELAS 1  .....  ",Tes1NumNiveles," niveles")
        print("           TESELAS 2  .....  ",Tes2NumNiveles," niveles")
        print("           TESELAS 3  .....  ",Tes3NumNiveles," niveles")
        print("")
        print("_________________________________________________________________")
        print("")
        print("       Comandos:")
        print("")
        print("          Salir de Usuario (1/S/E)")
        print("          Limpiar usuario (2/U/L)   >>> Esto crea un usuario de cero")
        print("          Guardar información (3/G/B)")
        print("")
        KEYsleep(1)
        y=0
        while y==0:
            Comando=str(KEYinput("     Comando deseado: "))
            if (Comando=="G")or(Comando=="g")or(Comando=="B")or(Comando=="b")or(Comando=="3")or(Comando=="1")or(Comando=="S")or(Comando=="E")or(Comando=="2")or(Comando=="U")or(Comando=="L")or(Comando=="u")or(Comando=="s")or(Comando=="e")or(Comando=="l"):
                y=1
                print(" OK  --  Comando válido")
            else:
                print("Comando no válido")
        if (Comando=="1")or(Comando=="S")or(Comando=="E")or(Comando=="s")or(Comando=="e"):
            print("")
            print("           SALIENDO DE USUARIO")
            KEYsleep(1)
        elif (Comando=="2")or(Comando=="U")or(Comando=="L")or(Comando=="u")or(Comando=="l"):
            print("")
            print("         BORRANDO INFORMACIÓN DEL USUARIO NÚMERO ",NumUsuario)
            KEYsleep(0.3)
            print("")
            print("Borrando número de usuario y creando el nuevo...")
            NumUsuario=NumUsuario+1
            if NumUsuario>9:
                NumUsuario=1
                print("Se vuelve a empezar con el usuario 1")
            KEYsleep(0.3)
            print("Ajustando el número de niveles...  [1/5]")
            NumNiveles=0
            KEYsleep(0.3)
            print("Ajustando el número de niveles...  [2/5]")
            Tes1NumNiveles=0
            KEYsleep(0.3)
            print("Ajustando el número de niveles...  [3/5]")
            Tes2NumNiveles=0
            KEYsleep(0.3)
            print("Ajustando el número de niveles...  [4/5]")
            Tes3NumNiveles=0
            KEYsleep(0.3)
            print("Ajustando el número de niveles...  [5/5]")
            w=0
            while w<(NumeroTotaldeNiveles-1):
                Niveles01[w]="0"
                w=w+1
            KEYsleep(0.3)
            print("Editando archivos de niveles...  [1/4]")
            KEYsleep(0.3)
            print("Editando archivos de niveles...  [2/4]")
            KEYsleep(0.3)
            print("Editando archivos de niveles...  [3/4]")
            KEYsleep(0.3)
            print("Editando archivos de niveles...  [4/4]")
            print("")
            KEYsleep(0.5)
            print("Proceso terminado, se ha creado el usuario número ",NumUsuario)
            print("Guarda información para mantener el cambio.")
            print("")
            c=KEYinput("          Enter para volver al menú general >>>")
            KEYsleep(1)
        elif (Comando=="3")or(Comando=="G")or(Comando=="g")or(Comando=="B")or(Comando=="b"):
            print("               GUARDAR INFORMACIÓN")
            # Archivo Teselas:
            Archivo=open(RUTAusuario,"w")
            YaVes=str("Us66PPCCode3451028Seguridad45322Qi5454igbkjew458763PINQwertyLaurusUsuario") # 0 posicionales
            YaVes=YaVes+(str(NumUsuario))+"N"
            Extra=int(3-(len(str(NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(NumNiveles))+"N1"
            Extra=int(3-(len(str(Tes1NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(Tes1NumNiveles))+"N2"
            Extra=int(3-(len(str(Tes2NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(Tes2NumNiveles))+"N3"
            Extra=int(3-(len(str(Tes3NumNiveles))))
            YaVes=YaVes+Extra*Cero
            YaVes=YaVes+(str(Tes3NumNiveles))+"beg56AnemonaCoral34"
            Archivo.write(YaVes)
            Archivo.close()
            # Archivo niveles:
            Niveles=open(RUTAniveles,"w")
            Retaila=""
            i=0
            while i<(NumeroTotaldeNiveles):
                L=str(Niveles01[i])
                Retaila=Retaila+L
                i=i+1
            Niveles.write(Retaila)
            Niveles.close()
            print("---- Información guardada.    ",YaVes," --- ",Retaila)
            print("")
            c=KEYinput("          Enter para volver al menú general >>>")
    elif Juego=="5":
        clear()
        print("")
        print("")
        print("                                 INFORMACIÓN")
        print("")
        print("")
        print("Habla a tus amigos del juego, harías a todos un gran favor.")
        print("Aquí tienes toda la información que puedas necesitar de TESELAS, en el sitio web:")
        print("")
        print("                        https://sites.google.com/view/teselas/inicio")
        print("")
        print("                             Correos de los creadores: ")
        print("")
        print("                diego.herasmiguez@gmail.com             pablo.aufhause@gmail.com")
        print("")
        print("")
        print("El juego tiene un aspecto matemático muy interesante, con relaciones con matrices, determinantes, adjuntos,")
        print("teoría de números, combinatoria, probabilidad... Al respecto hay muchas hipótesis y teorías. Para obtener información")
        print("sobre esto mira el sitio web oficial. ¡Estás invitado a ayudar!")
        print("")
        print("La estética del juego pretende ser minimalista, con dibujos ASCII que reflejan la sencillez de la dinámica de TESELAS.")
        print("Como algunos de los mejores juegos, con normas simples y estética suficiente se consigue gran complejidad y riqueza.")
        print("")
        KEYsleep(0.1)
        print("                                 FUTUROS PROYECTOS")
        print("")
        print("")
        print("      Hay muchos avances en cuannto a TESELAS se refiere. Estos son algunos de los caminos:")
        print("")
        print("-- Mejora de la aplicación .exe del juego. Añadir interfaces y mejorar funcionalidad.")
        print("")
        print("-- Crear TESELAS 4 con un modo espejo (como el 3) pero en 4x4.")
        print("")
        print("-- Progresar en el aspecto matemático de TESELAS.")
        print("")
        print("-- Crear una versión adaptada a cualquier sistema operativo (Windows, iOS, Linux...).")
        print("")
        print("-- Crear una aplicación de móvil.")
        print("")
        print("      Puedes contribuir a cualquiera de estos puntos, resultando de gran utilidad. Puedes formar parte del equipo")
        print("      y participar en futuros proyectos y juegos. Aparecerás en los créditos. Si tienes alguna idea o ganas de colaborar,")
        print("      contacta a los creadores o echa un vistazo al sitio web. También puedes ayudar donando cualquier cantidad.")
        print("      No tenemos ánimo de lucro, nuestro objetivo es llegar al máximo número de personas para que disfruten un juego")
        print("      creativo, ingenioso y, desde luego, entretenido. Para financiar nuestros esfuerzos tu colaboración, ya sea a través")
        print("      de tu ayuda activa o una pequeña colaboración, es vital. También hay que mantener y pagar el sitio web.")
        print("      MUCHAS GRACIAS. Aparecerás en los créditos, si quieres. Cualquier ayuda es bienvenida.")
        print("      Para cualquier duda o sugerencia, contacta con los creadores o visita el sitio web.")
        print("")
        print("Aquí tienes toda la información que puedas necesitar de TESELAS:")
        print("")
        print("                        https://sites.google.com/view/teselas/inicio")
        print("")
        print("                             Correos de los creadores: ")
        print("")
        print("                diego.herasmiguez@gmail.com             pablo.aufhause@gmail.com")
        print("")
        print("")
        print("           A continuación, está repetido el texto del inicio del juego:")
        print("")
        KEYsleep(0.1)
        print("Para ejecutar este juego como archivo de Python es aconsejable ejecutar en Visual Studio Code, o similares." )
        print("Esta es la versión definitiva del juego TESELAS. En un principio, era un juego para jugar con cachitos de papel," )
        print("inventado por Pablo de la Fuente Sancho en torno al 2019. Una tarde de Abril de 2025 programó, por primera vez," )
        print("un tablero de TESELAS. Este programa inicial sólo tenía un tablero, que ni siquiera interpretaba victorias, solo movías." )
        print("Con el tiempo, el programa fue haciéndose mejor, hasta llegar a TESELAS 1, el primer lanzamiento oficial." )
        print("Tutorial y niveles hechos por Diego Heras y Pablo de la Fuente. Más tarde, el tablero se expandió del 3x3 original" )
        print("al 4x4. Este es TESELAS 2. El objetivo, como en el 1, es igualar las teselas con los movimientos permitidos," )
        print("que se explican en el tutorial. La siguiente versión es TESELAS 3, donde se vuelve al tablero 3x3, pero con el objetivo" )
        print("de imitar el tablero de la derecha. En todas las versiones Diego Heras ha escrito tutoriales y preparado niveles." )
        print("" )
        print("Los derechos de distribución son de Pablo de la Fuente Sancho. Siempre que no sea con fines comerciales" )
        print("se puede distribuir, contactando primero con pablo.aufhause@gmail.com o diego.herasmiguez@gmail.com." )
        print("Contactar también para obtener las versiones individualmente como archivo de Python o cualquier otra cosa." )
        print("")
        print("              Sitio web de TESELAS: https://sites.google.com/view/teselas/inicio")
        print("")
        print("Este texto es el inicio del programa. Lo verás cuando abras el juego. Para navegar por la aplicación, " )
        print('ahora viene un tutorial. Puedes acceder a esta y más información desde el menú general en "Información"' )
        print("" )
        print("                                      NAVEGACIÓN POR EL JUEGO" )
        print("" )
        print("Este programa consta, además del tablero, de un TUTORIAL, de niveles precargados, de un modo desafío para retar" )
        print("a amigos y de un generador de posiciones aleatorias. Para cargar una posición, se copia el código en binario" )
        print("y se pega donde se quiera cargar. La navegación es muy intuitiva, con un índice en el que se selecciona por número." )
        print("Al salir de una sección, se vuelve a este índice-menú, común a todas las versiones. Ahí eliges a qué TESELAS jugar" )
        print("y gestionas tu usuario, la cuenta en la que se guarda tu información como jugador. Dentro de un juego, este es el menú:")
        print("")
        print("       EXPLICACIÓN DEL MENÚ:" )
        print("" )
        print("             1) TUTORIAL: Explica cómo jugar." )
        print("" )
        print("             2) NIVELES: Aquí están los códigos de los niveles." )
        print("" )
        print("             3) TABLERO LIBRE: Aquí no hay victoria, sólo el tablero interactivo." )
        print("                               Puedes cargar aquí códigos." )
        print("" )
        print("             4) MODO DESAFÍO: Cargas un código y ganas cuando resuelves el mosaico." )
        print("" )
        print("             5) GENERADOR DE CÓDIGOS: Genera un código aleatorio que puedes copiar." )
        print("" )
        print("             6) SALIR: Te permite sair de una versión determinada de TESELAS e ir" )
        print("                       al menú para elegir versión." )
        print("")
        KEYsleep(0.1)
        print("Cualquier orden tiene una longitud de 1 caracter, una letra o un número. Para hacerla, escribes" )
        print("el caracter de la orden y pulsas Enter en el teclado del ordenador. Esta es una versión de consola para " )
        print("ordenador, pero en un futuro habrá nuevos lanzamientos con interfaces y nuevas versiones. Para tener" )
        print("las últimas versiones escribe a pablo.aufhause@gmail.com o diego.herasmiguez@gmail.com que son" )
        print("los contactos de los creadores. En un plazo de 1 semana prometemos haber contestado. ¡O antes!")
        print("Es importante que para que se guarde la información de lo que has hecho guardes información, en el apartado")
        print("de usuario del menú de versiones.")
        KEYsleep(0.1)
        print("")
        print("Siempre en tu pantalla aparecerán las indicaciones de lo que puedes hacer; si te despistas, lee. Encima de")
        print("los tableros te aparecen el número de movimientos y el código del tablero en ese momento. Esos códigos,")
        print("en binario, guardan información de las teselas del tablero. Los niveles están en forma de código. Explicado antes,")
        print("para hacer un nivel copias (Ctrl+C) un código y lo pegas (Ctrl+V) donde quieras. Puedes pegarlo directamente en")
        print("el modo desafío, o entrar en tablero libre y elegir cargar un código (0). Para que un nivel se te marque como hecho")
        print("lo tienes que haber resuelto en el modo desafío. IMPORTANTE: que no se te olvide guardar información del usuario")
        print("antes de salir del juego, en el menú principal. En el tablero libre tienes un tablero a tu disposición, para")
        print("que pruebes movimientos o lo que quieras. Como siempre en los tableros, tienes el código de tu posición actual")
        print("la esquina superior derecha, para que lo guardes para jugar en otro momento o lo compartas para retar a tus amigos.")
        print("")
        c=KEYinput("                          Enter para volver al menú general >>>")
        KEYsleep(1)
    else:
        print("")
        print(" >>>  No es un número de una versión, prueba de nuevo.")
        KEYsleep(1)
##########################################
