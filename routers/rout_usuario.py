from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from modelos.mod_usuario import Usuario
from typing import List

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=Usuario)
def create_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

@router.get("/", response_model=List[Usuario])
def get_usuarios(session: Session = Depends(get_session)):
    return session.exec(select(Usuario)).all()
