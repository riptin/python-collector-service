import json
import redis
import sys
from datetime import datetime
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_QUEUE_NAME, TOPIC

if not redis:
    print("Redis package not available. Please check requirements.txt.")
    sys.exit(1)

try:
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
except Exception as e:
    print("Error connecting to redis:", e)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    topic = msg.topic
    #payload = msg.payload.decode()
    payload = msg.payload
    timestamp = datetime.now().isoformat()
    data = {"topic": topic, "value": payload, "timestamp": timestamp}

    try:
        redis_client.lpush(REDIS_QUEUE_NAME, json.dumps(data))
    except Exception as e:
        print("Redis push error:", e)

    print(f"Processed: {topic} = {payload}")