#!/usr/bin/env python3

import os
import socket
import time

from googlesearch import search

# Colors
# Bold
############
black = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
y = "\033[1;33m"  # Yellow
b = "\033[1;32m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White


############
def clear():
    os.system('clear')


def login():
    os.system('nohup pip3 install google &')
    os.system("nohup pip3 install beautifulsoup4 &")
    print('')
    clear()
    print(G + '''

dP                   oo          
88                               
88 .d8888b. .d8888b. dP 88d888b. 
88 88'  `88 88'  `88 88 88'  `88 
88 88.  .88 88.  .88 88 88    88 
dP `88888P' `8888P88 dP dP    dP 
                 .88             
             d8888P              

         ''')
    USERNAME = input(R + 'USERNAME:' + C)
    PASSWORD = input(R + 'PASSWORD:' + C)
    user = "7azabet"
    passwd = 'Palestine'
    if USERNAME == user and PASSWORD == passwd:
        time.sleep(.5)
        print(G + '[+] Done Successfully :) ')
        time.sleep(1)


    else:
        time.sleep(1)
        print(R + '[!] NOT FOUND')
        time.sleep(0.2)
        exit()


def banner():
    os.system('')
    os.system('cat banner/bannerlight.txt')


def test_connection():
    try:
        print(W + 'Checking Your Internet Connection...')
        time.sleep(2)
        socket.create_connection(("information-eg.blogspot.com", 80))
        print('\033[1;32m[+] You Are Connected')
        time.sleep(1)
        os.system('clear')
        print('')
    except OSError:
        print(R + '[!] You Are Not Connected To Internet')
        exit()


############
Dorks = ['(israel)>>>> site:.gov.il inurl:id', '(United Kingdom [uk] )>>>> site:.gov.uk inurl:id',
         '(United States Of American [us] )>>> site:.gov.us inurl:id', '(China)>>> site:.gov.cn inurl:id ']

XSS = ['inurl:".php?cmd="', 'inurl:".php?z="', 'inurl:".php?q="', 'inurl:".php?search="', 'inurl:".php?query="',
       'inurl:".php?searchst­ring="', 'inurl:".php?keyword=­"', 'inurl:".php?file="', 'inurl:".php?years="',
       'inurl:".php?txt="', 'inurl:".php?tag="', 'inurl:".php?max="', 'inurl:".php?from="', 'inurl:".php?author="',
       'inurl:".php?pass="', 'inurl:".php?feedback­="', 'inurl:".php?mail="', 'inurl:".php?cat="', 'inurl:".php?vote="',
       'inurl:search.php?q=', 'inurl:com_feedpostol­d/feedpost.php?url=', 'inurl:scrapbook.php?­id=',
       'inurl:headersearch.p­hp?sid=', 'inurl:/poll/­default.asp?catid=', 'inurl:/­search_results.php?se­arch=']

