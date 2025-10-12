import json
import os
import redis
import sys
from datetime import datetime
import paho.mqtt.client as mqtt
import config 

if not redis:
    print("Redis package not available. Please check requirements.txt.")
    sys.exit(1)
redis_client = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASSWORD)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code:", rc)
    client.subscribe(config.TOPIC)

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    timestamp = datetime.now().isoformat()
    data = {"topic": topic, "value": payload, "timestamp": timestamp}

    try:
        redis_client.lpush(config.REDIS_QUEUE_NAME, json.dumps(data))
    except Exception as e:
        print("Redis push error:", e)

    print(f"Processed: {topic} = {payload}")