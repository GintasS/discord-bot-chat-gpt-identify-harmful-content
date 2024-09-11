from baml_client import b
from baml_client.types import HarmfulMessageCategory

import logging

async def categorize_harmful_message(message : str) -> HarmfulMessageCategory:
  try:
    category = b.ExtractMessageCategoryFromMessage(message)
  except Exception as ex:
    logging.info("[Message Categorizer API] Error on categorizing a harmful message.", exc_info=True)
    return HarmfulMessageCategory.Other
  return category
  
  
