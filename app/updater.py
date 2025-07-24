import random
import time
import threading
from .metrics import temperature_gauge, humidity_gauge, vibration_gauge
from app.config import config

#funzione che ogni tot secondi aggiorna i valori delle metriche con numeri casuali
def update_metrics():
    while True:
        temperature_gauge.set(random.uniform(
            config['temperature']['min'],
            config['temperature']['max']
        ))
        humidity_gauge.set(random.uniform(
            config['humidity']['min'],
            config['humidity']['max']
        ))
        vibration_gauge.set(random.uniform(
            config['vibration']['min'],
            config['vibration']['max']
        ))
        time.sleep(config['update_interval'])

#thread separato che aggiorna continuamente i valori
def start_updater():
    update_thread = threading.Thread(target=update_metrics)
    update_thread.daemon = True #termino il thread quando il main termina
    update_thread.start()