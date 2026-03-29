import time
from collections import defaultdict

demand_count = defaultdict(int)

while True:
    zone = "Zone_A"
    demand_count[zone] += 1

    print(f"[DEMAND] {zone} → {demand_count[zone]}")
    time.sleep(3)