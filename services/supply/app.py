import time
from collections import defaultdict

supply_count = defaultdict(int)

while True:
    zone = "Zone_A"
    supply_count[zone] += 1

    print(f"[SUPPLY] {zone} → {supply_count[zone]}")
    time.sleep(4)