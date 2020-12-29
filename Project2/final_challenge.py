# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:20:24 2020

@author: tngo0508
"""

import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
    url = 'https://pastebin.com/Mfc9txQV'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0 \
                                           Win64 \
                                           x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 \
               '}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    if str(soup).find('Key') == -1:
        time.sleep(500)
        continue
    else:
        create_email = 'Subject: CHECK PASTEBIN - FOUND KEY'
        from_address = 'abc@gmail.com'
        to_address = 'sample@gmail.com'
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        # use SSL recommended
        mail.starttls()
        mail.login('username', 'password')
        mail.sendmail(from_address, to_address, create_email)
        mail.close()
        print("alert")
        break
