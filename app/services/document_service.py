from app.database.connection import client
from bson import ObjectId

def insert_document(db_name: str, collection_name: str, document: dict, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    result = db[collection_name].insert_one(document)
    return {
        "message": "Documento insertado",
        "id": str(result.inserted_id)
    }

def find_documents(db_name: str, collection_name: str, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    documents = list(db[collection_name].find({}))
    for doc in documents:
        doc["_id"] = str(doc["_id"])
    return {"data": documents}

def update_document(db_name: str, collection_name: str, filter_query: dict, new_data: dict, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    
    if "_id" in filter_query and isinstance(filter_query["_id"], str):
        filter_query["_id"] = ObjectId(filter_query["_id"])

    result = db[collection_name].update_many(filter_query, {"$set": new_data})
    return {
        "message": "Documento(s) actualizado(s)",
        "modified_count": result.modified_count
    }

def delete_document(db_name: str, collection_name: str, filter_query: dict, owner_id: str):
    database_name = f"{owner_id}_{db_name}"
    db = client[database_name]
    
    if "_id" in filter_query and isinstance(filter_query["_id"], str):
        filter_query["_id"] = ObjectId(filter_query["_id"])

    result = db[collection_name].delete_many(filter_query)
    return {
        "message": "Documento(s) eliminado(s)",
        "deleted_count": result.deleted_count
    }