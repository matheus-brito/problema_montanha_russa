# -*- coding: utf8 -*-
import threading
from MontanhaRussa import MontanhaRussa

# Inicia thread com método iniciar da classe MontanhaRussa
threadMontanhaRussa = threading.Thread(target=MontanhaRussa().iniciar, args=())

threadMontanhaRussa.start()
threadMontanhaRussa.join()