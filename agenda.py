from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime
from estadoagenda import EstadoAgenda
import enum

#from main import Base


#Modelo de dados da Agenda
class Agenda():
    __tablename__ = "agendas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    dataInicio = Column(DateTime, default=datetime.datetime.utcnow)
    dataFim = Column(DateTime, default=datetime.datetime.utcnow)
    local = Column(String)
    estadoAtualAgenda = Column(Enum(EstadoAgenda), default=EstadoAgenda.RECEBIDO)