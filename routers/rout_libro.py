from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from modelos.mod_libro import Libro
from typing import List

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.post("/", response_model=Libro)
def create_libro(libro: Libro, session: Session = Depends(get_session)):
    existing = session.exec(select(Libro).where(Libro.isbn == libro.isbn)).first()
    if existing:
        raise HTTPException(status_code=409, detail="ISBN ya existe")
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

@router.get("/", response_model=List[Libro])
def get_libros(ano_publicacion: int = None, session: Session = Depends(get_session)):
    query = select(Libro)
    if ano_publicacion:
        query = query.where(Libro.ano_publicacion == ano_publicacion)
    return session.exec(query).all()

@router.get("/{libro_id}", response_model=Libro)
def get_libro(libro_id: int, session: Session = Depends(get_session)):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro

@router.put("/{libro_id}", response_model=Libro)
def update_libro(libro_id: int, data: dict, session: Session = Depends(get_session)):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    for k, v in data.items():
        setattr(libro, k, v)
    session.add(libro)
    session.commit()
    session.refresh(libro)
    return libro

@router.delete("/{libro_id}")
def delete_libro(libro_id: int, session: Session = Depends(get_session)):
    libro = session.get(Libro, libro_id)
    if not libro:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    session.delete(libro)
    session.commit()
    return {"message": "Libro eliminado correctamente"}
