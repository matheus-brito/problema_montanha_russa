# -*- coding: utf8 -*-
import threading
from MontanhaRussa import MontanhaRussa

# Inicia thread com método iniciar da classe MontanhaRussa
threading.Thread(target=MontanhaRussa().iniciar, args=()).start()