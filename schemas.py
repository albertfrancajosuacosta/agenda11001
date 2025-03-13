from pydantic import BaseModel
import datetime
from models import EstadoAgenda

class AgendaCreate(BaseModel):
    titulo: str
    descricao: str
    dataInicio: datetime.datetime
    dataFim: datetime.datetime
    local: str

class AgendaUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    dataInicio: datetime.datetime | None = None
    dataFim: datetime.datetime | None = None
    local: str | None = None

class EstadoUpdate(BaseModel):
    estadoAtualAgenda: EstadoAgenda