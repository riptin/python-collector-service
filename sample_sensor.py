import time, random, json
import paho.mqtt.publish as publish
from config import BROKER, USERNAME, PASSWORD
import argparse

parser = argparse.ArgumentParser(description="Interval between calls in seconds.")
parser.add_argument('-s', '--sleep', type=int, default=0, required=False, help='Interval between calls in seconds')
args = parser.parse_args()
sleep_time = args.sleep

AUTH = {
    'username': USERNAME,
    'password': PASSWORD
}

def random_mac():
    mac = [random.randint(0x00, 0xFF) for _ in range(6)]
    return ':'.join(f'{b:02X}' for b in mac)

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# topic structure: sensors/<facility_id>/<gateway>/<device_type_id>/<device_mac_address>
while True:
    # facility_id = random.randint(1, 40)
    # device_type_id = random.randint(1, 4)
    # mac_address = random_mac()
    facility_id = random.choice([19])
    gateway = random_ip()
    device_type_id = random.choice([1,2])
    device_mac_address = random.choice([
        "B2:B7:C4:CC:F3:F8",
        "7B:47:5C:D0:9A:F8",
        "E3:94:83:4E:E2:71"
    ])   
    data = {
        "value": round(random.uniform(20, 30), 2),
        "temp": random.choice(["°F", "°C"])
    }

    print(f"Temp: {data["value"]}{data["temp"]}")

    try:
        publish.single(f"sensors/{facility_id}/{gateway}/{device_type_id}/{device_mac_address}", json.dumps(data), hostname=BROKER, auth=AUTH)
    except Exception as e:
        print("Publish failed:", e)
    if sleep_time > 0:
        time.sleep(sleep_time)



