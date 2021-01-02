# A worker process to listen for queued tasks.

import os 
from dotenv import load_dotenv
import redis
from rq import Worker, Queue, Connection

load_dotenv() 

listen = ['default']
#redis_url = os.environ['REDISTOGO_URL']
#redis_url = os.getenv((os.environ('REDISTOGO_URL')), 'redis://localhost:6379')

#conn = redis.from_url(redis_url)
conn = redis.from_url(os.getenv('REDISTOGO_URL'))

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()