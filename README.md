🚨 GuardianEye: An IoT Fire Detection and Alert System
Project Tagline: Your Smart Guardian Against Fire Hazards
🌟 Project Overview
The GuardianEye system is a state-of-the-art, IoT-based solution for real-time fire detection and alerts. It leverages the power of computer vision and a dedicated wireless camera to provide a robust and proactive safety mechanism. Designed to be deployed in homes, offices, or industrial settings, GuardianEye continuously monitors its surroundings, instantly identifying potential fire hazards and sending immediate notifications to a monitoring station.

This project is a complete end-to-end solution, featuring a low-cost, Wi-Fi-enabled camera module for video streaming and a powerful Python script for intelligent image processing. By combining the affordability and flexibility of the ESP32-CAM with the advanced capabilities of OpenCV, we've created a highly effective and easy-to-use safety system.

✨ Key Features
Real-Time Video Streaming: Utilizes a lightweight ESP32-CAM to stream live video over Wi-Fi. 🌐

Intelligent Fire Detection: Employs a robust computer vision algorithm based on HSV color space and contour analysis for reliable fire identification. 🔥

Visual & Audio Alerts: Provides immediate on-screen alerts in the Python application upon fire detection. 🔔

Simple & Accessible Hardware: Built with widely available and inexpensive components, making it accessible for hobbyists and professionals alike. 🛒

Wireless and Portable: The IoT design allows for flexible placement without the need for cumbersome cables. 🔋

⚙️ Technical Architecture
The system operates in a client-server model:

ESP32-CAM (The Camera Node): The ESP32-CAM acts as a web server, capturing video frames and serving them as a series of JPEG images.

Python Script (The Analytics Engine): A Python application running on a host computer acts as the client. It connects to the ESP32-CAM's IP address, fetches the live video stream, and runs the fire detection algorithm on each frame.

📦 Hardware & Software Requirements
Hardware
ESP32-CAM Module: The core camera unit.

FTDI Programmer: For uploading code to the ESP32-CAM.

Micro-USB Cable: To connect the programmer to your computer.

Power Supply: A 5V power source for the ESP32-CAM.

Software
Arduino IDE: For programming the ESP32-CAM.

Python 3.x: For running the detection script.

Required Python Libraries:

opencv-python: pip install opencv-python

numpy: pip install numpy

🚀 Getting Started
Step 1: Flash the ESP32-CAM
Open the esp32_cam_streamer.ino sketch in the Arduino IDE.

Go to Tools > Board and select AI Thinker ESP32-CAM.

Update the Wi-Fi ssid and password variables with your network credentials.

Connect your ESP32-CAM to your computer using the FTDI programmer.

Select the correct COM port and upload the sketch.

Open the Serial Monitor to find the IP address of your ESP32-CAM.

Step 2: Configure the Python Script
Open the fire_detection.py script.

Update the ESP32_CAM_URL variable with the IP address from your Serial Monitor.

ESP32_CAM_URL = 'http://YOUR_ESP32_CAM_IP_ADDRESS/cam-hi.jpg'

Ensure you have all the required Python libraries installed.

Step 3: Run the System
Power on your ESP32-CAM.

Run the Python script from your terminal:
