from app.server import app
from app.updater import start_updater

if __name__ == "__main__":
    start_updater()
    app.run(host="0.0.0.0", port=8000)