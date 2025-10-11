import install_packages

install_packages.check_packages()

import mqtt_callbacks

client = mqtt_callbacks.mqtt.Client()
client.on_connect = mqtt_callbacks.on_connect
client.on_message = mqtt_callbacks.on_message

client.connect(mqtt_callbacks.config.BROKER, mqtt_callbacks.config.PORT, 60)
client.loop_forever()