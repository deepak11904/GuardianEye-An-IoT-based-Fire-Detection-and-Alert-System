# File: fire_detection.py
# Description: This Python script uses OpenCV to connect to an ESP32-CAM,
#              analyze the video stream in real-time for fire, and
#              provide visual alerts.

import cv2
import urllib.request
import numpy as np
import threading
import time

# --- Configuration ---
# Replace this URL with the IP address of your ESP32-CAM
# To find the IP address, open the Arduino IDE's Serial Monitor after
# uploading the ESP32-CAM code and look for the IP address printed there.
ESP32_CAM_URL = 'http://192.168.1.100/cam-hi.jpg' # Use '/cam-lo.jpg' for lower resolution

# Global flag for fire detection status
fire_detected = False

# --- Functions ---
def get_stream():
    """Fetches a single frame from the ESP32-CAM's MJPEG stream."""
    try:
        req = urllib.request.urlopen(ESP32_CAM_URL)
        arr = np.array(bytearray(req.read()), dtype=np.uint8)
        frame = cv2.imdecode(arr, -1)
        return frame
    except Exception as e:
        print(f"Error fetching frame from ESP32-CAM: {e}")
        return None

def fire_detection_logic(frame):
    """
    Analyzes a single frame for the presence of fire.

    This function uses a color-based approach to detect potential fire.
    1. It converts the frame to the HSV color space, which is more robust to
       lighting changes than BGR.
    2. It defines a range of red/orange/yellow colors that are characteristic of fire.
    3. It creates a mask to isolate pixels that fall within this color range.
    4. It then uses contour detection to find connected regions of "fire" pixels.
    5. If a sufficiently large contour is found, it's considered a fire.
    """
    global fire_detected

    if frame is None:
        fire_detected = False
        return

    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color range for fire (red, orange, yellow) in HSV
    lower_fire = np.array([0, 100, 100])
    upper_fire = np.array([30, 255, 255])
    
    # Create a mask for fire-like colors
    fire_mask = cv2.inRange(hsv_frame, lower_fire, upper_fire)
    
    # Apply a Gaussian blur to the mask to reduce noise
    fire_mask = cv2.GaussianBlur(fire_mask, (21, 21), 0)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(fire_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Reset detection status
    fire_detected = False
    
    # Iterate through detected contours to check for fire
    for contour in contours:
        # Check if the contour is large enough to be considered fire
        if cv2.contourArea(contour) > 500: # Threshold can be adjusted
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, 'Fire Detected!', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            fire_detected = True
            break # Exit loop once a fire is found

def display_frame():
    """
    Main display loop for the video feed.
    
    This function continuously fetches frames from the camera,
    applies the fire detection logic, and displays the result.
    """
    while True:
        frame = get_stream()
        
        if frame is None:
            time.sleep(1) # Wait before trying again
            continue
        
        # Resize frame for faster processing and display
        frame = cv2.resize(frame, (640, 480))
        
        # Apply the fire detection logic to the frame
        fire_detection_logic(frame)
        
        # Display the output frame
        cv2.imshow('GuardianEye: Fire Detection', frame)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources
    cv2.destroyAllWindows()

if __name__ == '__main__':
    print("Starting GuardianEye Fire Detection System...")
    display_frame()
