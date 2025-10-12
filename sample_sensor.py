import time, random
import paho.mqtt.publish as publish
from config import BROKER, USERNAME, PASSWORD

TOPIC = "sensors/test"
AUTH = {
    'username': USERNAME,
    'password': PASSWORD
}

while True:
    temp = round(random.uniform(20, 30), 2)
    print(f"Temp: {temp}°C")

    try:
        publish.single(TOPIC, str(temp), hostname=BROKER, auth=AUTH)
    except Exception as e:
        print("Publish failed:", e)
    time.sleep(10)