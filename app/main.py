from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, select

app = FastAPI()

# ⚠️ Usa las mismas credenciales que definiste en docker-compose.yml
DATABASE_URL = "postgresql://admin:admin123@db:5432/fastapi_db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

# Cargamos la tabla users
users = metadata.tables.get("users")

@app.get("/")
def read_root():
    if users is None:
        return {"error": "La tabla 'users' no está disponible."}

    with engine.connect() as conn:
        result = conn.execute(select(users)).fetchall()
        users_list = [{"id": row.id, "name": row.name, "email": row.email} for row in result]

    return {"usuarios": users_list}
