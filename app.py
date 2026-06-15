from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Enterprise Weather API",
        "status": "Running Successfully",
        "developer": "Radhika"
    })

@app.route("/weather")
def weather():

    # User se city lena
    city = request.args.get("city", "Pune")

    # Supported cities
    cities = {
        "Pune": (18.52, 73.85),
        "Delhi": (28.61, 77.20),
        "Mumbai": (19.07, 72.87),
        "Bangalore": (12.97, 77.59)
    }

    # Check city
    if city not in cities:
        return jsonify({
            "error": "City not supported"
        }), 404

    # Latitude & Longitude
    latitude, longitude = cities[city]

    # Weather API URL
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    try:
        response = requests.get(url)
        data = response.json()

    except Exception as e:
        return jsonify({
            "error": "Unable to fetch weather data"
        }), 500

    return jsonify({
        "city": city,
        "temperature": data["current"]["temperature_2m"]
    })
if __name__ == "__main__":
    app.run(debug=True)
    