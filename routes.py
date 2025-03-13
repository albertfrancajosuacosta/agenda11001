from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import AgendaCreate, AgendaUpdate, EstadoUpdate
from crud import criar_agenda, listar_agendas, obter_agenda, atualizar_agenda, deletar_agenda, alterar_estado
from dependencies import get_db

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Não é muito, mas é trabalho honesto."}

@router.post("/agendas/")
def criar_nova_agenda(agenda: AgendaCreate, db: Session = Depends(get_db)):
    return criar_agenda(db, agenda)

@router.get("/agendas/")
def listar_todas_agendas(db: Session = Depends(get_db)):
    return listar_agendas(db)

@router.get("/agendas/{agenda_id}")
def buscar_agenda(agenda_id: int, db: Session = Depends(get_db)):
    agenda = obter_agenda(db, agenda_id)
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")
    return agenda

@router.patch("/agendas/{agenda_id}/estado")
def alterar_estado(agenda_id: int, estado_update: EstadoUpdate, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")

    agenda.estadoAtualAgenda = estado_update.estadoAtualAgenda
    db.commit()
    db.refresh(agenda)
    return agenda


#########################################################




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