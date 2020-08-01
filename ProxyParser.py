#!/usr/bin/python3
# -*- utf-8 -*-

from bs4 import BeautifulSoup
import requests
from datetime import datetime
from termcolor import colored

print(colored("A file with proxy server links is begin created! Please wait...", "green"))

def proxies():
	proxies = []
	link = "https://www.sslproxies.org/" #site with proxy servers
	r = requests.get(link)
	s = BeautifulSoup(r.text, "html.parser")
	for i in s.find_all("tr")[:30]:
		try:
			data = i.find_all("td")
			address = data[0].text
			port = data[1].text
			type_ = data[4].text
			proxy = address + ":" + port
			proxies.append("https://" + proxy)
		except:
			pass
	return proxies

proxy_list = proxies()
length = len(proxy_list)

with open("ListOfProxyServers.txt", "w", encoding="utf-8") as f:
	f.write("List of proxy servers relative to " + str(datetime.now()) + "\n") #file creation time
	for i in range(0, length):
		if i == length:
			f.write(proxy_list[i])
		f.write(proxy_list[i] + "\n")
	f.close()
print(colored("File created!", 'green'))