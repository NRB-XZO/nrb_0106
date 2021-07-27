#!/usr/bin/env python
# -*- coding: utf-8 -*-
# NRB SECURITY
from time import sleep
import os
from os import system, chdir
from subprocess import *
import webbrowser
import getpass
import random
import requests
from os import system
from bs4 import BeautifulSoup
random_number = random.randint(1,100)
location_list = ["https://goo.gl/maps/u1dP8sTe95jRyRky5","https://goo.gl/maps/JByQkHuhfqp3b75t9","https://goo.gl/maps/bMuPYU6bvGnBXzKr7","https://goo.gl/maps/nHnRnR8zHEU3eavD9","https://goo.gl/maps/orVHT47dULRfr3h69"]
while True:
    try:
        x = "oyuncak"
        url = "https://www.cimri.com/arama?q={}".format(x)
        responce = requests.get(url)
        html_icerigi = responce.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        if random_number > 70:
            sleep(1)
            print("""

            Bağlantı Bekleniyor...


            """)
            sleep(10)
            system("clear")
            for i in range(1, 101):
                print("Bağlantı Kuruluyor {}%".format(i))
                system("clear")
            sleep(5)
            print("Bağlantı kuruldu")
            sleep(3)
            print("""
            
            1-Messages
            2-Location
            """)
            q3 = int(input("İnput:"))
            if q3 == 1:
                webbrowser.open(location_list[random.randint(0,5)],new=0,autoraise=True)
        else:
            print("Baglanti bulunamadi")
            break
    except:
        print("İNTERNET BAGLANTİSİ YOK")
        break
