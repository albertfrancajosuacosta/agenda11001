from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime
import enum

# Definição do banco de dados SQLite
DATABASE_URL = "sqlite:///./agendas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Definição dos estados da agenda
class EstadoAgenda(str, enum.Enum):
    RECEBIDO = "RECEBIDO"
    CONFIRMADO = "CONFIRMADO"
    ATENDIDO = "ATENDIDO"
    CANCELADO = "CANCELADO"


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


# Criação do banco de dados
Base.metadata.create_all(bind=engine)


# Modelo Pydantic para entrada de dados
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


# Dependência de sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Inicializando FastAPI
app = FastAPI()

# Rotas CRUD
@app.post("/agendas/", response_model=AgendaCreate)


def criar_agenda(agenda: AgendaCreate, db: Session = Depends(get_db)):
    nova_agenda = Agenda(**agenda.dict())
    db.add(nova_agenda)
    db.commit()
    db.refresh(nova_agenda)
    return nova_agenda


@app.get("/agendas/")
def listar_agendas(db: Session = Depends(get_db)):
    #return 'oi'
    return db.query(Agenda).all()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/agendas/{agenda_id}")
def obter_agenda(agenda_id: int, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")
    return agenda


@app.put("/agendas/{agenda_id}")
def atualizar_agenda(agenda_id: int, agenda_update: AgendaUpdate, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")

    for key, value in agenda_update.dict(exclude_unset=True).items():
        setattr(agenda, key, value)

    db.commit()
    db.refresh(agenda)
    return agenda


@app.delete("/agendas/{agenda_id}")
def deletar_agenda(agenda_id: int, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")

    db.delete(agenda)
    db.commit()
    return {"message": "Agenda deletada com sucesso"}


@app.patch("/agendas/{agenda_id}/estado")
def alterar_estado(agenda_id: int, estado_update: EstadoUpdate, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")

    agenda.estadoAtualAgenda = estado_update.estadoAtualAgenda
    db.commit()
    db.refresh(agenda)
    return agenda

# Rodar API: `uvicorn main:app --reload`
