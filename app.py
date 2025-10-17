# import install_packages
# install_packages.check_packages()

from config import BROKER, PORT, USERNAME, PASSWORD
from functools import partial
import redis_callbacks
import paho.mqtt.client as mqtt
import argparse

parser = argparse.ArgumentParser(description="Maximum number of queued rows.")
parser.add_argument('-m', '--max', type=int, required=False, help='Maximum number to process')
args = parser.parse_args()
max_number = args.max

client = mqtt.Client()
client.on_connect = redis_callbacks.on_connect
client.on_message = partial(redis_callbacks.on_message_sync, max=max_number)
client.username_pw_set(USERNAME, PASSWORD)

client.connect(BROKER, int(PORT), 60)
client.loop_forever()