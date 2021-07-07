# -*- coding: utf8 -*-

import semaforos

'''
===================================================================
=  Este arquivo contém as variáveis e funções globais utilizadas  =
=  no programa                                                    = 
===================================================================    
'''

fila = []                   # Fila de passageiros
numPassageiros = 0          # Número de passageiros no carro atual
tempoEsperaMinimo = None    # Tempo mínimo de espera na fila
tempoEsperaMaximo = None    # Tempo máximo de espera na fila
somaTempoEspera = 0         # Somatório dos tempos de espera na fila

def printMensagem(mensagem):
    semaforos.printMsg.acquire()
    print(mensagem)
    semaforos.printMsg.release()