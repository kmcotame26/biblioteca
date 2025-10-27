from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date

class LibroAutorLink(SQLModel, table=True):
    autor_id: Optional[int] = Field(default=None, foreign_key="autor.id", primary_key=True)
    libro_id: Optional[int] = Field(default=None, foreign_key="libro.id", primary_key=True)

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    isbn: str
    ano_publicacion: int
    copias_disponibles: int = 1
    editorial_id: Optional[int] = Field(default=None, foreign_key="editorial.id")
    genero_id: Optional[int] = Field(default=None, foreign_key="genero.id")

    autores: List[LibroAutorLink] = Relationship(back_populates="libro")
    editorial: Optional["Editorial"] = Relationship(back_populates="libros")
    genero: Optional["Genero"] = Relationship(back_populates="libros")
    prestamos: List["Prestamo"] = Relationship(back_populates="libro")
