from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from modelos.mod_editoral import Editorial
from typing import List

router = APIRouter(prefix="/editoriales", tags=["Editoriales"])

@router.post("/", response_model=Editorial)
def create_editorial(editorial: Editorial, session: Session = Depends(get_session)):
    session.add(editorial)
    session.commit()
    session.refresh(editorial)
    return editorial

@router.get("/", response_model=List[Editorial])
def get_editoriales(session: Session = Depends(get_session)):
    return session.exec(select(Editorial)).all()

@router.put("/{editorial_id}", response_model=Editorial)
def update_editorial(editorial_id: int, data: dict, session: Session = Depends(get_session)):
    editorial = session.get(Editorial, editorial_id)
    if not editorial:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    for k, v in data.items():
        setattr(editorial, k, v)
    session.add(editorial)
    session.commit()
    session.refresh(editorial)
    return editorial

@router.delete("/{editorial_id}")
def delete_editorial(editorial_id: int, session: Session = Depends(get_session)):
    editorial = session.get(Editorial, editorial_id)
    if not editorial:
        raise HTTPException(status_code=404, detail="Editorial no encontrada")
    session.delete(editorial)
    session.commit()
    return {"message": "Editorial eliminada correctamente"}
