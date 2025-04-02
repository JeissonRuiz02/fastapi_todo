from app.db.session import engine
from app.db.base import Base
from app.models.user import User
from app.models.task import Task


print("Creando tablas...")
Base.metadata.create_all(bind=engine)
print("¡Listo!")
