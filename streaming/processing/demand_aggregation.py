from collections import defaultdict

demand_count = defaultdict(int)

def process_demand(event):
    if event["event_type"] == "ride_request":
        zone = event["zone_id"]
        demand_count[zone] += 1

    return demand_count