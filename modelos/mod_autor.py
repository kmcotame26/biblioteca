from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Autor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    pais_origen: str
    ano_nacimiento: int

    libros: List["LibroAutorLink"] = Relationship(back_populates="autor")
