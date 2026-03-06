from flask import Flask, jsonify
import redis
import random

app = Flask(__name__)

# Connect to Redis container
redis_client = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)

def compute_surge():
    demand = random.randint(1, 20)
    supply = random.randint(1, 20)

    ratio = demand / supply

    surge = 1.0

    if ratio > 1:
        surge = min(3.0, round(ratio, 2))

    return surge


@app.route("/update_surge/<zone>")
def update_surge(zone):

    surge_multiplier = compute_surge()

    redis_key = f"zone:{zone}:surge"

    # Store surge with TTL (60 seconds)
    redis_client.set(redis_key, surge_multiplier, ex=60)

    return jsonify({
        "zone": zone,
        "surge_multiplier": surge_multiplier,
        "status": "updated"
    })


@app.route("/get_surge/<zone>")
def get_surge(zone):

    redis_key = f"zone:{zone}:surge"

    surge = redis_client.get(redis_key)

    return jsonify({
        "zone": zone,
        "surge_multiplier": surge
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)