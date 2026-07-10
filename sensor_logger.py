# sensor_logger.py
import csv
import random
import time
from datetime import datetime

def read_sensor():
    """Simulates reading temperature and vibration sensor data"""
    temp = round(random.uniform(20.0, 90.0), 2)
    vibration = round(random.uniform(0, 5.0), 2)
    return temp, vibration

def log_data(filename="sensor_data.csv", readings=10, interval=1):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Temperature_C", "Vibration_Level"])

        for _ in range(readings):
            temp, vib = read_sensor()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, temp, vib])
            print(f"{timestamp} | Temp: {temp}°C | Vibration: {vib}")
            time.sleep(interval)

if __name__ == "__main__":
    log_data()