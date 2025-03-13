# Projeto agendas-api


O projeto Agenda tem como objetivo oferecer funcionalidades para a gestão eficiente de compromissos.

# Métodos

```python
@app.get("/")
def root():
    return {"message": "Não é muito, mas é trabalho honesto."}
```

```python
@app.post("/agendas/", response_model=AgendaCreate)
def criar_agenda(agenda: AgendaCreate, db: Session = Depends(get_db)):
    nova_agenda = Agenda(**agenda.dict())
    db.add(nova_agenda)
    db.commit()
    db.refresh(nova_agenda)
    return nova_agenda
```

```python
@app.get("/agendas/")
def listar_agendas(db: Session = Depends(get_db)):
    #return 'oi'
    return db.query(Agenda).all()
```

```python
@app.get("/agendas/{agenda_id}")
def obter_agenda(agenda_id: int, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")
    return agenda
```

```python
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
```

```python
@app.delete("/agendas/{agenda_id}")
def deletar_agenda(agenda_id: int, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")

    db.delete(agenda)
    db.commit()
    return {"message": "Agenda deletada com sucesso"}
```

```python
@app.patch("/agendas/{agenda_id}/estado")
def alterar_estado(agenda_id: int, estado_update: EstadoUpdate, db: Session = Depends(get_db)):
    agenda = db.query(Agenda).filter(Agenda.id == agenda_id).first()
    if not agenda:
        raise HTTPException(status_code=404, detail="Agenda não encontrada")

    agenda.estadoAtualAgenda = estado_update.estadoAtualAgenda
    db.commit()
    db.refresh(agenda)
    return agenda
```


# Backlog - Tarefas - Agenda-api


## 📌 Tarefas Back-End:
- [X] Criar estrutura do banco de dados SQLite
- [X] Criar modelo de dados para Agendas
- [X] Implementar CRUD para agendas (Criar, Listar, Atualizar, Deletar)
- [X] Criar endpoint para alteração de estado da agenda
- [ ] Adicionar testes unitários
- [X] Criar `Dockerfile` para containerizar a aplicação
- [X] Escrever README com instruções

## 📌 Tarefas Front-End (Opcional):
- [ ] Criar interface React para gerenciar agendas
- [ ] Implementar consumo da API com `axios`
- [ ] Estilizar a interface com Material-UI ou Bootstrap




# Bibliotecas

- fastapi
- unicorn
- sqlalchemy
