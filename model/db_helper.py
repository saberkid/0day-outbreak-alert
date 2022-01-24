from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .common import Base

def setup_db(db_name):
    engine = create_engine('sqlite:///{}'.format(db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return engine, Session
