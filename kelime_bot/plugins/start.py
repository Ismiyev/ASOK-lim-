from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕️ Məni Grupa Əlavə Et➕️", url=f"http://t.me/ASOsozutap_bot?startgroup=new")
    ],
    [
        InlineKeyboardButton("Werab Qoxulu ✈️", url="https://t.me/WerabliAnlar"),
        InlineKeyboardButton("Owner 👨🏻‍💻", url="https://t.me/ismiyev95"),
    ]
])


START = """
**• Salam ⚡

• Mən Söz 𓄂𝙰𝚂𝙾🇦🇿 Federasiyasının Rəsmi hazırlanmış oyun Botuyam 🎮 

• Əyləncəli vaxt Keçirmək üçün Mənimlə Oynaya bilərsən ✍🏻 

• Bot @ASOsozutap_bot istediyiniz qrupa atıb mənimlə vaxtınızı əyləncəli keçirə bilərsiz🙂 @WerabliAnlar . 🌪️**

➤ Məlumat üçün 👉 /komek bas. Komandalar Asand və Rahatdır. 
"""

HELP = """
**✌️ Komandalar Menyusuja Xoşgəldin.📌**
/oyun - Oyunu Başlatmaq üçün..
/kec - Cəmi 3 keçid Haqqınız Var.. 
/reyting - Oyuncular arasındaki Xal məlumatı..
/dayan - Oyundan çıxmaq üçün lazımlı olan komandasıdır.. 
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("komek"))
async def help(bot, message):
  await message.reply_photo("https://i.ibb.co/K6QTywd/images-17.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command(basla")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Oyun Qrupunuzda Artıq Davam Edir ✍🏻 \n Oyunu dayandırmaq üçün yazın /dayan")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nQarışıq Söz Tapma Oyunu Başladı .\n\nBol Şanslar @ASOresmi 🇦🇿 !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazanacağınız Xal: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən düzgün sözü tapın @ASOresmi 🇦🇿
        """
        await c.send_message(m.chat.id, text)
        
