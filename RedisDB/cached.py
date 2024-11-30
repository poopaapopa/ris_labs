from RedisDB.connection import RedisCache

def cached_result(key, db_config, data=None):
    redis_cache = RedisCache(db_config)
    redis_cache.reconnect_if_needed()
    if data is not None:
        redis_cache.save(key, data)
    return redis_cache.read(key)
