from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
import datetime
import enum
from database import Base

class EstadoAgenda(str, enum.Enum):
    RECEBIDO = "RECEBIDO"
    CONFIRMADO = "CONFIRMADO"
    ATENDIDO = "ATENDIDO"
    CANCELADO = "CANCELADO"

class Agenda(Base):
    __tablename__ = "agendas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    dataInicio = Column(DateTime, default=datetime.datetime.utcnow)
    dataFim = Column(DateTime, default=datetime.datetime.utcnow)
    local = Column(String)
    estadoAtualAgenda = Column(Enum(EstadoAgenda), default=EstadoAgenda.RECEBIDO)