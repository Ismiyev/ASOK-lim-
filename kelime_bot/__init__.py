from time import sleep
from pyrogram import Client
import logging


# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)





# Hesap
API_ID = "14903098"
API_HASH = "5418b39e08dca24d4e0ab24b5d5b38f8"
TOKEN = "5509121112:AAHi71oF-9jbrhENuXLxStBhMeEe5NBKV04" 
USERNAME = "ASOsozutap_bot" 




# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
    )


# Oyun Verileri
oyun = {}


# rating
rating = {}





# !!!!!!!!!!!!!! DEĞİŞTİR KESİNLİKLE !!!!!!!!!!!!!!!!
#      SAHİBİN USER ID'Sİ
OWNER_ID = 5251416015

