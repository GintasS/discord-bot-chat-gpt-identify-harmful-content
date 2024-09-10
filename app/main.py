import logging
from discord_bot import client

from configuration.constants import *
from database import database_functions
from database.database_functions import *
from database.dbsetup import initalize_db_session

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO, format="%(levelname)s %(funcName)s: %(message)s")
  logging.info("[main.py] Starting Discord API Client...")

  Environment.set_correct_environment()
  database_functions.Session = initalize_db_session()
  client.run(Discord.API_BOT_TOKEN)