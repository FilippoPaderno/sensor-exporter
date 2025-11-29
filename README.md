# Sensor Exporter con Dashboard Web

Simulatore di sensori industriali con interfaccia web dinamica e supporto per Prometheus.  
##Progetto personale realizzato per esercizio e apprendimento.
Pensato per applicazioni nel mondo dell'automazione, monitoring e IoT.

## Funzionalità

- Simulazione realistica di tre sensori:
  - Temperatura (°C)
  - Umidità (%)
  - Vibrazione (0–10)
- Endpoint `/metrics` compatibile con Prometheus
- Interfaccia web aggiornata in tempo reale (JavaScript + Flask)
- Struttura modulare e pronta per Docker

## Struttura del progetto
sensor-exporter/
 - app/
    - metrics.py # Definizione delle metriche
    - updater.py # Generazione e aggiornamento metriche
    - server.py # Flask + endpoint /metrics e /
    - templates/
      - dashboard.html # Interfaccia utente HTML
 - exporter.py # Main runner
 - requirements.txt # Dipendenze Python
 - Dockerfile # Container Docker
 - README.md 

## Avvio

### 1. Clona il progetto

```bash
git clone https://github.com/FilippoPaderno/sensor-exporter.git
cd sensor-exporter
```

### 2. Crea e attiva ambiente virtuale
```bash
python -m venv ve
source ve/bin/activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Avvia il progetto
```bash
python exporter.py
```

Dashboard: http://localhost:8000
Metriche Prometheus: http://localhost:8000/metrics

### Configurazione
Puoi personalizzare l’intervallo di aggiornamento e il range dei valori modificando config.yaml

### Esecuzione con Docker
```bash
docker build -t sensor-exporter .
docker run -p 8000:8000 sensor-exporter
```

### Esecuzione con Docker di Prometheus e Grafana
Avvia Prometheus: 
```bash
docker run -d \
  -p 9090:9090 \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

Avvia Grafana:
```bash
docker run -d \
  -p 3000:3000 \
  grafana/grafana
```

Accedi a Grafana su http://localhost:3000
User: admin, Password: admin (default)

### Importazione dashboard Grafana
- Entra in Grafana → "+" → Import
- Seleziona grafana-dashboard.json dal progetto
- Scegli Prometheus come data source
- Fatto! Visualizza i grafici delle metriche simulate 

## Tecnologie usate

- Python
- Flask
- Prometheus Client
- Threading

