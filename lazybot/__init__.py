    # Credit @BongoBondhuSheikhMujiburRahman.
    # Please Don't remove credit.
    # Born to make history @BongoBondhuSheikhMujiburRahman !

    # Thank you BongoBondhuSheikhMujiburRahman for helping us in this Journey
    # 🥰  Thank you for giving me credit @BongoBondhuSheikhMujiburRahmanr  🥰

    # for any error please contact me -> telegram@BongoBondhuSheikhMujiburRahmanr or insta @BongoBondhuSheikhMujiburRahmanr 
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

from pyrogram import Client

from pyrogram import Client
from configs import Config
from configs import *


Bot = Client(
    name=Config.BOT_USERNAME,
    in_memory=True,
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    sleep_threshold=5,
    workers=50,
)
multi_clients = {}
work_loads = {}

