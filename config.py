# © 𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 🌿

import os
import logging
from os import environ
from logging.handlers import RotatingFileHandler
from time import time

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "13666216"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f3a456b486290011638fb4b312f9be70")

#Your Telegram Bot's API Token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7572076027:AAG2_9cz5jItaszpa7RgmiQQOVVCe78e94M")

#Bot Owner's Telegram ID 
OWNER_ID = int(os.environ.get("OWNER_ID", "5465110453"))

#No Need to Change This 
PORT = os.environ.get("PORT", "8080")

#No need to Change This 
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
