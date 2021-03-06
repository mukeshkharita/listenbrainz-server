
from redis import Redis
import redis
import time
from listenbrainz.listenstore import RedisListenStore

_redis = None

def init_redis_connection(logger, host, port):
    """Create a connection to the Redis server."""

    global _redis
    while True:
        try:
            logger.info("Connecting to redis {}:{}".format(host, port))
            _redis = RedisListenStore(logger, {
                'REDIS_HOST': host,
                'REDIS_PORT': port
            })
            _redis.check_connection()
            break
        except redis.exceptions.ConnectionError as e:
            logger.error("Connection to redis failed: {}".format(str(e)))
            logger.error("Sleeping 2 seconds and trying again...")
            time.sleep(2)

    return _redis
