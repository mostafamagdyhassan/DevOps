from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Summary, Counter, Gauge
import sqlite3

app = Flask(__name__)
DATABASE = "sensor_data.db"

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
DATA_COUNTER = Counter('sensor_data_received_total', 'Total sensor data received')
TEMP_GAUGE = Gauge('latest_temperature', 'Latest temperature value')
HUMIDITY_GAUGE = Gauge('latest_humidity', 'Latest humidity value')

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id TEXT,
            temperature REAL,
            humidity REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")

@app.route("/data", methods=["POST"])
@REQUEST_TIME.time()
def collect_data():
    d = request.json
    TEMP_GAUGE.set(d["temperature"])
    HUMIDITY_GAUGE.set(d["humidity"])
    DATA_COUNTER.inc()

    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO sensor_data (sensor_id, temperature, humidity) VALUES (?, ?, ?)",
                     (d["sensor_id"], d["temperature"], d["humidity"]))

    return jsonify({"status": "success"}), 201

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    init_db()
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
