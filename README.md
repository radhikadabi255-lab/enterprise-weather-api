# Enterprise Weather API

A Flask-based Weather API that fetches real-time weather data using the Open-Meteo API.

## Features

* Real-time weather data
* Dynamic city selection
* JSON responses
* Error handling with try-except
* Dockerized application
* Git version controlled

## Tech Stack

* Python
* Flask
* Requests
* Docker
* Git & GitHub

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Run with Docker

```bash
docker build -t weather-api .
docker run -d -p 5000:5000 --name weather-container weather-api
```

## API Endpoints

### Home

`GET /`

### Weather

`GET /weather?city=Delhi`

## Author

Radhika Dabi
