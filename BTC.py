import requests
import json
import time

from datetime import datetime
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync,Button
from telethon import functions,types
from random import randint

api_id = 14732436
api_hash = "6a6dcca1828828119158463284f00897"
TOKEN = "5568423399:AAHLjvgKe4Hc_KLwkWaKCfPT95vIuBXtXUk"
client = TelegramClient('bot',api_id,api_hash).start(bot_token=TOKEN)

@client.on(events.NewMessage)
async def html(e):
    client.parse_mode = 'html'

@client.on(events.NewMessage)
async def start(event):
    if event.raw_text == "/start":
        user = await event.get_sender()
        mention = get_mention(user.id, user.first_name)
        await event.respond(f"<b>Ciao {mention} con questo bot potrai vedere il valore in tempo reale di alcune criptovalute 💲</b>",
                            buttons = [[Button.inline("🟠 BTC","btc")],
                                       [Button.inline("🔵 ETH","eth"), Button.inline("🐕 DOGE coin","doge")],
                                       [Button.inline("⚪️ LTC","ltc"), Button.inline("🟢 USDT","usdt")],
                                       [Button.inline("🟡 BUSD","busd")],
                                       [Button.inline("🇬🇧 Language","lang")],
                                       [Button.url("🧑🏻‍💻 Developer","t.me/GOLD26KDNA")]])


