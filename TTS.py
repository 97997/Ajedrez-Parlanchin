import win32com.client
# This Python file uses the following encoding: utf-8
import os, sys
# coding=utf-8

def y(n):
    try:
        return {
            0: 'a',
            1: 'b',
            2: 'c',
            3: 'd',
            4: 'e',
            5: 'f',
            6: 'g',
            7: 'h'
        }[n]
    except:
        return "muy a la derecha o a la izquieda"
        #.get(x,8)

def x(n):
    try:
        return {
                0: 8,
                1: 7,
                2: 6,
                3: 5,
                4: 4,
                5: 3,
                6: 2,
                7: 1
            }[n]
    except:
        return("muy arriba o abajo")

        #.get(x,8) ## 8 is used as default
#print f('a')
def coordToText(coor):
    text =""
    if coor[1] == 8:
        text+=" Esta muy arriba o muy abajo"
        ##dasllkda coordenada y no f
    else:
        text+=str(y(coor[1]))
    text += str(x(coor[0]))
    text+=" "
    return text
def hablar(texto):
    hablador = win32com.client.Dispatch("SAPI.SpVoice")
    hablador.Speak(texto)
def pieceColorToText(color): #w(hite) or b(lack)
    return {
        'w': 'blanco',
        'b': 'negro',
    }[color]
def pieceTypeToText(piece):
    return {
        'R': 'Torre',
        'T': 'Caballo',
        'B': 'Alfil',
        'Q': 'Dama',
        'K': 'Rey',
        'P': 'Peon'
    }[piece]

#Like my doors
