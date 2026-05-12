from app.database.connection import client

def create_collection(db_name: str, collection_name: str, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    db.create_collection(collection_name)
    return {"message": f"Colección '{collection_name}' creada"}

def list_collections(db_name: str, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    collections = db.list_collection_names()
    return {"collections": collections}

def delete_collection(db_name: str, collection_name: str, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    db.drop_collection(collection_name)
    return {"message": f"Colección '{collection_name}' eliminada"}