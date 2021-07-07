# -*- coding: utf8 -*-
import time
from random import randint

import config
import semaforos
import globais

class Carro:
    
    def __init__(self, id):
        self.id = id
        self.tempoPasseio = 0   #Tempo total de passeio deste carro
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
        semaforos.embarque.release(config.c)
        
        time.sleep(config.te)
        
        semaforos.carroCheio.acquire()
        
        globais.printMensagem("Carro " + str(self.id) + " está cheio.")
        globais.printMensagem("Fila: " + str(globais.fila))
        
    def aguardarDesembarque(self):
        semaforos.desembarque.release(config.c)
        time.sleep(config.te)
        globais.printMensagem("Carro " + str(self.id) + " está vazio.")
        
    def passear(self):
        globais.printMensagem("Carro " + str(self.id) + " inciou o passeio.")
        
        tempoInicioPasseio = time.time()
        
        time.sleep(config.tm)
        
        self.tempoPasseio += time.time() - tempoInicioPasseio
        