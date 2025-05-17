import os
import sys
import logging
import traceback

# Add project root to Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

from flask import Flask, render_template, request, jsonify

# Import with full path
from src.routing.address_route import get_route_distance
from src.routing.fuel_model import estimate_fuel_cost

# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    
    try:
        if request.method == 'POST':
            start_address = request.form.get('start_address')
            end_address = request.form.get('end_address')
            
            logging.info(f'Received addresses: {start_address} to {end_address}')
            
            try:
                # Get route distance
                distance = get_route_distance(start_address, end_address)
                logging.info(f'Route distance calculated: {distance} miles')
                
                # Default fuel parameters (can be made configurable later)
                fuel_consumption_rate = 0.04  # gallons per mile
                fuel_price = 3.50  # dollars per gallon

                # Estimate fuel cost
                cost = estimate_fuel_cost(
                    distance=distance, 
                    fuel_consumption_rate=fuel_consumption_rate, 
                    fuel_price=fuel_price
                )
                logging.info(f'Fuel cost calculated: ${cost}')

                result = {
                    'start_address': start_address,
                    'end_address': end_address,
                    'distance': round(distance, 2),
                    'cost': round(cost, 2)
                }
            except Exception as route_error:
                logging.error(f'Route calculation error: {route_error}')
                logging.error(traceback.format_exc())
                error = f"Could not retrieve route: {str(route_error)}"
    
    except Exception as e:
        logging.critical(f'Unexpected error: {e}')
        logging.critical(traceback.format_exc())
        error = f"Unexpected error: {str(e)}"
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    # Bind to all interfaces to allow external access
    app.run(host='0.0.0.0', port=5001, debug=True)
