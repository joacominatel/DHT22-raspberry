<h1>Requirements</h1>

*Hardware*
   - Raspberry Pi 3 with Internet connectivity
   - DHT22 temperature and humidity sensor
   - Breadboard and jumper wires (for sensor connection)

*Software*
    - Python 3.x installed on Raspberry Pi
    - Install `requirements.txt`

*Steps*
1. Prepare Raspberry Pi
2. Connect DHT22 Sensor:
    - Connect the DHT22 sensor to the Raspberry Pi using the GPIO pins. Refer to the hardware setup section in the script description for details.
3. Install required Python libraries with pip3

*Usage GUIDE*
1. Edit the script:
    - Modify the `MQTT_BROKER` variable to the address of your MQTT broker.
    - If necessary, adjust the `SENSOR_PIN` to match the GPIO pin number you-ve connected your DHT22 sensor to.
2. Run the script
    - Execute the script by running the following command in a terminal
    ```python3 path/to/app.py```
3. Monitoring and logs:
    - The script will continuously read data from the DHT22 sensor and publish it to the specified MQTT topic
    - Sensor readings along with timestamps will be logged to a file named sensor_data.log in the same directory as the script
    - Ensure your MQTT client or server is set up to subscribe to the topic you specified in the script for real-time data monitoring