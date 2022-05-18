from threading import Thread
import serial
import RPi.GPIO as GPIO
import time
    
ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

def set_up_lora():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(27,GPIO.OUT)
    
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)

def serial_listen():
    while True:

        #SERIAL READ

        data = ser.readline()
        serialMsg = data.decode('ascii','ignore')

        if serialMsg != "" :

            print('Got lora msg: "{0}"'.format(serialMsg))
        
        time.sleep(0.1)
    
    
def serial_send():
    while True:
        message = input('What would you like to send\n')
        
        print('Going to send message to lora module: "{0}"'.format(message))
        ser.write(message.encode(encoding='ascii'))
        time.sleep(0.1)
        print('Written to serial')
        ser.flush()
        time.sleep(0.1)
        print('Serial flushed')

#set_up_lora()

#thread1 = Thread( target=serial_listen )
#thread1.start()

#thread2 = Thread( target=serial_send )
#thread2.start()

serial_send()
