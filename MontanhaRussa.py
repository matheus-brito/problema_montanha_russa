# -*- coding: utf8 -*-
import threading
from threading import Timer
import time
import random

from Carro import Carro
from Passageiro import Passageiro

import config
import semaforos
import globais

class MontanhaRussa:
    def __init__(self):
        self.carros = []
        self.threadsCarros = [] 
        self.threadCriarPassageiros = None
        
    def iniciar(self):
        for i in range(0, config.m):
            carro = Carro(i)
            threadCarro = threading.Thread(target=carro.iniciar, args=())
            
            self.carros.append(carro)
            self.threadsCarros.append(threadCarro)
            
            threadCarro.start()
            
        self.threadCriarPassageiros = threading.Thread(target=self.criarPassageiros, args=())
        
        self.threadCriarPassageiros.start()
        
        self.threadCriarPassageiros.join()
        
        semaforos.todosOsPassageirosAtendidos.acquire()
        
        globais.printMensagem("ACABOU")

    def criarPassageiros(self): 
        for i in range (0, config.n):
            passageiro = Passageiro(i)
            
            globais.fila.append(passageiro)
            globais.printMensagem("Passageiro " + str(i) + " chegou à fila.")
            threading.Thread(target=passageiro.iniciar, args=()).start()
            
            tp = random.randint(config.tpIntervalo[0], config.tpIntervalo[1])
            time.sleep(tp)
