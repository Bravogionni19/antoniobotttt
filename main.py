import telethon
import os
import traceback

from datetime import datetime
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync,Button
from telethon import functions,types
from random import randint

if not os.path.exists("session_bot"):
    os.mkdir("session_bot")

api_id = 14732436
api_hash = "6a6dcca1828828119158463284f00897"
client = TelegramClient('session_bot/bot_token',api_id,api_hash).start(bot_token="5703635162:AAEaqkMVjOMkyQcI_JHjFmttrVDxRVyv3JY")

ADMIN = [2073457253]        # metti id tuo
OWNER = [2073457253]        # metti id tuo 


@client.on(events.NewMessage)
async def start(e):
    client.parse_mode = 'html'
            

@client.on(events.NewMessage)
async def start(event):    
    if event.raw_text == "/start":
        user = await event.get_sender()
        mention = get_mention(user.id, user.first_name)
        if not user.id in ADMIN:        
            await event.respond(f"Hi <i>{mention}</i>Welcome to <b><tg-spoiler>Queezy PostBot</tg-spoiler></b> Bot πΉ You are not a channel admin For buy Admin subscription DM to admin π¨βπ»Admin id is <b>@Queezy7</b> π―π| @Queezysdpostbot")      # modifica @ stock
        else:
            await event.respond(f"Hi <i>{mention}</i>Welcome to <b><tg-spoiler>Queezy PostBot</tg-spoiler></b>Bot πΉ\nYou are admin β",      # modifica @ stock
                        buttons = [[Button.inline("π¬ Post","post1")],
                                   [Button.inline("β Comandi","cmd")]])

@client.on(events.NewMessage)
async def suca(event):
    global ADMIN 
    user = await event.get_sender()
    mention = get_mention(user.id, user.first_name)
    if event.text.startswith("/admin") and user.id in ADMIN:
        text = event.text.replace("/admin", "")
        try:
            ADMIN.append(int(event.text.split()[1]))            
            await event.respond(f"<b>β β L'utente {text} Γ¨ diventato admin!</b>")
        except:
            traceback.print_exc()
    elif event.text.startswith("/unadmin") and user.id in ADMIN:
        text = event.text.replace("/unadmin", "")
        try:
            ADMIN.remove(int(event.text.split()[1]))
            await event.respond(f"<b>π§Ή β utente {text} Γ¨ stato rimosso da admin!</b>")
        except:
            traceback.print_exc()
                
        
@client.on(events.NewMessage)
async def post(e):
    user = await e.get_sender()
    mention = get_mention(user.id, user.first_name)
    if e.text.startswith("/post") and user.id in ADMIN:
        text = e.text.replace("/post", "")
        stock = 'QueezyStock'   # inserisci la @ del tuo stock (non inserire anche "@"
        if e.photo:
            photo = e.media.photo
          
            await client.send_file(stock, photo, caption = text + f"\n\nPosted by {mention}")
        elif e.media:
            try:
                if e.media.webpage:
                    
                    await client.send_message(stock, caption = text + f"\n\nPosted by {mention}")                   
                    return
            except:
                media = e.media.document
                
                await bot.send_file(stock, media, caption = text + f"\n\nPosted by {mention}")
                
                return
        else:
            ciao = f"posted by {mention}"
            await client.send_message(stock, text + f"\n\nPosted by {mention}")           
            await e.respond("<b>π« Post inviato! </b>")
                        
                  
        
            
# -----------------------CALLBACK----------------------#

@client.on(events.CallbackQuery)
async def cmd(e):

    if e.data == b"back":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        if not user.id in ADMIN:        
            await e.edit(f"ππ» {mention}.\n\n<b>Questo bot Γ¨ stato ideato per @QueezyStock π\n\nβ<i>NON</i> sei admin")     # modifica @ stock
                        
        else:
            await e.edit(f"ππ» {mention}.\n\n<b>Questo bot Γ¨ stato ideato per @QueezyStock π\n\nβ<i>SEI</i> sei admin",      # modifica @ stock
                        buttons = [[Button.inline("π¬ Post","post1")],
                                   [Button.inline("β Comandi","cmd")]])
        
    
    if e.data == b"cmd":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        await e.edit(f"Benvenuto {mention} nella sezione comandi!\n\n<b>βComandi Founder:</b>\n\nπ /admin [ID] aggiunge utente alla lista admin\nπ /unadmin [ID] rimuove utente dalla lista\n\n<b>β Comandi Admin:</b>\n\nπ /post [messaggio] invia messaggio da postare nel canale",
                     buttons = [[Button.inline("π Indietro","back")]])

    if e.data == b"post1":
        await e.edit("<b>Per inviare un messaggio nel canale usa /post {messaggio}</b>", buttons = [[Button.inline("π Indietro","back")]])

def get_mention(user_id: int, mention: str) -> str: 
#    mention = get_mention(user.id, user.first_name)
    return (f"<a href=tg://user?id={user_id}>{mention}</a>")                                                   

client.run_until_disconnected() 
