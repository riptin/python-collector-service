import json
import redis
import sys
from datetime import datetime
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_QUEUE_NAME, TOPIC

if not redis:
    print("Redis package not available. Please check requirements.txt.")
    sys.exit(1)

try:
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0)
    pong = redis_client.ping()
    queue_len = redis_client.llen(REDIS_QUEUE_NAME)
except ConnectionError as e:
    print("Could not connect to Redis:", e)
    sys.exit(1)
except TimeoutError as e:
    print("Redis connection timed out:", e)
    sys.exit(1)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with code:", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg, max=0):
    topic = msg.topic
    try:
        payload = msg.payload.decode('utf-8')
    except UnicodeDecodeError:
        payload = msg.payload.hex() 
    data = {
        "topic": topic,
        "value": payload,
        "timestamp": datetime.now().isoformat()
    }

    queue_len = redis_client.llen(REDIS_QUEUE_NAME)

    if max and queue_len >= max:
        print(f"Queue limit reached ({max}). Skipping: {topic}")
        return

    try:
        redis_client.rpush(REDIS_QUEUE_NAME, json.dumps(data))
        print(f"Processed: {topic}")
    except Exception as e:
        print("Redis push error:", e)