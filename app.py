try:
    import redis
    r = redis.Redis(host="localhost", port=6379)
    r.ping()
except:
    r = None