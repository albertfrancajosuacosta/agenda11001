import enum
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import datetime
from estadoagenda import EstadoAgenda
from agenda import Agenda
import enum

class EstadoUpdate(BaseModel):
    estadoAtualAgenda: EstadoAgenda
