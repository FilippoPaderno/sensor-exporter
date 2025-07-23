from flask import Flask
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

#creazione dell'app Flask
app = Flask(__name__)

#endpoint per le metriche
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}
