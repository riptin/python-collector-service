import redis
import json
from config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_QUEUE_NAME

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)
print('Selected DB: ',redis_client.connection_pool.connection_kwargs['db'])
items = redis_client.lrange(REDIS_QUEUE_NAME, 0, -1)
for item in items:
    data = json.loads(item)
    print(data)