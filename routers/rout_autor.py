from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from modelos.mod_autor import Autor
from typing import List

router = APIRouter(prefix="/autores", tags=["Autores"])

@router.post("/", response_model=Autor)
def create_autor(autor: Autor, session: Session = Depends(get_session)):
    session.add(autor)
    session.commit()
    session.refresh(autor)
    return autor

@router.get("/", response_model=List[Autor])
def get_autores(session: Session = Depends(get_session)):
    return session.exec(select(Autor)).all()

@router.get("/{autor_id}", response_model=Autor)
def get_autor(autor_id: int, session: Session = Depends(get_session)):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor

@router.put("/{autor_id}", response_model=Autor)
def update_autor(autor_id: int, data: dict, session: Session = Depends(get_session)):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    for k, v in data.items():
        setattr(autor, k, v)
    session.add(autor)
    session.commit()
    session.refresh(autor)
    return autor

@router.delete("/{autor_id}")
def delete_autor(autor_id: int, session: Session = Depends(get_session)):
    autor = session.get(Autor, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    session.delete(autor)
    session.commit()
    return {"message": "Autor eliminado correctamente"}
