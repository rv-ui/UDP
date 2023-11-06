import socket

from time import sleep

import RPi.GPIO as gpio

import dht11



gpio.cleanup()

# init sensor

gpio.setmode(gpio.BOARD)

gpio.setup(40,gpio.OUT)



dht=dht11.DHT11(pin=40)



buffer_size = 1024

#msg_from_server = "Hi I am Server"

server_port = 1237

server_ip = '10.205.5.134'



#convert msg_from_server to bytes

#bytes_to_send = msg_from_server.encode('utf-8')



#create socket

RPIsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# bind it with the server id and port created

RPIsocket.bind((server_ip,server_port))





print("server is up and listening...")

#cnt =0

try:

    while True: 

        cmd,address = RPIsocket.recvfrom(buffer_size)

        cmd=cmd.decode('utf-8')

        print(cmd)

        print('Client Address: ',address[0])

    

        if cmd=='DHT':

            #get DHT11 data

            result = dht.read()

            if result.is_valid():

                data = str(result.temperature)+':'+str(result.humidity)

                data= data.encode('utf-8')

                RPIsocket.sendto(data,address)

            if result.is_valid()==False:

                data='Bad Measurement'

                print(data)

                data= data.encode('utf-8')

                RPIsocket.sendto(data,address)

            

        if cmd!='DHT':

            data='Invalid Request'

            data= data.encode('utf-8')

            RPIsocket.sendto(data,address)

except KeyboardInterrupt:

    gpio.cleanup()



