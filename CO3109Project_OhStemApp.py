from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from mqtt import *
from machine import RTC
import ntptime
import time
from aiot_lcd1602 import LCD1602
from event_manager import *
from aiot_rgbled import RGBLed
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20
import math

aiot_lcd1602 = LCD1602()

event_manager.reset()

def on_mqtt_message_receive_callback__str_FarmGenius_____pump__(pump):
  global TT, LED, RT, TT2, FarmGenius, LEDnumber, RH, SM, LUX, GDD
  pin3.write_analog(round(translate((int(pump)), 0, 100, 0, 1023)))

tiny_rgb = RGBLed(pin0.pin, 4)

def on_mqtt_message_receive_callback__str_FarmGenius_____led__(LED):
  global pump, TT, RT, TT2, FarmGenius, LEDnumber, RH, SM, LUX, GDD
  LEDnumber = translate((int(LED)), 0, 100, 0, 4)
  if LEDnumber == 0:
    tiny_rgb.show(0, hex_to_rgb('#000000'))
  elif LEDnumber == 1:
    tiny_rgb.show(0, hex_to_rgb('#000000'))
    tiny_rgb.show(1, hex_to_rgb('#00ff00'))
  elif LEDnumber == 2:
    tiny_rgb.show(0, hex_to_rgb('#000000'))
    tiny_rgb.show(1, hex_to_rgb('#00ff00'))
    tiny_rgb.show(2, hex_to_rgb('#00ff00'))
  elif LEDnumber == 3:
    tiny_rgb.show(0, hex_to_rgb('#000000'))
    tiny_rgb.show(1, hex_to_rgb('#00ff00'))
    tiny_rgb.show(2, hex_to_rgb('#00ff00'))
    tiny_rgb.show(3, hex_to_rgb('#00ff00'))
  else:
    tiny_rgb.show(0, hex_to_rgb('#00ff00'))

# Mô tả hàm này...
def _C4_90i_E1_BB_81u_khi_E1_BB_83n_m_C3_A1y_b_C6_A1m_v_C3_A0__C4_91_C3_A8n():
  global pump, TT, LED, RT, TT2, FarmGenius, LEDnumber, RH, SM, LUX, GDD, aiot_dht20, tiny_rgb, aiot_lcd1602
  mqtt.on_receive_message((str(FarmGenius) + 'pump'), on_mqtt_message_receive_callback__str_FarmGenius_____pump__)
  mqtt.on_receive_message((str(FarmGenius) + 'led'), on_mqtt_message_receive_callback__str_FarmGenius_____led__)

aiot_dht20 = DHT20()

def on_event_timer_callback_n_Z_E_L_d():
  global pump, TT, LED, RT, TT2, FarmGenius, LEDnumber, RH, SM, LUX, GDD
  aiot_dht20.read_dht20()
  RT = aiot_dht20.dht20_temperature()
  RH = aiot_dht20.dht20_humidity()
  SM = round(translate((pin1.read_analog()), 0, 4095, 0, 100))
  LUX = round(3.92881 * math.exp(0.00194325 * pin2.read_analog()) - 3.92881)
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('RT:')
  aiot_lcd1602.move_to(3, 0)
  aiot_lcd1602.putstr(RT)
  aiot_lcd1602.move_to(7, 0)
  aiot_lcd1602.putstr('*C')
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr('RH:')
  aiot_lcd1602.move_to(13, 0)
  aiot_lcd1602.putstr(RH)
  aiot_lcd1602.move_to(15, 0)
  aiot_lcd1602.putstr('%')
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('LUX:')
  aiot_lcd1602.move_to(4, 1)
  aiot_lcd1602.putstr('')
  aiot_lcd1602.move_to(4, 1)
  aiot_lcd1602.putstr(LUX)
  aiot_lcd1602.move_to(10, 1)
  aiot_lcd1602.putstr('SM:')
  aiot_lcd1602.move_to(13, 1)
  aiot_lcd1602.putstr(SM)
  aiot_lcd1602.move_to(15, 1)
  aiot_lcd1602.putstr('%')
  mqtt.publish((str(FarmGenius) + 'temp'), RT)
  mqtt.publish((str(FarmGenius) + 'humidity'), RH)
  mqtt.publish((str(FarmGenius) + 'soil'), SM)
  mqtt.publish((str(FarmGenius) + 'light'), LUX)

event_manager.add_timer_event(30000, on_event_timer_callback_n_Z_E_L_d)

def on_button_a_pressed():
  global pump, TT, LED, RT, TT2, FarmGenius, LEDnumber, RH, SM, LUX, GDD
  if TT == '1':
    TT = '0'
    pump = 0
    pin3.write_analog(round(translate((int(pump)), 0, 100, 0, 1023)))
    mqtt.publish((str(FarmGenius) + 'pump'), pump)
  else:
    TT = '1'
    pump = 100
    pin3.write_analog(round(translate((int(pump)), 0, 100, 0, 1023)))
    mqtt.publish((str(FarmGenius) + 'pump'), pump)

button_a.on_pressed = on_button_a_pressed

def on_button_b_pressed():
  global pump, TT, LED, RT, TT2, FarmGenius, LEDnumber, RH, SM, LUX, GDD
  if TT2 == '1':
    TT2 = '0'
    LED = 0
  else:
    TT2 = '1'
    LED = 100
  if TT2 == '1':
    tiny_rgb.show(0, hex_to_rgb('#00ff00'))
    mqtt.publish((str(FarmGenius) + 'led'), LED)
  else:
    tiny_rgb.show(0, hex_to_rgb('#000000'))
    mqtt.publish((str(FarmGenius) + 'led'), LED)

button_b.on_pressed = on_button_b_pressed

if True:
  display.scroll('IoT')
  mqtt.connect_wifi('ACLAB', 'ACLAB2023')
  mqtt.connect_broker(server='io.adafruit.com', port=1883, username='ihabcoT', password='')
  FarmGenius = 'farmgenius-grapegrow.bbc-'
  display.scroll('OK')
  ntptime.settime()
  (year, month, mday, week_of_year, hour, minute, second, milisecond) = RTC().datetime()
  RTC().init((year, month, mday, week_of_year, hour+7, minute, second, milisecond))
  aiot_lcd1602.clear()
  GDD = 0
  TT = 0
  TT2 = 0

while True:
  mqtt.check_message()
  event_manager.run()
  _C4_90i_E1_BB_81u_khi_E1_BB_83n_m_C3_A1y_b_C6_A1m_v_C3_A0__C4_91_C3_A8n()
  time.sleep_ms(10)
