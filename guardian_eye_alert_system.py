#!/usr/bin/env python3
"""
GuardianEye Fire Detection Alert System
Python implementation for data processing and alert management
Complements the C++ sensor system for comprehensive fire monitoring
"""

import time
import random
import json
from datetime import datetime
from typing import Dict, List, Tuple

class GuardianEyeAlertSystem:
    """
    Alert management system for fire detection data processing
    """
    
    def __init__(self, config_file: str = None):
        self.alert_history: List[Dict] = []
        self.thresholds = {
            'temperature': 60.0,  # Celsius
            'smoke': 300.0,       # PPM
            'gas': 1000.0         # PPM
        }
        self.alert_contacts = [
            "fire_department@emergency.gov",
            "security@industrial.com",
            "maintenance@company.com"
        ]
        self.is_monitoring = False
        
    def process_sensor_data(self, temperature: float, smoke: float, gas: float) -> Dict:
        """
        Process incoming sensor data and determine alert status
        """
        timestamp = datetime.now().isoformat()
        
        sensor_data = {
            'timestamp': timestamp,
            'temperature': temperature,
            'smoke': smoke,
            'gas': gas,
            'status': 'normal'
        }
        
        # Analyze fire risk
        fire_risk_score = self.calculate_fire_risk(temperature, smoke, gas)
        sensor_data['fire_risk_score'] = fire_risk_score
        
        # Determine alert level
        if fire_risk_score >= 0.8:
            sensor_data['status'] = 'critical_alert'
            self.trigger_emergency_alert(sensor_data)
        elif fire_risk_score >= 0.6:
            sensor_data['status'] = 'warning'
            self.trigger_warning_alert(sensor_data)
        
        # Store data for analysis
        self.alert_history.append(sensor_data)
        
        return sensor_data
    
    def calculate_fire_risk(self, temperature: float, smoke: float, gas: float) -> float:
        """
        Calculate fire risk score based on sensor readings (0.0 - 1.0)
        """
        temp_risk = min(temperature / (self.thresholds['temperature'] * 1.5), 1.0)
        smoke_risk = min(smoke / (self.thresholds['smoke'] * 1.5), 1.0)
        gas_risk = min(gas / (self.thresholds['gas'] * 1.5), 1.0)
        
        # Weighted average with temperature having highest priority
        risk_score = (temp_risk * 0.4 + smoke_risk * 0.35 + gas_risk * 0.25)
        return round(risk_score, 2)
    
    def trigger_emergency_alert(self, data: Dict):
        """
        Trigger emergency alert for critical fire conditions
        """
        print("🚨 EMERGENCY FIRE ALERT 🚨")
        print(f"Time: {data['timestamp']}")
        print(f"Risk Score: {data['fire_risk_score']}")
        print(f"Temperature: {data['temperature']}°C")
        print(f"Smoke: {data['smoke']} PPM")
        print(f"Gas: {data['gas']} PPM")
        
        # Simulate emergency notifications
        for contact in self.alert_contacts:
            print(f"📧 Emergency notification sent to: {contact}")
        
        # Log to emergency system
        self.log_emergency_event(data)
    
    def trigger_warning_alert(self, data: Dict):
        """
        Trigger warning alert for elevated fire conditions
        """
        print("⚠️  FIRE WARNING ⚠️")
        print(f"Risk Score: {data['fire_risk_score']}")
        print("Conditions are elevated - monitoring closely")
    
    def log_emergency_event(self, data: Dict):
        """
        Log emergency event for audit trail
        """
        log_entry = {
            'event_type': 'FIRE_EMERGENCY',
            'data': data,
            'actions_taken': [
                'Emergency contacts notified',
                'Fire suppression systems activated',
                'Evacuation procedures initiated'
            ]
        }
        
        # In real implementation, this would write to database/file
        print(f"📝 Event logged: {log_entry['event_type']}")
    
    def generate_report(self) -> Dict:
        """
        Generate monitoring report from collected data
        """
        if not self.alert_history:
            return {"message": "No data available for report generation"}
        
        total_readings = len(self.alert_history)
        critical_alerts = sum(1 for reading in self.alert_history if reading['status'] == 'critical_alert')
        warnings = sum(1 for reading in self.alert_history if reading['status'] == 'warning')
        
        avg_temp = sum(reading['temperature'] for reading in self.alert_history) / total_readings
        avg_smoke = sum(reading['smoke'] for reading in self.alert_history) / total_readings
        avg_gas = sum(reading['gas'] for reading in self.alert_history) / total_readings
        
        report = {
            'monitoring_period': {
                'start': self.alert_history[0]['timestamp'],
                'end': self.alert_history[-1]['timestamp'],
                'total_readings': total_readings
            },
            'alert_summary': {
                'critical_alerts': critical_alerts,
                'warnings': warnings,
                'normal_readings': total_readings - critical_alerts - warnings
            },
            'average_readings': {
                'temperature': round(avg_temp, 2),
                'smoke': round(avg_smoke, 2),
                'gas': round(avg_gas, 2)
            }
        }
        
        return report
    
    def simulate_monitoring_session(self, duration_minutes: int = 5):
        """
        Simulate a monitoring session with random sensor data
        """
        print("🛡️  GuardianEye Alert System - Starting Monitoring Session")
        print(f"Duration: {duration_minutes} minutes")
        print("-" * 50)
        
        self.is_monitoring = True
        readings = duration_minutes * 2  # 2 readings per minute
        
        for i in range(readings):
            # Simulate sensor readings
            temperature = 25 + random.uniform(-5, 45)  # 20-70°C
            smoke = random.uniform(0, 500)             # 0-500 PPM
            gas = random.uniform(0, 1500)              # 0-1500 PPM
            
            # Process the data
            result = self.process_sensor_data(temperature, smoke, gas)
            
            print(f"Reading {i+1}/{readings}: Status = {result['status'].upper()}")
            time.sleep(0.5)  # Simulate real-time processing
        
        self.is_monitoring = False
        
        # Generate and display final report
        print("\n" + "="*50)
        print("📊 MONITORING REPORT")
        print("="*50)
        report = self.generate_report()
        print(json.dumps(report, indent=2))

def main():
    """
    Main function to demonstrate GuardianEye Alert System
    """
    print("GuardianEye Fire Detection Alert System")
    print("Python Data Processing Module")
    print("="*40)
    
    # Initialize the alert system
    guardian_eye = GuardianEyeAlertSystem()
    
    # Run a simulation
    guardian_eye.simulate_monitoring_session(duration_minutes=2)
    
    print("\nGuardianEye monitoring session completed successfully! 🛡️")

if __name__ == "__main__":
    main()