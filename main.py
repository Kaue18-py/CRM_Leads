from datetime import datetime
from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Funil API",
    description="API REST de gestão de leads e funil de vendas",
)
class Etapa(str, Enum):
    novo = "novo"
    contatado = "contatado"
    negociando = "negociando"
    fechado = "fechado"
    perdido = "perdido"
class LeadEntrada(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    empresa: str | None = None
    origem: str
    observacoes: str | None = None
class Lead(LeadEntrada):
    id: int
    etapa: Etapa = Etapa.novo
    criado_em: datetime