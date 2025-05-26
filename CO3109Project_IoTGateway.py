import serial.tools.list_ports
from datetime import datetime
import random
import time
import sys
from Adafruit_IO import MQTTClient

AIO_FEED_ID = "farmgenius-grapegrow"
AIO_USERNAME = "ihabcoT"
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)
    print("Nhan du lieu: " + payload)

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()

def message(client , feed_id , payload):
client.loop_background()

while True:
    time.sleep(30)
    temp = random.randint(25, 30)
    humidity = random.randint(74, 77)
    light = random.randint(3000, 4000)
    soil = random.randint(62, 65)

    now = datetime.now()
    print("Thoi gian:", now)
    print("Cap nhat nhiet do:", temp)
    print("Cap nhat do am khong khi:", humidity)
    print("Cap nhat cuong do anh sang:", light)
    print("Cap nhat do am dat:", soil)
    client.publish("farmgenius-grapegrow.bbc-temp", temp)
    client.publish("farmgenius-grapegrow.bbc-humidity", humidity)
    client.publish("farmgenius-grapegrow.bbc-light", light)
    client.publish("farmgenius-grapegrow.bbc-soil", soil)
