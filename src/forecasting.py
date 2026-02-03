def simulate_fi_trajectory(current_value, years, baseline_growth, drivers):
    """
    Simulates FI growth based on a baseline and active policy drivers.
    
    Args:
        current_value (float): Starting ownership % (e.g., 49.0)
        years (int): Number of years to forecast (e.g., 3 for 2025-2027)
        baseline_growth (float): Natural growth rate (e.g., 0.02 for 2%)
        drivers (dict): Additive impact of specific policies
    """
    results = []
    total_impact = sum(drivers.values())
    combined_rate = baseline_growth + total_impact
    
    val = current_value
    for year in range(1, years + 1):
        val = val * (1 + combined_rate)
        # Cap at 100% (physical limit)
        val = min(val, 100.0)
        results.append(round(val, 2))
        
    return results