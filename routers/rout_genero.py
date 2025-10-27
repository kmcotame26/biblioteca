from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from modelos.mod_genero import Genero
from typing import List

router = APIRouter(prefix="/generos", tags=["Géneros"])

@router.post("/", response_model=Genero)
def create_genero(genero: Genero, session: Session = Depends(get_session)):
    session.add(genero)
    session.commit()
    session.refresh(genero)
    return genero

@router.get("/", response_model=List[Genero])
def get_generos(session: Session = Depends(get_session)):
    return session.exec(select(Genero)).all()
