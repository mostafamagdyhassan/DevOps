from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "sensor_data.db"

@app.route("/summary")
def summary():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT AVG(temperature), MIN(temperature), MAX(temperature), AVG(humidity), MIN(humidity), MAX(humidity) FROM sensor_data")
        res = cur.fetchone()

    return jsonify({
        "avg_temp": round(res[0], 2),
        "min_temp": res[1],
        "max_temp": res[2],
        "avg_humidity": round(res[3], 2),
        "min_humidity": res[4],
        "max_humidity": res[5]
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
