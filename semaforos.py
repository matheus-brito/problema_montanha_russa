# -*- coding: utf8 -*-

import threading
import config

'''
==================================================================
=    Este arquivo contém os semáforos utilizados no programa     =
==================================================================    
'''

embarque = threading.Semaphore(0)
desembarque = threading.Semaphore(0)

ordemEmbarque = [threading.Semaphore(0) for i in range(0, config.m)]
ordemEmbarque[0].release()

ordemDesmbarque = [threading.Semaphore(0) for i in range(0, config.m)]
ordemDesmbarque[0].release()

carroCheio = threading.Semaphore(0)

ordemPassageiros = [threading.Semaphore(0) for i in range(0, config.n)]
ordemPassageiros[0].release()

printMsg = threading.Semaphore()
