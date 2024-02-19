import Adafruit_DHT
import paho.mqtt.client as mqtt
import time
import datetime

# Sensor setup
SENSOR = Adafruit_DHT.DHT22
SENSOR_PIN = 4  # GPIO pin connected to the sensor

# MQTT setup
MQTT_BROKER = "mqtt.example.com"
MQTT_PORT = 1883
MQTT_TOPIC = "home/temperature"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)
    if humidity is not None and temperature is not None:
        return humidity, temperature
    else:
        print("Failed to retrieve data from the sensor")
        return None, None

def log_data(humidity, temperature):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sensor_data.log", "a") as file:
        file.write(f"{timestamp}, Temperature: {temperature} C, Humidity: {humidity}%\n")

def main():
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_connect
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()

    try:
        while True:
            humidity, temperature = read_sensor()
            if humidity is not None and temperature is not None:
                log_data(humidity, temperature)
                payload = f"Temperature: {temperature} C, Humidity: {humidity}%"
                mqtt_client.publish(MQTT_TOPIC, payload)
            time.sleep(10)  # Delay between readings
    except KeyboardInterrupt:
        print("Script terminated by user")
    finally:
        mqtt_client.loop_stop()

if __name__ == "__main__":
    main()
