from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, ForeignKey
from sqlalchemy.types import TEXT, Date, DateTime, String
from sqlalchemy.orm import relationship

from .common import Base


class ImportRecord(Base):
    # entry for the entire test attempt
    __tablename__ = 'import_record'
    id = Column(Integer, primary_key=True)
    cve = Column(TEXT, nullable=True)
    title = Column(TEXT, nullable=True)
    start_datetime = Column(DateTime, nullable=True)
    end_datetime = Column(DateTime, nullable=True)
    count = Column(Integer, nullable=False, default=0)
