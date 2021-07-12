# -*- coding: utf8 -*-

import threading
import config

'''
==================================================================
=    Este arquivo contém os semáforos utilizados no programa     =
==================================================================    
'''

embarque = threading.Semaphore(0)       # Sinalizar que passageiros podem embarcar
desembarque = threading.Semaphore(0)    # Sinalizar que passageiros podem desembarcar

ordemEmbarque = [threading.Semaphore(0) for i in range(0, config.m)]    # Garantir que carros permaneçam em ordem
ordemEmbarque[0].release()

ordemDesmbarque = [threading.Semaphore(0) for i in range(0, config.m)]  # Garantir que carros permaneçam em ordem
ordemDesmbarque[0].release()

carroCheio = threading.Semaphore(0)     # Sinalizar que carro está cheio
carroVazio = threading.Semaphore(0)     # Sinalizar que carro está vazio

ordemPassageiros = [threading.Semaphore(0) for i in range(0, config.n)] # Garantir que passageiros embarquem na ordem da fila
ordemPassageiros[0].release()

todosOsPassageirosAtendidos = threading.Semaphore(0)  # Sinalizar que o todos os passageiros foram atendidos 

printMsg = threading.Semaphore(0)                     # Controlar acesso ao output
printMsg.release()
