from collections import defaultdict

supply_count = defaultdict(int)

def process_supply(event):
    if event["event_type"] == "driver_available":
        zone = event["zone_id"]
        supply_count[zone] += 1

    return supply_count

def get_supply(zone):
    return supply_count[zone]