# -*- coding: utf8 -*-

import semaforos

'''
===================================================================
=  Este arquivo contém as variáveis e funções globais utilizadas  =
=  no programa                                                    = 
===================================================================    
'''

fila = []                       # Fila de passageiros
numPassageirosEmbarque = 0      # Número de passageiros que embarcaram no carro atual
numPassageirosDesembarque = 0   # Número de passageiros que desembarcaram do carro atual
numPassageirosAtendidos = 0     # Número de passageiros atendidos desde o início da execução
tempoEsperaMinimo = None        # Tempo mínimo de espera na fila
tempoEsperaMaximo = None        # Tempo máximo de espera na fila
somaTempoEspera = 0             # Somatório dos tempos de espera na fila

def printMensagem(mensagem):
    semaforos.printMsg.acquire()
    print(mensagem)
    semaforos.printMsg.release()