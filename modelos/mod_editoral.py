from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Editorial(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    pais: str

    libros: List["Libro"] = Relationship(back_populates="editorial")
