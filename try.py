# import re
# l="buyApe(uint256 apeIndex)"

# hh=re.split('(\d+)',l)
# print(hh)

# if "buyApe(uint" in hh:
#     print("success")








# from telegram.ext import Updater, CommandHandler
# import requests
# import re

# chat_id="-1001277267102"
# # contents = requests.get('https://ipfs.io/ipfs/QmfZU7bmmxmiih6JQ3WX5i8HNBEsrauQJ7jggCwmk1EVZT').json()
# # image_url = "https://ipfs.io/ipfs/QmfZU7bmmxmiih6JQ3WX5i8HNBEsrauQJ7jggCwmk1EVZT"
# message="Hi My name is Dadson Dennis Derrick I am testing"



# bot.send_photo(chat_id=chat_id, photo=image_url)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import json
# from telegram.ext import Updater, CommandHandler
# import requests
# import re


# import urllib.request

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
# driver = webdriver.Chrome("/home/kwamena/SmartCOntract/chromedriver", chrome_options=options)


# def get_usd():

#     print(toys)


# print(get_usd)


# def msg(token,trx,converted,image):
#     message=("""
#     #BoredApeTronClub #{} has been bought for {}TRX 
#     #{}$

#     Link

#     #Tron #NFT

#     {}

#     Join   https://t.me/boredapetron


#     """).format(token,trx,converted,image)

#     return message


# sia=msg(10,100,100)
# print(sia)



# import re


# String="enterBidForApe(uint256 apeIndex)"

# list_=re.split("(\d+)",String)
# print(list_)



# constant="acceptBidForApe(uint"
# const_="buyApe(uint"
# hallow="enterBidForApe(uint"



from http.client import responses
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
from telegram.ext import Updater, CommandHandler
import requests
import re


import urllib.request

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/home/kwamena/SmartCOntract/chromedriver", chrome_options=options)
chat_id="-1001277267102"

driver.get("https://tronscan.org/#/transaction/0e69e79d5623a471f306b3ceb39a966ed5946213648d193deddb5739d115cdfa")

import telebot

bot_token = '1997316336:AAHpwbMLpH1MQ_zzfJ4V2B0UtQhH3V94EAg'
chat_id = '-1001277267102'

bot = telebot.TeleBot(bot_token)
bot.config['api_key'] = bot_token

#python 3


def get_usd():
    driver.get("https://www.coingecko.com/en/coins/tron")
    return driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[1]/div/div[1]/div[4]/div/div[1]/span[1]/span").text







def msg(token,trx,converted,Link_):
    message=("""Bored Ape on Tron #{} has been bought for {} TRX 
    (${} ) 
    
    {}   
   
    """).format(token,trx,converted,Link_)

    return message



def send_message(chat_id):
    files={'photo':open('/home/kwamena/SmartCOntract/image.png','rb')}
    res=requests.post('https://api.telegram.org/bot1997316336:AAHpwbMLpH1MQ_zzfJ4V2B0UtQhH3V94EAg/sendPhoto?chat_id={}'.format(chat_id),files=files)

constant="acceptBidForApe(uint"
const_="buyApe(uint"
hallow="enterBidForApe(uint"

# def telegram_bot_sendtext(bot_message):

#     bot_token = '1997316336:AAHpwbMLpH1MQ_zzfJ4V2B0UtQhH3V94EAg'
#     bot_chatID = '-1001277267102'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text='+bot_message

#     response = requests.get(send_text)
#     return response.json()
    



# driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div[2]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]").click()

time.sleep(20)
text=driver.find_element_by_css_selector("#root > div.tron-wrapper > main > div > div > div:nth-child(2) > div > div.content > div > div:nth-child(8) > div.flex1 > div:nth-child(1) > div").text

list_=re.split("(\d+)",text)
print(list_)

