
from distutils.log import debug
import threading
from defer import return_value
import serial
import logging
import time
import datetime
import subprocess

port = '/dev/ttyUSB0'
baud = 250000
ser = None

def KILL_function():

    while True:
        subprocess.call(['sh', './apps_prog_kill_test.sh'])
        result = subprocess.check_output(['adb devices'], shell=True)
        result = str(result, "utf-8" )
        if "offline" in result:
            logging.info('Apps_Proc_Killed_Sucessfully')
            break
            
#       else:
#            logging.debug('Apps_Proc_Failed_To_Kill !!TRYING AGAIN!!')

def sniff_function():
    bl = []
    master_list = []
    byte_size = 1
    start_byte = "af"                               # start byte defined in ESC protocol as 0xAF    
    ser = serial.Serial(port, baud, timeout = 1)    # open serial port
    
    timeout = 0.3                                   # minutes to run
    seconds = timeout * 60

    if ser.is_open is False:
        exit(1)
    time.sleep(1)

    start_time = round(time.time())

    while True:
        current_time = time.time()
        elapsed_time =current_time - start_time
        if elapsed_time > seconds:                  # time out loop
            break

        s = ser.read(byte_size)
        s = s.hex()                                 # stores byte into string list
        if not s:
            continue
        if s == start_byte or not s:
            bl = []
            bl.append(s)
            while True:
                s = (ser.read(byte_size)).hex()     # stores byte into string list
                bl.append(s)
                if s == 'ae' or s == 'a8':
                    master_list.append(bl)
                    bl = []
                    
                    for x in master_list:
                        logging.debug('List: %s',x)
                        time.sleep(1)
                        
                    break

                #with open('test.txt', 'ab') as f:
                 #   f.write(b'hi\n')


if __name__ == "__main__":

    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        filename='ESC_log.log',filemode='w',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')

    sniff = threading.Thread(target=sniff_function)
    logging.info("start sniffing data...")
    sniff.start()
    time.sleep(5)
    KILL = threading.Thread(target=KILL_function)
    KILL.start()
    logging.info("Apps_Proc_Kill_Start")

