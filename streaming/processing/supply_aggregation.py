from collections import defaultdict

supply_count = defaultdict(int)

def process_supply(event):
    if event["event_type"] == "driver_available":
        zone = event["zone_id"]
        supply_count[zone] += 1

    return supply_count