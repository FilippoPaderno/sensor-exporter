import yaml
import os

# Percorso del file di configurazione
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')

# Funzione per caricare il file YAML
def load_config():
    with open(CONFIG_PATH, 'r') as file:
        return yaml.safe_load(file)

config = load_config()