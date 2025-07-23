# Sensor Exporter (Prometheus + Flask)

Questo progetto simula un **esportatore di metriche** per sensori industriali, utile per testare una pipeline di **monitoraggio e automazione**.

## Funzionalità

- Generazione simulata di metriche:
  - Temperatura (°C)
  - Umidità (%)
  - Vibrazione (0–10)
- Server Flask con endpoint `/metrics`
- Compatibile con Prometheus/Grafana
- Struttura modulare e professionale

## Struttura del progetto
sensor-exporter/
│
├── app/
│ ├── metrics.py # Definizione delle metriche
│ ├── updater.py # Generazione e aggiornamento metriche
│ └── server.py # Flask + endpoint /metrics
│
├── exporter.py # Main runner
├── requirements.txt # Dipendenze
├── README.md 
└── venv/ # Ambiente virtuale

## ▶️ Avvio

### 1. Crea e attiva ambiente virtuale

```bash
python3 -m venv venv
source venv/bin/activate

### 2. Crea e attiva ambiente virtuale
```bash
pip install -r requirements.txt

### 3. Avvia il server
```bash
python exporter.py

Apri il browser su: http://localhost:8000/metrics

## Tecnologie usate

- Python
- Flask
- Prometheus Client
- Threading

