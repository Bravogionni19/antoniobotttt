import requests
import json
import time

from telethon.sync import TelegramClient
from datetime import datetime
from telethon import TelegramClient,events,sync,Button
from telethon import functions,types
from random import randint


api_id = 14732436
api_hash = "6a6dcca1828828119158463284f00897"
TOKEN = "5640964615:AAEBdaVCTUDDdz-hIHSjnt5-9W935cAU9d8"
client = TelegramClient('BTC',api_id,api_hash).start(bot_token=TOKEN)

canale = 'BTCpricees'


@client.on(events.NewMessage)
async def ciao(e):
    if e.raw_text == "/start":
        await e.respond("ciao")

while True:    
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
    data = response.json()
    currency = data["data"]["base"]
    price = data["data"]["amount"]
    client.send_message(canale, price + "$")
    time.sleep(5)


client.run_until_disconnected() 
