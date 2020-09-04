from functions.mysql import *
import subprocess as sp
import time
from discord_webhook import DiscordWebhook
import time
from datetime import datetime
import os
from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError

PATH = os.environ['WEBHOOK']

while True:
    
    now = datetime.now()
    data_atual = (str(now.year) + str("/") +  str(now.month)  + str("/") + str(now.day))
    hora_atual= (str(now.hour) + str(":") +  str(now.minute)  + str(":") + str(now.second))
    name_mysql = cmdmysql("SELECT * FROM aplicacoes")

    for row in name_mysql:
        status,result = sp.getstatusoutput("ping -c1 -w2 " + str(row[2]))
        if status == 0:
            print("System " + str(row[2]) + " is UP !")
            try:
                with urllib.request.urlopen(row[3]) as f:
                    if "html" or "HTML" in f:
                        print("Site ONLINE" + str(row[3]))
                
            except urllib.error.URLError as err:
                print(err)
                if str(err) == '<urlopen error [Errno -2] Name or service not known>':
                    print("Site fora do ar"+ str(row[3]) )
            
        else:
            print("System " + str(row[2]) + " is DOWN !")

