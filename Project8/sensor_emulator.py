import requests, random, time, os

COLLECTOR_URL = os.getenv("COLLECTOR_URL", "http://data-collector:5000/data")

def generate_data():
    return {
        "sensor_id": "sensor-1",
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2)
    }

while True:
    data = generate_data()
    try:
        res = requests.post(COLLECTOR_URL, json=data)
        print(f"Sent data: {data} | Status: {res.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)
