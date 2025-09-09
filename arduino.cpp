// File: esp32_cam_streamer.ino
// Description: This Arduino sketch configures an ESP32-CAM to stream
//              video over Wi-Fi, making it accessible to the Python script.

#include "esp_camera.h"
#include <WiFi.h>

// --- Configuration ---
// Replace with your Wi-Fi credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Pin definition for the ESP32-CAM board
#define CAMERA_MODEL_AI_THINKER // ESP32-CAM model

// Included from esp32-camera.h
static camera_config_t config;

// --- Function Declarations ---
void startCameraServer();
void setup_wifi();

// --- Main Setup and Loop ---
void setup() {
  Serial.begin(115200);
  Serial.setDebugOutput(true);
  Serial.println();
  
  // Set up Wi-Fi
  setup_wifi();

  // Initialize camera
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = 5;
  config.pin_d1 = 18;
  config.pin_d2 = 19;
  config.pin_d3 = 21;
  config.pin_d4 = 36;
  config.pin_d5 = 39;
  config.pin_d6 = 34;
  config.pin_d7 = 35;
  config.pin_xclk = 0;
  config.pin_pclk = 22;
  config.pin_vsync = 23;
  config.pin_href = 25;
  config.pin_sscb_sda = 26;
  config.pin_sscb_scl = 27;
  config.pin_pwdn = 32;
  config.pin_reset = -1;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_VGA; // Set resolution (e.g., QQVGA, QVGA, VGA, SVGA, XGA, SXGA, UXGA)
  config.jpeg_quality = 10;
  config.fb_count = 1;
  
  // Initialize the camera
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }
  
  // Start the video stream server
  startCameraServer();

  // Print IP address for client connection
  Serial.print("Camera Ready! Use 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' to connect");
}

void loop() {
  // Nothing to do in the loop, as the camera server runs in the background.
  // This sketch serves a stream, it doesn't process video itself.
  delay(10000);
}

// Function to connect to Wi-Fi
void setup_wifi() {
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
}
