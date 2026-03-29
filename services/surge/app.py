import time
import random

def calculate_surge(demand, supply):
    if supply == 0:
        return 3.0

    ratio = demand / supply

    if ratio <= 1:
        return 1.0
    elif ratio <= 2:
        return 1.5
    elif ratio <= 3:
        return 2.0
    else:
        return 3.0

while True:
    # simulate real-time values
    demand = random.randint(50, 150)
    supply = random.randint(10, 100)

    surge = calculate_surge(demand, supply)

    print(f"[SURGE] Demand={demand}, Supply={supply}, Surge={surge}")

    time.sleep(5)