import time, random
import paho.mqtt.publish as publish
from config import BROKER, USERNAME, PASSWORD

AUTH = {
    'username': USERNAME,
    'password': PASSWORD
}

while True:
    # topic structure: sensors/<facility_id>/<gateway_id>/<sensor_type_id>/<sensor_id>
    facility_id = random.randint(1, 100)
    gateway_id = random.randint(1, 20)
    sensor_type_id = random.randint(1, 4)
    sensor_id = random.randint(1, 100)
    temp = round(random.uniform(20, 30), 2)

    print(f"Temp: {temp}°C")

    try:
        publish.single(f"sensors/{facility_id}/{gateway_id}/{sensor_type_id}/{sensor_id}", str(temp), hostname=BROKER, auth=AUTH)
    except Exception as e:
        print("Publish failed:", e)
    time.sleep(10)