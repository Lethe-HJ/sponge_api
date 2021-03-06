# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata





class SensorDatum(Base):
    __tablename__ = 'sensor_data_1'

    data_id = Column(String(255), primary_key=True)
    datetime = Column(DateTime, nullable=False, server_default=FetchedValue())
    value = Column(String(255))





class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    password = Column(String(32), nullable=False)
    access_level = Column(Integer, server_default=FetchedValue())
    last_login = Column(DateTime, server_default=FetchedValue())
    create_time = Column(DateTime, server_default=FetchedValue())
