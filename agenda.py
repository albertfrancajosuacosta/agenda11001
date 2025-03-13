from estadoagenda import EstadoAgenda
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime


Base = declarative_base()

# Modelo de dados da Agenda
class Agenda(Base):
    __tablename__ = "agendas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    dataInicio = Column(DateTime, default=datetime.datetime.utcnow)
    dataFim = Column(DateTime, default=datetime.datetime.utcnow)
    local = Column(String)
    estadoAtualAgenda = Column(Enum(EstadoAgenda), default=EstadoAgenda.RECEBIDO)