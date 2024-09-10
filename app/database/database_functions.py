from discord import Message
from database.entities.discord_message_entity import DiscordHarmfulMessageEntity
import pandas as pd
import sqlalchemy as sa

Session = None

def create_harmful_message_entity(discord_message : Message, harmful_message_category : str):
  return DiscordHarmfulMessageEntity(
    discord_message_id = discord_message.id,
    channel_id=discord_message.channel.id,
    text=discord_message.content,
    user=discord_message.author.name,
    category = discord_message.channel.category.name,
    channel=discord_message.channel.name,
    created_at=discord_message.created_at,
    harmful_message_category = harmful_message_category
  )

def push_new_harmful_message_to_db(question_entity : DiscordHarmfulMessageEntity):
  with Session.begin() as session:
    session.add(question_entity)
  
def get_harmful_messages_grouped_by_category():
  with Session.begin() as session:
    query = session.query(
        DiscordHarmfulMessageEntity.harmful_message_category,
        sa.func.count(DiscordHarmfulMessageEntity.discord_message_id).label('count')
    ).group_by(DiscordHarmfulMessageEntity.harmful_message_category).all()

    # Convert the query result to a DataFrame
    df = pd.DataFrame(query, columns=['harmful_message_category', 'count'])
    return df

