from datetime import datetime
from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Funil API",
    description="API REST de gestão de leads e funil de vendas",
)
