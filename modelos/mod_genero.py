from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Genero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str

    libros: List["Libro"] = Relationship(back_populates="genero")