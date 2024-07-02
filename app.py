from flask import Flask, request ,jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    try:
        # Get location data
        location_response = requests.get(f'https://ipapi.co/{client_ip}/json/')
        location_data = location_response.json()
        location = location_data.get('city', 'Unknown Location')

        # Get weather data
        weather_params = {
            "key": API_KEY,
            "q": location
        }
        weather_response = requests.get(WEATHER_API_URL, params=weather_params)
        weather_data = weather_response.json()
        temperature = weather_data['current']['temp_c']
        
        response = {
            'client_ip': client_ip,
            'location': location,
            'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}'
        }

        return jsonify(response)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',  port=5003)