@client.on(events.CallbackQuery)
async def price(e):
    if e.data == b"back":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        await e.edit(f"<b>Ciao {mention} con questo bot potrai vedere il valore in tempo reale di alcune criptovalute 💲</b>",
                            buttons = [[Button.inline("🟠 BTC","btc")],
                                       [Button.inline("🔵 ETH","eth"), Button.inline("🐕 DOGE coin","doge")],
                                       [Button.inline("⚪️ LTC","ltc"), Button.inline("🟢 USDT","usdt")],
                                       [Button.inline("🟡 BUSD","busd")],
                                       [Button.inline("🇬🇧 Language","lang")],
                                       [Button.url("🧑🏻‍💻 Developer","t.me/GOLD26KDNA")]])
        
    elif e.data == b"back1":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        await e.edit(f"<b>Hi {mention} with this bot you will be able to see the real-time value of some crypto currencies 💲</b>",
                            buttons = [[Button.inline("🟠 BTC","btc1")],
                                       [Button.inline("🔵 ETH","eth1"), Button.inline("🐕 DOGE coin","doge1")],
                                       [Button.inline("⚪️ LTC","ltc1"), Button.inline("🟢 USDT","usdt1")],
                                       [Button.inline("🟡 BUSD","busd1")],
                                       [Button.inline("🇮🇹 Lingua","lang")],
                                       [Button.url("🧑🏻‍💻 Developer","t.me/GOLD26KDNA")]])

    elif e.data == b"lang":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        await e.edit(f"<b>Hi {mention} with this bot you will be able to see the real-time value of some crypto currencies 💲</b>",
                            buttons = [[Button.inline("🟠 BTC","btc1")],
                                       [Button.inline("🔵 ETH","eth1"), Button.inline("🐕 DOGE coin","doge1")],
                                       [Button.inline("⚪️ LTC","ltc1"), Button.inline("🟢 USDT","usdt1")],
                                       [Button.inline("🟡 BUSD","busd1")],
                                       [Button.inline("🇮🇹 Lingua","lang1")],
                                       [Button.url("🧑🏻‍💻 Developer","t.me/GOLD26KDNA")]])

    elif e.data == b"lang1":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        await e.edit(f"<b>Ciao {mention} con questo bot potrai vedere il valore in tempo reale di alcune criptovalute 💲</b>",
                            buttons = [[Button.inline("🟠 BTC","btc")],
                                       [Button.inline("🔵 ETH","eth"), Button.inline("🐕 DOGE coin","doge")],
                                       [Button.inline("⚪️ LTC","ltc"), Button.inline("🟢 USDT","usdt")],
                                       [Button.inline("🟡 BUSD","busd")],
                                       [Button.inline("🇬🇧 Language","lang")],
                                       [Button.url("🧑🏻‍💻 Developer","t.me/GOLD26KDNA")]])
    elif e.data == b"btc":
        response = requests.get("https://api.coinbase.com/v2/prices/BTC-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}€", buttons = [[Button.inline("USD","btc3")],
                                                                 [Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"eth":
        response = requests.get("https://api.coinbase.com/v2/prices/ETH-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price ETH</b> ➩{price}€", buttons = [[Button.inline("USD","eth3")],
                                                               [Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"doge":
        response = requests.get("https://api.coinbase.com/v2/prices/DOGE-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price DOGE</b> ➩ {price}€", buttons = [[Button.inline("USD","doge3")],
                                                                 [Button.inline("⬅️ Indietro","back")]])
                                                                 

    elif e.data == b"ltc":
        response = requests.get("https://api.coinbase.com/v2/prices/LTC-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price LTC</b> ➩{price}€", buttons = [[Button.inline("USD","ltc3")],
                                                               [Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"usdt":
        response = requests.get("https://api.coinbase.com/v2/prices/USDT-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price USDT</b> ➩{price}€", buttons = [[Button.inline("USD","usdt3")],
                                                                [Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"busd":
        response = requests.get("https://api.coinbase.com/v2/prices/BUSD-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BUSD</b> ➩{price}€", buttons = [[Button.inline("USD","busd3")],
                                                                [Button.inline("⬅️ Indietro","back")]])
                                                                
        
    elif e.data == b"btc1":
        response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}€", buttons = [[Button.inline("USD","btc4")],
                                                                 [Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"eth1":
        response = requests.get("https://api.coinbase.com/v2/prices/ETH-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price ETH</b> ➩{price}$", buttons = [[Button.inline("USD","eth4")],
                                                               [Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"doge1":
        response = requests.get("https://api.coinbase.com/v2/prices/DOGE-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price DOGE</b> ➩ {price}$", buttons = [[Button.inline("USD","doge4")],
                                                                 [Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"ltc1":
        response = requests.get("https://api.coinbase.com/v2/prices/LTC-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price LTC</b> ➩{price}€", buttons = [[Button.inline("USD","ltc4")],
                                                               [Button.inline("⬅️ Indietro","back1")]])
                                                               

    elif e.data == b"usdt1":
        response = requests.get("https://api.coinbase.com/v2/prices/USDT-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price USDT</b> ➩{price}€", buttons = [[Button.inline("USD","usdt4")],
                                                                [Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"busd1":
        response = requests.get("https://api.coinbase.com/v2/prices/BUSD-EUR/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BUSD</b> ➩{price}€", buttons = [[Button.inline("USD","busd4")],
                                                                [Button.inline("⬅️ Indietro","back1")]])
       
        
# ---------------------------- USD CRYPTO PRICE----------------------------------#       

    elif e.data == b"btc3":
        response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"eth3":
        response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price ETH </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"doge3":
        response = requests.get("https://api.coinbase.com/v2/prices/DOGE-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"ltc3":
        response = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"usdt3":
        response = requests.get("https://api.coinbase.com/v2/prices/USDT-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$",buttons = [[Button.inline("⬅️ Indietro","back")]])

    elif e.data == b"busd3":
        response = requests.get("https://api.coinbase.com/v2/prices/BUSD-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$",buttons = [[Button.inline("⬅️ Indietro","back")]])


# -----------------------------ITALIAN CALLBACK----------------------------------#
    elif e.data == b"btc4":
        response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"eth4":
        response = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price ETH </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"doge4":
        response = requests.get("https://api.coinbase.com/v2/prices/DOGE-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"ltc4":
        response = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$", buttons = [[Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"usdt4":
        response = requests.get("https://api.coinbase.com/v2/prices/USDT-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$",buttons = [[Button.inline("⬅️ Indietro","back1")]])

    elif e.data == b"busd4":
        response = requests.get("https://api.coinbase.com/v2/prices/BUSD-USD/buy")
        data = response.json()
        currency = data["data"]["base"]
        price = data["data"]["amount"]
        await e.edit(f"<b>Price BTC </b> ➩ {price}$",buttons = [[Button.inline("⬅️ Indietro","back1")]])      
        
# -------------------------------------------------------------------------------#
def get_mention(user_id: int, mention: str) -> str:
#    mention = get_mention(user.id, user.first_name)
    return (f"<a href=tg://user?id={user_id}>{mention}</a>")

client.run_until_disconnected()                       
