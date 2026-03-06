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