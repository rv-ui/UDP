import socket

from time import sleep

#msg_from_client = ' Hi, I am Client'

#bytes_to_send = msg_from_client.encode('utf-8')

server_address = ('10.205.3.193',1237)

buffer_size = 1024



udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)





while True:

    #cmd = input('DHT for dht sensor data: ')

    cmd = 'DHT'

    cmd=cmd.encode('utf-8')

    udp_client.sendto(cmd,server_address)

    #udp_client.sendto(bytes_to_send,server_address)



    #waiting for data

    data,address = udp_client.recvfrom(buffer_size)

    data=data.decode('utf-8')



    data_array = data.split(':')



    if len(data_array)==1:

        print('no data')

    if len(data_array)==2:

        print('Temperature: ',data_array[0],' ','Humidity: ',data_array[1])

    sleep(1)
