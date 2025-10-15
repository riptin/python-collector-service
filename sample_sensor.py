import time, random, json
import paho.mqtt.publish as publish
from config import BROKER, USERNAME, PASSWORD

AUTH = {
    'username': USERNAME,
    'password': PASSWORD
}

def random_mac():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    return ':'.join(f'{b:02X}' for b in mac)

while True:
    # topic structure: sensors/<facility_id>/<gateway>/<sensor_type_id>/<sensor_id>
    facility_id = random.randint(1, 100)
    gateway = random_mac()
    sensor_type_id = random.randint(1, 4)
    sensor_device_id = random.randint(1, 100)
    data = {
        "value": round(random.uniform(20, 30), 2),
        "temp": random.choice(["°F", "°C"])
    }

    print(f"Temp: {data["value"]}{data["temp"]}")

    try:
        publish.single(f"sensors/{facility_id}/{gateway}/{sensor_type_id}/{sensor_device_id}", json.dumps(data), hostname=BROKER, auth=AUTH)
    except Exception as e:
        print("Publish failed:", e)
    time.sleep(1)



