from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "Enterprise Weather API",
        "status": "Running Successfully",
        "developer": "Radhika",
        "version": "2.0"
    })


@app.route("/weather")
def weather():

    city = request.args.get("city", "Pune")

    cities = {
        "Pune": (18.52, 73.85),
        "Delhi": (28.61, 77.20),
        "Mumbai": (19.07, 72.87),
        "Bangalore": (12.97, 77.59)
    }

    if city not in cities:
        return jsonify({
            "error": "City not supported",
            "supported_cities": list(cities.keys())
        }), 404

    latitude, longitude = cities[city]

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        current = data["current"]

    except Exception:
        return jsonify({
            "error": "Unable to fetch weather data"
        }), 500

    return jsonify({
        "developer": "Radhika",
        "project": "Enterprise Weather API",
        "city": city,
        "latitude": latitude,
        "longitude": longitude,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind_speed": current["wind_speed_10m"],
        "wind_direction": current["wind_direction_10m"],
        "time": current["time"]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
