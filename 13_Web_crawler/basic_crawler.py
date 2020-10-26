#!/usr/bin/env python

import requests


def request(url):
    try:
        return requests.get('https://' + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = '10.0.2.21/mutillidae'
with open('/root/Downloads/word_list/dir_list.txt', 'r') as word_list:  
       # '/root/Downloads/word_list/dir_list.txt' is location of file containing word list.
    for line in word_list:
        word = line.strip()
        test_url = target_url + '/' + word
        response = request(test_url)
        if response:
            print('URL Discovered --->: ' + test_url)
    print('All Done')
