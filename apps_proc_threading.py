
import threading
import serial
import logging
import time
import datetime
import subprocess

port = '/dev/ttyUSB0'
baud = 250000

ser = serial.Serial(port, baud, timeout = 0)  # open serial port

def KILL_function():
    time.sleep(5)
    subprocess.call(['sh', './apps_prog_kill_test.sh'])

    if exit == 0:
        logging.debug('Apps_Proc_Killed_Sucessfully')
    else:
        logging.debug('Apps_Proc_Failed_To_Kill')


def sniff_function():
    bl = []
    master_list = []
    byte_size = 1
    start_byte = "af"              # start byte defined in ESC protocol as 0xAF    

    while True:
        #ser = serial.Serial(port, baud, timeout = 0)  # open serial port
        s = ser.read(byte_size)
        s = s.hex()    # stores byte into string list
        if not s:
            continue
        if s == start_byte or not s:
            bl = []
            bl.append(s)
            while True:
                s = (ser.read(byte_size)).hex()    # stores byte into string list
                bl.append(s)
                if s == 'ae' or s == 'a8':
                    master_list.append(bl)
                    bl = []
                    logging.debug(master_list)
                    for x in master_list:
                        logging.debug('List: %s',x)
                        time.sleep(1)
                        ser.close()
                    break


if __name__ == "__main__":
    logging.basicConfig(filename='ESC_log.log',format='%(asctime)s %(message)s',filemode='w')
    logging.debug('start')
    ser = serial.Serial(port, baud, timeout = 0)  # open serial port
    sniff = threading.Thread(target=sniff_function)
    logging.info("Main    : before running thread")
    sniff.start()
    KILL = threading.Thread(target=KILL_function)
    KILL.start()
    logging.info("Main    : wait for the thread to finish")
    # sniff.join()
    logging.info("Main    : all done")


# _relay_thread_sync = threading.Event()

# # Parse script argumentsthreading in python
# 	description = ""
# 	parser = argparse.ArgumentParser(description=description)
# 	parser.add_argument('-n', '--number', help='Number of loops', default=1, required=False, type=int)
# 	parser.add_argument('-d', '--debug_port', help='Debug serial port', default='/dev/tty.usbserial-A10L8XE4', required=False, type=str)
# 	parser.add_argument('-s', '--relay_port', help='Relay serial port', default='/dev/tty.usbserial-14210', required=False, type=str)
# 	parser.add_argument('-r', '--reset_wait', help='Relay reset wait (sec)', default=2, required=False, type=int)
# 	parser.add_argument('-b', '--bootup_wait', help='Bootup wait (sec)', default=10, required=False, type=int)
# 	args = vars(parser.parse_args())
# 	return args


# def logging_thread(dir_nam, debug_port):
# 	file_name = str(int(time.time())) + ".txt"
# 	log_name = os.path.join(dir_nam, file_name)

# 	log = True 
# 	if log:
# 		print("[INFO] - logger - Opening debug serial port: " + debug_port, flush=True)
# 		debug_ser = serial.Serial(debug_port,115200, timeout=1)
# 		debug_ser.flush()
# 		print("[INFO] - logger - Success: opened debug serial port", flush=True)

# 	while True:

# 		if _relay_thread_sync.is_set():
# 			print("[INFO] - logger - stopping logging thread", flush=True)
# 			break

# 		if log:
# 			line=None
# 			try:
# 				line = debug_ser.readline()
# 			except:
# 				print("[ERROR] - logger - readline", flush=True)
            
# 			if line:
# 				try:
# 					with open(log_name, 'ab') as f:
# 						f.write(line)
# 				except:
# 					print("[ERROR] - logger - file write", flush=True)
 
# 				try:
# 					print(line.decode())
# 				except:
# 					print("[ERROR] - logger - print write", flush=True)
# 		else:
# 			# debug
# 			time.sleep(0.1)

# 	try:
# 		if log:
# 			if debug_ser.is_open:
# 				print("[INFO] closing debug serial port", flush=True)
# 				debug_ser.close()
# 	except:
# 		print("[ERROR] close debug port", flush=True)


# if __name__ == "__main__":
# 	"""
# 	This program will generate log files for each boot cycle
# 	"""
# 	args = parse_args()
# 	loops = args["number"]
# 	debug_port = args["debug_port"]
# 	relay_port = args["relay_pConvert Indentation to Spacesort"]
# 	reset_wait = args["reset_wait"]
# 	bootup_wait = args["bootup_wait"]

# 	epoch_time = time.time()

# 	#relay_port='/dev/ttyUSB0'
# 	print("[INFO] Opening relay serial port: " + relay_port)
# 	relay_ser = serial.Serial(relay_port,9600, timeout=1)
# 	print("[INFO] Success: relay debug serial port")
# 	time.sleep(0.5)

# 	dir_name = "logs-" + str(int(time.time()))
# 	os.mkdir(dir_name) 

# 	for n in range(loops):
        
# 		# stop existing and start new logging thread
# 		print("[INFO] starting logging thread: " + str(n) + " of " + str(loops))
        
# 		log_thread = threading.Thread(target=logging_thread, args=(dir_name,debug_port,), name='logging-thread')
# 		log_thread.start()

# 		if True:
# 			print("[INFO] resetting target")
# 			# reset device using relay
# 			relay_ser.write(serial.to_bytes([0xA0, 0x01, 0x00, 0xA1])) 
            
# 			print("[INFO] waiting for reset: " + str(reset_wait) + " (sec)")
# 			time.sleep(reset_wait)
# 			relay_ser.write(serial.to_bytes([0xA0, 0x01, 0x01, 0xA2]))

# 		print("[INFO] waiting for bootup: " + str(bootup_wait) + " (sec)")
# 		time.sleep(bootup_wait)

# 		print("[INFO] stopping logging thread...")
# 		_relay_thread_sync.set()
# 		log_thread.join()
# 		_relay_thread_sync.clear()
