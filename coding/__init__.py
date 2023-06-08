from telethon import TelegramClient
import logging
import time 

openai_key = "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"

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "5853396122:AAEsWJHn8ahJLvwZvquPXxN_TeB8glEn1go"

bot = TelegramClient("pencil", api_id, api_hash).start(bot_token = bot_token)