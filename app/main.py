from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- 1. IMPORTAR ESTO

# Auth
from app.routes.auth_routes import router as auth_router
# Database
from app.routes.database_routes import router as database_router
# Collections
from app.routes.collection_routes import router as collection_router
# Documents
from app.routes.document_routes import router as document_router
# Queries
from app.routes.query_routes import router as query_router

app = FastAPI()

# --- 2. AGREGAR LA CONFIGURACIÓN DE CORS AQUÍ ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones de cualquier origen (frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, OPTIONS)
    allow_headers=["*"],  # Permite todos los headers (Authorization, Content-Type, etc.)
)
# -------------------------------------------------

# Auth Routes
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

# Database Routes
app.include_router(database_router)

# Collection Routes
app.include_router(collection_router)

# Document Routes
app.include_router(document_router)

# Query Routes
app.include_router(query_router)

@app.get("/")
def home():
    return {
        "message": "Backend Running"
    }