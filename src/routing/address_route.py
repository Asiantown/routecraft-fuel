"""
Address to Route Distance Module for RouteCraft.

This module provides functionality to convert addresses to route distances
using the OpenRouteService API.
"""

import os
from dotenv import load_dotenv
import openrouteservice

# Load environment variables from .env file
load_dotenv()

# Initialize ORS client using API key from environment variable
ors_client = openrouteservice.Client(key=os.getenv('ORS_API_KEY'))

def get_route_distance(start_address: str, end_address: str) -> float:
    """
    Get driving distance between two addresses using OpenRouteService.
    
    Args:
        start_address (str): Starting address for route
        end_address (str): Destination address for route
    
    Returns:
        float: Distance of the route in miles
    
    Raises:
        ValueError: If geocoding or routing fails
    """
    try:
        # Geocode start address
        start_geocode = ors_client.pelias_search(text=start_address)
        if not start_geocode['features']:
            raise ValueError(f"Could not geocode start address: {start_address}")
        start_coords = start_geocode['features'][0]['geometry']['coordinates']
        
        # Geocode end address
        end_geocode = ors_client.pelias_search(text=end_address)
        if not end_geocode['features']:
            raise ValueError(f"Could not geocode end address: {end_address}")
        end_coords = end_geocode['features'][0]['geometry']['coordinates']
        
        # Get route directions
        route = ors_client.directions(
            coordinates=[start_coords, end_coords],
            profile='driving-car',
            format='geojson'
        )
        
        # Extract distance and convert to miles
        distance_meters = route['features'][0]['properties']['summary']['distance']
        distance_miles = distance_meters / 1609.34
        
        return round(distance_miles, 2)
    
    except Exception as e:
        print(f"Error calculating route distance: {e}")
        raise
