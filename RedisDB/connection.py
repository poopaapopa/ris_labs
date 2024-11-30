import redis, json

class RedisCache:
    def __init__(self, config):
        self.config = config
        self.conf = self.connect()
    def connect(self):
        return redis.Redis(**self.config)
    def reconnect_if_needed(self):
        try:
            _ = self.conf.ping()
        except:
            self.conf = self.connect()
    def save(self, key, value):
        self.conf.set(key, value=json.dumps(value))
    def read(self, key):
        return self.conf.get(key)