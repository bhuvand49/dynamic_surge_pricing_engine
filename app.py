import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
try:
    import redis
    r = redis.Redis(host="localhost", port=6379)
    r.ping()
except:
    r = None