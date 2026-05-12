from fastapi import APIRouter, Depends
# Importamos require_admin en lugar de get_current_user
from app.middleware.role_middleware import require_admin
from app.schemas.database_schema import (
    CreateDatabaseSchema,
    DeleteDatabaseSchema
)
from app.services.database_service import (
    create_database,
    list_databases,
    delete_database
)

router = APIRouter(
    prefix="/db",
    tags=["Database"]
)

# Crear base de datos (Requiere Admin)
@router.post("/create")
def create_new_database(
    data: CreateDatabaseSchema,
    current_user: dict = Depends(require_admin)
):
    return create_database(
        db_name=data.db_name,
        user_id=current_user["id"]  # <-- CAMBIO AQUI
    )

# Listar bases de datos (Requiere Admin)
@router.get("/list")
def get_databases(
    current_user: dict = Depends(require_admin)
):
    return list_databases(
        user_id=current_user["id"]  # <-- CAMBIO AQUI
    )

# Eliminar base de datos (Requiere Admin)
@router.delete("/delete")
def remove_database(
    data: DeleteDatabaseSchema,
    current_user: dict = Depends(require_admin)
):
    return delete_database(
        db_name=data.db_name,
        user_id=current_user["id"]  # <-- CAMBIO AQUI
    )