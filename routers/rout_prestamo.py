from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from modelos.mod_prestamo import Prestamo
from modelos.mod_libro import Libro
from typing import List

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])

@router.post("/", response_model=Prestamo)
def create_prestamo(prestamo: Prestamo, session: Session = Depends(get_session)):
    libro = session.get(Libro, prestamo.libro_id)
    if not libro or libro.copias_disponibles <= 0:
        raise HTTPException(status_code=400, detail="No hay copias disponibles")
    libro.copias_disponibles -= 1
    session.add(prestamo)
    session.commit()
    session.refresh(prestamo)
    return prestamo

@router.get("/", response_model=List[Prestamo])
def get_prestamos(session: Session = Depends(get_session)):
    return session.exec(select(Prestamo)).all()
