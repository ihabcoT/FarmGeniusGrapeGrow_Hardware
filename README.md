# 🍇 IoT FarmGenius GrapeGrow System

A smart grape farming system designed to monitor and manage environmental conditions using IoT technologies. This system integrates multiple sensors (temperature, soil/air moisture, light) and output devices (LCD screen, LED lights, pump), connected to Adafruit IO via MQTT for data management.

## 🤝 Team

- 👨‍💻 4 Computer Science students
- 👷‍♂️ 1 Computer Engineering student (hardware & system integration lead)

## 📌 Features

- **Sensor Monitoring:**
  - Temperature
  - Soil moisture
  - Air humidity
  - Light intensity (with analog-to-lux conversion)
- **Output Devices:**
  - LCD display for real-time status
  - LED lights
  - Water pump for automated irrigation
- **Connectivity:**
  - Real-time data transmission via a simple IoT gateway
  - Remote control and visualization via [Adafruit IO] ([https://io.adafruit.com/ihabcoT/dashboards/farmgenius-grapegrow])
- **Protocols:**
  - MQTT for efficient IoT communication

## 🛠 Technologies Used

- **Hardware:** Yolo:Bit, DHT20 (temperature sensor, air humidity sensor), soil moisture sensor, LDR sensor, LCD, LEDs, pump
- **Software:** OhStem App, Adafruit IO

## 📷 Testing Screenshots

- **Hardware Settings (AIoT KIT):**

![image](https://github.com/user-attachments/assets/8e0918e2-a865-471c-900e-2bb193106c0a)

- **Light Test:**

![image](https://github.com/user-attachments/assets/ef8791d1-e146-40fd-b0f9-6b4f09f2e528)

![image](https://github.com/user-attachments/assets/ddd278c0-aa17-4c42-9f7b-df1e7f71f065)


## 🚀 Getting Started

1. Clone this repository.
2. Upload the firmware to your Yolo:Bit using OhStem App.
3. Configure your Adafruit IO credentials in the code.
4. Power the hardware and monitor sensor data via the dashboard.
