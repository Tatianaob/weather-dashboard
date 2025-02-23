from flask import Flask, render_template, request
import requests
from config import API_KEY

app = Flask(__name__)

# Replace this with your actual API key
API_KEY = API_KEY

# Function to get current weather data from OpenWeatherMap
def get_weather_data(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(base_url)
    return response.json()

# Function to get 5-day forecast data
def get_forecast_data(city):
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=5&appid={API_KEY}"
    response = requests.get(base_url)
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather_data(city)
        forecast = get_forecast_data(city)  # Fetch the 5-day forecast data

        # Determine background color based on weather description
        if weather["weather"][0]["description"].lower() in ["clear", "sunny", "few clouds"]:
            bg_color = "bg-warning"  # Sunny or clear weather: Yellow
        elif "rain" in weather["weather"][0]["description"].lower():
            bg_color = "bg-primary"  # Rainy weather: Blue
        elif "cloud" in weather["weather"][0]["description"].lower():
            bg_color = "bg-secondary"  # Cloudy weather: Gray
        else:
            bg_color = "bg-light"  # Default for other weather conditions

        return render_template("index.html", weather=weather, forecast=forecast, bg_color=bg_color)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
