#!/usr/bin/env python
# running for python2
import re
import requests
import urlparse


def link_extraction(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    links = link_extraction(url)
    for link in links:
        link = urlparse.urljoin(target_url, link)

        if '#' in link:
            link = link.split('#')[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


target_url = 'http://10.0.2.21/mutillidae/'
target_links = []
crawl(target_url)
