    # Credit @BongoBondhuSheikhMujiburRahman.
    # Please Don't remove credit.
    # Born to make history @BongoBondhuSheikhMujiburRahman !

    # Thank you BongoBondhuSheikhMujiburRahman for helping us in this Journey
    # 🥰  Thank you for giving me credit @BongoBondhuSheikhMujiburRahmanr  🥰

    # for any error please contact me -> telegram@BongoBondhuSheikhMujiburRahmanr or insta @BongoBondhuSheikhMujiburRahmanr 
import asyncio
import logging
from configs import Config
from configs import *
from pyrogram import Client
from util.config_parser import TokenParser
from . import multi_clients, work_loads, Bot


async def initialize_clients():
    multi_clients[0] = Bot
    work_loads[0] = 0
    all_tokens = TokenParser().parse_from_env()
    if not all_tokens:
        print("No additional clients found, using default client")
        return
    
    async def start_client(client_id, token):
        try:
            print(f"Starting - Client {client_id}")
            if client_id == len(all_tokens):
                await asyncio.sleep(2)
                print("This will take some time, please wait...")
            client = await Client(
                name=str(client_id),
                api_id=Config.API_ID,
                api_hash=Config.API_HASH,
                bot_token=token,
                sleep_threshold=SLEEP_THRESHOLD,
                no_updates=True,
                in_memory=True
            ).start()
            work_loads[client_id] = 0
            return client_id, client
        except Exception:
            logging.error(f"Failed starting Client - {client_id} Error:", exc_info=True)
    
    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
    multi_clients.update(dict(clients))
    if len(multi_clients) != 1:
        MULTI_CLIENT = True
        print("Multi-Client Mode Enabled")
    else:
        print("No additional clients were initialized, using default client")
