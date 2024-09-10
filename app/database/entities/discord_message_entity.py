import sqlalchemy as sa
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from sqlalchemy.orm import relationship

from sqlalchemy import BigInteger

from baml_client.types import HarmfulMessageCategory
from configuration.constants import *
from database.base import Base

class DiscordHarmfulMessageEntity(Base):
  __tablename__ = "messages"
 
  discord_message_id = sa.Column(BigInteger, primary_key=True)  
  channel_id = sa.Column(BigInteger)
  text = sa.Column(sa.Unicode(Validation.DISCORD_MESSAGE_MAX_LENGTH), nullable=False)
  user = sa.Column(sa.Unicode(Validation.USERNAME_MAX_LENGTH), nullable=False)
  category = sa.Column(sa.Unicode(Validation.DISCORD_CATEGORY_MAX_LENGTH), nullable=True)
  channel = sa.Column(sa.Unicode(Validation.DISCORD_CHANNEL_MAX_LENGTH), nullable=False)
  created_at = sa.Column(sa.TIMESTAMP, nullable=False)
  harmful_message_category = sa.Column(sa.Enum(HarmfulMessageCategory), nullable=True)

# Define the Question schema using Marshmallow
class DiscordHarmfulMessageEntitySchema(SQLAlchemySchema):
  class Meta:
    model = DiscordHarmfulMessageEntity
    load_instance = True  # Optional: deserialize to model instances   

  discord_message_id = auto_field()
  channel_id = auto_field()
  text = auto_field()
  user = auto_field()
  category = auto_field()
  channel = auto_field()
  created_at = auto_field()
  harmful_message_category = auto_field()