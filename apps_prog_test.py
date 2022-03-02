
import serial
import time 

# import csv

# # open the file in the write mode
# f = open('/home/mikhail/Desktop/data.csv', 'w')

# # create the csv writer
# writer = csv.writer(f)

port = '/dev/ttyUSB0'
baud = 250000

ser = serial.Serial(port, baud, timeout = 0)  # open serial port

byte_size = 1
start_byte = "af"              # start byte defined in ESC protocol as 0xAF
end_byte =  'ae'
seconds = 2
bl = []
master_list = []
t = 0.1

start_time = round(time.time())
x = ser.read(5)
while True: 
    # current_time = time.time()
    # elapsed_time =current_time - start_time
    # if elapsed_time > seconds:  # time out loop
    #     break
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
            #if s == start_byte:
            if s == 'ae' or s == 'a8':
                master_list.append(bl)
                bl = []
                time.sleep(t) ##
                for x in master_list:
                    print(x)
                break
        else:
            bl.append(s)

for x in master_list:
    print(x)
# # write a row to the csv file
# writer.writerow(master_list)

ser.close()                     # close port 