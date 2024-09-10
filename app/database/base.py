from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

def create_tables_if_not_exist(engine):
    Base.metadata.create_all(engine)