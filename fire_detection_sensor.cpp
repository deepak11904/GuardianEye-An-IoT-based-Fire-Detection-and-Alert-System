#include <iostream>
#include <cstdlib>
#include <chrono>
#include <thread>

/**
 * GuardianEye Fire Detection Sensor System
 * C++ implementation for IoT-based fire hazard monitoring
 * Simulates sensor readings and fire detection logic
 */

class FireDetectionSensor {
private:
    double temperatureThreshold;
    double smokeThreshold;
    double gasThreshold;
    bool alertActive;

public:
    FireDetectionSensor(double tempThresh = 60.0, double smokeThresh = 300.0, double gasThresh = 1000.0) 
        : temperatureThreshold(tempThresh), smokeThreshold(smokeThresh), gasThreshold(gasThresh), alertActive(false) {}

    // Simulate temperature sensor reading (in Celsius)
    double readTemperature() {
        return 20.0 + (rand() % 50); // Random temperature between 20-70°C
    }

    // Simulate smoke detector reading (PPM)
    double readSmokeLevel() {
        return rand() % 500; // Random smoke level 0-500 PPM
    }

    // Simulate gas sensor reading (PPM)
    double readGasLevel() {
        return rand() % 1500; // Random gas level 0-1500 PPM
    }

    // Fire detection logic
    bool detectFire() {
        double temp = readTemperature();
        double smoke = readSmokeLevel();
        double gas = readGasLevel();

        std::cout << "Sensor Readings - Temp: " << temp << "°C, Smoke: " << smoke 
                  << " PPM, Gas: " << gas << " PPM" << std::endl;

        // Fire detection conditions
        bool fireDetected = (temp > temperatureThreshold) || 
                           (smoke > smokeThreshold) || 
                           (gas > gasThreshold);

        if (fireDetected && !alertActive) {
            triggerAlert();
            alertActive = true;
        } else if (!fireDetected && alertActive) {
            alertActive = false;
            std::cout << "ALERT CLEARED: Conditions normal" << std::endl;
        }

        return fireDetected;
    }

    // Trigger fire alert
    void triggerAlert() {
        std::cout << "🔥 FIRE ALERT! 🔥" << std::endl;
        std::cout << "Emergency protocols activated!" << std::endl;
        std::cout << "Notifying authorities and personnel..." << std::endl;
    }

    // Get current status
    void getStatus() {
        std::cout << "GuardianEye Status: " << (alertActive ? "ALERT ACTIVE" : "MONITORING") << std::endl;
        std::cout << "Thresholds - Temp: " << temperatureThreshold 
                  << "°C, Smoke: " << smokeThreshold 
                  << " PPM, Gas: " << gasThreshold << " PPM" << std::endl;
    }
};

int main() {
    std::cout << "GuardianEye Fire Detection System Starting..." << std::endl;
    
    FireDetectionSensor guardian;
    guardian.getStatus();
    
    // Simulate continuous monitoring
    for (int i = 0; i < 10; i++) {
        std::cout << "\n--- Monitoring Cycle " << (i + 1) << " ---" << std::endl;
        guardian.detectFire();
        std::this_thread::sleep_for(std::chrono::seconds(2));
    }
    
    std::cout << "\nGuardianEye monitoring session completed." << std::endl;
    return 0;
}