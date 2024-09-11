from configuration.constants import *

def format_harmful_message(username, harmful_message_category):
  return Discord.HARMFUL_MESSAGE_REPLY_TEXT.format(username, harmful_message_category)