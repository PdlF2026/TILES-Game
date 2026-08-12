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
                text=text+" (Do not press Ctrl+C)"+str(text[len(text)-1])
                fawly=False
    return Dev

def KEYsleep(t):
    q=True
    while q:
        try:
            time.sleep(t)
            q=False
        except KeyboardInterrupt:
            print("> (Do not press Ctrl+C)")
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
        if (W=="l")or(W=="r")or(W=="L")or(W=="R")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="0")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("not valid command")
def C2inputT1(text=str):
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="l")or(W=="r")or(W=="L")or(W=="R")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("not valid command")
def TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C):
    print("")
    print("           L\\            A |                B |                 C |             /R")
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
    if (Acc=="l")or(Acc=="L"):
        A_A=not(A_A)
        B_B=not(B_B)
        C_C=not(C_C)
    if (Acc=="r")or(Acc=="R"):
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
        print("CODE PROCESSED")
        return None
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
################################


################################  TESELAS 2
def CinputT2(text=str): # Con carga de código
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="q")or(W=="Q")or(W=="w")or(W=="W")or(W=="r")or(W=="R")or(W=="4")or(W=="l")or(W=="d")or(W=="L")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="0")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("not valid command")
def C2inputT2(text=str): # Sin carga de código
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="q")or(W=="Q")or(W=="w")or(W=="W")or(W=="r")or(W=="R")or(W=="4")or(W=="l")or(W=="d")or(W=="L")or(W=="D")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("not valid command")
def TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D):
    print("")
    print("            L\\           A |                 B |                 C |                 D |            /R")
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
            print("                  Flip the centre: W",end="")
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
            print("                  Flip the corners: Q",end="")
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
    if (Acc=="L")or(Acc=="l"):
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
        print("CODE PROCESSED")
        return None
    #::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
################################


################################  TESELAS 3
def CinputT3(text=str):
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="l")or(W=="r")or(W=="L")or(W=="R")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="0")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("not valid command")
def C2inputT3(text=str):
    y=0
    while y==0:
        W=str(KEYinput(text))
        if (W=="r")or(W=="l")or(W=="R")or(W=="L")or(W=="1")or(W=="2")or(W=="3")or(W=="A")or(W=="B")or(W=="C")or(W=="E")or(W=="a")or(W=="b")or(W=="c")or(W=="e"):
            y=1
            return W
        else:
            print("not valid command")
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
    print("        L\\           A |                B |                 C |           /R  ")
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
    if (Acc=="L")or(Acc=="l"):
        A_A=not(A_A)
        B_B=not(B_B)
        C_C=not(C_C)
    if (Acc=="R")or(Acc=="r"):
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
        print("CODE PROCESSED")
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
print("                                                  TILES")
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
print("                                           Send the game to your friends!")
print("")
KEYsleep(1.2)
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
    print("New user.")
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
        print("All right")
    else:
        print("The game files have a problem, might have been edited.")
        print("Please, do not change the files of the game.")
        print("")
        while True:
            win.Beep(300,500)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("SOLUTIONS:")
            print('1) For a good beginninng, search in your computer ')
            print('the files named "NNN.txt" and "UST.txt".')
            print("2) Delete the files.")
            print("3) Ask for advise to pablo.aufhause@gmail.com or diego.herasmiguez@gmail.com")
            c=KEYinput("The game is stopped until the problem is solved. >>>")
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
    print("New user.")
else:
    print("Gathering levels information...")
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
        print("All right")
    else:
        print("The game files have a problem, they might have been edited.")
        print("Please, do not change the files of the game.")
        print("")
        while True:
            win.Beep(300,500)
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::")
            print("SOLUTIONS:")
            print('1) For a good beginning, search in your computer ')
            print('the files named "NNN.txt" and "UST.txt".')
            print("2) Delete the files.")
            print("3) Ask for advise to pablo.aufhause@gmail.com or diego.herasmiguez@gmail.com")
            c=KEYinput("The game is stopped until the problem is solved. >>>")
c=KEYinput("Press Enter. If it doesn't work, click the screen of the game and press Enter again.  ---->>> ")

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################

if True: # Copyright (c) 2026 Pablo de la Fuente Sancho - Licensed under the MIT License
    clear()
    print("")
    print("")
    print("                                        TILES    ")
    print("")
    print("")
    print("                    You will inmerse yourself in the game TILES experience.")
    print("")
    print("")
    print("                             email addresses of the developers: ")
    print("")
    print("                diego.herasmiguez@gmail.com             pablo.aufhause@gmail.com")
    print("")
    print("       The game was programmed by Pablo de la Fuente Sancho. The original idea is his, too.")
    print("  Diego Heras is a friend who helped writing the tutorials in spanish, and testing the game many times")
    print("             to search for problems. He also helped suggesting navigation ideas.")
    print("")
    print("")
    print("")
    print("                                            INFORMATION")
    print("")
    print("A long time ago, a ten-year-old Pablo created a game, originally played with paper pieces." )
    print("The game didn't have a name, it came later. The original (classic) board of the game consists in a 3x3 distribution" )
    print("of elements with 2 positions, for instance white and black." )
    print("To play, the person has to flip the elements (little paper pieces in the classic version) by hand, according" )
    print("to some rules. However, the process was tiresome, boring. That's the reason why the computer version was created." )
    print("It is an app for the Windows desktop, programmed in the coding language Python." )
    print("There are two other versions of the game, TILES 2 and TILES 3, with some differences." )
    print("To play, you will find a tutorial for each version in the section thereof." )
    print("It is a 1 player game, but you can send challenges to your friends, as a competition." )
    print('')
    print('The original name in spanish is "Teselas", the name of each single piece of a mosaic. It is because the game board')
    print('resembles a mosaic, in which the "teselas" are the tiles, the translation to english. Although it is not')
    print('an accurate translation, it keeps the idea of dynamic tiles, which the player flips with actions.')
    print("" )
    print("All rights related to this game and the app belong to Pablo de la Fuente Sancho." )
    print("If you send the game to a friend so that he/she can play it, contact one of these emails" )
    print("pablo.aufhause@gmail.com or diego.herasmiguez@gmail.com to let us know that the game is spreading out." )
    print("                  Write, contact, the emails to ask any question as well." )
    print("")
    print("              Website of the game: https://sites.google.com/view/teselas/inicio")
    print("")
    print("This text you're reading is the start text. It will appear every time you open the game." )
    print('Once it has been red it is not necessary to read it again, so you can skip the start text whenever you want.' )
    print('You can access the text and more information in the "Information", to which you can access via the General Menu.')
    KEYsleep(1)
    print("" )
    print("                                      HOW TO NAVIGATE THE GAME" )
    print("" )
    print("The app contains for every version (TILES 1, 2 and 3): the tutorial, some levels, the game board (free board)," )
    print("the challenge mode (also to complete the levels) and a random position generator.")
    print("The information of the position of the game is coded in the binary code. To use it, just COPY (Ctrl+C) the code" )
    print("and PASTE (Ctrl+V) it where you want to play it. This way, you are able to send the level to a friend, or to play" )
    print("the position (levels are certain positions) in the mode you prefer, pasting the code where you want.")
    print("")
    print("VERY IMPORTANT information: how to navigate the game. It is organized by 2 menus. ")
    print("The first menu is to choose the version of the game, or to access some features. This is how it looks like:")
    if True:
        print("")
        print("                                           GENERAL MENU")
        print("")
        print("")
        print("                               Choose typing the number of the choice.")
        print("")
        print("                       --   1) TILES 1      Original 3x3 game.")
        print("")
        print("                       --   2) TILES 2      4x4 extension, with new options.")
        print("")
        print("                       --   3) TILES 3      Try to imitate the model position.")
        print("")
        print("                       --   4) USER         About your game account.")
        print("")
        print("                       --   5) INFORMATION  General info of game and app.")
    print("")
    print("")
    print("The first three options are the game versions. In the the forth section you can see how many levels you've solved")
    print("and restart. In the section 5 you have more information, besides the start text.")
    print("")
    print("Inside the 3 first options, you have the Game Menu. It's the same for the three TILES games.")
    print("This is how it looks like:")
    if True:
        print("")
        print("                                 GAME MENU")
        print("")
        print("          1) Tutorial")
        print("")
        print("          2) Levels list")
        print("")
        print("          3) Free board")
        print("")
        print("          4) Challenge mode (to try levels)")
        print("")
        print("          5) Random code generator")
        print("")
        print("          6/E) Exit TILES 1")
    print("" )
    print("" )
    print('In the "Levels list" section, you access the LIST of the levels codes. To try a level, COPY (Ctrl+C) the code' )
    print("of the level and paste it where you want. JUST copy the binary code (0 and 1), not the space next to it." )
    print("You can PASTE (Ctrl+V) the level code in the ",'"Free board"'," section to upload the position," )
    print("so the game board adquires the position given by the code." )
    print("TO DO A LEVEL")
    print('To try the level directly (the most recommended if you are trying levels) access the "Challenge mode"')
    print("and paste there the level code you have COPIED (Ctrl+C) from the levels codes list below.")
    print('If you solve the level, the code in the LIST of levels will appear as "Solved".')
    print('Remember: the levels for each TILES (1, 2 and 3) are available in "Levels list"')
    print("section of the corresponding version of TILES. ALSO IN CHALLENGE MODE")
    print("It is also posible to send the code to a friend, as a challenge.")
    print('To generate a random position (a random code) access 5, "Random code generator", and you will see the code.')
    print("Notice that the given code could be too difficult.")
    print('You can type "6" or "E" to exit the Game Menu of this TILES and returnn to the General Menu.')
    print('As always, write the choice and click "Enter" in the keyboard.')
    print("")
    print("In general, the letter E is the command for exiting the section you're in. For ALL commands, write using the keyboard")
    print("and press Enter.")
    print("Once you get used to navigate it's very easy, it works as a website. Anyway, the available commands,")
    print("the actions that can be done, are always written, so if you forget something, just read.")
    print("")
    print("                                    Let's play!!!")
    print("")
    print('FOR EVERY COMMAND, WRITE AND THEN CLICK "ENTER" IN THE KEYBOARD. TO PLAY AND NAVIGATE THE GAME,')
    print("ALL YOU NEED IS THE KEYBOARD")
    print("")
    KEYsleep(1)
    print("")
    c=KEYinput("                              Enter to begin >>>  ")
