from configuration.constants import Database

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from database.base import create_tables_if_not_exist

def initalize_db_session():
  postgres_connection_string = Database.POSTGRES_DATABASE_URL
  engine = sa.create_engine(postgres_connection_string, echo=True)
  Session = sessionmaker(engine)
  create_tables_if_not_exist(engine)
  return Session