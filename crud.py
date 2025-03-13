from sqlalchemy.orm import Session
from models import Agenda, EstadoAgenda
from schemas import AgendaCreate, AgendaUpdate, EstadoUpdate

def criar_agenda(db: Session, agenda: AgendaCreate):
    nova_agenda = Agenda(**agenda.dict())
    db.add(nova_agenda)
    db.commit()
    db.refresh(nova_agenda)
    return nova_agenda

def listar_agendas(db: Session):
    return db.query(Agenda).all()

def obter_agenda(db: Session, agenda_id: int):
    return db.query(Agenda).filter(Agenda.id == agenda_id).first()

def atualizar_agenda(db: Session, agenda_id: int, agenda_update: AgendaUpdate):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        return None
    for key, value in agenda_update.dict(exclude_unset=True).items():
        setattr(agenda, key, value)
    db.commit()
    db.refresh(agenda)
    return agenda

def deletar_agenda(db: Session, agenda_id: int):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if agenda:
        db.delete(agenda)
        db.commit()
    return agenda

def alterar_estado(db: Session, agenda_id: int, estado_update: EstadoUpdate):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if agenda:
        agenda.estadoAtualAgenda = estado_update.estadoAtualAgenda
        db.commit()
        db.refresh(agenda)
    return agenda