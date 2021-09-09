# import json
  
# # JSON data:
# x =  """{ "organization":"GeeksForGeeks",
#         "city":"Noida",
#         "country":"India"}"""
 
# # python object to be appended
# y = """{ "organization":"GeeksForGeeks",
#         "city":"Noida",
#         "country":"India"}"""
 
# # parsing JSON string:
# z = json.loads(x)
  
# # appending the data
# z.update(y)
 
# # the result is a JSON string:
# print(json.dumps(z))

# import requests
# client="EAAAEJfPVGcLR-RTP0eOiFz4AB8Rl4tYJvHpunXpAIN0nhyHnh5jQfl4_unKYBF7"
# result = client.orders.search_orders(
#   body = {
#     "location_ids": [
#       "LD7NS4BDDYE0Q"
#     ],
#     "limit": 3
#   }
# )

# if result.is_success():
#   print(result.body)
# elif result.is_error():
#   print(result.errors)

# from square.client import Client
import requests

# ACCESS_TOKEN="jaksjdkajsdkjaskdjasjdkasjd"

# client = Client(
#     access_token=ACCESS_TOKEN,
#     environment=("DEFAULT", "environment"),
# )
# locations_api = client.locations
# result = locations_api.list_locations()



# if __name__ == "__main__":
#     @ignore_unexpected_kwargs


def msg(token,trx,converted,Link_):
    message=("#BoredApeTronClub #{} has been bought for {}TRX #{}${}#Tron #NFTJoin   https://t.me/boredapetron").format(token,trx,converted,Link_)

    return message


# def telegram_bot_sendtext(bot_message):

#     bot_token = '1997316336:AAHpwbMLpH1MQ_zzfJ4V2B0UtQhH3V94EAg'
#     
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&text='+bot_message

#     response = requests.get(send_text)
#     return response.json()
    





# # print(message)
# print(telegram_bot_sendtext("#BoredApeTronClub #432 has been bought for 6000TRX #40$hhppppp.com#Tron #NFTJoin   https://t.me/boredapetron"))







# message=msg(432,6000,40,"hhppppp.com")




# bot.polling()