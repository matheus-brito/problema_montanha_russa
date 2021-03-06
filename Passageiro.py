# -*- coding: utf8 -*-
import time

import config
import semaforos
import globais

class Passageiro:
    
    def __init__(self, id):
        self.id = id
        self.tempoChegada = time.time()  # tempo de chegada deste passageiro à fila

    def iniciar(self):
            # garantindo embarque na ordem da fila
            semaforos.ordemPassageiros[self.id].acquire()
            
            # passageiro embarca
            semaforos.embarque.acquire()
            globais.numPassageirosEmbarque += 1
            globais.fila.pop(0)
            
            globais.printMensagem("Passageiro " + str(self.id) + " EMBARCA.")
            
            # se o carro está cheio, libera o semáforo carroCheio
            if(globais.numPassageirosEmbarque == config.c):
                semaforos.carroCheio.release()
                globais.numPassageirosEmbarque = 0
            
            # próximo passageiro da fila pode embarcar
            if(self.id + 1 < config.n):
                semaforos.ordemPassageiros[self.id + 1].release()
            
            # quando o passeio inicia, é contabilizado tempo de espera do passageiro na fila
            semaforos.carroEmPasseio.acquire()
            self.registrarTempoEspera()
            
            # passageiro desembarca
            semaforos.desembarque.acquire()
            
            globais.numPassageirosDesembarque += 1
            
            # se todos desembarcaram, libera o semáforo carroVazio
            if(globais.numPassageirosDesembarque == config.c):
                semaforos.carroVazio.release()
                globais.numPassageirosDesembarque = 0
            else:
                semaforos.desembarque.release() # próximo passageiro pode desembarcar
    
    def registrarTempoEspera(self):
        tempoEspera = time.time() - self.tempoChegada
        
        if(globais.tempoEsperaMinimo == None or tempoEspera < globais.tempoEsperaMinimo):
            globais.tempoEsperaMinimo = tempoEspera
        
        if(globais.tempoEsperaMaximo == None or tempoEspera > globais.tempoEsperaMaximo):
            globais.tempoEsperaMaximo = tempoEspera
            
        globais.somaTempoEspera += tempoEspera