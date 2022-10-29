import telethon
import traceback

from datetime import datetime
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync,Button
from telethon import functions,types
from random import randint


api_id = 14732436
api_hash = "6a6dcca1828828119158463284f00897"
TOKEN = "5717563450:AAFQtABtb8TY4tyJ8Vs6pi1OeA39d04hDBE"
client = TelegramClient('bot',api_id,api_hash).start(bot_token=TOKEN)

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
            await event.respond(f"👋🏻 {mention}.\n\n<b>Questo bot è stato ideato per @QueezyStock 🔒\n\n❌<i>NON</i> sei admin")      # modifica @ stock
        else:
            await event.respond(f"👋🏻 {mention}.\n\n<b>Questo bot è stato ideato per @QueezyStock 🔒\n\n✅<i>SEI</i> admin",      # modifica @ stock
                        buttons = [[Button.inline("📬 Post","post1")],
                                   [Button.inline("✍ Comandi","cmd")]])

@client.on(events.NewMessage)
async def suca(event):
    global ADMIN 
    user = await event.get_sender()
    mention = get_mention(user.id, user.first_name)
    if event.text.startswith("/admin") and user.id in ADMIN:
        text = event.text.replace("/admin", "")
        try:
            ADMIN.append(int(event.text.split()[1]))            
            await event.respond(f"<b>✅ → L'utente {text} è diventato admin!</b>")
        except:
            traceback.print_exc()
    elif event.text.startswith("/unadmin") and user.id in ADMIN:
        text = event.text.replace("/unadmin", "")
        try:
            ADMIN.remove(int(event.text.split()[1]))
            await event.respond(f"<b>🧹 → utente {text} è stato rimosso da admin!</b>")
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
            await e.respond("<b>📫 Post inviato! </b>")
                        
                  
        
            
# -----------------------CALLBACK----------------------#

@client.on(events.CallbackQuery)
async def cmd(e):

    if e.data == b"back":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        if not user.id in ADMIN:        
            await e.edit(f"👋🏻 {mention}.\n\n<b>Questo bot è stato ideato per @QueezyStock 🔒\n\n❌<i>NON</i> sei admin")     # modifica @ stock
                        
        else:
            await e.edit(f"👋🏻 {mention}.\n\n<b>Questo bot è stato ideato per @QueezyStock 🔒\n\n✅<i>SEI</i> sei admin",      # modifica @ stock
                        buttons = [[Button.inline("📬 Post","post1")],
                                   [Button.inline("✍ Comandi","cmd")]])
        
    
    if e.data == b"cmd":
        user = await e.get_sender()
        mention = get_mention(user.id, user.first_name)
        await e.edit(f"Benvenuto {mention} nella sezione comandi!\n\n<b>✍Comandi Founder:</b>\n\n🔘 /admin [ID] aggiunge utente alla lista admin\n🔘 /unadmin [ID] rimuove utente dalla lista\n\n<b>✍ Comandi Admin:</b>\n\n🔘 /post [messaggio] invia messaggio da postare nel canale",
                     buttons = [[Button.inline("🔙 Indietro","back")]])

    if e.data == b"post1":
        await e.edit("<b>Per inviare un messaggio nel canale usa /post {messaggio}</b>", buttons = [[Button.inline("🔙 Indietro","back")]])

def get_mention(user_id: int, mention: str) -> str: 
#    mention = get_mention(user.id, user.first_name)
    return (f"<a href=tg://user?id={user_id}>{mention}</a>")                                                   

client.run_until_disconnected() 
