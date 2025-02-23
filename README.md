# weather-dashboard

This is a **Weather Dashboard** web application built using **Flask**. It allows users to view the weather forecast for any city by querying a weather API. The app is hosted on **AWS EC2** and is designed to be a fun, interactive way to explore the weather for different cities around the world.

## Features

- **Search for any city** to get real-time weather information.
- Displays key weather details such as temperature, humidity, wind speed, and more.
- Uses the **OpenWeatherMap API** to fetch weather data.
- Hosted on **AWS EC2** and accessible through a web browser.

## Technologies Used

- **Flask** (Python Web Framework)
- **HTML5**, **CSS3** (Frontend)
- **OpenWeatherMap API** (Weather Data)
- **AWS EC2** (Hosting)
- **GitHub** (Version Control)
- **Python 3.x**

## AWS Services Used

- **Amazon EC2 (Elastic Compute Cloud)**: Used to host the web application on a virtual machine instance in the cloud. EC2 provides scalable computing capacity to run your application.

- **Amazon Security Groups**: Configured security groups on EC2 to control the inbound and outbound traffic to the instance. Opened port 5000 to allow access to the Flask application.

## Setup

Follow these steps to get the project running on your local machine.

### Prerequisites

- **Python 3.x** (preferably in a virtual environment)
- **pip** for Python package management
- **Flask** (for web server)
- **requests** (for making HTTP requests to the weather API)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Tatianaob/weather-dashboard.git
   cd weather-dashboard
