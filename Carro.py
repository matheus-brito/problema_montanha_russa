# -*- coding: utf8 -*-
import time
from random import randint

import config
import semaforos
import globais

class Carro:
    
    def __init__(self, id):
        self.id= id
        globais.printMensagem("Carro " + str(self.id) + " está vazio.")

    def iniciar(self):
        while True:
            semaforos.ordemEmbarque[self.id].acquire()
            
            self.aguardarEmbarque()
            
            semaforos.ordemEmbarque[0 if self.id == config.m-1 else self.id+1].release()
            
            self.passear()
            
            semaforos.ordemDesmbarque[self.id].acquire()
            
            self.aguardarDesembarque()
            
            semaforos.ordemDesmbarque[0 if self.id == config.m-1 else self.id+1].release()
            
    def aguardarEmbarque(self):
        semaforos.embarque.acquire()
        
        for i in range (0, config.c):
            globais.fila.pop(0)
        
        time.sleep(config.te)
        globais.printMensagem("Carro " + str(self.id) + " está cheio.")
        globais.printMensagem("Fila: " + str(globais.fila))
        
    def aguardarDesembarque(self):
        time.sleep(config.te)
        globais.printMensagem("Carro " + str(self.id) + " está vazio.")
        
    def passear(self):
        time.sleep(config.tm)
        globais.printMensagem("Carro " + str(self.id) + " inciou o passeio.")