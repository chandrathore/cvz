from telethon import events
from .. import bot
import asyncio
import openai

openai.api_key = "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"
#openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True,pattern= "(?i)/ask"))
async def _gpt(event):
  # if event.sender_id ==(5141254330)
  await event.reply("yes! you are my Developer, you developed me very well")
  # else:
   # await evemt .reply("you are user:nice to meet you")
  await event.reply(event)

