from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Prestamo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha_prestamo: datetime = Field(default_factory=datetime.utcnow)
    fecha_devolucion: Optional[datetime] = None
    usuario_id: Optional[int] = Field(default=None, foreign_key="usuario.id")
    libro_id: Optional[int] = Field(default=None, foreign_key="libro.id")

    usuario: Optional["Usuario"] = Relationship(back_populates="prestamos")
    libro: Optional["Libro"] = Relationship(back_populates="prestamos")
