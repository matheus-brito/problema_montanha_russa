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
            # garante ordem da operação de embarque
            semaforos.ordemEmbarque[self.id].acquire()
            
            haPassageiros = self.aguardarEmbarque()
            
            if(not haPassageiros):
                semaforos.ordemEmbarque[0 if self.id == config.m-1 else self.id+1].release()
                break
            
            # inicia passeio
            semaforos.carroEmPasseio.release(config.c)  # sinaliza para passageiros que o passeio iniciou
            globais.printMensagem("++++++++++++  Carro " + str(self.id) + " inciou o passeio.     ++++++++++++")
            tempoInicioPasseio = time.time()
            
            semaforos.ordemEmbarque[0 if self.id == config.m-1 else self.id+1].release()
            
            # aguarda tempo do passeio
            time.sleep(config.tm)
            self.tempoPasseio += time.time() - tempoInicioPasseio
            
            # garante ordem da operação de desembarque
            semaforos.ordemDesmbarque[self.id].acquire()
            
            globais.printMensagem("------------  Carro " + str(self.id) + " finalizou o passeio.  ------------")

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
        
        haPassageiros = semaforos.carroCheio.acquire(timeout=60) #timeout caso nao haja mais passageiros a atender
        
        if(not haPassageiros):
            return False
        
        globais.printMensagem("Carro " + str(self.id) + " está cheio.")
        
        return True
        
    def aguardarDesembarque(self):
        semaforos.desembarque.release()    # um passgeiro desembarca por vez em qualquer ordem
        
        time.sleep(config.te)
        
        semaforos.carroVazio.acquire()
        globais.printMensagem("Carro " + str(self.id) + " está vazio.")