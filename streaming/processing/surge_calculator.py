def calculate_surge(demand, supply):

    # Handle edge case
    if supply == 0:
        return 3.0

    ratio = demand / supply

    # Surge logic based on ratio
    if ratio <= 1:
        surge = 1.0
    elif ratio <= 2:
        surge = 1.5
    elif ratio <= 3:
        surge = 2.0
    else:
        surge = 3.0

    return round(surge, 2)