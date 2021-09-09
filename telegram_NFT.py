from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json
from telegram.ext import Updater, CommandHandler
import requests
import re
import telebot

import urllib.request

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/home/kwamena/SmartCOntract/chromedriver", chrome_options=options)
chat_id="-1001277267102"

bot_token = '1997316336:AAHpwbMLpH1MQ_zzfJ4V2B0UtQhH3V94EAg'
# chat_id = '-1001277267102'

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



# print("me")



while True:
    driver.get("https://tronscan.org/#/contract/TWAKyXJZbwXHRAoDgkeHx5pGG72A57j3Zj/transactions")


    time.sleep(30)
    checker=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div[2]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/div/div[1]").text
    checker=int(checker)
    print(checker)

    if checker !=0:
        print("Not Zero")
        print("wait")
        driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div[2]/div[1]/section/div[2]/div/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]").click()
        
        time.sleep(20)
        text=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[7]/div[2]/div[1]").text
        print(text)

        list_=re.split("(/+d)",text)
        print(list_)

        if const_ in list_:
            print("yes")


            try:
                token=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[4]/div[2]/div/div[3]/div[2]/a").text
                token=int(token)
                print(token)
            except Exception as e:
                print(e)
                token=0

            # try:
            #     trx=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/span").text
            #     trx = trx.replace(',', '')
            #     trx=trx.split("\n")[0]
            #     print(trx)
            #     trx=int(trx)
            #     print(trx)

            # except Exception as e:
            #     print(e)




                print(token)

                    
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
                           
                        
                        driver.get("https://www.coingecko.com/en/coins/tron")
                        toys=driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[1]/div/div[1]/div[4]/div/div[1]/span[1]/span").text
                        removed=toys[1:]
                        removed=float(removed)
                        # print(type(removed))
                        
                        
                        converted=removed*checker
                        converted = "{:.2f}".format(converted)

                        Link_="https://boredapetronclub.com/ape/{}".format(token)


                        messah=msg(token,checker,converted,Link_)

                        send_message(chat_id=chat_id)
                        print(bot.send_message(chat_id,messah))

        elif constant in list_:

                toke_=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[7]/div[2]/div[2]/div[2]").text
                trx=driver.find_element_by_xpath("/html/body/div/div[2]/main/div/div/div[2]/div/div[2]/div/div[3]/div[2]/div/div/span").text
                trx = trx.replace(',', '')
                trx=trx.split("\n")[0]
                print(trx)
                trx=int(trx)
                print(trx)
                
                toke_=int(toke_)
                returner=get_usd()



                with open("image.json", "r") as read_file:
                    json_string = json.load(read_file)
                    tokens = json_string["collection"]
                    low=[]

                    for token__ in tokens:

                        new_=low.append(token__)
                    
                        if toke_ in low:
                            indx = low.index(token)
                            response = token["image"]

                            print(response)
                            urllib.request.urlretrieve('{}', "image.png".format(response))

                            print("success")

                convertor=returner*checker
                convertor = "{:.2f}".format(convertor)


                message=""""
                Bid on Bored Ape #{} was accepted for  {}TRX  

                (${})

                {}
                                
                """.format(toke_,trx,convertor)

                send_message(chat_id=chat_id)

                print(bot.send_message(chat_id,message))




            


            

    





    else:
        print("IT was Zero")


    time.sleep(30)