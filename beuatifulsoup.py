# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import wget

import requests
import urllib.request
import sys
import importlib
importlib.reload(sys)
#sys.setdefaultencoding('utf8')

url = "http://zangsisi.net/?p=501524"
response = requests.get(url)
data = response.text
print(data.encode('utf-8'))
#soup = bs4.(data, 'lxml')
soup = BeautifulSoup(data, 'html.parser')
tags = soup.find_all('img')
i = 0

imgfile = "http://zangsisi.net/wp-content/uploads/2018/05/012-128.jpg"
filepath = "C:\\Users\\kwan\\Desktop\\python\\"
filetype = ".jpg"

#print(filename)

# urllib.request.urlretrieve(imgfile, filename)
for tag in tags:

    print(tag.get('src'))
    path = filepath+str(i)+filetype
    print(path)
    wget.download(tag.get('src'), path)
    #urllib.request.urlretrieve(tag.get('src'), path)
    i = i +1
