from fastapi import APIRouter, Depends
from app.middleware.jwt_middleware import get_current_user
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

# Crear base de datos
@router.post("/create")
def create_new_database(
    data: CreateDatabaseSchema,
    current_user: dict = Depends(get_current_user)
):
    return create_database(
        db_name=data.db_name,
        owner_id=current_user["id"]
    )

# Listar bases de datos
@router.get("/list")
def get_databases(
    current_user: dict = Depends(get_current_user)
):
    return list_databases(
        owner_id=current_user["id"]
    )

# Eliminar base de datos
@router.delete("/delete")
def remove_database(
    data: DeleteDatabaseSchema,
    current_user: dict = Depends(get_current_user)
):
    return delete_database(
        db_name=data.db_name,
        owner_id=current_user["id"]
    )