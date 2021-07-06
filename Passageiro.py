# -*- coding: utf8 -*-
import time
from random import randint
import enum 

import config
import semaforos

class Passageiro:
    
    def __init__(self, id):
        self.id = id
        self.status = PassageiroStatus.fila

    def iniciar(self):
        while True:
            pass
    
    def __repr__(self):
        return str(self.id)

class PassageiroStatus(enum.Enum):
    fila = 1
    passeando = 2
    concluido = 3