from fastapi import FastAPI
from database import engine, Base
import routes

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(routes.router)
