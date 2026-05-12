# app/routes/document_routes.py

from fastapi import APIRouter, Depends
# Importamos nuestros nuevos validadores de roles
from app.middleware.role_middleware import require_write, require_read
from app.schemas.document_schema import (
    InsertDocumentSchema, UpdateDocumentSchema, DeleteDocumentSchema
)
from app.services.document_service import (
    insert_document, find_documents, update_document, delete_document
)

router = APIRouter(prefix="/document", tags=["Documents"])

# Insertar documento (Requiere Escritura o Admin)
@router.post("/insert")
def insert_new_document(
    data: InsertDocumentSchema,
    current_user: dict = Depends(require_write) # <--- CAMBIO AQUÍ
):
    return insert_document(
        db_name=data.db_name,
        collection_name=data.collection_name,
        document=data.document,
        owner_id=current_user["id"]
    )

# Obtener documentos (Requiere Lectura, Escritura o Admin)
@router.get("/find")
def get_documents(
    db_name: str,
    collection_name: str,
    current_user: dict = Depends(require_read) # <--- CAMBIO AQUÍ
):
    return find_documents(
        db_name=db_name, collection_name=collection_name, owner_id=current_user["id"]
    )

# Actualizar (Requiere Escritura)
@router.put("/update")
def update_existing_document(
    data: UpdateDocumentSchema,
    current_user: dict = Depends(require_write)
):
    return update_document(...)

# Eliminar (Requiere Escritura)
@router.delete("/delete")
def remove_document(
    data: DeleteDocumentSchema,
    current_user: dict = Depends(require_write)
):
    return delete_document(...)