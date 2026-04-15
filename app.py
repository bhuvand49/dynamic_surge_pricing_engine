import os

redis_host = os.getenv("REDIS_HOST", "localhost")
print("Dynamic Surge Pricing Engine Running...")