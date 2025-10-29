from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = ("sqlite:///biblioteca.db""")
engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    from modelos import mod_autor, mod_libro, mod_editoral, mod_genero, mod_usuario, mod_prestamo
    SQLModel.metadata.create_all(engine)
