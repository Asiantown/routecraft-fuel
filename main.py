from src.routing.fuel_model import estimate_fuel_cost

def main():
    # Hardcoded input for now
    distance = 100  # miles
    fuel_consumption_rate = 0.04  # gallons per mile
    fuel_price = 3.50  # dollars per gallon

    cost = estimate_fuel_cost(distance, fuel_consumption_rate, fuel_price)
    print(f"Estimated fuel cost for {distance} miles: ${cost:.2f}")

if __name__ == "__main__":
    main()
