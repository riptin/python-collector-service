# import install_packages
# install_packages.check_packages()

from config import BROKER, PORT, USERNAME, PASSWORD
import redis_callbacks
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.on_connect = redis_callbacks.on_connect
client.on_message = redis_callbacks.on_message
client.username_pw_set(USERNAME, PASSWORD)

client.connect(BROKER, int(PORT), 60)
client.loop_forever()