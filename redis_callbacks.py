import json
import redis
import sys
import asyncio
from datetime import datetime
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_QUEUE_NAME, TOPIC

if not redis:
    print("Redis package not available. Please check requirements.txt.")
    sys.exit(1)

try:
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=0)
    pong = redis_client.ping()
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

async def on_message(client, userdata, msg, max=0):
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    data = {
        "topic": topic,
        "value": payload,
        "timestamp": datetime.now().isoformat()
    }

    try:
        queue_len = await redis_client.llen(REDIS_QUEUE_NAME)

        if max > 0 and queue_len >= max:
            print("Queue limit {max} reached")
            return
    
        redis_client.rpush(REDIS_QUEUE_NAME, json.dumps(data))
    except Exception as e:
        print("Redis push error:", e)

    print(f"Processed: {topic}")

def on_message_sync(client, userdata, msg, max=0):
    asyncio.run(on_message(client, userdata, msg, max=max))