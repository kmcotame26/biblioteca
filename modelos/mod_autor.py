from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class LibroAutorLink(SQLModel, table=True):
    autor_id: Optional[int] = Field(default=None, foreign_key="autor.id", primary_key=True)
    libro_id: Optional[int] = Field(default=None, foreign_key="libro.id", primary_key=True)

class Autor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    pais_origen: str
    ano_nacimiento: int

    libros: List["Libro"] = Relationship(back_populates="autor")