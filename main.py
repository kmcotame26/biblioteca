from fastapi import FastAPI
from database import init_db
from routers import (
    rout_autor,
    rout_libro,
    rout_editorial,
    rout_genero,
    rout_usuario,
    rout_prestamo
)

app = FastAPI(title="Sistema de Gestión de Biblioteca")

@app.on_event("startup")
def on_startup():
    init_db()

# Routers
app.include_router(rout_autor.router)
app.include_router(rout_libro.router)
app.include_router(rout_editorial.router)
app.include_router(rout_genero.router)
app.include_router(rout_usuario.router)
app.include_router(rout_prestamo.router)
