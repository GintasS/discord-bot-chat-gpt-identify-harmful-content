import discord
import logging

from messages.harmful_message_categorizer import categorize_harmful_message
from messages.is_message_a_harmful_message_categorizer import is_discord_message_a_harmful_message
from baml_client.types import HarmfulMessageCategory
from database.database_functions import *
from utilities.helper import *

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  logging.info("[Discord API] Client is initialized.")

  guild_count = 0
  for guild in client.guilds:
    guild_count = guild_count + 1

  logging.info(f"[Discord API] Bot is ready! He is in {guild_count} servers.")

@client.event
async def on_message(message):
  logging.info(f"[Discord API] Received a new message: {message.content}")

  # Ignore bot messages.
  if message.author == client.user:
    logging.info(f"[Discord API] Skipping message from the bot itself.")
    return
    
  message_type = await is_discord_message_a_harmful_message(message.content)
  if message_type is True:
    logging.info("[Discord API] [Message Categorizer] Message identified as harmful.")
    
    harmful_message_subtype = await categorize_harmful_message(message.content)
    logging.info(f"[Discord API] [Message Categorizer] Harmful message subtype: {harmful_message_subtype}")
    new_harmful_message = create_harmful_message_entity(message, harmful_message_subtype)
    push_new_harmful_message_to_db(new_harmful_message)
    
    target_channel = get_discord_channel(message.channel.id)
    reply_message = format_harmful_message(message.author.name, harmful_message_subtype)
    await send_discord_message(target_channel, reply_message)
    logging.info("[Discord API] [Message Categorizer] Warning message was sent.")
  else:
    logging.info(f"[Discord API] [Message Categorizer] Message categorized as safe: {message.content}.")

def get_discord_channel(discord_channel_id):
  try:
    logging.info(f"[Discord API] Attempting to get a channel by ID: {discord_channel_id}")
    channel = client.get_channel(discord_channel_id)
    return channel
  except Exception as ex:
    logging.error(f"[Discord API] Failed to on get a Discord channel. ", exc_info=True)
    return

async def send_discord_message(discord_channel, message_text):
  try:
    logging.info(f"[Discord API] Attempting to send a message to {discord_channel.category}:{discord_channel.name}. Message content: {message_text}")
    discord_message = await discord_channel.send(message_text)
    return discord_message
  except Exception as ex:
    logging.error(f"[Discord API] Failed to send a message. Error details: ", exc_info=True)
    return