sql = ['- https://www.gov.il/en/subjects/certificates_and_passports/id',
       '- https://services.mod.gov.il/Help/Api/GET-api-SubReq-id',
       '- https://services.mod.gov.il/Help/Api/DELETE-api-MarketingDestination-id',
       '- http://gpophoto.gov.il/haetonot/Eng_ShowPage.aspx?id=6', '- https://knesset.gov.il/mk/arb/mk.asp?ID=790',
       '- https://en.caa.gov.il/index.php?option=com_content&view=article&id=666&Itemid=371',
       '- https://services.mod.gov.il/Help/Api/DELETE-api-MarketingProduct-id',
       '- https://services.mod.gov.il/Help/Api/DELETE-api-Tester-id',
       '- https://services.mod.gov.il/Help/Api/PUT-api-SubReq-id',
       '- https://old.cbs.gov.il/reader/cw_usr_view_Folder?ID=141',
       '- https://mfa.gov.il/MFA/Government/Communiques/2003/ISA+Arrests+Ala-ah+Sheikh+Ale-id+-+Feb+12-+2003.htm',
       '- https://itrade.gov.il/netherlands2/tag/beller-id/',
       '- https://services.mod.gov.il/Help/Api/DELETE-api-Tester-id',
       '- https://services.mod.gov.il/Help/Api/GET-api-SaveDraft-id',
       '- https://services.mod.gov.il/Help/Api/DELETE-api-MarketingProduct-id',
       '- https://services.mod.gov.il/Help/Api/GET-api-SaveDraft-id',
       '- https://embassies.gov.il/bucharest/NewsAndEvents/Pages/New-lab-test-to-ID-early-lung-cancer-.aspx',
       '- http://www.parishcouncilwebsites.com/getting-started.php?id=12', '- http://www.evertz.com/frame/Bulk.php?id=',
       '- http://www.excelsiorhotel.com/prenotazioni_it.php?id_offerte=2',
       '- http://www.languagelink.com.cn/messageboard/language_convert.php?id=2',
       '- http://www.oil.lt/index.php?id=home&L=1', '- http://www.eurotubi.com/notizia-it.php?id=2',
       '- http://www.eminentelectronics.net/phones.php?carrier_id=11', '- http://dbees.com/text.php?id=6',
       '- http://convert2mp3.net/c-mp3.php?url=http', '- http://www.associazionecaniliveneto.it/news_eventi.php?id=354',
       '- http://www.apdcc.com.ar/mapa-countries.php?id=0',
       '- http://www.motoracingsupermotard.it/cardetail.php?id_car=148', '- http://ririechamber.com/business.php?id=28',
       '- http://www.univaq.it/en/macroarea.php?id=2,''- http://oxxygene.ro/article_it.php?id=68',
       '- https://resourcecentre.globaliris.com/getting-started.php?id=opencart',
       '- http://consulsthailand.org/countries.php?id=36',
       '- http://us.fulbrightonline.org/program_regions_countries.php?id=5',
       '- https://www.allvoi.com/phones.php?id=27',
       '- http://www.simsim.ge/programs.php?id=8- http://grzl.net/it.php?id=4',
       '- http://www.comesaria.org/site/en/countries.php?id_article=3',
       '- https://www.mantisbt.org/bugs/view.php?id=13065',
       '- http://www.kristanix.com/getstarted.php?id=SE- http://www.radioendirect.net/countries.php?idCat=51']
############
print('')
login()
clear()
banner()
print(C + '''

[1] Ready Dorks
[2] Search For Dorks
[3] Download & Install sqlmap Tool
[4] XSS Dorks
[5] Sites affected by sql

''')
g = '\033[1;32m'
while True:
    choice = input('\033[1;31mCHOICE>>>' + y)
    if choice == '1':
        print('\033[1;32mWait...')
        for dork in Dorks:
            time.sleep(1)
            print(g+dork)
        print('')

    elif choice == '2':
        test_connection()
        word = input(y + 'Enter The Dork That You Wanna Search:' + P)
        if word == "":
            print('[!] Not Found')
            exit()
        count = int(input(y + 'Enter The Number Of Search Result:' + P))
        if count == "":
            print('[!] Not Found')
            exit()
        for url in search(word, stop=count):
            print('')
            time.sleep(1)
            print(f'\033[1;32m[+] URL Found: \033[1;36m{url} ')
        print(W + '<=======================>')
        print('')
    elif choice == '3':
        accept = input(y + 'Do You Wanna Install sqlmap Tool...?! (y/n)' + P)
        if accept == "y":
            print(G + "[+] Downloading sqlmap Tool..." + y)
            time.sleep(2)
            os.system("clear")
            os.system('cat banner/bannersql.txt')
            os.system("git clone https://github.com/sqlmapproject/sqlmap")
        elif accept == 'n':
            print(W + 'Okay,Done :) ')
        else:
            print(R + '[!] No Choices')
            exit()

    elif choice == '4':
        print(P + 'Wait...')
        time.sleep(1)
        for xss in XSS:
            time.sleep(1)
            print(g + xss)
    elif choice == '5':
        print(P + 'Wait...')
        time.sleep(1)
        for sql_dork in sql:
            time.sleep(1)
            print(g + sql_dork)
        print(R + '<<<<<<< Fuck israel >>>>>>>')
    elif choice == 'x':
        time.sleep(1)
        close = 'Good Bye Bro :) '
        for char in close:
            time.sleep(0.1)
            print(char, end=' ')
        print('')
        exit()

    else:
        print('\033[1;31m[!] ERROR 404')

