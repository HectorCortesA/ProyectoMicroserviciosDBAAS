from fastapi import FastAPI

# Auth
from app.routes.auth_routes import (
    router as auth_router
)

# Database
from app.routes.database_routes import (
    router as database_router
)

# Collections
from app.routes.collection_routes import (
    router as collection_router
)

# Documents
from app.routes.document_routes import (
    router as document_router
)

# Queries
from app.routes.query_routes import (
    router as query_router
)

app = FastAPI()

# Auth Routes
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

# Database Routes
app.include_router(
    database_router
)

# Collection Routes
app.include_router(
    collection_router
)

# Document Routes
app.include_router(
    document_router
)

# Query Routes
app.include_router(
    query_router
)

@app.get("/")
def home():

    return {
        "message": "Backend Running"
    }