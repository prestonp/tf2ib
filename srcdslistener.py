#!/usr/bin/python

import config
import psycopg2
import socket
import time

database = psycopg2.connect('dbname=tf2ib host=localhost user=tf2ib password=' + config.databasePassword)
cursor = database.cursor()

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(('173.255.206.107', 27069))
listener.listen(1)
servers = ["208.115.210.90", "208.115.210.91", "208.115.210.92", "208.115.210.93", "208.115.210.94"]
while 1:
    try:
        connection, address = listener.accept()
    except:
        listener.listen(1)
        continue
    try:
        data = connection.recv(4096)
    except:
        continue
    print data
    print address[0] 
    if data and address[0] in servers:
        print 'authorized'
        cursor.execute('INSERT INTO srcds VALUES (%s, %s)', (data, int(time.time())))
        database.commit()
        connection.close()
