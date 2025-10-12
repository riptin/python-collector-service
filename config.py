from dotenv import load_dotenv
import os

load_dotenv()

BROKER = os.getenv('MSQT_ADDRESS', 'localhost')
PORT = os.getenv('MSQT_PORT', 1883)
USERNAME = os.getenv('MSQT_USERNAME', '')
PASSWORD = os.getenv('MSQT_PASSWORD', '')
TOPIC = os.getenv('MSQT_TOPIC', 'sensors/#')
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')
REDIS_QUEUE_NAME = os.getenv('REDIS_QUEUE_NAME', 'sensor_queue')