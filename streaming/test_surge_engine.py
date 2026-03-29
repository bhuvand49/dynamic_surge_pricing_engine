from streaming.processing.demand_aggregation import get_demand
from streaming.processing.supply_aggregation import get_supply
from streaming.processing.surge_calculator import calculate_surge

def run_test():
    zone = "Zone_A"

    demand = get_demand(zone)
    supply = get_supply(zone)

    surge = calculate_surge(demand, supply)

    print(f"Zone: {zone}")
    print(f"Demand: {demand}")
    print(f"Supply: {supply}")
    print(f"Surge Multiplier: {surge}")

if __name__ == "__main__":
    run_test()