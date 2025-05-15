"""
Fuel cost estimation module for RouteCraft.

This module provides a simple fuel cost estimation based on 
distance, fuel consumption rate, and current fuel prices.
"""

def estimate_fuel_cost(
    distance: float = 100.0, 
    fuel_consumption_rate: float = 0.04, 
    fuel_price: float = 3.50
) -> float:
    """
    Calculate estimated fuel cost for a route.
    
    Args:
        distance (float): Total route distance in miles
        fuel_consumption_rate (float): Fuel consumption in gallons per mile
        fuel_price (float): Price of fuel per gallon
    
    Returns:
        float: Estimated total fuel cost
    """
    fuel_cost = distance * fuel_consumption_rate * fuel_price
    return round(fuel_cost, 2)
