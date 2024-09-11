from baml_client import b

import logging

async def is_discord_message_a_harmful_message(message : str) -> bool:
  try:
    message_type = b.IdentifyHarmfulDiscordMessage(message)
    return message_type.is_harmful is True
  except Exception as ex:
    logging.info("[Message Categorizer API] Error on identifying whether a message is a harmful one", exc_info=True)
    return False
#logging.info("The error indicates that the function IdentifyHarmfulDiscordMessage is not an asynchronous function and thus cannot be awaited. We need to call it without 'await' and handle it accordingly.")
