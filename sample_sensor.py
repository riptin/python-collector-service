import time, random
import paho.mqtt.publish as publish
from config import BROKER, USERNAME, PASSWORD

AUTH = {
    'username': USERNAME,
    'password': PASSWORD
}

sensors = ['thermometer', 'infrared', 'pyrometer']

while True:
    # topic structure: sensors/<facility_id>/<sensor_type>/<sensor_id>
    facility_id = random.randint(1, 100)
    sensor_type = random.choice(sensors)
    sensor_id = random.randint(1, 100)
    temp = round(random.uniform(20, 30), 2)

    print(f"Temp: {temp}°C")

    try:
        publish.single(f"sensors/{facility_id}/{sensor_type}/{sensor_id}", str(temp), hostname=BROKER, auth=AUTH)
    except Exception as e:
        print("Publish failed:", e)
    time.sleep(10)