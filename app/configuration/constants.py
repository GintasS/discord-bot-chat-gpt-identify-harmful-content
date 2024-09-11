from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

class Environment:
  CURRENT_ENVIRONMENT_NAME = str(os.environ['CURRENT_ENVIRONMENT_NAME'])

  def set_correct_environment():
    if Environment.CURRENT_ENVIRONMENT_NAME == "DEV":
      Database.POSTGRES_DATABASE_URL = str(os.environ['DEV_POSTGRES_DATABASE_URL'])
    elif Environment.CURRENT_ENVIRONMENT_NAME == "TEST":
      Database.POSTGRES_DATABASE_URL = str(os.environ['TEST_POSTGRES_DATABASE_URL'])
    elif Environment.CURRENT_ENVIRONMENT_NAME == "PROD":
      Database.POSTGRES_DATABASE_URL = str(os.environ['PROD_POSTGRES_DATABASE_URL'])

class Database:   
  POSTGRES_DATABASE_URL = None
  
class Discord:
  API_BOT_TOKEN = os.environ['DISCORD_API_BOT_TOKEN']
  HARMFUL_MESSAGE_REPLY_TEXT = "Warning: User: {} has written a harmful message categorized as {}."

class Validation:
  USERNAME_MAX_LENGTH = 32
  DISCORD_MESSAGE_MAX_LENGTH = 2000
  DISCORD_CHANNEL_MAX_LENGTH = 25
  DISCORD_CATEGORY_MAX_LENGTH = 25