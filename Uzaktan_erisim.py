# !/usr/bin/env python
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
number_list = ["+90 505 138 1731","+90 534 684 9153","+90 542 846 1942","+90 535 238 4106","+90 552 928 8978","+90 536 565 3212"]
random_number = random.randint(1, 100)
location_list = ["https://goo.gl/maps/u1dP8sTe95jRyRky5", "https://goo.gl/maps/JByQkHuhfqp3b75t9",
                 "https://goo.gl/maps/bMuPYU6bvGnBXzKr7", "https://goo.gl/maps/nHnRnR8zHEU3eavD9",
                 "https://goo.gl/maps/orVHT47dULRfr3h69"]
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
except:
    print("İnternet bağlantısı yok")
    exit()
while True:
    print("""

                1-Messages
                2-Location
                3-Call log
                """)
    q3 = int(input("İnput:"))
    if q3 == 2:
        webbrowser.open(location_list[random.randint(0, 5)], new=0, autoraise=True)
    elif q3 == 1:
        print("Accessing message logs")
        sleep(20)
        print("ERROR")
        sleep(4)
    elif q3 == 3:
        asdf = random.randint(0, 100)
        if asdf < 10:
            print("Erişim sağlanıyor...")
            sleep(5)
            print("Herhangi bir aramada değil")
        elif 11 < asdf < 110:
            print("Erişim sağlanıyor..")
            sleep(5)
            print("""
                         1: +90 538 030 8093
                         2: {}
                         Şu an görüşüyorlar

                        """.format(number_list[random.randint(0, 7)]))
            sleep(5)
        else:
            continue
    print("Baglanti bulunamadi")
    break
