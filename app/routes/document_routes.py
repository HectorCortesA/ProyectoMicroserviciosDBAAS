from fastapi import APIRouter, Depends
from app.middleware.jwt_middleware import get_current_user
from app.schemas.document_schema import (
    InsertDocumentSchema,
    UpdateDocumentSchema,
    DeleteDocumentSchema
)
from app.services.document_service import (
    insert_document,
    find_documents,
    update_document,
    delete_document
)

router = APIRouter(
    prefix="/document",
    tags=["Documents"]
)

# Insertar documento
@router.post("/insert")
def insert_new_document(
    data: InsertDocumentSchema,
    current_user: dict = Depends(get_current_user)
):
    return insert_document(
        db_name=data.db_name,
        collection_name=data.collection_name,
        document=data.document,
        owner_id=current_user["id"]
    )

# Obtener documentos
@router.get("/find")
def get_documents(
    db_name: str,
    collection_name: str,
    current_user: dict = Depends(get_current_user)
):
    return find_documents(
        db_name=db_name,
        collection_name=collection_name,
        owner_id=current_user["id"]
    )

# Actualizar documento
@router.put("/update")
def update_existing_document(
    data: UpdateDocumentSchema,
    current_user: dict = Depends(get_current_user)
):
    return update_document(
        db_name=data.db_name,
        collection_name=data.collection_name,
        filter_query=data.filter_query,
        new_data=data.new_data,
        owner_id=current_user["id"]
    )

# Eliminar documento
@router.delete("/delete")
def remove_document(
    data: DeleteDocumentSchema,
    current_user: dict = Depends(get_current_user)
):
    return delete_document(
        db_name=data.db_name,
        collection_name=data.collection_name,
        filter_query=data.filter_query,
        owner_id=current_user["id"]
    )