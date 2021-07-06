# -*- coding: utf8 -*-

import semaforos

'''
===================================================================
=  Este arquivo contém as variáveis e funções globais utilizadas  =
=  no programa                                                    = 
===================================================================    
'''

fila = []                   # Número de cadeiras por carro

def printMensagem(mensagem):
    semaforos.printMsg.acquire()
    print(mensagem)
    semaforos.printMsg.release()