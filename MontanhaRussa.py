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

def montanhaRussa():
    for i in range(0, config.m):
        threading.Thread(target=Carro(i).iniciar, args=()).start()
        
    threading.Thread(target=criarPassageiros, args=()).start()

def criarPassageiros(): 
    for i in range (0, config.n):
        passageiro = Passageiro(i)
        
        globais.fila.append(passageiro)
        threading.Thread(target=passageiro.iniciar, args=()).start()
        globais.printMensagem("Passageiro " + str(i) + " chegou à fila.")

        if(len(globais.fila) >= config.c):
            semaforos.embarque.release()
        
        tp = random.randint(config.tpIntervalo[0], config.tpIntervalo[1])
        time.sleep(tp)
    
montanhaRussa()
