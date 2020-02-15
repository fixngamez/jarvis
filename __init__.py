import serial
import RPi.GPIO as GPIO      
import os, time

led1=17
led2=27
led3=22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.output(led1 , 0)
GPIO.output(led2 , 0)
GPIO.output(led3 , 0)

actor.add_keyword("turn on red light", Controlredledon())
actor.add_keyword("turn off red light", Controlredledoff())
actor.add_keyword("turn on blue light", Controlblueledon())
actor.add_keyword("turn off blue light", Controlblueledoff())
actor.add_keyword("turn on green light", Controlgreenledon())
actor.add_keyword("turn off green light", Controlgreenledoff())
actor.add_keyword("turn on all lights", Controlallledon())
actor.add_keyword("turn off all lights", Controlallledoff())
actor.add_keyword("blink lights", Controlledblink())





class Controlredledon():
    def run(self, voice_command):
          GPIO.output(led1 , 1)
 
class Controlredledoff():
    def run(self, voice_command):
          GPIO.output(led1 , 0)

class Controlblueledon():
    def run(self, voice_command):
          GPIO.output(led2 , 1)

class Controlblueledoff():
    def run(self, voice_command):
          GPIO.output(led2 , 0)

class Controlgreenledon():
    def run(self, voice_command):
          GPIO.output(led3 , 1)

class Controlgreenledoff():
    def run(self, voice_command):
          GPIO.output(led3 , 0)


class Controlallledon():
    def run(self, voice_command):
        GPIO.output(led1 , 1)
        GPIO.output(led2 , 1)
        GPIO.output(led3 , 1)

class Controlallledoff():
    def run(self, voice_command):
        GPIO.output(led1 , 0)
        GPIO.output(led2 , 0)
        GPIO.output(led3 , 0)


class Controlledblink():
    def run(self, voice_command):
        for k in range (100):
         GPIO.output(led1 , 1)
         GPIO.output(led2 , 1)
         GPIO.output(led3 , 1)
         time.sleep(0.1)
         GPIO.output(led1 , 0)
         GPIO.output(led2 , 0)
         GPIO.output(led3 , 0)
         time.sleep(0.1)

 