if const_ in list_:
    print("was inside")

    try:
        token=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[4]/div[2]/div/div[3]/div[2]/a").text
        
        token=int(token)

        token=1938
        print(token)

    except Exception as e:
        token=0
        print(e)

    try:
        trx=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/span").text
        trx = trx.replace(',', '')
        trx=trx.split("\n")[0]
        print(trx)
        trx=int(trx)
        print(trx)

    except Exception as e :
        print(e)

        




    if token !=0:
        print("token is not zero")
        with open("image.json", "r") as read_file:
            json_string = json.load(read_file)

            collections_ = json_string["collection"]

        

            for collection in collections_:
                token_=collection['tokenId']
                # print(token__)
                if token ==token_:
                    response=collection['image']
                    break

            print(response)
            urllib.request.urlretrieve(response, "image.png")

            print("success")
            
            driver.get("https://www.coingecko.com/en/coins/tron")
            toys=driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[1]/div/div[1]/div[4]/div/div[1]/span[1]/span").text
            removed=toys[1:]
            removed=float(removed)
            print(removed)
            # print(type(removed))
            Link_="https://boredapetronclub.com/ape/{}".format(token)
            
            converted=removed*trx

            messah=msg(token,trx,converted,Link_)
            # print(messah)

            send_message(chat_id)
            # bot.send_
            
            print(bot.send_message(chat_id,messah))

else:
    print("not in it ")
# while True:


#     time.sleep(30)
#     checker=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div[2]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/div/div[1]").text
#     checker=int(checker)

#     if checker !=0:
        # hash_=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div[2]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]").text

        # driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div[2]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]").click()
        
        # time.sleep(20)
        # text=driver.find_element_by_css_selector("#root > div.tron-wrapper > main > div > div > div:nth-child(2) > div > div.content > div > div:nth-child(8) > div.flex1 > div:nth-child(1) > div").text

        # list_=re.split("(/+d)",text)

        # if const_ in list_:


        #     try:
        #         token=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[4]/div[2]/div/div[3]/div[2]/a").text
        #         token=int(token)
        #     except:
        #         token=0

        #     try:
        #         trx=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/span").text

        #     except:
        #         pass




        #     if token !=0:
        #         with open("image.json", "r") as read_file:
        #             json_string = json.load(read_file)
        #             tokens = json_string["collection"]
        #             low=[]

        #             for token__ in tokens:

        #                 new_=low.append(token_)
                    
        #                 if token in low:
        #                     indx = low.index(token)
        #                     response = token["image"]

        #                     print(response)
        #                     urllib.request.urlretrieve('{}', "image.png".format(response))

        #                     print("success")
                            
        #                     driver.get("https://www.coingecko.com/en/coins/tron")
        #                     toys=driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[1]/div/div[1]/div[4]/div/div[1]/span[1]/span").text
        #                     removed=toys[1:]
        #                     removed=float(removed)
        #                     # print(type(removed))
                            
                            
        #                     converted=removed*token
        #                     Link_="https://tronscan.org/#/transaction/{}".format(hash_)

        #                     messah=msg(token,trx,converted,Link_)

        #                     send_message(chat_id=chat_id,message=messah)

        # elif constant in list_:

        #         toke_=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[7]/div[2]/div[2]/div[2]").text
        #         trx=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/span").text
        #         toke_=int(toke_)
        #         returner=get_usd()



        #         with open("image.json", "r") as read_file:
        #             json_string = json.load(read_file)
        #             tokens = json_string["collection"]
        #             low=[]

        #             for token__ in tokens:

        #                 new_=low.append(token_)
                    
        #                 if toke_ in low:
        #                     indx = low.index(token)
        #                     response = token["image"]

        #                     print(response)
        #                     urllib.request.urlretrieve('{}', "image.png".format(response))

        #                     print("success")

        #         convertor=returner*toke_


        #         message=""""
        #         Bid on Bored Ape #{} was accepted for  {}TRX  ${}

        #         {}
                                
        #         """.format(toke_,trx,convertor)

        #         send_message(chat_id=chat_id,message=message)





            


            

    





    # else:
    #     print("IT was Zero")


    # time.sleep(30)