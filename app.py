from flask import Flask
import os

app = Flask(__name__)

# Optional Redis (safe)
try:
    import redis
    r = redis.Redis(host="localhost", port=6379)
    r.ping()
except:
    r = None

@app.route("/")
def home():
    return "Dynamic Surge Pricing Engine Running 🚀"

# Render PORT fix
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)