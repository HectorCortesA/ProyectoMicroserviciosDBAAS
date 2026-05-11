from fastapi import APIRouter, Depends
from app.middleware.jwt_middleware import get_current_user
from app.schemas.query_schema import (
    FilterQuerySchema,
    AggregateQuerySchema
)
from app.services.query_service import (
    filter_documents,
    aggregate_documents
)

router = APIRouter(
    prefix="/query",
    tags=["Queries"]
)

# Filtros
@router.post("/filter")
def filter_data(
    data: FilterQuerySchema,
    current_user: dict = Depends(get_current_user)
):
    return filter_documents(
        db_name=data.db_name,
        collection_name=data.collection_name,
        filters=data.filters,
        owner_id=current_user["id"]
    )

# Aggregations
@router.post("/aggregate")
def aggregate_data(
    data: AggregateQuerySchema,
    current_user: dict = Depends(get_current_user)
):
    return aggregate_documents(
        db_name=data.db_name,
        collection_name=data.collection_name,
        pipeline=data.pipeline,
        owner_id=current_user["id"]
    )