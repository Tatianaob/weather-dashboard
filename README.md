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
2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
3: Install required dependencies:

   ```bash
   pip install -r requirements.txt
   Create a config.py file and add your API key:

   Go to OpenWeatherMap and sign up to get your free API key.
   In the project directory, create a config.py file:

   API_KEY = "your_openweathermap_api_key"

4: Run the Flask application:

   ```bash
   python app.py
   Visit the app in your web browser:

   Open http://127.0.0.1:5000/ to access the weather dashboard.
   
5: Deployment
The application is hosted on an AWS EC2 instance. If you'd like to deploy this app to your own EC2 instance:
   - Create an EC2 instance in your AWS account (free tier should work).
   - SSH into your EC2 instance and install Python, Flask, and any necessary dependencies.
   - Upload the project files to the EC2 instance.
   - Run the Flask application on your EC2 instance.
   - Ensure that port 5000 is open in your EC2 instance's security group settings to allow access from the web.

Contributing
   Feel free to fork this project, make changes, and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
