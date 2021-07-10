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
    def iniciar(self):
        for i in range(0, config.m):
            threading.Thread(target=Carro(i).iniciar, args=()).start()
            
        threading.Thread(target=self.criarPassageiros, args=()).start()

    def criarPassageiros(self): 
        for i in range (0, config.n):
            passageiro = Passageiro(i)
            
            globais.fila.append(passageiro)
            globais.printMensagem("Passageiro " + str(i) + " chegou à fila.")
            threading.Thread(target=passageiro.iniciar, args=()).start()
            
            tp = random.randint(config.tpIntervalo[0], config.tpIntervalo[1])
            time.sleep(tp)
