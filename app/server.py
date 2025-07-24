from flask import Flask, render_template
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from app.metrics import temperature_gauge, humidity_gauge, vibration_gauge

#creazione dell'app Flask
app = Flask(__name__)

#endpoint per le metriche
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/')
def home():
    temperature = temperature_gauge._value.get()
    humidity = humidity_gauge._value.get()
    vibration = vibration_gauge._value.get()
    return render_template('dashboard.html', temperature=temperature, humidity=humidity, vibration=vibration)

@app.route('/api/metrics')
def metrics_api():
    return {
        "temperature": temperature_gauge._value.get(),
        "humidity": humidity_gauge._value.get(),
        "vibration": vibration_gauge._value.get()
    }