while True: # BUCLE JUEGO
    TOTAL="dentro"
    if True: # MENÚ DE VERSIONES
        clear()
        print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
        print("        User ",NumUsuario)
        print("")
        print("                                           GENERAL MENU")
        print("")
        print("")
        print("                               Choose typing the number of the choice.")
        print("")
        print("                       --   1) TILES 1      Original 3x3 game.")
        print("")
        print("                       --   2) TILES 2      4x4 extension, with new options.")
        print("")
        print("                       --   3) TILES 3      Try to imitate the model position.")
        print("")
        print("                       --   4) USER         About your game account.")
        print("")
        print("                       --   5) INFORMATION  General info of game and app.")
        print("")
        print("")
        print("                              Is recommended to start by TILES 1.")
        print("")
        print("")
        KEYsleep(0.5)
    Juego=str(KEYinput("                          Type the number of your choice >>>  "))
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
        print("                             TILES 1")
        print("")
        print("")
        print("       The original game, in a 3x3 game board. The aim is to set all")
        print("       tiles with the same colour. The first version.")
        print("")
        KEYsleep(0.5)
        c=KEYinput("                         Enter to begin  >>>  ")
        while TOTAL=="dentro":
            clear()
            print("")
            print("                     TILES 1")
            print("")
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            print("")
            TableroT1(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            KEYsleep(0.5)
            clear()
            print("")
            print("                                 GAME MENU")
            print("")
            print("          1) Tutorial")
            print("")
            print("          2) Levels list")
            print("")
            print("          3) Free board")
            print("")
            print("          4) Challenge mode (to try levels)")
            print("")
            print("          5) Random code generator")
            print("")
            print("          6/E) Exit TILES 1")
            print("")
            print("")
            KEYsleep(0.5)
            Ellec=str(KEYinput("                                            Your choice: "))
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
                print("                                         TILES 1 TUTORIAL")
                print("")
                print("")
                KEYsleep(1)
                clear()
                print("First, let's take a look at the board. It has 3 lines and 3 columns. There are two 3-length diagonals.")
                print("Some tiles are black and others are white. The state of the tiles' colour is the POSITION.")
                TableroT1(A_A,not(A_B),A_C,not(B_A),not(B_B),B_C,C_A,C_B,not(C_C)) # MUESTRA EL TABLERO CON UNA DETERMINADA CONFIGURACIÓN
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                print("")
                TableroT1(A_A,not(A_B),A_C,not(B_A),not(B_B),B_C,C_A,C_B,not(C_C))
                print("")
                print("In the example board position, as you can see, all tiles have not the same colour. The aim of the game is to set")
                print("all the tiles with the same state, white or black.")
                print("")
                print("To do it, you have ACTIONS. Columns (A, B, C), lines (1, 2, 3) or the board's diagonals (L, R).")
                print("Arround the board you have the indications of the COMMAND associated to the action. To do an action,")
                print('type where you see ">>>" the letter (in the game, not now, this is the tutorial), and press Enter.')
                print("When you do an ACTION you FLIP the tiles, like if they were coins or paper pieces, between white and black.")
                print("Each move you do an action. This way, if you want to flip the right column and then the left diagonal, you first")
                print('write "C" and press Enter in the keyboard. Then, you write "L" and press Enter. Each action switches the colour')
                print('of the tiles affected. By doing this, manage to make all tiles have the same colour.')
                print("")
                print("     LET'S SEE AN EXAMPLE")
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                print("")
                print("             EXAMPLE")
                print("")
                TableroT1(not(A_A),A_B,not(A_C),B_A,not(B_B),B_C,not(C_A),C_B,not(C_C))
                print("")
                print("Now we can see a different position of the board. How to manage to equalise the tiles?")
                print("First, we can flip the middle line, in order to form one column of the same colour in the middle.")
                print('We type "2" because it is the second line (there is an indication) and press Enter:')
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                print("")
                TableroT1(not(A_A),A_B,not(A_C),not(B_A),B_B,not(B_C),not(C_A),C_B,not(C_C))
                print("")
                print("As you can see, after the ACTION the tiles affected have swithced their colour.")
                print("Now, we notice that the middle column has the only tiles with different status.")
                print("Realise that the solution is to flip the middle column. To do it,")
                print('type "B" (see the indication above the column) and then Enter:')
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT1(not(A_A),not(A_B),not(A_C),not(B_A),not(B_B),not(B_C),not(C_A),not(C_B),not(C_C))
                print("")
                print("Done! We now have all the tiles with the same colour.")
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT1(not(A_A),A_B,A_C,B_A,not(B_B),B_C,C_A,C_B,not(C_C))
                print("")
                print("Here is another example, an easy one. Try to figure out how to solve it on your own.")
                print("Continue the tutorial to get the solution. Tip: try to  figure out the COMMAND (1, 2, L, B, C ...)")
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                print('The solution is "L", because this way the left diagonal is flipped.')
                print("In the left up corner and in the right up corner can be seen the indications for the LEFT diagonal (L)")
                print("and the RIGHT (R) diagonal, respectively.")
                print("")
                TableroT1(not(A_A),A_B,A_C,B_A,not(B_B),B_C,C_A,C_B,not(C_C))
                print("")
                print('So...     "L" and then Enter...')
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                print("And the level is solved. Only one move was required, but the normal ones for TILES 1 normally require more.")
                print("")
                print("THIS IS THE GAME.")
                print("The first time it can seem a little bit confusing, but later, after trying it, is very easy.")
                print("We recommend you to try the first levels.")
                print("Be careful, it's common to give up the first try. However,  you can do actions randomly to get used to the tiles,")
                print("paying attention to how they flip.")
                print('After playing for some time, you will recognise some positions you have solved before, and knnow how to solve the level')
                print("from there. Here is where one trick lays: sometimes it is easier to try to get to some known position instead of directly")
                print("solving the position.")
                print("Anyway, just have fun. With a little practice you will understand the game.")
                print("")
                print("If you can't solve a level, don't worry, just exit and try a differennt  one.")
                print("People who have try it agree that it is very funny and challenging.")
                print("TRY SOME LEVELS OR THE FREE BOARD TO GET USED")
                print("")
                c=input("Press Enter to exit the tutorial    >>>")
                clear()
            elif Ellec=="2": # niveles
                clear()
                print("")
                print("                              LEVELS LIST")
                print("")
                print("            Copy (Ctrl+C) the binary number, only the numbers.")
                print("            You can paste the code in Free board or in Challenge mode.")
                print("")
                print("        1)  101010010     ",end="")
                if ((Niveles01[0])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        2)  101010101     ",end="")
                if ((Niveles01[1])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("Level solved")
                else:
                    print(" ")
                print("        3)  110111011     ",end="")
                if ((Niveles01[2])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        4)  101011111     ",end="")
                if ((Niveles01[3])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        5)  111100101     ",end="")
                if ((Niveles01[4])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        6)  101111010     ",end="")
                if ((Niveles01[5])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        7)  100101110     ",end="")
                if ((Niveles01[6])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        8)  001011110     ",end="")
                if ((Niveles01[7])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        9)  010110000     ",end="")
                if ((Niveles01[8])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       10)  010100000     ",end="")
                if ((Niveles01[9])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       11)  110010011     ",end="")
                if ((Niveles01[10])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       12)  001110110     ",end="")
                if ((Niveles01[11])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       13)  101100111     ",end="")
                if ((Niveles01[12])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       14)  010101101     ",end="")
                if ((Niveles01[13])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       15)  111110010     ",end="")
                if ((Niveles01[14])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       16)  100011011     ",end="")
                if ((Niveles01[15])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       17)  010000101     ",end="")
                if ((Niveles01[16])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       18)  110011110     ",end="")
                if ((Niveles01[17])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.3)
                c=KEYinput("          Enter to exit  >>>")
                KEYsleep(0.5)
            elif Ellec=="3": # tablero libre
                exit=0
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          FREE BOARD       ||  ",mov," moves  ||  Code: ",CodeT1("0"))
                    print("")
                    print("In Free Board you have a board to do whatever you want. There is no victory.")
                    print("To upload a code (a level or a position), type number 0. To exit, type E.")
                    print("")
                    TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(CinputT1("            >>>  "))
                    mov=mov+1
                    ControlT1(JJJ) # Ejecuta la acción correspondiente.
                    print("")
                    print("                Last command: ",JJJ)
                    KEYsleep(0.4)
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("EXITING FREE BOARD")
                        print("")
                        KEYsleep(1)
                    if JJJ=="0":
                        mov=0
                        clear()
                        print("")
                        print("")
                        print("      UPLOAD A CODE           ||  Current code: ",CodeT1("0"))
                        print("")
                        print("The information of a certain position of the game board is in the binary code.")
                        print("Depending on the status of a tile, if it is white or black, the code will show 0 or 1.")
                        print("In the right up corner of the screen, the current board code (the actual position code)")
                        print("will be displayed so that you can COPY (ctrl+C) it to have the code of the position.")
                        print("The code consists in ONLY numbers, 0 or 1.")
                        print(" (To exit and come back to Free Board, type the letter E where the code is requested)")
                        print("")
                        KEYsleep(0.5)
                        cunt=0
                        while cunt==0:
                            Www=str(KEYinput("         Paste (or write) the code (9 numbers)    >>>   "))
                            if (Www=="e")or(Www=="E")or((len(Www))==9):
                                cunt=1
                                Kods=str(Www)
                            else:
                                print("Apparently, the code provided is not correct. You might have pasted some spaces.")
                                print("Tip: write one by one the figures of the code, you have it above. Try again.")
                                print("")
                        if (Kods=="E")or(Kods=="e"):
                            print("The code upload is cancelled. Returning to Free Board.")
                            KEYsleep(0.18)
                        else:
                            CodeT1("1",Kods)
                        KEYsleep(0.5)
            elif Ellec=="4": # modo desafío
                exit=0
                clear()
                print("")
                print("      UPLOAD A CODE FOR CHALLENGE MODE       (To cancel, type letter E)")
                print("")
                print("You can upload the code you want or copy (Ctrl+C) and paste (Ctrl+V) one of the levels below.")
                print("1- copy the code of the level you want 2- paste it")
                print("COPY ONLY THE CODE  Tip: double click on the number, once it is selected in white, Ctrl+C to copy.")
                print("")
                print("        1)  101010010     ",end="")
                if ((Niveles01[0])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        2)  101010101     ",end="")
                if ((Niveles01[1])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("Level solved")
                else:
                    print(" ")
                print("        3)  110111011     ",end="")
                if ((Niveles01[2])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        4)  101011111     ",end="")
                if ((Niveles01[3])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        5)  111100101     ",end="")
                if ((Niveles01[4])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        6)  101111010     ",end="")
                if ((Niveles01[5])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        7)  100101110     ",end="")
                if ((Niveles01[6])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        8)  001011110     ",end="")
                if ((Niveles01[7])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        9)  010110000     ",end="")
                if ((Niveles01[8])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       10)  010100000     ",end="")
                if ((Niveles01[9])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       11)  110010011     ",end="")
                if ((Niveles01[10])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       12)  001110110     ",end="")
                if ((Niveles01[11])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       13)  101100111     ",end="")
                if ((Niveles01[12])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       14)  010101101     ",end="")
                if ((Niveles01[13])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       15)  111110010     ",end="")
                if ((Niveles01[14])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       16)  100011011     ",end="")
                if ((Niveles01[15])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       17)  010000101     ",end="")
                if ((Niveles01[16])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       18)  110011110     ",end="")
                if ((Niveles01[17])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                KEYsleep(0.5)
                print("")
                print("")
                cunt=0
                while cunt==0:
                    Www=str(KEYinput("         Paste (or write) the code (9 numbers)    >>>   "))
                    if (Www=="e")or(Www=="E")or((len(Www))==9):
                        cunt=1
                        Kods=str(Www)
                    else:
                        print("Apparently, the code provided is not correct. You might have pasted some spaces.")
                        print("Tip: write one by one the figures of the code, you have it above. Try again.")
                        print("")
                if (Kods=="E")or(Kods=="e"):
                    print("The code upload is cancelled. Returning to Free Board.")
                    exit=1
                else:
                    CodeT1("1",Kods)
                    Trew=CodeT1("0")
                KEYsleep(0.5)
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          CHALLENGE MODE       ||  ",mov," moves  ||  Code: ",CodeT1("0"))
                    print("")
                    print("Manage to set all tiles in the same colour, whether white or black. To exit, type letter E.")
                    print("")
                    TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(C2inputT1("            >>>  "))
                    mov=mov+1
                    ControlT1(JJJ)
                    print("")
                    print("                Last command: ",JJJ)
                    KEYsleep(0.4)
                    if ((A_A)and(A_B)and(A_C)and(B_A)and(B_B)and(B_C)and(C_A)and(C_B)and(C_C))or((not(A_A))and(not(A_B))and(not(A_C))and(not(B_A))and(not(B_B))and(not(B_C))and(not(C_A))and(not(C_B))and(not(C_C))):
                        clear()
                        print("")
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        KEYsleep(0.2)
                        print("")
                        print("                You have solved the level !!!")
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
                        print("                 VICTORY")
                        print("")
                        print("        You have set all tiles of the same colour in ",mov," moves.")
                        print("        Original code: ",Trew)
                        print("")
                        TableroT1(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                        KEYsleep(1)
                        c=KEYinput("                Enter to continue    >>>   ")
                        exit=1
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("EXITING CHALLENGE MODE")
                        print("")
                        KEYsleep(1)
                Guardar() #TO DO
            elif Ellec=="5": # generar código aleatorio
                clear()
                print("")
                print("          RANDOM CODE GENERATOR")
                print("")
                bb=str("")
                u=0
                while u<9:
                    sup=str(random.randint(0,1))
                    bb=bb+sup
                    u=u+1
                print("The random position code: ",bb,"     (it can be too difficult)")
                print("")
                KEYsleep(0.5)
                c=KEYinput("   Copy the code if you want and press Enter.          >>>")
            elif (Ellec=="6")or(Ellec=="e")or(Ellec=="E"): # salida
                TOTAL="fuera"
                clear()
                print("")
                print("")
                print("     exiting TILES 1")
                KEYsleep(1)
            else:
                clear()
                print("")
                print("       WHAT YOU'VE DONE (",Ellec,") IS NOT AN OPTION")
                KEYsleep(0.5)
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
        print("                             TILES 2")
        print("")
        print("")
        print("       Extension of TILES 1: from 3x3 to 4x4, 16 tiles in a board. ")
        print("       Same objective. New actions available to flip the tiles.")
        print("")
        KEYsleep(0.5)
        c=KEYinput("                         Enter to begin  >>>  ")
        while TOTAL=="dentro":
            clear()
            print("")
            print("                         TILES 2")
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
            print("                                 GAME MENU")
            print("")
            print("          1) Tutorial")
            print("")
            print("          2) Levels list")
            print("")
            print("          3) Free board")
            print("")
            print("          4) Challenge mode (to try levels)")
            print("")
            print("          5) Random code generator")
            print("")
            print("          6/E) Exit TILES 2")
            print("")
            print("")
            KEYsleep(0.5)
            Ellec=str(KEYinput("                                            Your choice: "))
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
                print("                            TILES 2 TUTORIAL")
                print("")
                print("     The board is like the TILES 1 board, but in 4x4.")
                TableroT2(A_A,A_B,not(A_C),not(A_D),not(B_A),not(B_B),B_C,B_D,C_A,C_B,not(C_C),not(C_D),not(D_A),not(D_B),D_C,D_D)
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                print("The aim is the same as in TILES 1: managing to equalise all the tiles, to set them with same colour.")
                print("")
                print("ACTIONS: columns (A, B, C, D), lines (1, 2, 3, 4), two diagonals (L, R), the corners (Q) and the centre (W).")
                print('Pressing "Q" the four tiles of the corners are flipped. Pressing "W" the centered little 2x2-size square is flipped.')
                print("Everything works like in TILES 1, but with two extra features (Q and W) and the extra line and column.")
                print("")
                print("     LET'S SEE AN EXAMPLE")
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                print("             EXAMPLE")
                print("")
                TableroT2(not(A_A),A_B,not(A_C),A_D,B_A,B_B,B_C,B_D,not(C_A),C_B,C_C,not(C_D),D_A,D_B,not(D_C),not(D_D))# 0101111101101100
                print("")
                print("We can see the position of the 4x4 board. Sometimes, specially in TILES 2, the player can have trouble")
                print("when it comes to visualising the solution (many tiles, more actions available...). In this cases, it can be helpful")
                print("to do random actions, but with sense. Random actions lead to positions that can be easier solved.")
                print("However, this suggestion doesn't mean that you should play without thinking. This way, you will end up")
                print("in the previous position. It turns out that a powerful method when you're stuck is to randomly move, and, after a few")
                print("actions, thinking again. This tip will no longer be necessary when you get used to TILES 2.")
                print("So, focusing again in the demo level... What can we do? We can flip a line, for example.")
                print('      Action command: "2"  (to flip the second line)')
                print("see what happens--->")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT2(not(A_A),A_B,not(A_C),A_D,not(B_A),not(B_B),not(B_C),not(B_D),not(C_A),C_B,C_C,not(C_D),D_A,D_B,not(D_C),not(D_D))
                print("")
                print("Now, the line tiles have switched their colour. We can continue by intuition (a skill developed with experience),")
                print('and do the action "R", flipping the diagonal wich starts in the RIGHT up corner.')
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT2(not(A_A),A_B,not(A_C),not(A_D),not(B_A),not(B_B),B_C,not(B_D),not(C_A),not(C_B),C_C,not(C_D),not(D_A),D_B,not(D_C),not(D_D))
                print("")
                print("As you can see, the diagonal has been flipped. Let's flip the CENTRE (W).")
                print("This is a new action, so pay attention to see the change.")
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT2(not(A_A),A_B,not(A_C),not(A_D),not(B_A),B_B,not(B_C),not(B_D),not(C_A),C_B,not(C_C),not(C_D),not(D_A),D_B,not(D_C),not(D_D))
                print("")
                print("Have you seen the difference? The four tiles placed in the centre have been flipped. The actual position is very")
                print("easy to solve, there's only a column in a different colour. Doing the corresponding action to flip that column,")
                print('            "B" and then we press Enter (as always)')
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                print("")
                clear()
                TableroT2(not(A_A),not(A_B),not(A_C),not(A_D),not(B_A),not(B_B),not(B_C),not(B_D),not(C_A),not(C_B),not(C_C),not(C_D),not(D_A),not(D_B),not(D_C),not(D_D))
                print("")
                print("The level is solved! It can seem very difficult, but it isn't much harder than the 3x3. Just keep in mind")
                print("that there are more actions available. Some people reported TILES 2 to be easier than TILES 1, probably")
                print("because once you've undertood the 3x3 this is similar, but funnier. It is common to solve many levels")
                print("by doing random actions. Novetheless, try to figure out the steps of the solution from the beginning,")
                print("it is not that hard, and will increase your spatial intelligence and focusing skills. ENJOY!!!")
                print("")
                c=KEYinput("                        Press Enter to exit the tutorial  >>>")
                KEYsleep(0.5)
                clear()
            elif Ellec=="2": # niveles
                clear()
                print("")
                print("                              LEVELS LIST")
                print("")
                print("            Copy (Ctrl+C) the binary number, only the numbers.")
                print("            You can paste the code in Free board or in Challenge mode.")
                print("")
                print("        1)  1001011001101001     ",end="")
                if ((Niveles01[18])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        2)  0001010000101000     ",end="")
                if ((Niveles01[19])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("Level solved")
                else:
                    print(" ")
                print("        3)  0000100110010000     ",end="")
                if ((Niveles01[20])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        4)  1011001011011011     ",end="")
                if ((Niveles01[21])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        5)  0011111110011010     ",end="")
                if ((Niveles01[22])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        6)  1010000010010011     ",end="")
                if ((Niveles01[23])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        7)  1101100011100100     ",end="")
                if ((Niveles01[24])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        8)  1101111001110100     ",end="")
                if ((Niveles01[25])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        9)  0010100000010100     ",end="")
                if ((Niveles01[26])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       10)  1010100100000011     ",end="")
                if ((Niveles01[27])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       11)  0101101001010101     ",end="")
                if ((Niveles01[28])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       12)  0111010011011110     ",end="")
                if ((Niveles01[29])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       13)  1011111001111101     ",end="")
                if ((Niveles01[30])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       14)  0101110011001010     ",end="")
                if ((Niveles01[31])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       15)  1011111010000010     ",end="")
                if ((Niveles01[32])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       16)  1100100111110101     ",end="")
                if ((Niveles01[33])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       17)  0011100111110101     ",end="")
                if ((Niveles01[34])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       18)  0010100011101011     ",end="")
                if ((Niveles01[35])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.3)
                c=KEYinput("          Enter to exit  >>>")
                KEYsleep(0.5)
            elif Ellec=="3": # tablero libre
                exit=0
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          FREE BOARD       ||  ",mov," moves  ||  Code: ",CodeT2("0"))
                    print("")
                    print("In Free Board you have a board to do whatever you want. There is no victory.")
                    print("To upload a code (a level or a position), type number 0. To exit, type E.")
                    print("")
                    TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D)
                    JJJ=str(CinputT2("            >>>  "))
                    mov=mov+1
                    ControlT2(JJJ)
                    print("")
                    print("                Last command: ",JJJ)
                    KEYsleep(0.4)
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("EXITING FREE BOARD")
                        print("")
                        KEYsleep(1)
                    if JJJ=="0":
                        mov=0
                        clear()
                        print("")
                        print("")
                        print("      UPLOAD A CODE           ||  Current code: ",CodeT2("0"))
                        print("")
                        print("The information of a certain position of the game board is in the binary code.")
                        print("Depending on the status of a tile, if it is white or black, the code will show 0 or 1.")
                        print("In the right up corner of the screen, the current board code (the actual position code)")
                        print("will be displayed so that you can COPY (ctrl+C) it to have the code of the position.")
                        print("The code consists in ONLY numbers, 0 or 1.")
                        print(" (To exit and come back to Free Board, type the letter E where the code is requested)")
                        print("")
                        KEYsleep(0.5)
                        cunt=0
                        while cunt==0:
                            Www=str(KEYinput("         Paste (or write) the code (16 numbers)    >>>   "))
                            if (Www=="e")or(Www=="E")or((len(Www))==16):
                                cunt=1
                                Kods=str(Www)
                            else:
                                print("Apparently, the code provided is not correct. You might have pasted some spaces.")
                                print("Tip: write one by one the figures of the code, you have it above. Try again.")
                                print("")
                        if (Kods=="E")or(Kods=="e"):
                            print("The code upload is cancelled. Returning to Free Board.")
                            KEYsleep(0.18)
                        else:
                            CodeT2("1",Kods)
                        KEYsleep(0.5)
            elif Ellec=="4": # modo desafío
                exit=0
                clear()
                print("")
                print("      UPLOAD A CODE FOR CHALLENGE MODE       (To cancel, type letter E)")
                print("")
                print("You can upload the code you want or copy (Ctrl+C) and paste (Ctrl+V) one of the levels below.")
                print("1- copy the code of the level you want 2- paste it")
                print("COPY ONLY THE CODE  Tip: double click on the number, once it is selected in white, Ctrl+C to copy.")
                print("")
                print("        1)  1001011001101001     ",end="")
                if ((Niveles01[18])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        2)  0001010000101000     ",end="")
                if ((Niveles01[19])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("Level solved")
                else:
                    print(" ")
                print("        3)  0000100110010000     ",end="")
                if ((Niveles01[20])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        4)  1011001011011011     ",end="")
                if ((Niveles01[21])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        5)  0011111110011010     ",end="")
                if ((Niveles01[22])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        6)  1010000010010011     ",end="")
                if ((Niveles01[23])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        7)  1101100011100100     ",end="")
                if ((Niveles01[24])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        8)  1101111001110100     ",end="")
                if ((Niveles01[25])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        9)  0010100000010100     ",end="")
                if ((Niveles01[26])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       10)  1010100100000011     ",end="")
                if ((Niveles01[27])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       11)  0101101001010101     ",end="")
                if ((Niveles01[28])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       12)  0111010011011110     ",end="")
                if ((Niveles01[29])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       13)  1011111001111101     ",end="")
                if ((Niveles01[30])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       14)  0101110011001010     ",end="")
                if ((Niveles01[31])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       15)  1011111010000010     ",end="")
                if ((Niveles01[32])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       16)  1100100111110101     ",end="")
                if ((Niveles01[33])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       17)  0011100111110101     ",end="")
                if ((Niveles01[34])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       18)  0010100011101011     ",end="")
                if ((Niveles01[35])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.5)
                cunt=0
                while cunt==0:
                    Www=str(KEYinput("         Paste (or write) the code (16 numbers)    >>>   "))
                    if (Www=="e")or(Www=="E")or((len(Www))==16):
                        cunt=1
                        Kods=str(Www)
                    else:
                        print("Apparently, the code provided is not correct. You might have pasted some spaces.")
                        print("Tip: write one by one the figures of the code, you have it above. Try again.")
                        print("")
                if (Kods=="E")or(Kods=="e"):
                    print("The code upload is cancelled. Returning to Free Board.")
                    exit=1
                else:
                    CodeT2("1",Kods)
                    Trew=CodeT2("0")
                KEYsleep(0.5)
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          CHALLENGE MODE       ||  ",mov," moves  ||  Code: ",CodeT2("0"))
                    print("")
                    print("Manage to set all tiles in the same colour, whether white or black. To exit, type letter E.")
                    print("")
                    TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D)
                    JJJ=str(C2inputT2("            >>>  "))
                    mov=mov+1
                    ControlT2(JJJ)
                    print("")
                    print("                Last command: ",JJJ)
                    KEYsleep(0.4)
                    if ((A_A)and(A_B)and(A_C)and(A_D)and(B_A)and(B_B)and(B_C)and(B_D)and(C_A)and(C_B)and(C_C)and(C_D)and(D_A)and(D_B)and(D_C)and(D_D))or((not(A_A))and(not(A_B))and(not(A_C))and(not(A_D))and(not(B_A))and(not(B_B))and(not(B_C))and(not(B_D))and(not(C_A))and(not(C_B))and(not(C_C))and(not(C_D))and(not(D_A))and(not(D_B))and(not(D_C))and(not(D_D))):
                        clear()
                        print("")
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        KEYsleep(0.2)
                        print("")
                        print("                You have solved the level !!!")
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
                        print("                 VICTORY")
                        print("")
                        print("        You have set all tiles of the same colour in ",mov," moves.")
                        print("        Original code: ",Trew)
                        print("")
                        TableroT2(A_A,A_B,A_C,A_D,B_A,B_B,B_C,B_D,C_A,C_B,C_C,C_D,D_A,D_B,D_C,D_D)
                        KEYsleep(1)
                        c=KEYinput("                Enter to continue    >>>   ")
                        exit=1
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("EXITING CHALLENGE MODE")
                        print("")
                        KEYsleep(1)
                Guardar() #TO DO
            elif Ellec=="5": # generar código aleatorio
                clear()
                print("")
                print("          RANDOM CODE GENERATOR")
                print("")
                bb=str("")
                u=0
                while u<16:
                    sup=str(random.randint(0,1))
                    bb=bb+sup
                    u=u+1
                print("The random position code: ",bb,"     (it can be too difficult)")
                print("")
                KEYsleep(0.5)
                c=KEYinput("   Copy the code if you want and press Enter.          >>>")
            elif (Ellec=="6")or(Ellec=="e")or(Ellec=="E"): # salida
                TOTAL="fuera"
                clear()
                print("")
                print("")
                print("     exiting TILES 2")
                KEYsleep(1)
            else:
                clear()
                print("")
                print("       WHAT YOU'VE DONE (",Ellec,") IS NOT AN OPTION")
                KEYsleep(0.5)
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
        print("                        TILES 3")
        print("")
        print("")
        print("       Different aim. In this version, you have to manage to imitate")
        print("       the right board, the model. 3x3 board, same actions as TILES 1.")
        print("")
        KEYsleep(0.5)
        c=KEYinput("                         Enter to begin  >>>  ")
        while TOTAL=="dentro":
            clear()
            print("")
            print("                     TILES 3")
            print("")
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            print("")
            TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
            print("         _________________________________________________________")
            print("         _________________________________________________________")
            KEYsleep(0.5)
            clear()
            print("")
            print("                                 GAME MENU")
            print("")
            print("          1) Tutorial")
            print("")
            print("          2) Levels list")
            print("")
            print("          3) Free board")
            print("")
            print("          4) Challenge mode (to try levels)")
            print("")
            print("          5) Random code generator")
            print("")
            print("          6/E) Exit TILES 3")
            print("")
            print("")
            KEYsleep(0.5)
            Ellec=str(KEYinput("                                            Your choice: "))
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
                print("                            TILES 3 TUTORIAL")
                print("")
                print("In this this version of TILES, the screen displays 2 boards.")
                print("The left board is the interactive one. Your actions affect this board.")
                print("The available moves are the same as TILES 1 moves, columns (A, B, C), lines (1, 2, 3)")
                print("and the 2 diagonals (L, R).")
                print("However, the aim is no longer to equalise all tiles. Now, you have to imitate the model board,")
                print("placed at the right part of the screen. This board doesn't change.")
                print("")
                TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,C_A,not(C_B),not(C_C))
                print("")
                print("We have to manage to set our tiles (in the left board) as in the right board, the model.")
                print("We can start flipping the third line (3).")
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT3(A_A,not(A_B),A_C,not(B_A),B_B,B_C,not(C_A),C_B,C_C)
                print("")
                print('The next step would be the "A" action. Continue the tutorial and pay attention.')
                print("Can you already visualise the solution?")
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT3(not(A_A),not(A_B),A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                print("")
                print("Take a look at both boards. If we flip the first line, they will look the same.")
                print('   "1" + Enter  (remember that to send a command to the computer, you have to press Enter)')
                print("")
                c=KEYinput("                        Press Enter to continue the tutorial  >>>")
                clear()
                TableroT3(A_A,A_B,not(A_C),B_A,B_B,B_C,C_A,C_B,C_C)
                print("")
                print("DONE! Now, the two boards have the same position.")
                print("There are many options, many of them not represneted in the 20 levels of TILES 3.")
                print("We encourage you to send challenges with your friends.")
                print("This one is the hardest TILES, do not give up.")
                print("")
                c=KEYinput("                        Press Enter to exit the tutorial  >>>")
                KEYsleep(0.5)
                clear()
            elif Ellec=="2": # niveles
                clear()
                print("")
                print("                              LEVELS LIST")
                print("")
                print("            Copy (Ctrl+C) the binary number, only the numbers.")
                print("            You can paste the code in Free board or in Challenge mode.")
                print("")
                print("        1)  110101001111111010     ",end="")
                if ((Niveles01[36])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        2)  000001010001110110     ",end="")
                if ((Niveles01[37])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("Level solved")
                else:
                    print(" ")
                print("        3)  101111100010101100     ",end="")
                if ((Niveles01[38])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        4)  100101011111000010     ",end="")
                if ((Niveles01[39])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        5)  011010011000111101     ",end="")
                if ((Niveles01[40])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        6)  101100000100011011     ",end="")
                if ((Niveles01[41])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        7)  100011011011000110     ",end="")
                if ((Niveles01[42])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        8)  011000000011010000     ",end="")
                if ((Niveles01[43])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        9)  101000100100111000     ",end="")
                if ((Niveles01[44])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       10)  010110101001001011     ",end="")
                if ((Niveles01[45])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       11)  110001010110011101     ",end="")
                if ((Niveles01[46])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       12)  011100010000101110     ",end="")
                if ((Niveles01[47])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       13)  001010101101000011     ",end="")
                if ((Niveles01[48])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       14)  111110011011111000     ",end="")
                if ((Niveles01[49])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       15)  111101110100100101     ",end="")
                if ((Niveles01[50])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       16)  011001101111010110     ",end="")
                if ((Niveles01[51])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       17)  011011101011011010     ",end="")
                if ((Niveles01[52])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       18)  010011000001111100     ",end="")
                if ((Niveles01[53])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       19)  101010011110100000     ",end="")
                if ((Niveles01[54])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       20)  101000100000011011     ",end="")
                if ((Niveles01[55])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.3)
                c=KEYinput("          Enter to exit   >>>")
                KEYsleep(0.5)
            elif Ellec=="3": # tablero libre
                exit=0
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          FREE BOARD       ||  ",mov," moves  ||  Code: ",CodeT3("0"))
                    print("")
                    print("In Free Board you have a board to do whatever you want. There is no victory.")
                    print("To upload a code (a level or a position), type number 0. To exit, type E.")
                    print("")
                    TableroT3(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(CinputT3("            >>>  "))
                    mov=mov+1
                    ControlT3(JJJ)
                    print("")
                    print("                Last command: ",JJJ)
                    KEYsleep(0.4)
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("EXITING FREE BOARD")
                        print("")
                        KEYsleep(1)
                    if JJJ=="0":
                        mov=0
                        clear()
                        print("")
                        print("")
                        print("      UPLOAD A CODE           ||  Current code: ",CodeT3("0"))
                        print("")
                        print("The information of a certain position of the game board is in the binary code.")
                        print("Depending on the status of a tile, if it is white or black, the code will show 0 or 1.")
                        print("In the right up corner of the screen, the current board code (the actual position code)")
                        print("will be displayed so that you can COPY (ctrl+C) it to have the code of the position.")
                        print("The code consists in ONLY numbers, 0 or 1.")
                        print(" (To exit and come back to Free Board, type the letter E where the code is requested)")
                        print("")
                        KEYsleep(0.5)
                        cunt=0
                        while cunt==0:
                            Www=str(KEYinput("         Paste (or write) the code (18 numbers)    >>>   "))
                            if (Www=="e")or(Www=="E")or((len(Www))==18):
                                cunt=1
                                Kods=str(Www)
                            else:
                                print("Apparently, the code provided is not correct. You might have pasted some spaces.")
                                print("Tip: write one by one the figures of the code, you have it above. Try again.")
                                print("")
                        if (Kods=="E")or(Kods=="e"):
                            print("The code upload is cancelled. Returning to Free Board.")
                            KEYsleep(0.18)
                        else:
                            CodeT3("1",Kods)
                        KEYsleep(0.5)
            elif Ellec=="4": # modo desafío
                exit=0
                clear()
                print("")
                print("      UPLOAD A CODE FOR CHALLENGE MODE       (To cancel, type letter E)")
                print("")
                print("You can upload the code you want or copy (Ctrl+C) and paste (Ctrl+V) one of the levels below.")
                print("1- copy the code of the level you want 2- paste it")
                print("COPY ONLY THE CODE  Tip: double click on the number, once it is selected in white, Ctrl+C to copy.")
                print("")
                print("        1)  110101001111111010     ",end="")
                if ((Niveles01[36])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        2)  000001010001110110     ",end="")
                if ((Niveles01[37])=="1"):  # 18 T1 - 18 T2 - 20 T3 - Total=56
                    print("Level solved")
                else:
                    print(" ")
                print("        3)  101111100010101100     ",end="")
                if ((Niveles01[38])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        4)  100101011111000010     ",end="")
                if ((Niveles01[39])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        5)  011010011000111101     ",end="")
                if ((Niveles01[40])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        6)  101100000100011011     ",end="")
                if ((Niveles01[41])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        7)  100011011011000110     ",end="")
                if ((Niveles01[42])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        8)  011000000011010000     ",end="")
                if ((Niveles01[43])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("        9)  101000100100111000     ",end="")
                if ((Niveles01[44])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       10)  010110101001001011     ",end="")
                if ((Niveles01[45])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       11)  110001010110011101     ",end="")
                if ((Niveles01[46])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       12)  011100010000101110     ",end="")
                if ((Niveles01[47])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       13)  001010101101000011     ",end="")
                if ((Niveles01[48])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       14)  111110011011111000     ",end="")
                if ((Niveles01[49])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       15)  111101110100100101     ",end="")
                if ((Niveles01[50])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       16)  011001101111010110     ",end="")
                if ((Niveles01[51])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       17)  011011101011011010     ",end="")
                if ((Niveles01[52])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       18)  010011000001111100     ",end="")
                if ((Niveles01[53])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       19)  101010011110100000     ",end="")
                if ((Niveles01[54])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("       20)  101000100000011011     ",end="")
                if ((Niveles01[55])=="1"):
                    print("Level solved")
                else:
                    print(" ")
                print("")
                print("")
                KEYsleep(0.5)
                cunt=0
                while cunt==0:
                    Www=str(KEYinput("         Paste (or write) the code (18 numbers)    >>>   "))
                    if (Www=="e")or(Www=="E")or((len(Www))==18):
                        cunt=1
                        Kods=str(Www)
                    else:
                        print("Apparently, the code provided is not correct. You might have pasted some spaces.")
                        print("Tip: write one by one the figures of the code, you have it above. Try again.")
                        print("")
                if (Kods=="E")or(Kods=="e"):
                    print("The code upload is cancelled. Returning to Free Board.")
                    exit=1
                else:
                    CodeT3("1",Kods)
                    Trew=CodeT3("0")
                KEYsleep(0.5)
                mov=0
                while exit==0:
                    clear()
                    print("")
                    print("          CHALLENGE MODE       ||  ",mov," moves  ||  Code: ",CodeT3("0"))
                    print("")
                    print("Manage to imitate the position of the right model board. To exit, type letter E.")
                    print("")
                    TableroT3(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                    print("")
                    JJJ=str(C2inputT3("            >>>  "))
                    mov=mov+1
                    ControlT3(JJJ)
                    print("")
                    print("                Last command: ",JJJ)
                    KEYsleep(0.4)
                    if ((A_A==a1a)and(A_B==a1b)and(A_C==a1c)and(B_A==b1a)and(B_B==b1b)and(B_C==b1c)and(C_A==c1a)and(C_B==c1b)and(C_C==c1c)):
                        clear()
                        print("")
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        print("")
                        KEYsleep(0.2)
                        print("               VICTORY")
                        KEYsleep(0.2)
                        print("")
                        print("                You have solved the level !!!")
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
                        print("                 VICTORY")
                        print("")
                        print("        You have imitated the right board in ",mov," moves.")
                        print("        Original code: ",Trew)
                        print("")
                        TableroT3(A_A,A_B,A_C,B_A,B_B,B_C,C_A,C_B,C_C)
                        KEYsleep(1)
                        c=KEYinput("                Enter to continue    >>>   ")
                        exit=1
                    if (JJJ=="E")or(JJJ=="e"):
                        exit=1
                        print("EXITING CHALLENGE MODE")
                        print("")
                        KEYsleep(1)
                Guardar() #TO DO
            elif Ellec=="5": # generar código aleatorio
                clear()
                print("")
                print("          RANDOM CODE GENERATOR")
                print("")
                bb=str("")
                u=0
                while u<18:
                    sup=str(random.randint(0,1))
                    bb=bb+sup
                    u=u+1
                print("The random position code: ",bb,"     (it can be too difficult)")
                print("")
                KEYsleep(0.5)
                c=KEYinput("   Copy the code if you want and press Enter.          >>>")
            elif (Ellec=="6")or(Ellec=="e")or(Ellec=="E"): # salida
                TOTAL="fuera"
                clear()
                print("")
                print("")
                print("     exiting TILES 3")
                KEYsleep(1)
            else:
                clear()
                print("")
                print("       WHAT YOU'VE DONE (",Ellec,") IS NOT AN OPTION")
                KEYsleep(0.5)
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
            while laurus<57:
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
        print("           USER")
        print("")
        print("       User number ",NumUsuario)
        print("")
        print("       ",NumNiveles," levels solved")
        print("")
        print("           TILES 1  .....  ",Tes1NumNiveles,"/18 levels")
        print("           TILES 2  .....  ",Tes2NumNiveles,"/18 levels")
        print("           TILES 3  .....  ",Tes3NumNiveles,"/20 levels")
        print("")
        print("_________________________________________________________________")
        print("")
        print("       Commands:")
        print("")
        print("          Exit User section (1/S/E)")
        print("          Delete user (2/U/L)   >>> This action creates a new user")
        print("          Save information (3/G/B)")
        print("")
        KEYsleep(1)
        y=0
        while y==0:
            Comando=str(KEYinput("     Command wanted: "))
            if (Comando=="G")or(Comando=="g")or(Comando=="B")or(Comando=="b")or(Comando=="3")or(Comando=="1")or(Comando=="S")or(Comando=="E")or(Comando=="2")or(Comando=="U")or(Comando=="L")or(Comando=="u")or(Comando=="s")or(Comando=="e")or(Comando=="l"):
                y=1
                print(" OK  --  Valid command")
            else:
                print("Invalid command.")
        if (Comando=="1")or(Comando=="S")or(Comando=="E")or(Comando=="s")or(Comando=="e"):
            print("")
            print("           EXITING USER SECTION")
            KEYsleep(1)
        elif (Comando=="2")or(Comando=="U")or(Comando=="L")or(Comando=="u")or(Comando=="l"):
            print("")
            print("  --- Are you sure that you want to delete the current user?")
            print("      This will remove the information.   Yes: y ; No: n")
            print("")
            Comando=str(KEYinput(" y/n     >>> "))
            if Comando=="y":
                print("")
                print("         REMOVING USER ",NumUsuario," INFORMATION")
                KEYsleep(0.3)
                print("")
                print("Creating new user...")
                NumUsuario=NumUsuario+1
                if NumUsuario>9:
                    NumUsuario=1
                    print("New user: USER 1")
                KEYsleep(0.3)
                print("Adjusting number of levels...  [1/5]")
                NumNiveles=0
                KEYsleep(0.3)
                print("Adjusting number of levels...  [2/5]")
                Tes1NumNiveles=0
                KEYsleep(0.3)
                print("Adjusting number of levels...  [3/5]")
                Tes2NumNiveles=0
                KEYsleep(0.3)
                print("Adjusting number of levels...  [4/5]")
                Tes3NumNiveles=0
                KEYsleep(0.3)
                print("Adjusting number of levels...  [5/5]")
                w=0
                try:
                    while w<(NumeroTotaldeNiveles+2):
                        Niveles01[w]="0"
                        w=w+1
                except:
                    pass
                KEYsleep(0.3)
                print("Modifying game files...  [1/4]")
                KEYsleep(0.3)
                print("Modifying game files...  [2/4]")
                KEYsleep(0.3)
                print("Modifying game files...  [3/4]")
                KEYsleep(0.3)
                print("Modifying game files...  [4/4]")
                print("")
                KEYsleep(0.5)
                print("Process finished successfully. New user: USER ",NumUsuario)
                print("SAVE the information in the USER section to accept the new user.")
                print("")
                Guardar()
                c=KEYinput("          Enter to exit USER and return to General menu >>>  ")
            elif Comando=="n":
                print("")
                print("  NEW USER CREATION CANCELLED")
                print("")
                print("Your user is: USER ",NumUsuario)
            else:
                print("")
                print("The command is not valid, it isn't an option. The default option is to CANCEL")
                print("the creation of the new user, because if not, the player could lose his/her information.")
            KEYsleep(1)
        elif (Comando=="3")or(Comando=="G")or(Comando=="g")or(Comando=="B")or(Comando=="b"):
            print("               SAVE INFORMATION")
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
            print("---- Information saved.    ",YaVes," --- ",Retaila)
            print("")
            c=KEYinput("          Enter to return to General menu >>>")
    elif Juego=="5": # info
        clear()
        print("")
        print("")
        print("                                   INFORMATION AND MORE")
        print("")
        print("")
        print("     TALK TO YOUR FRIENDS ABOUT THE GAME, THIS WILL HELP A LOT THE DIFFUSION OF THE GAME")
        print("")
        print("                        https://sites.google.com/view/teselas/inicio")
        print("")
        print("                             email addresses of the developers: ")
        print("")
        print("                pablo.aufhause@gmail.com             diego.herasmiguez@gmail.com")
        print("")
        print("")
        print("Despite the simple graphics, the game is very interesting and many people have enjoyed it.")
        print("")
        print("                                 FUTURE PROJECTS")
        print("")
        print("")
        print("      We are improving always, so your collaboration is welcomed. These are some goals to achieve:")
        print("")
        print("-- Improving the game app (.exe). To add interfaces and a version for macOS.")
        print("")
        print("-- Creating the 4x4 version of TILES 3.")
        print("")
        print("-- Learning about the mathematical aspect of TILES.")
        print("")
        print("-- Creating the game app for smartphones.")
        print("")
        print("      You can help with any of this goals, being very helpful. Join the present developement team")
        print("      and participate in future projects and videogames. Your name will appear in the game credits.")
        print("      Contact us to ask about. The team consist in Pablo and, at least 5 members.")
        print("      We don't want profit, the objective is to spread the game to as many people as posible.")
        print("      To maintain the website (in a future) and the Google Play developer account, we need to spend money.")
        print("      Help us supporting the efforts donating money, doesn't matter the amount. To do it, text")
        print("      the developers.")
        print("      THANK YOU. Donating, you have the latest versions of the game, and the new videogames released.")
        print("      Whether you are likely to donate or not, TELLING your friends about the game is crucial, so,")
        print("      if you consider the game interesting and creative (it's totally original), HELP.")
        print("")
        print("Here is some extra information about the game TILES (TESELAS). The website is continously being developed.")
        print("")
        print("                   Website link:  https://sites.google.com/view/teselas/inicio")
        print("")
        print("                             To contact the creators: ")
        print("")
        print("                pablo.aufhause@gmail.com             diego.herasmiguez@gmail.com")
        print("")
        print("")
        print("           The text that appears at the beginning of the game is shown below:")
        print("")
        print("-----------------------------------------------------------------------------------------------------------------")
        print("")
        print("                                        TILES    ")
        print("")
        print("")
        print("                    You will inmerse yourself in the game TILES experience.")
        print("")
        print("")
        print("                             email addresses of the developers: ")
        print("")
        print("                pablo.aufhause@gmail.com             diego.herasmiguez@gmail.com")
        print("")
        print("       The game was programmed by Pablo de la Fuente Sancho. The original idea is his, too.")
        print("  Diego Heras is a friend who helped writing the tutorials in spanish, and testing the game many times")
        print("             to search for problems. He also helped suggesting navigation ideas.")
        print("")
        print("")
        print("                                            INFORMATION")
        print("")
        print("A long time ago, a ten-year-old Pablo created a game, originally played with paper pieces." )
        print("The game didn't have a name, it came later. The original (classic) board of the game consists in a 3x3 distribution" )
        print("of elements with 2 positions, for instance white and black." )
        print("To play, the person has to flip the elements (little paper pieces in the classic version) by hand, according" )
        print("to some rules. However, the process was tiresome, boring. That's the reason why the computer version was created." )
        print("It is an app for the Windows desktop, programmed in the coding language Python." )
        print("There are two other versions of the game, TILES 2 and TILES 3, with some differences." )
        print("To play, you will find a tutorial for each version in the section thereof." )
        print("It is a 1 player game, but you can send challenges to your friends, as a competition." )
        print('')
        print('The original name in spanish is "Teselas", the name of each single piece of a mosaic. It is because the game board')
        print('resembles a mosaic, in which the "teselas" are the tiles, the translation to english. Although it is not')
        print('an accurate translation, it keeps the idea of dynamic tiles, which the player flips with actions.')
        print("" )
        print("All rights related to this game and the app belong to Pablo de la Fuente Sancho." )
        print("If you send the game to a friend so that he/she can play it, contact one of these emails" )
        print("pablo.aufhause@gmail.com or diego.herasmiguez@gmail.com to let us know that the game is spreading out." )
        print("                  Write, contact, the emails to ask any question as well." )
        print("")
        print("              Website of the game: https://sites.google.com/view/teselas/inicio")
        print("")
        print("This text you're reading is the start text. It will appear every time you open the game." )
        print('Once it has been red it is not necessary to read it again, so you can skip the start text whenever you want.' )
        print('You can access the text and more information in the "Information", to which you can access via the General Menu.')
        KEYsleep(1)
        print("" )
        print("                                      HOW TO NAVIGATE THE GAME" )
        print("" )
        print("The app contains for every version (TILES 1, 2 and 3): the tutorial, some levels, the game board (free board)," )
        print("the challenge mode (also to complete the levels) and a random position generator.")
        print("The information of the position of the game is coded in the binary code. To use it, just COPY (Ctrl+C) the code" )
        print("and PASTE (Ctrl+V) it where you want to play it. This way, you are able to send the level to a friend, or to play" )
        print("the position (levels are certain positions) in the mode you prefer, pasting the code where you want.")
        print("")
        print("VERY IMPORTANT information: how to navigate the game. It is organized by 2 menus. ")
        print("The first menu is to choose the version of the game, or to access some features. This is how it looks like:")
        if True:
            print("")
            print("                                           GENERAL MENU")
            print("")
            print("")
            print("                               Choose typing the number of the choice.")
            print("")
            print("                       --   1) TILES 1      Original 3x3 game.")
            print("")
            print("                       --   2) TILES 2      4x4 extension, with new options.")
            print("")
            print("                       --   3) TILES 3      Try to imitate the model position.")
            print("")
            print("                       --   4) USER         About your game account.")
            print("")
            print("                       --   5) INFORMATION  General info of game and app.")
        print("")
        print("")
        print("The first three options are the game versions. In the the forth section you can see how many levels you've solved")
        print("and restart. In the section 5 you have more information, besides the start text.")
        print("")
        print("Inside the 3 first options, you have the Game Menu. It's the same for the three TILES games.")
        print("This is how it looks like:")
        if True:
            print("")
            print("                                 GAME MENU")
            print("")
            print("          1) Tutorial")
            print("")
            print("          2) Levels list")
            print("")
            print("          3) Free board")
            print("")
            print("          4) Challenge mode")
            print("")
            print("          5) Random code generator")
            print("")
            print("          6/E) Exit TILES 1")
        print("" )
        print("" )
        print('In the "Levels list" section, you access the LIST of the levels codes. To try a level, COPY (Ctrl+C) the code' )
        print("of the level and paste it where you want. JUST copy the binary code (0 and 1), not the space next to it." )
        print("You can PASTE (Ctrl+V) the level code in the ",'"Free board"'," section to upload the position," )
        print("so the game board adquires the position given by the code." )
        print("To try the level directly (the most recommended if you're trying levels) access the ",'"Challenge mode"')
        print("and paste there the level code you have COPIED (Ctrl+C). If you solve the level, the code in the LIST of levels,")
        print('will appear as "Solved". Remember: the levels for each TILES (1, 2 and 3) are available in "Levels list"')
        print("section of the corresponding version of TILES.")
        print("It is also posible to send the code to a friend, as a challenge.")
        print('To generate a random position (a random code) access 5, "Random code generator", and you will see the code.')
        print("Notice that the given code could be too difficult.")
        print('You can type "6" or "E" to exit the Game Menu of this TILES and returnn to the General Menu.')
        print('As always, write the choice and click "Enter" in the keyboard.')
        print("")
        print("In general, the letter E is the command for exiting the section you're in. For ALL commands, write using the keyboard")
        print("and press Enter.")
        print("Once you get used to navigate it's very easy, it works as a website. Anyway, the available commands,")
        print("the actions that can be done, are always written, so if you forget something, just read.")
        print("")
        print("                                    Let's play!!!")
        print("")
        print('FOR EVERY COMMAND, WRITE AND THEN CLICK "ENTER" IN THE KEYBOARD. TO PLAY AND NAVIGATE THE GAME,')
        print("ALL YOU NEED IS THE KEYBOARD")
        print("")
        c=KEYinput("                          Enter to return to General Menu >>>")
        KEYsleep(1)
    else:
        print("")
        print('       "',Juego,'" IS NOT AN OPTION')
        KEYsleep(1)
##########################################
