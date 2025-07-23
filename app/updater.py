import random
import time
import threading
from .metrics import temperature_gauge, humidity_gauge, vibration_gauge

#funzione che ogni tot secondi aggiorna i valori delle metriche con numeri casuali
def update_metrics():
    while True:
        temperature_gauge.set(random.uniform(20.0, 100.0))
        humidity_gauge.set(random.uniform(0.0, 100.0))
        vibration_gauge.set(random.uniform(0.0, 10.0))
        time.sleep(5)

#thread separato che aggiorna continuamente i valori
def start_updater():
    update_thread = threading.Thread(target=update_metrics)
    update_thread.daemon = True #termino il thread quando il main termina
    update_thread.start()