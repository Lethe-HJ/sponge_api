# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Node(Base):
    __tablename__ = 'nodes'

    nid = Column(Integer, primary_key=True)
    name = Column(String(255))
    location = Column(String(255))
    status = Column(Integer)


class SensorDatum(Base):
    __tablename__ = 'sensor_data'

    data_id = Column(String(255), primary_key=True)
    sid = Column(Integer, nullable=False)
    datetime = Column(DateTime, nullable=False, server_default=FetchedValue())
    value = Column(String(255))
    type = Column(ForeignKey('sensor_type.id'), nullable=False, index=True)

    sensor_type = relationship('SensorType', primaryjoin='SensorDatum.type == SensorType.id', backref='sensor_data')


class SensorType(Base):
    __tablename__ = 'sensor_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    notes = Column(String(50), nullable=False)


class Sensor(Base):
    __tablename__ = 'sensors'

    sid = Column(Integer, primary_key=True)
    nid = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    type = Column(ForeignKey('sensor_type.id'), nullable=False, index=True)

    sensor_type = relationship('SensorType', primaryjoin='Sensor.type == SensorType.id', backref='sensors')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    password = Column(String(32), nullable=False)
    access_level = Column(Integer, server_default=FetchedValue())
    last_login = Column(DateTime, server_default=FetchedValue())
    create_time = Column(DateTime, server_default=FetchedValue())
