import discord
import logging

from messages.harmful_message_categorizer import categorize_harmful_message
from messages.is_message_a_harmful_message_categorizer import is_discord_message_a_harmful_message
from baml_client.types import HarmfulMessageCategory
from database.database_functions import *


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  logging.info("[Discord API] Client is initialized successfully.")

  guild_count = 0
  for guild in client.guilds:
    guild_count = guild_count + 1

  logging.info(f"[Discord API] Discord Bot is ready! He is in {guild_count} servers.")

@client.event
async def on_message(message):
  logging.info(f"[Discord API] A new message has been received: {message.content}")

  # Ignore bot messages.
  if message.author == client.user:
    logging.info(f"[Discord API] IGNORING a message, it came from the Discord BOT itself.")
    return
    
  message_type = await is_discord_message_a_harmful_message(message.content)
  if message_type is True:
    logging.info("[Discord API] [Message Categorizer] The message has been IDENTIFIED as HARMFUL TYPE.")
    
    harmful_message_subtype = await categorize_harmful_message(message.content)
    new_harmful_message = create_harmful_message_entity(message, harmful_message_subtype)
    push_new_harmful_message_to_db(new_harmful_message)

    logging.info(f"[Discord API] [Message Categorizer] The message has been later identified of having this HARMFUL SUBTYPE: {harmful_message_subtype}")
  else:
    logging.info(f"[Discord API] [Message Categorizer] The message has been categorized as SAFE: {message.content}.")