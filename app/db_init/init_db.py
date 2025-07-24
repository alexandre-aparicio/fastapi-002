from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, insert


DATABASE_URL = "postgresql://admin:admin123@db:5432/fastapi_db"
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Definición de la tabla 'users'
users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, unique=True, nullable=False),
)

def init():
    print("Inicializando base de datos...")

    # Crea las tablas si no existen
    metadata.create_all(engine)

    # Usa una transacción que se confirme automáticamente
    with engine.begin() as conn:
        result = conn.execute(users.select())
        existing_users = result.fetchall()

        if not existing_users:
            print("📝 Insertando usuarios de ejemplo...")
            conn.execute(insert(users), [
                {"name": "Ana Aparicio", "email": "ana@example.com"},
                {"name": "Carlos Ripoll", "email": "carlos@example.com"},
                {"name": "Lucía Gómez", "email": "lucia@example.com"},
                {"name": "Pedro López", "email": "pedro@example.com"},
                {"name": "Marta Díaz", "email": "marta@example.com"},
            ])
        else:
            print("Usuarios ya existentes, no se insertan duplicados.")

    print("Tablas creadas y datos insertados.")

if __name__ == "__main__":
    init()
