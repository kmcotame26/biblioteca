from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)  # ✅ autoincrementa
    nombre: str
    correo: str
    telefono: str

    prestamos: List["Prestamo"] = Relationship(back_populates="usuario")
