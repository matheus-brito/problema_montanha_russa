# -*- coding: utf8 -*-
import time
from random import randint

import config
import semaforos
import globais

class Carro:
    
    def __init__(self, id):
        self.id = id
        self.tempoInicio = time.time()  # tempo de início do funcionamento deste carro
        self.tempoPasseio = 0           # tempo total de passeio deste carro
        globais.printMensagem("Carro " + str(self.id) + " está vazio.")

    def iniciar(self):
        while True:
            # garante ordem dos carros e atomiza operação de embarque
            semaforos.ordemEmbarque[self.id].acquire()
            
            self.aguardarEmbarque()
            
            semaforos.ordemEmbarque[0 if self.id == config.m-1 else self.id+1].release()
            
            # inicia passeio
            self.passear()
            
            # garante ordem dos carros e atomiza operação de desembarque
            semaforos.ordemDesmbarque[self.id].acquire()

            self.aguardarDesembarque()

            # atualiza numPassageirosAtendidos
            globais.numPassageirosAtendidos += config.c

            # se todos os passageiros foram atendidos, libera semáforo todosOsPassageirosAtendidos
            if(globais.numPassageirosAtendidos == config.n):
                semaforos.todosOsPassageirosAtendidos.release()

            semaforos.ordemDesmbarque[0 if self.id == config.m-1 else self.id+1].release()
            
    def aguardarEmbarque(self):
        semaforos.embarque.release(config.c) # passageiros embarcam na ordem da fila
        
        time.sleep(config.te)
        
        semaforos.carroCheio.acquire()
        
        globais.printMensagem("Carro " + str(self.id) + " está cheio.")
        
    def aguardarDesembarque(self):
        semaforos.desembarque.release()    # um passgeiro desembarca por vez em qualquer ordem
        
        time.sleep(config.te)
        
        semaforos.carroVazio.acquire()
        globais.printMensagem("Carro " + str(self.id) + " está vazio.")
        
    def passear(self):
        globais.printMensagem("Carro " + str(self.id) + " inciou o passeio.")
        
        tempoInicioPasseio = time.time()
        
        time.sleep(config.tm)
        
        self.tempoPasseio += time.time() - tempoInicioPasseio
        
        globais.printMensagem("Carro " + str(self.id) + " finalizou o passeio.")
        