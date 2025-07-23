from prometheus_client import Gauge

#definizione metriche
#temperatura simulata in gradi celsius
temperature_gauge = Gauge('temperature_celsius', 'Temperatura in celsius')

#umidità simulata in percentuale
humidity_gauge = Gauge('humidity_percentage', 'Umidità in percentuale')

#Vibrazione simulata (0-10)
vibration_gauge = Gauge('vibration_level', 'Livello vibrazione')