import os

BROKER = os.getenv('BROKER_ADDRESS', 'localhost')
PORT = int(os.getenv('BROKER_PORT', 1883))
TOPIC = os.getenv('BROKER_TOPIC', 'sensors/#')
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_QUEUE_NAME = os.getenv('REDIS_QUEUE_NAME', 'sensor_queue')