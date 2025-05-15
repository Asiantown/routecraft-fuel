from src.routing.fuel_model import estimate_fuel_cost
from src.routing.address_route import get_route_distance

def main():
    # Get user input for addresses
    print("RouteCraft Fuel Cost Estimator")
    start_address = input("Enter your starting address: ")
    end_address = input("Enter your destination address: ")

    try:
        # Get route distance
        distance = get_route_distance(start_address, end_address)
        
        # Default fuel parameters (can be made configurable later)
        fuel_consumption_rate = 0.04  # gallons per mile
        fuel_price = 3.50  # dollars per gallon

        # Estimate fuel cost
        cost = estimate_fuel_cost(
            distance=distance, 
            fuel_consumption_rate=fuel_consumption_rate, 
            fuel_price=fuel_price
        )

        # Print results
        print("\n📍 Route Details:")
        print(f"From: {start_address}")
        print(f"To: {end_address}")
        print(f"Total Distance: {distance:.2f} miles")
        print(f"Estimated Fuel Cost: ${cost:.2f}")

    except Exception:
        print("Could not retrieve route — please check your addresses and try again.")

if __name__ == "__main__":
    main()
