from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date
from modelos.mod_autor import LibroAutorLink

class Libro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    isbn: str
    ano_publicacion: int
    copias_disponibles: int = 1
    autor_id: Optional[int] = Field(default=None, foreign_key="autor.id")
    genero_id: Optional[int] = Field(default=None, foreign_key="genero.id")

    autor: Optional["Autor"] = Relationship(back_populates="libros")
    editorial: Optional["Editorial"] = Relationship(back_populates="libros")
    genero: Optional["Genero"] = Relationship(back_populates="libros")
    prestamos: List["Prestamo"] = Relationship(back_populates="libro")